from typing import Literal
import json, os
import numpy as np
import torch
import torch.nn as nn
import trimesh
from peft import PeftModel, LoraConfig, get_peft_model
from pytorch3d.ops import sample_farthest_points
from scipy.spatial import cKDTree
from tqdm import tqdm
from transformers import (
    AutoTokenizer, Qwen2ForCausalLM, Qwen2Model, PreTrainedModel, AutoModelForCausalLM)
from transformers.modeling_outputs import CausalLMOutputWithPast


class FourierPointEncoder(nn.Module):
    def __init__(self, hidden_size):
        super().__init__()
        frequencies = 2.0 ** torch.arange(8, dtype=torch.float32)
        self.register_buffer('frequencies', frequencies, persistent=False)
        self.projection = nn.Linear(51, hidden_size)

    def forward(self, points):
        x = points
        x = (x.unsqueeze(-1) * self.frequencies).view(*x.shape[:-1], -1)
        x = torch.cat((points, x.sin(), x.cos()), dim=-1)
        x = x.to(self.projection.weight.dtype)
        x = self.projection(x)
        return x


class CADRecode(Qwen2ForCausalLM):
    def __init__(self, config):
        PreTrainedModel.__init__(self, config)
        self.model = Qwen2Model(config)
        self.vocab_size = config.vocab_size
        self.lm_head = nn.Linear(config.hidden_size, config.vocab_size, bias=False)

        torch.set_default_dtype(torch.float32)
        self.point_encoder = FourierPointEncoder(config.hidden_size)
        torch.set_default_dtype(torch.bfloat16)

    def forward(self,
                input_ids=None,
                attention_mask=None,
                point_cloud=None,
                position_ids=None,
                past_key_values=None,
                inputs_embeds=None,
                labels=None,
                use_cache=None,
                output_attentions=None,
                output_hidden_states=None,
                return_dict=None,
                cache_position=None):
        output_attentions = output_attentions if output_attentions is not None else self.config.output_attentions
        output_hidden_states = output_hidden_states if output_hidden_states is not None else self.config.output_hidden_states
        return_dict = return_dict if return_dict is not None else self.config.use_return_dict

        # concatenate point and text embeddings
        if past_key_values is None or past_key_values.get_seq_length() == 0:
            assert inputs_embeds is None
            inputs_embeds = self.model.embed_tokens(input_ids)
            point_embeds = self.point_encoder(point_cloud).bfloat16()
            inputs_embeds[attention_mask == -1] = point_embeds.reshape(-1, point_embeds.shape[2])
            attention_mask[attention_mask == -1] = 1
            input_ids = None
            position_ids = None

        # decoder outputs consists of (dec_features, layer_state, dec_hidden, dec_attn)
        outputs = self.model(
            input_ids=input_ids,
            attention_mask=attention_mask,
            position_ids=position_ids,
            past_key_values=past_key_values,
            inputs_embeds=inputs_embeds,
            use_cache=use_cache,
            output_attentions=output_attentions,
            output_hidden_states=output_hidden_states,
            return_dict=return_dict,
            cache_position=cache_position)

        hidden_states = outputs[0]
        logits = self.lm_head(hidden_states)
        logits = logits.float()

        loss = None
        if labels is not None:
            # Shift so that tokens < n predict n
            shift_logits = logits[..., :-1, :].contiguous()
            shift_labels = labels[..., 1:].contiguous()
            # Flatten the tokens
            loss_fct = nn.CrossEntropyLoss()
            shift_logits = shift_logits.view(-1, self.config.vocab_size)
            shift_labels = shift_labels.view(-1)
            # Enable model parallelism
            shift_labels = shift_labels.to(shift_logits.device)
            loss = loss_fct(shift_logits, shift_labels)

        if not return_dict:
            output = (logits,) + outputs[1:]
            return (loss,) + output if loss is not None else output

        return CausalLMOutputWithPast(
            loss=loss,
            logits=logits,
            past_key_values=outputs.past_key_values,
            hidden_states=outputs.hidden_states,
            attentions=outputs.attentions)

    def prepare_inputs_for_generation(self, *args, **kwargs):
        model_inputs = super().prepare_inputs_for_generation(*args, **kwargs)
        model_inputs['point_cloud'] = kwargs['point_cloud']
        return model_inputs


