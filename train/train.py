import os
import tempfile
from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple, Union

import cadquery as cq
import numpy as np
import open3d
import skimage.io
import torch
import torch.nn as nn
import torch.nn.functional as F
import trimesh
# import wandb
from datasets import Dataset
from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training
from pytorch3d.ops import sample_farthest_points
from transformers import (AutoTokenizer, BitsAndBytesConfig, Qwen3ForCausalLM,
                          Qwen3Model, TrainingArguments)
from transformers.modeling_outputs import CausalLMOutputWithPast
from transformers.tokenization_utils_base import PaddingStrategy, PreTrainedTokenizerBase
from trl import SFTConfig, SFTTrainer


######## CONFIG ########

NUM_POINT_TOKENS = 256 # As mentioned in paper Sec 4.3
MAX_CODE_TOKENS = 768 # Adjust based on your dataset analysis
MAX_SEQ_LENGTH = NUM_POINT_TOKENS + MAX_CODE_TOKENS # Set max_seq_length in SFTConfig


######## MODELs ########

class FourierPointEncoder(torch.nn.Module):
    def __init__(self, hidden_size, num_frequencies=8):
        super().__init__()
        # Frequencies from 2^0 to 2^(num_frequencies-1)
        frequencies = 2.0 ** torch.arange(num_frequencies, dtype=torch.float32)
        self.register_buffer("frequencies", frequencies, persistent=False)
        # Input dim: 3 (coords) + 3*num_freq (sin) + 3*num_freq (cos)
        input_dim = 3 + 3 * num_frequencies * 2
        self.projection = torch.nn.Linear(input_dim, hidden_size)

    def forward(self, points):
        # points shape: (batch_size, num_points, 3)
        x = points # (B, N, 3)
        # Calculate fourier features
        points_proj = points.unsqueeze(-1) * self.frequencies # (B, N, 3, F)
        points_proj = points_proj.view(*points.shape[:-1], -1) # (B, N, 3*F)
        # Concatenate [points, sin(points_proj), cos(points_proj)]
        x = torch.cat((points, points_proj.sin(), points_proj.cos()), dim=-1) # (B, N, 3 + 3*F*2)
        x = self.projection(x) # (B, N, hidden_size)
        return x