class Fusion360EvalDataset(torch.utils.data.Dataset):
    def __init__(self, fusion360_root: str, num_points: int = 256, num_pre_points: int = 8192) -> None:
        self.data = []
        with open(os.path.join(fusion360_root, f"train_test.json"), 'r') as f:
            uuid_list = json.load(f)["test"]
        for uuid in uuid_list:


            # if uuid != "100155_57ec5fc6_0000":
            #     continue


            self.data.append({
                "uuid": uuid,
                "gt_mesh": os.path.join(fusion360_root, "reconstruction", f"{uuid}.obj"),
            })

        self.data.sort(key=lambda d: d["uuid"]) # Sort by uuid
        self.num_points = num_points
        self.num_pre_points = num_pre_points
        print(f"[Fusion360EvalDataset] Total data num: {len(self.data)}")

    @staticmethod
    def mesh_to_point_cloud(mesh, n_points: int, n_pre_points: int, seed: int = 0):
        vertices, _ = trimesh.sample.sample_surface(mesh, n_pre_points)#, seed=seed)
        if len(vertices) < n_points:
            raise ValueError(f"Mesh doesn't have enough vertices: {len(vertices)}=")

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
        data = self.data[idx]
        uuid = data["uuid"]

        # load GT mesh
        gt_mesh = trimesh.load_mesh(data["gt_mesh"])
        if isinstance(gt_mesh, trimesh.Scene): # Handle scenes if necessary
            print(f"Warning: Loaded a trimesh.Scene for {uuid}. Attempting to extract geometry.")
            # Simple approach: combine all geometries
            gt_mesh = gt_mesh.dump(concatenate=True)
            if not isinstance(gt_mesh, trimesh.Trimesh) or len(gt_mesh.vertices) == 0:
                raise ValueError(f"Warning: Loaded empty or invalid mesh for UUID {uuid}.")

        # normalize mesh
        center = gt_mesh.bounds[0] + (gt_mesh.bounds[1] - gt_mesh.bounds[0]) / 2.0
        gt_mesh.apply_translation(-center)
        scale = 2.0 / max(gt_mesh.extents) if max(gt_mesh.extents) > 1e-6 else 1.0 # Avoid division by zero
        gt_mesh.apply_scale(scale)

        # sample points
        np.random.seed(0)
        point_cloud = self.mesh_to_point_cloud(gt_mesh, self.num_points, self.num_pre_points)
        if point_cloud is None:
            RuntimeError(f"Failed to generate point cloud for: {uuid}")

        return {
            "uuid": uuid,
            "point_cloud": point_cloud,
            "gt_mesh": gt_mesh,
        }