class CADRecode(Qwen3ForCausalLM):
    # Keep __init__ as you have it, ensuring point_encoder uses float32 internally if needed
    def __init__(self, config):
        super().__init__(config) # Call Qwen2ForCausalLM's __init__

        # Store hidden_size explicitly if needed elsewhere, otherwise use config.hidden_size
        self._hidden_size = config.hidden_size
        self.num_point_tokens = NUM_POINT_TOKENS

        # Create point encoder - ensure it's compatible with the model's dtype expectations
        # We might need to manage dtypes carefully during the forward pass
        self.point_encoder = FourierPointEncoder(config.hidden_size)

    # Add gradient checkpointing enabling for the point encoder if needed
    def enable_input_require_grads(self):
       super().enable_input_require_grads()
       self.point_encoder.requires_grad_(True)

    def forward(
        self,
        input_ids: Optional[torch.LongTensor] = None,
        attention_mask: Optional[torch.Tensor] = None,
        point_cloud: Optional[torch.Tensor] = None,
        position_ids: Optional[torch.LongTensor] = None,
        past_key_values: Optional[List[torch.FloatTensor]] = None,
        inputs_embeds: Optional[torch.FloatTensor] = None, # Still accept for flexibility/generation
        labels: Optional[torch.LongTensor] = None,
        use_cache: Optional[bool] = None,
        output_attentions: Optional[bool] = None,
        output_hidden_states: Optional[bool] = None,
        return_dict: Optional[bool] = None,
        cache_position: Optional[torch.LongTensor] = None,
    ) -> Union[Tuple, CausalLMOutputWithPast]:

        # Determine if this is the first forward pass (no past_key_values)
        # and if we need to process point clouds based on input args
        is_first_step = (past_key_values is None)
        # Need point cloud if it's the first step and input_ids are present
        process_points = (is_first_step and point_cloud is not None and input_ids is not None)

        if process_points:
            # --- Point Cloud Injection (Simpler) ---
            num_point_tokens = self.num_point_tokens # Get from config or constant

            # 1. Get Token Embeddings for the code part ONLY
            # Code part starts after the placeholders
            code_input_ids = input_ids[:, num_point_tokens:]
            code_embeds = self.model.embed_tokens(code_input_ids)

            # 2. Get Point Embeddings
            if point_cloud.ndim == 2: point_cloud = point_cloud.unsqueeze(0)
            point_embeds = self.point_encoder(point_cloud.to(dtype=torch.float32))
            point_embeds = point_embeds.to(code_embeds.dtype) # Match dtype

            # Ensure shapes match expected num_point_tokens
            if point_embeds.shape[1] != num_point_tokens:
                # Handle mismatch, maybe slice point_embeds or raise error
                print(f"Warning: Mismatch point embeds {point_embeds.shape[1]} vs placeholders {num_point_tokens}")
                # Example: Slice point_embeds if too long, pad if too short (needs pad value)
                # point_embeds = point_embeds[:, :num_point_tokens, :] # Simple truncate

            # 3. Combine Embeddings: [Point | Code]
            inputs_embeds = torch.cat([point_embeds, code_embeds], dim=1)

            # 4. Adjust Attention Mask (replace -1 with 1)
            # Assuming attention_mask was passed correctly from collator
            final_attention_mask = torch.where(attention_mask == -1, 1, attention_mask)
            input_ids = None # Using embeddings now
        elif inputs_embeds is None:
            # Normal embedding if not first step or no points
            inputs_embeds = self.model.embed_tokens(input_ids)
            final_attention_mask = attention_mask
            input_ids = None
        else:
            # Embeddings passed directly
            final_attention_mask = attention_mask # Assume mask is correct

        # --- Pass to Qwen Model ---
        outputs = self.model(
            input_ids=input_ids, # Will be None if embeddings were generated/combined
            attention_mask=final_attention_mask,
            position_ids=position_ids,
            past_key_values=past_key_values,
            inputs_embeds=inputs_embeds,
            use_cache=use_cache,
            output_attentions=output_attentions,
            output_hidden_states=output_hidden_states,
            return_dict=return_dict,
            cache_position=cache_position,
        )

        # --- Logits and Loss ---
        hidden_states = outputs[0]
        logits = self.lm_head(hidden_states)
        logits = logits.float()

        loss = None
        if labels is not None:
            # Standard loss calculation (NLL)
            shift_logits = logits[..., :-1, :].contiguous()
            shift_labels = labels[..., 1:].contiguous() # Model shifts labels
            loss_fct = nn.CrossEntropyLoss()
            # Flatten logits and labels
            loss = loss_fct(shift_logits.view(-1, self.config.vocab_size), shift_labels.view(-1))

        # --- Return ---
        if not return_dict:
            # Ensure output structure matches base class expectations
            # Typically (logits, past_key_values, hidden_states, attentions)
            # outputs[1:] contains the rest after hidden_states (outputs[0])
            output = (logits,) + outputs[1:]
            #return (loss,) + output if loss is not None else output (NOTE: SOMEHOW TRAINING FAILS)

        past_key_values_out = getattr(outputs, "past_key_values", None)
        # Use outputs.hidden_states if available (usually is if return_dict=True default)
        hidden_states_out = getattr(outputs, "hidden_states", outputs[0] if isinstance(outputs, tuple) else None)
        attentions_out = getattr(outputs, "attentions", None)

        return CausalLMOutputWithPast(
            loss=loss,
            logits=logits,
            past_key_values=past_key_values_out,
            hidden_states=hidden_states_out,
            attentions=attentions_out,
        )

    # prepare_inputs_for_generation needs careful adjustment if using point clouds
    # It needs to ensure 'point_cloud' is passed correctly and potentially handle
    # the initial embedding generation if `inputs_embeds` isn't managed externally.
    def prepare_inputs_for_generation(self, input_ids, past_key_values=None, inputs_embeds=None, point_cloud=None, attention_mask=None, **kwargs):
        # Standard logic from base class
        model_inputs = super().prepare_inputs_for_generation(input_ids, past_key_values=past_key_values, inputs_embeds=inputs_embeds, attention_mask=attention_mask, **kwargs)

        # Ensure point_cloud is passed along
        # Generation usually starts with input_ids, so the first forward call needs point_cloud
        # Subsequent calls use past_key_values and don't need the full point_cloud tensor again,
        # but we need to pass *something* or None to satisfy the signature.
        # This depends heavily on how generation is initiated.
        # Let's assume point_cloud is only needed for the *first* step.
        if past_key_values is None:
             model_inputs['point_cloud'] = point_cloud
        else:
             model_inputs['point_cloud'] = None # Not needed after first step

        # The attention mask also needs special handling during generation if it contains -1
        # This might require overriding the generation loop or careful setup.
        # For now, assume the initial attention_mask is prepared correctly outside.
        model_inputs['attention_mask'] = attention_mask

        return model_inputs


######## DATASETS ########

class CADRecodeDataset(torch.utils.data.Dataset):
    def __init__(self, data_root: str, tokenizer: PreTrainedTokenizerBase, num_points=NUM_POINT_TOKENS, num_pre_points=8192) -> None:
        self.data = []
        print(f"Loading data from: {data_root}")
        for root, dirs, files in os.walk(data_root):
            for cad_file in files:
                if cad_file.endswith(".py"):
                    self.data.append(os.path.join(root, cad_file))
        print(f"Found {len(self.data)} python files.")
        self.data.sort()
        self.tokenizer = tokenizer
        self.num_points = num_points
        self.num_pre_points = num_pre_points
        # Store im_start_token string/ID for convenience
        self.im_start_token = "<|im_start|>" # Or fetch from tokenizer if it has an attribute


    def mesh_to_point_cloud(self, mesh, n_points: int, n_pre_points: int):
        vertices, _ = trimesh.sample.sample_surface(mesh, n_pre_points)
        if len(vertices) < n_points:
                print(f"Warning: Not enough points sampled ({len(vertices)}), requested {n_pre_points}. Using {len(vertices)}.")
                # Handle cases with fewer points if necessary (e.g., repeat points)
                if len(vertices) == 0: # Handle empty mesh case
                    print("Error: Mesh resulted in 0 sampled points.")
                    return None # Or return a placeholder zero tensor
                n_pre_points = len(vertices)
                n_points = min(n_points, n_pre_points)

        if n_pre_points == n_points: # If sampling exactly n_points, FPS is not needed
            ids = np.arange(n_points)
        else:
            # Ensure vertices tensor is float32 for FPS
            _, ids = sample_farthest_points(torch.tensor(vertices, dtype=torch.float32).unsqueeze(0), K=n_points)
            ids = ids[0].numpy()

        sampled_points = np.asarray(vertices[ids], dtype=np.float32)
        return sampled_points

    def __len__(self) -> int:
        return len(self.data)

    def __getitem__(self, idx: int):
        cad_code_filepath = self.data[idx]
        with open(cad_code_filepath, 'r') as f:
            cad_code_str = f.read()

        # 1. Execute CadQuery Code safely (consider restricted execution if needed)
        local_env = {'cq': cq} # Provide cq module
        exec(cad_code_str, {'cq': cq}, local_env)
        cad_model = local_env.get('r') or local_env.get('result') # Check common variable names

        if cad_model is None or not isinstance(cad_model, cq.Workplane):
            raise RuntimeError(f"Error: No valid CadQuery Workplane ('r' or 'result') found in: {cad_code_filepath}")

        # Attempt to get a compound or solid
        final_shape = cad_model.combine().val()
        if not isinstance(final_shape, (cq.Solid, cq.Compound)):
            raise RuntimeError(f"Error: Extracted final_shape is not Solid/Compound. Type: {type(final_shape)}. File: {cad_code_filepath}")

        # 2. Convert to Mesh (using temporary file for simplicity)
        with tempfile.NamedTemporaryFile(suffix=".stl", delete=True) as tmp_file:
            cq.exporters.export(final_shape, tmp_file.name) # Use cq.exporters
            # Check if file is empty after export
            if os.path.getsize(tmp_file.name) == 0:
                RuntimeError(f"Error: Exported STL file is empty for: {cad_code_filepath}")
            gt_mesh = trimesh.load_mesh(tmp_file.name)

        # 3. Sample Points & Normalize
        # Normalize mesh before sampling
        center = gt_mesh.bounds[0] + (gt_mesh.bounds[1] - gt_mesh.bounds[0]) / 2.0
        gt_mesh.apply_translation(-center)
        scale = 2.0 / max(gt_mesh.extents) if max(gt_mesh.extents) > 1e-6 else 1.0 # Avoid division by zero
        gt_mesh.apply_scale(scale)

        point_cloud = self.mesh_to_point_cloud(gt_mesh, self.num_points, self.num_pre_points)

        if point_cloud is None:
            RuntimeError(f"Error: Failed to generate point cloud for: {cad_code_filepath}")

        # 4. Format output: Prepend <|im_start|> to the code string
        #    Do not manually add EOS token; tokenizer handles it.
        formatted_code = f"{self.im_start_token}{cad_code_str}"

        return {"point_cloud": torch.tensor(point_cloud, dtype=torch.float32),
                "target_code": formatted_code}