if __name__ == '__main__':
    # device = 'cuda' if torch.cuda.is_available() else 'cpu'
    # attn_implementation = 'flash_attention_2' if torch.cuda.is_available() else None
    # tokenizer = AutoTokenizer.from_pretrained(
    #     '/home/user2/wns/cad-recode/Qwen2-1.5B',
    #     pad_token='<|im_end|>',
    #     padding_side='left')
    # model = CADRecode.from_pretrained(
    #     '/home/user2/wns/cad-recode/cad-recode-v1.5',
    #     torch_dtype=torch.bfloat16,
    #     attn_implementation=attn_implementation).eval().to(device)
    # model.to(torch.bfloat16)
    # CHECKPOINT_DIR = "cad-recode-dpo-lr1e-06-final"
    # model = CADRecode.from_pretrained(
    #     CHECKPOINT_DIR,
    #     torch_dtype=torch.bfloat16,
    # ).eval().to(device)
    BASE_MODEL_PATH = '/home/user2/wns/cad-recode/Qwen3-1.7B'
    CHECKPOINT_DIR = '/home/user2/wns/cad-recode/cad-recode-qwen3/checkpoint-68200' 
    POINT_ENCODER_WEIGHTS_PATH = os.path.join(CHECKPOINT_DIR, "point_encoder_weights.bin")

    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    attn_implementation = 'flash_attention_2' if torch.cuda.is_available() else None

    print(f"Loading full model from checkpoint: {CHECKPOINT_DIR}")

    tokenizer = AutoTokenizer.from_pretrained(
        BASE_MODEL_PATH,
        pad_token='<|im_end|>',
        padding_side='left',
        trust_remote_code=True
    )
    print(f"Tokenizer loaded from: {BASE_MODEL_PATH}")

    print(f"Loading base LLM (Qwen3ForCausalLM) from: {BASE_MODEL_PATH}")
    base_llm = AutoModelForCausalLM.from_pretrained(
        BASE_MODEL_PATH,
        torch_dtype=torch.bfloat16, 
        attn_implementation=attn_implementation,
        trust_remote_code=True
    )
    print("Base LLM loaded.")

    print("Instantiating CADRecode model structure (initially random weights for Qwen and point_encoder)...")
    model = CADRecode(base_llm.config) 

    model.model = base_llm.model
    model.lm_head = base_llm.lm_head
    print("Base LLM's core model and lm_head assigned to CADRecode instance.")

    peft_config_for_loading = LoraConfig(
        r=64,
        lora_alpha=16,
        target_modules=[
            "q_proj", "k_proj", "v_proj", "o_proj", 
            "gate_proj", "up_proj", "down_proj"
        ], 
        lora_dropout=0.1,
        bias="none",
        task_type="CAUSAL_LM",
    )

    print("Applying PEFT LoRA to the CADRecode model structure (only Qwen layers will be wrapped)...")
    model = get_peft_model(model, peft_config_for_loading) 
    print("CADRecode model (now a PeftModelForCausalLM) prepared.")

    print(f"Loading LoRA adapters for base LLM layers from: {CHECKPOINT_DIR}")
    model.load_adapter(CHECKPOINT_DIR, adapter_name="default")
    print("LoRA adapters for base LLM layers loaded.")

    print(f"Attempting to load point_encoder weights from: {POINT_ENCODER_WEIGHTS_PATH}")
    if os.path.exists(POINT_ENCODER_WEIGHTS_PATH):
        point_encoder_state_dict = torch.load(POINT_ENCODER_WEIGHTS_PATH, map_location='cpu')
        
        model.base_model.model.point_encoder.load_state_dict(point_encoder_state_dict, strict=True) 
        print("Point_encoder weights loaded successfully.")
    else:
        print(f"Error: {POINT_ENCODER_WEIGHTS_PATH} not found. 'point_encoder' will be randomly initialized.")
        print("Please ensure the specified CHECKPOINT_DIR contains 'point_encoder_weights.bin'.")

    model.eval().to(device)
    print("Full model (CADRecode with Qwen3-1.7B + LoRA + trained point_encoder) ready for inference.")


    fusion360_dataset = Fusion360EvalDataset("/home/user2/wns/cad-recode/r1.0.1")
    eval_summary = {}
    invalid_gt_num = 0
    invalid_pred_num = 0

    for i, data in enumerate(tqdm(fusion360_dataset)):
        uuid = data["uuid"]
        point_cloud = data["point_cloud"]
        gt_mesh = data["gt_mesh"]

        input_ids = [tokenizer.pad_token_id] * len(point_cloud) + [tokenizer('<|im_start|>')['input_ids'][0]]
        attention_mask = [-1] * len(point_cloud) + [1]
        with torch.no_grad():
            batch_ids = model.generate(
                input_ids=torch.tensor(input_ids).unsqueeze(0).to(model.device),
                attention_mask=torch.tensor(attention_mask).unsqueeze(0).to(model.device),
                point_cloud=torch.tensor(point_cloud.astype(np.float32)).unsqueeze(0).to(model.device),
                max_new_tokens=768,
                pad_token_id=tokenizer.pad_token_id)
        py_string = tokenizer.batch_decode(batch_ids)[0]
        begin = py_string.find('<|im_start|>') + 12
        end = py_string.find('<|endoftext|>')
        py_string = py_string[begin: end]
        print("Output:", py_string)

        try:
            exec(py_string, globals())
            compound = globals()['r'].val()
            vertices, faces = compound.tessellate(0.001, 0.1)
            pred_mesh = trimesh.Trimesh([(v.x, v.y, v.z) for v in vertices], faces)

            pred_mesh.apply_transform(trimesh.transformations.scale_matrix(1 / 100 / 2))
            pred_mesh.apply_transform(trimesh.transformations.translation_matrix([0.5, 0.5, 0.5]))
            gt_mesh.apply_transform(trimesh.transformations.scale_matrix(1 / 2))
            gt_mesh.apply_transform(trimesh.transformations.translation_matrix([0.5, 0.5, 0.5]))

            n_points = 8192
            gt_points, _ = trimesh.sample.sample_surface(gt_mesh, n_points, seed=0)
            pred_points, _ = trimesh.sample.sample_surface(pred_mesh, n_points, seed=0)

            gt_distance, _ = cKDTree(gt_points).query(pred_points, k=1)
            pred_distance, _ = cKDTree(pred_points).query(gt_points, k=1)
            cd = np.mean(np.square(gt_distance)) + np.mean(np.square(pred_distance))

            # Ensure meshes are suitable for boolean operations (see step 1)
            if not gt_mesh.is_volume:
                gt_mesh.process(validate=True)
            if not pred_mesh.is_volume:
                pred_mesh.process(validate=True)

            if not gt_mesh.is_volume:
                raise KeyError("GT mesh is not a volume, cannot calculate reliable intersection.")
            if not pred_mesh.is_volume:
                raise ValueError("Pred mesh is not a volume, cannot calculate reliable intersection.")

            # Calculate the intersection *mesh*
            intersection_mesh = gt_mesh.intersection(pred_mesh)

            # Calculate the volume *from* the intersection mesh
            # Check if the intersection is empty or invalid before getting volume
            if intersection_mesh is not None and not intersection_mesh.is_empty:
                # Sometimes boolean ops can create non-volume results, check again
                if not intersection_mesh.is_volume:
                    # Attempt quick fix, may not always work
                    intersection_mesh.process(validate=True)
                intersection_volume = intersection_mesh.volume
                # Add a small tolerance check for negative volumes which can indicate issues
                if intersection_volume < -1e-6:
                    print(f"Warning: Negative intersection volume ({intersection_volume}), likely issue with boolean op.")
                    intersection_volume = 0.0
                elif intersection_volume < 0:
                    intersection_volume = 0.0 # Clamp small negative noise to zero
            else:
                intersection_volume = 0.0

            # Get volumes of original meshes
            gt_volume = gt_mesh.volume
            pred_volume = pred_mesh.volume

            # Calculate union volume using inclusion-exclusion
            union_volume = gt_volume + pred_volume - intersection_volume

            # Calculate IoU, handle potential division by zero
            if union_volume > 1e-6: # Use a small tolerance
                iou = intersection_volume / union_volume
            else:
                # If union is zero, IoU is 1 if intersection is also zero (both empty), else 0
                iou = 1.0 if intersection_volume < 1e-6 else 0.0

            eval_summary[uuid] = {"CD": cd * 1000, "IoU": iou, "pred": py_string}
        except KeyError as e:
            print(f"Error ({uuid}):", e)
            invalid_gt_num += 1
            invalid_pred_num += 1
            eval_summary[uuid] = {"CD": None, "IoU": None, "pred": py_string}
            continue
        except Exception as e:
            print(f"Error ({uuid}):", e)
            invalid_pred_num += 1
            eval_summary[uuid] = {"CD": None, "IoU": None, "pred": py_string}
            continue

        # if i >= 10: break

    CDs = np.array([x["CD"] for x in eval_summary.values() if x["CD"] is not None])
    IoUs = np.array([x["IoU"] for x in eval_summary.values() if x["IoU"] is not None])
    print("======== Summary ========")
    print(f"CD mean: {np.mean(CDs)}")
    print(f"CD median: {np.median(CDs)}")
    print(f"IoU mean: {np.mean(IoUs)}")
    print(f"Invalid preds: {invalid_pred_num} / {len(fusion360_dataset)} (within which {invalid_gt_num} GTs are invalid)")

    with open("eval results.json", "w") as f:
        json.dump(eval_summary, f, indent=4)