@dataclass
class DataCollatorForCADRecode:
    tokenizer: PreTrainedTokenizerBase
    max_length: Optional[int] = None
    pad_to_multiple_of: Optional[int] = None
    num_point_tokens: int = NUM_POINT_TOKENS
    ignore_index: int = -100

    def __post_init__(self):
        if self.tokenizer.padding_side != 'left':
            raise ValueError("Tokenizer must be initialized with padding_side='left'.")
        if self.tokenizer.pad_token_id is None:
            raise ValueError("Tokenizer must have a pad_token_id set.")

    def __call__(self, features: List[Dict[str, Union[torch.Tensor, str]]]) -> Dict[str, torch.Tensor]:
        valid_features = [f for f in features if f is not None]
        if not valid_features:
            # Return empty tensors
            return {
                 "input_ids": torch.empty((0, self.max_length or self.num_point_tokens), dtype=torch.long),
                 "attention_mask": torch.empty((0, self.max_length or self.num_point_tokens), dtype=torch.long),
                 "labels": torch.empty((0, self.max_length or self.num_point_tokens), dtype=torch.long),
                 "point_cloud": torch.empty((0, self.num_point_tokens, 3), dtype=torch.float32)
             }

        batch_pc = [f["point_cloud"] for f in valid_features]
        batch_code = [f["target_code"] for f in valid_features]

        pad_token_id = self.tokenizer.pad_token_id
        batch_size = len(valid_features)

        # 1. Tokenize the code part (<|im_start|> included) with LEFT padding
        max_code_length = self.max_length - self.num_point_tokens if self.max_length else None
        if max_code_length is not None and max_code_length <= 0:
            raise ValueError(f"Calculated max_code_length ({max_code_length}) is not positive.")

        # Tokenizer handles left padding for the code part
        tokenized_outputs = self.tokenizer(
            batch_code,
            padding="max_length" if max_code_length else "longest", # Pad to max_code_length
            max_length=max_code_length,
            truncation=True,
            return_tensors="pt",
            pad_to_multiple_of=self.pad_to_multiple_of,
            add_special_tokens=True, # Add EOS
        )
        # code_input_ids shape: (batch_size, max_code_length)
        # e.g., [ [PAD, PAD, START, T1, T2, EOS], [PAD, START, T1, T2, T3, EOS] ]
        code_input_ids = tokenized_outputs["input_ids"]
        # code_attention_mask shape: (batch_size, max_code_length)
        # e.g., [ [0,   0,   1,     1,  1,  1],   [0,   1,     1,  1,  1,  1] ]
        code_attention_mask = tokenized_outputs["attention_mask"]

        # 2. Create PC placeholders and their mask
        pc_placeholders_ids = torch.full((batch_size, self.num_point_tokens), pad_token_id, dtype=torch.long)
        pc_placeholder_mask = torch.full((batch_size, self.num_point_tokens), -1, dtype=torch.long)

        # 3. Concatenate final input_ids and attention_mask
        # Structure: [ PC_PLHDR | Padded_Code ]
        input_ids = torch.cat([pc_placeholders_ids, code_input_ids], dim=1)
        # Structure: [ -1       | 0s_and_1s ]
        attention_mask = torch.cat([pc_placeholder_mask, code_attention_mask], dim=1)

        # 4. Create Labels (Aligned with input_ids, NO shift here)
        labels = input_ids.clone()
        # Ignore PC placeholders (first num_point_tokens)
        labels[:, :self.num_point_tokens] = self.ignore_index
        # Ignore padding tokens (where final attention_mask is 0)
        labels[attention_mask == 0] = self.ignore_index

        # 5. Stack point clouds
        point_clouds_tensor = torch.stack(batch_pc)

        # Final length check (optional)
        assert input_ids.shape[1] == self.max_length, f"Warning: Final sequence length {input_ids.shape[1]} != expected max_length {self.max_length}"
        assert 0 <= input_ids.min() and input_ids.max() < len(self.tokenizer)

        return {
            "input_ids": input_ids,
            "attention_mask": attention_mask,
            "labels": labels,
            "point_cloud": point_clouds_tensor,
        }


######## TRAIN ########

if __name__ == "__main__":
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model_id = "/home/user2/wns/cad-recode/Qwen3-1.7B" # Base model
    # model_id = "filapro/cad-recode-v1.5" # Use this if you want to continue fine-tuning their model

    # Quantization Config (for QLoRA)
    # bnb_config = BitsAndBytesConfig(
    #     load_in_4bit=True,
    #     bnb_4bit_use_double_quant=True,
    #     bnb_4bit_quant_type="nf4",
    #     bnb_4bit_compute_dtype=torch.bfloat16
    # )

    # Tokenizer
    tokenizer = AutoTokenizer.from_pretrained(model_id, pad_token='<|im_end|>', padding_side='left', trust_remote_code=True)

    # Model - Load with quantization
    model = CADRecode.from_pretrained(
        model_id,
        # quantization_config=bnb_config,
        torch_dtype=torch.bfloat16, # Load in compute dtype
        attn_implementation="flash_attention_2" if torch.cuda.is_available() else None,
        device_map={'': torch.cuda.current_device()}, # Automatically distribute model layers
        trust_remote_code=True
    )

    # Prepare model for K-bit training (important for QLoRA)
    # model = prepare_model_for_kbit_training(model)
    # Enable gradient checkpointing in the base model
    model.gradient_checkpointing_enable()

    # PEFT Config (LoRA)
    peft_config = LoraConfig(
        r=64,  # Rank of LoRA matrices
        lora_alpha=16, # Scaling factor
        target_modules="all-linear", # Apply LoRA to all linear layers (common practice)
        # Or target specific modules like: ["q_proj", "k_proj", "v_proj", "o_proj", "gate_proj", "up_proj", "down_proj"]
        lora_dropout=0.1,
        bias="none",
        task_type="CAUSAL_LM",
    )
    # Apply PEFT to the model
    model = get_peft_model(model, peft_config)
    model.print_trainable_parameters()

    print("Unfreezing point_encoder parameters...")
    for name, param in model.base_model.model.point_encoder.named_parameters():
        param.requires_grad = True
        print(f"  Set requires_grad=True for: {name}")

    # Print trainable parameters *again* to verify
    print("Trainable parameters *after* unfreezing point_encoder:")
    model.print_trainable_parameters()

    # Datasets
    train_dataset = CADRecodeDataset("cad-recode-v1.5-data/train", tokenizer=tokenizer)
    eval_dataset = CADRecodeDataset("cad-recode-v1.5-data/val", tokenizer=tokenizer)

    # Data Collator
    data_collator = DataCollatorForCADRecode(
        tokenizer=tokenizer,
        max_length=MAX_SEQ_LENGTH, # Pass max sequence length
        pad_to_multiple_of=8 # Optional: for efficiency
    )

    # Trainer Args
    training_args = SFTConfig(
        output_dir="cad-recode-qwen3",
        num_train_epochs=3,
        per_device_train_batch_size=2, # Adjust based on GPU memory
        per_device_eval_batch_size=2,
        gradient_accumulation_steps=4, # Effective batch size = 8 * 2 = 16
        gradient_checkpointing=True, # Already enabled in model, TRL uses it too
        # optim="paged_adamw_32bit", # Paged optimizer for QLoRA
        learning_rate=2e-4, # Adjust as needed
        lr_scheduler_type="cosine", # Cosine scheduler is common
        max_seq_length=MAX_SEQ_LENGTH, # Set max sequence length
        logging_steps=10,
        eval_strategy="steps",
        eval_steps=50, # Evaluate less frequently
        save_strategy="steps",
        save_steps=100,
        save_total_limit=2, # Keep only the best and the latest checkpoint
        load_best_model_at_end=True,
        metric_for_best_model="eval_loss",
        greater_is_better=False,
        bf16=True, # Use bfloat16
        tf32=True, # Use TF32 on Ampere+ GPUs
        max_grad_norm=0.3,
        warmup_ratio=0.03,
        weight_decay=0.01, # Added weight decay
        push_to_hub=False, # Set to True to push checkpoints to HF Hub
        report_to="tensorboard", #"tensorboard"
        gradient_checkpointing_kwargs={"use_reentrant": False},
        # dataset_text_field="", # Not needed with custom collator handling everything
        dataset_kwargs={"skip_prepare_dataset": True}, # Crucial
        remove_unused_columns=False, # Important: Keep point_cloud column
    )

    # wandb.init(
    #     project="CADRecode",
    #     name="cad-recode",
    #     config=training_args,
    # )

    trainer = SFTTrainer(
        model=model,
        args=training_args,
        train_dataset=train_dataset,
        eval_dataset=eval_dataset,
        data_collator=data_collator, # Use the custom collator
        peft_config=peft_config, # Pass PEFT config
        # dataset_text_field="target_code", # Not strictly needed if collator handles tokenization
    )

    print("Starting training...")
    trainer.train()

    # Save the final adapter model
    print("Saving final adapter model...")
    trainer.save_model("cad-recode-finetuned-final")
    tokenizer.save_pretrained("cad-recode-finetuned-final")