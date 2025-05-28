import json
import os
import tempfile
from dataclasses import dataclass, field
from typing import Dict, List, Literal, Optional, Tuple, Union

import cadquery as cq
import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
import trimesh
import tensorboard
from datasets import Dataset, Features, Value, Sequence, Array2D
from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training
from pytorch3d.ops import sample_farthest_points
from transformers.models.auto.tokenization_auto import AutoTokenizer
from transformers.utils.quantization_config import BitsAndBytesConfig
from transformers.models.qwen2.modeling_qwen2 import Qwen2ForCausalLM
from transformers.modeling_outputs import CausalLMOutputWithPast
from transformers.tokenization_utils_base import PreTrainedTokenizerBase
from trl import DPOConfig, DPOTrainer
from trl.trainer.utils import flush_left, pad, pad_to_length, selective_log_softmax
######## CONFIG ########
NUM_POINT_TOKENS = 256 # As mentioned in paper Sec 4.3
MAX_CODE_TOKENS = 768 # Adjust based on your dataset analysis
MAX_SEQ_LENGTH = NUM_POINT_TOKENS + MAX_CODE_TOKENS # Set max_seq_length in TraiiningConfig
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


class CADRecode(Qwen2ForCausalLM):
    def __init__(self, config):
        super().__init__(config) # Call Qwen2ForCausalLM's __init__

        # Store hidden_size explicitly if needed elsewhere, otherwise use config.hidden_size
        self._hidden_size = config.hidden_size
        self.num_point_tokens = NUM_POINT_TOKENS
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

            # 3. Combine Embeddings: [Point | Code]
            inputs_embeds = torch.cat([point_embeds, code_embeds], dim=1)

            # 4. Adjust Attention Mask (replace -1 with 1)
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

    def prepare_inputs_for_generation(self, input_ids, past_key_values=None, inputs_embeds=None, point_cloud=None, attention_mask=None, **kwargs):
        # Standard logic from base class
        model_inputs = super().prepare_inputs_for_generation(input_ids, past_key_values=past_key_values, inputs_embeds=inputs_embeds, attention_mask=attention_mask, **kwargs)

        if past_key_values is None:
             model_inputs['point_cloud'] = point_cloud
        else:
             model_inputs['point_cloud'] = None # Not needed after first step

        model_inputs['attention_mask'] = attention_mask

        return model_inputs
######## DATASETS ########
class Fusion360DPODataset(torch.utils.data.Dataset):
    def __init__(self, data_root: str, split: Literal["train", "validation"], num_points=NUM_POINT_TOKENS, num_pre_points=8192) -> None:
        self.data = []
        # train_test.json 文件应位于 data_root 中
        split_file_path = os.path.join(data_root, "train_val.json")
        try:
            with open(split_file_path, 'r') as f:
                # JSON包含一个字典，键是拆分 ("train", "validation")
                # 值是标识符列表 (例如 "train_batch_63_630020")
                identifiers_list = json.load(f)[split]
        except FileNotFoundError:
            print(f"错误：拆分文件 {split_file_path} 未找到。")
            raise
        except KeyError:
            print(f"错误：拆分 '{split}' 在 {split_file_path} 中未找到。")
            raise

        for identifier in identifiers_list:
            winner_path = os.path.join(data_root, "cadquery", f"{identifier}_winner.py")
            loser_path = os.path.join(data_root, "cadquery", f"{identifier}_loser.py")
            # GT 网格是位于 'reconstruction' 子目录中的 STL 文件
            gt_mesh_path = os.path.join(data_root, "reconstruction", f"{identifier}.stl")

            if os.path.isfile(winner_path) and os.path.isfile(loser_path) and os.path.isfile(gt_mesh_path):
                self.data.append({
                    "identifier": identifier, # 存储标识符
                    "gt_mesh_path": gt_mesh_path,
                    "winner_path": winner_path,
                    "loser_path": loser_path,
                })
            # else:
                # 在 dpo_generator 中记录跳过的样本总数，这里可以减少冗余打印
                # print(f"警告: 标识符 {identifier} 的文件缺失。将跳过。")

        print(f"[dpo_dataset] 在 {data_root} 中为拆分 '{split}' 找到 {len(self.data)}/{len(identifiers_list)} 个有效样本。")
        if not self.data and identifiers_list: # 如果列表不为空但没有加载数据，说明有问题
             print(f"警告：拆分 '{split}' 没有加载任何数据，尽管 train_test.json 中有条目。请检查路径和文件是否存在。")


        self.data.sort(key=lambda d: d["identifier"]) # 按标识符排序
        self.num_points = num_points
        self.num_pre_points = num_pre_points
        self.im_start_token = "<|im_start|>"

    def mesh_to_point_cloud(self, mesh: trimesh.Trimesh, n_points: int, n_pre_points: int) -> Optional[np.ndarray]:
        if not isinstance(mesh, trimesh.Trimesh) or mesh.is_empty or len(mesh.vertices) == 0:
            return None

        if len(mesh.vertices) < n_pre_points:
            n_pre_points = len(mesh.vertices)
        if n_pre_points == 0:
            return None

        try:
            vertices, _ = trimesh.sample.sample_surface(mesh, n_pre_points)
        except Exception:
            return None
        if len(vertices) == 0:
            return None

        current_num_vertices = len(vertices)
        target_n_points = n_points # 保存原始请求的点数以供最终检查

        if current_num_vertices < target_n_points:
            # 如果严格要求原始 n_points，则返回 None；否则调整 n_points
            # 对于 DPO，我们希望点云维度一致，所以如果不能满足 self.num_points，则跳过
            return None # 或者调整 n_points = current_num_vertices，但这会导致数据维度不一致

        # 如果调整后的 n_points (或原始n_points) 等于预采样点数，则直接从预采样点中选择
        if n_pre_points == target_n_points:
            if current_num_vertices < target_n_points: return None
            indices = np.random.choice(current_num_vertices, target_n_points, replace=False)
            sampled_points = np.asarray(vertices[indices], dtype=np.float32)
        else:
            if target_n_points > current_num_vertices : return None # K > N for FPS
            try:
                points_tensor = torch.tensor(vertices, dtype=torch.float32).unsqueeze(0)
                if points_tensor.shape[1] == 0: return None
                # 确保 K (target_n_points) 不大于 N (points_tensor.shape[1])
                k_for_fps = min(target_n_points, points_tensor.shape[1])
                if k_for_fps == 0 : return None
                if k_for_fps < target_n_points: # 如果 FPS 无法采样到 target_n_points
                    return None

                _, ids = sample_farthest_points(points_tensor, K=k_for_fps)
                sampled_points = np.asarray(vertices[ids[0].cpu().numpy()], dtype=np.float32)
            except Exception:
                return None
        
        # 最终检查点数是否与类属性 num_points 一致
        if sampled_points.shape[0] != self.num_points:
            return None
        return sampled_points

    def __len__(self) -> int:
        return len(self.data)

    def __getitem__(self, idx: int) -> Optional[Dict]:
        item_meta = self.data[idx] # 重命名以避免与最终返回的 item 混淆
        identifier = item_meta["identifier"]

        try:
            with open(item_meta["winner_path"], 'r') as f:
                winner_code = f.read()
            with open(item_meta["loser_path"], 'r') as f:
                loser_code = f.read()

            # 加载 GT 网格 (.stl)
            gt_mesh = trimesh.load_mesh(item_meta["gt_mesh_path"])

            if isinstance(gt_mesh, trimesh.Scene):
                if not gt_mesh.geometry: return None # 场景为空
                # 尝试合并场景中的所有 Trimesh 对象
                valid_geometries = [g for g in gt_mesh.geometry.values() if isinstance(g, trimesh.Trimesh) and not g.is_empty]
                if not valid_geometries: return None # 场景中没有有效的 Trimesh 对象
                gt_mesh = trimesh.util.concatenate(valid_geometries)
            
            if not isinstance(gt_mesh, trimesh.Trimesh) or gt_mesh.is_empty or len(gt_mesh.vertices) == 0:
                return None

            # 归一化网格
            if gt_mesh.bounds is None or max(gt_mesh.extents) <= 1e-9: # 使用更小的阈值并检查 bounds
                 return None # 无法安全归一化
            
            center = gt_mesh.centroid
            gt_mesh.apply_translation(-center)
            scale = 2.0 / max(gt_mesh.extents) # 此时 max(gt_mesh.extents) > 0
            gt_mesh.apply_scale(scale)

            # 采样点云
            point_cloud = self.mesh_to_point_cloud(gt_mesh, self.num_points, self.num_pre_points)

            if point_cloud is None:
                return None
            
            # 确保返回的点云数量严格等于 self.num_points
            if point_cloud.shape[0] != self.num_points:
                return None

        except Exception: # 捕获任何未预料到的错误
            # print(f"错误: 处理样本 {identifier} 时发生意外错误: {e}") # 可以在 generator 中统一处理日志
            return None

        return {
            "uuid": identifier, # 保持 'uuid' 作为键名以兼容下游代码
            "point_cloud": point_cloud,
            "prompt": self.im_start_token,
            "chosen": winner_code,
            "rejected": loser_code,
            "winner_code": f"{self.im_start_token}{winner_code}",
            "loser_code": f"{self.im_start_token}{loser_code}",
        }

def dpo_generator(data_root: str, split: Literal["train", "validation"], num_points: int, num_pre_points: int):
    # 在内部实例化原始的 PyTorch 数据集
    # data_root 是类似 "/home/user2/wns/cad-recode/dpo_data" 的路径
    pytorch_dataset = Fusion360DPODataset(data_root, split, num_points, num_pre_points)
    
    if not pytorch_dataset.data: # 如果数据集为空
        print(f"警告: dpo_generator 未能从 {data_root} 为拆分 '{split}' 加载任何数据。")
        return # 产生一个空的迭代器

    skipped_count = 0
    total_count = len(pytorch_dataset)

    for i in range(total_count):
        try:
            item = pytorch_dataset[i] # __getitem__ 现在可以返回 None
            if item is not None:
                yield item
            else:
                skipped_count += 1
        except Exception:
            # 理论上 __getitem__ 应该自己处理异常并返回 None，但这里再加一层保险
            skipped_count += 1
            # print(f"警告: dpo_generator 在处理来自 {data_root} 的样本时捕获到意外异常并跳过。")
            continue
    
    if skipped_count > 0:
        print(f"信息: dpo_generator 在拆分 '{split}' 的 {total_count} 个总样本中，跳过了 {skipped_count} 个样本。")
    if skipped_count == total_count and total_count > 0:
        print(f"警告: dpo_generator 跳过了拆分 '{split}' 中的所有样本。请检查数据质量和处理逻辑。")




@dataclass
class DataCollatorForDPOCADRecode:
    tokenizer: PreTrainedTokenizerBase
    max_length: Optional[int] = None
    pad_to_multiple_of: Optional[int] = None
    num_point_tokens: int = NUM_POINT_TOKENS

    def __post_init__(self):
        if self.tokenizer.padding_side != 'left':
            raise ValueError("Tokenizer must be initialized with padding_side='left'.")
        if self.tokenizer.pad_token_id is None:
            raise ValueError("Tokenizer must have a pad_token_id set.")
        self.pad_token_id = tokenizer.pad_token_id

    def __call__(self, examples: list[dict[str, Union[list, str]]]) -> Dict[str, torch.Tensor]:
        """
        Because of the trainer's _prepare_dataset, the data is modified into the folowing format:
            features[i] = {
                "uuid": str,
                "point_cloud": list[tuple[float, float, float]],
                "prompt_input_id": list[int] (usually length = 1, corresponding to <|im_start|>),
                "chosen_input_ids": list[int],
                "rejected_input_ids": list[int],
                "winner_code": str,
                "loser_code": str,
            }
        In the above, the tokenizer is already applied, EOS is appended, but the padding is not applied.
        """
        batch_size = len(examples)

        # Convert to tensor
        prompt_input_ids = [torch.tensor(example["prompt_input_ids"]) for example in examples]
        prompt_attention_mask = [torch.ones_like(input_ids) for input_ids in prompt_input_ids]
        chosen_input_ids = [torch.tensor(example["chosen_input_ids"]) for example in examples]
        chosen_attention_mask = [torch.ones_like(input_ids) for input_ids in chosen_input_ids]
        rejected_input_ids = [torch.tensor(example["rejected_input_ids"]) for example in examples]
        rejected_attention_mask = [torch.ones_like(input_ids) for input_ids in rejected_input_ids]
        batch_pc = [torch.tensor(f["point_cloud"]) for f in examples]

        # Pad
        output = {}
        output["prompt_input_ids"] = pad(prompt_input_ids, padding_value=self.pad_token_id, padding_side="left")
        output["prompt_attention_mask"] = pad(prompt_attention_mask, padding_value=0, padding_side="left")
        output["chosen_input_ids"] = pad(chosen_input_ids, padding_value=self.pad_token_id)
        output["chosen_attention_mask"] = pad(chosen_attention_mask, padding_value=0)
        output["rejected_input_ids"] = pad(rejected_input_ids, padding_value=self.pad_token_id)
        output["rejected_attention_mask"] = pad(rejected_attention_mask, padding_value=0)
        assert output["prompt_input_ids"].shape == (batch_size, 1)

        # Prepend PC placeholders and their mask
        pc_placeholders_ids = torch.full((batch_size, self.num_point_tokens), self.pad_token_id, dtype=torch.long)
        pc_placeholder_mask = torch.full((batch_size, self.num_point_tokens), 1, dtype=torch.long)  # If set -1, QWen2 throwns an error

        output["prompt_input_ids"] = torch.cat([pc_placeholders_ids, output["prompt_input_ids"]], dim=1)
        output["prompt_attention_mask"] = torch.cat([pc_placeholder_mask, output["prompt_attention_mask"]], dim=1)

        # Stack point clouds
        point_clouds_tensor = torch.stack(batch_pc)
        if point_clouds_tensor.shape != (batch_size, self.num_point_tokens, 3): # Assuming 3D points
             raise ValueError(f"Unexpected point_cloud tensor shape: {point_clouds_tensor.shape}. Expected: {(batch_size, self.num_point_tokens, 3)}")

        output["point_cloud"] = point_clouds_tensor

        return output
######## TRAINER ########

class CADRecodeDPOTrainer(DPOTrainer):

    @staticmethod
    def concatenated_inputs(
            batch: dict[str, Union[list, torch.LongTensor]], padding_value: int,
        ) -> dict[str, torch.LongTensor]:
        output = {}

        # For the prompt, the input_ids are the same for both the chosen and rejected responses
        output["prompt_input_ids"] = torch.cat([batch["prompt_input_ids"], batch["prompt_input_ids"]], dim=0)
        output["prompt_attention_mask"] = torch.cat(
            [batch["prompt_attention_mask"], batch["prompt_attention_mask"]], dim=0
        )
        if "pixel_values" in batch:
            output["pixel_values"] = torch.cat([batch["pixel_values"], batch["pixel_values"]], dim=0)

        if "pixel_attention_mask" in batch:
            output["pixel_attention_mask"] = torch.cat(
                [batch["pixel_attention_mask"], batch["pixel_attention_mask"]], dim=0
            )
        if "image_sizes" in batch:
            output["image_sizes"] = torch.cat([batch["image_sizes"], batch["image_sizes"]], dim=0)

        # Concatenate the chosen and rejected completions
        max_completion_length = max(batch["chosen_input_ids"].shape[1], batch["rejected_input_ids"].shape[1])
        output["completion_input_ids"] = torch.cat(
            (
                pad_to_length(batch["chosen_input_ids"], max_completion_length, pad_value=padding_value),
                pad_to_length(batch["rejected_input_ids"], max_completion_length, pad_value=padding_value),
            ),
        )
        output["completion_attention_mask"] = torch.cat(
            (
                pad_to_length(batch["chosen_attention_mask"], max_completion_length, pad_value=0),
                pad_to_length(batch["rejected_attention_mask"], max_completion_length, pad_value=0),
            ),
        )

        # add point cloud
        output["point_cloud"] = torch.cat([batch["point_cloud"], batch["point_cloud"]], dim=0)

        return output

    def concatenated_forward(self, model: nn.Module, batch: dict[str, Union[list, torch.LongTensor]]):
        """Run the given model on the given batch of inputs, concatenating the chosen and rejected inputs together.

        We do this to avoid doing two forward passes, because it's faster for FSDP.
        """
        num_examples = batch["prompt_input_ids"].shape[0]

        concatenated_batch = self.concatenated_inputs(batch, padding_value=self.padding_value)

        model_kwargs = {"point_cloud": concatenated_batch["point_cloud"]}  # NOTE: CHANGED HERE!!!
        if self.aux_loss_enabled:
            model_kwargs["output_router_logits"] = True

        # Add the pixel values and attention masks for vision models
        if "pixel_values" in concatenated_batch:
            model_kwargs["pixel_values"] = concatenated_batch["pixel_values"]
        if "pixel_attention_mask" in concatenated_batch:
            model_kwargs["pixel_attention_mask"] = concatenated_batch["pixel_attention_mask"]
        if "image_sizes" in concatenated_batch:
            model_kwargs["image_sizes"] = concatenated_batch["image_sizes"]

        prompt_input_ids = concatenated_batch["prompt_input_ids"]
        prompt_attention_mask = concatenated_batch["prompt_attention_mask"]
        completion_input_ids = concatenated_batch["completion_input_ids"]
        completion_attention_mask = concatenated_batch["completion_attention_mask"]
        if self.is_encoder_decoder:
            labels = completion_input_ids
            labels[completion_attention_mask == 0] = self.label_pad_token_id
            outputs = model(
                input_ids=prompt_input_ids,
                attention_mask=prompt_attention_mask,
                labels=labels,  # we need the labels for the logits to be returned
                **model_kwargs,
            )
            logits = outputs.logits
            loss_mask = completion_attention_mask.bool()
        else:
            # Concatenate the prompt and completion inputs
            input_ids = torch.cat((prompt_input_ids, completion_input_ids), dim=1)
            attention_mask = torch.cat((prompt_attention_mask, completion_attention_mask), dim=1)
            # Mask the prompt but not the completion for the loss
            loss_mask = torch.cat(
                (torch.zeros_like(prompt_attention_mask), completion_attention_mask),
                dim=1,
            )

            attention_mask, input_ids, loss_mask = flush_left(attention_mask, input_ids, loss_mask)

            # Truncate right
            if self.max_length is not None:
                if self.truncation_mode == "keep_end":
                    input_ids = input_ids[:, -self.max_length :]
                    attention_mask = attention_mask[:, -self.max_length :]
                    loss_mask = loss_mask[:, -self.max_length :]
                elif self.truncation_mode == "keep_start":
                    input_ids = input_ids[:, : self.max_length]
                    attention_mask = attention_mask[:, : self.max_length]
                    loss_mask = loss_mask[:, : self.max_length]
                else:
                    raise ValueError(
                        f"Unknown truncation mode: '{self.truncation_mode}'. Should be one of ['keep_end', "
                        "'keep_start']."
                    )

            if self.use_logits_to_keep:

                first_compute_index = loss_mask.nonzero(as_tuple=True)[1].min()
                logits_to_keep = (loss_mask.shape[1] - first_compute_index).item() + 1  # +1 for the first label
                model_kwargs["logits_to_keep"] = logits_to_keep

            if self.padding_free:

                input_ids = input_ids[attention_mask.bool()].unsqueeze(0)
                loss_mask = loss_mask[attention_mask.bool()].unsqueeze(0)
                position_ids = attention_mask.cumsum(1)[attention_mask.bool()].unsqueeze(0) - 1
                model_kwargs["position_ids"] = position_ids
            else:
                model_kwargs["attention_mask"] = attention_mask
            outputs = model(input_ids, **model_kwargs)
            logits = outputs.logits

            # Offset the logits by one to align with the labels
            labels = torch.roll(input_ids, shifts=-1, dims=1)
            loss_mask = torch.roll(loss_mask, shifts=-1, dims=1).bool()

            if self.use_logits_to_keep:

                labels = labels[:, -logits_to_keep:]
                loss_mask = loss_mask[:, -logits_to_keep:]

        if logits.shape[:2] != labels.shape[:2]:
            # for llava, the returned logits include the image tokens (placed before the text tokens)
            seq_len = labels.shape[1]
            logits = logits[:, -seq_len:]

        # Compute the log probabilities of the labels
        labels[~loss_mask] = 0  # dummy token; we'll ignore the losses on these tokens later
        per_token_logps = selective_log_softmax(logits, labels)
        per_token_logps[~loss_mask] = 0
        per_token_logps = torch.roll(per_token_logps, shifts=1, dims=1)

        if self.padding_free:
            # Unflatten the per_token_logps (shape: [1, sum_seq_len] -> [batch_size, seq_len])
            batch_size, seq_len = attention_mask.shape
            per_token_logps_ = torch.zeros(
                batch_size, seq_len, device=outputs.logits.device, dtype=outputs.logits.dtype
            )
            per_token_logps_[attention_mask.bool()] = per_token_logps
            per_token_logps = per_token_logps_

        all_logps = per_token_logps.sum(-1)

        output = {}

        if self.use_weighting:
            with torch.no_grad():
                # Eq (2) of the WPO paper: https://huggingface.co/papers/2406.11827
                logprobs = F.log_softmax(logits, dim=-1)
                weights_adjustment_factor = torch.logsumexp(2 * logprobs, dim=-1)  # same as sum(probs**2) in log space
                per_token_logps_adjusted = per_token_logps - weights_adjustment_factor
                all_weights = (per_token_logps_adjusted * loss_mask).sum(-1) / loss_mask.sum(-1)
                chosen_weights = all_weights[:num_examples]
                rejected_weights = all_weights[num_examples:]
                output["policy_weights"] = torch.clamp(torch.exp(chosen_weights + rejected_weights), max=1)

        if self.args.rpo_alpha is not None:
            # Only use the chosen logits for the RPO loss
            chosen_logits = logits[:num_examples]
            chosen_labels = labels[:num_examples]

            # Compute the log probabilities of the labels
            output["nll_loss"] = F.cross_entropy(
                torch.flatten(chosen_logits, end_dim=1), torch.flatten(chosen_labels, end_dim=1), ignore_index=0
            )

        if self.loss_type == "ipo":
            all_logps = all_logps / loss_mask.sum(-1)

        output["chosen_logps"] = all_logps[:num_examples]
        output["rejected_logps"] = all_logps[num_examples:]

        # Compute the mean logits
        if self.padding_free:
            split_idx = (position_ids == 0).nonzero(as_tuple=True)[1][num_examples]
            mean_chosen_logits = logits[0, :split_idx][loss_mask[0, :split_idx]].mean()
            mean_rejected_logits = logits[0, split_idx:][loss_mask[0, split_idx:]].mean()
        else:
            mean_chosen_logits = logits[:num_examples][loss_mask[:num_examples]].mean()
            mean_rejected_logits = logits[num_examples:][loss_mask[num_examples:]].mean()

        output["mean_chosen_logits"] = mean_chosen_logits
        output["mean_rejected_logits"] = mean_rejected_logits

        if self.aux_loss_enabled:
            output["aux_loss"] = outputs.aux_loss

        return output
######## TRAIN ########

if __name__ == "__main__":
    # device = "cuda" if torch.cuda.is_available() else "cpu"
    local_rank = int(os.environ.get("LOCAL_RANK", 0))
    torch.cuda.set_device(local_rank)
    device = f"cuda:{local_rank}"
    
    model_id = "/home/user2/wns/cad-recode/cad-recode-v1.5"

    # DPO Specific Hyperparameters
    dpo_beta = 0.1 # Regularization parameter for DPO loss
    dpo_loss_type = "sigmoid" # Common loss type for DPO

    # Quantization Config (for QLoRA)
    # bnb_config = BitsAndBytesConfig(
    #     load_in_4bit=True,
    #     bnb_4bit_use_double_quant=True,
    #     bnb_4bit_quant_type="nf4",
    #     bnb_4bit_compute_dtype=torch.bfloat16
    # )

    # Tokenizer
    tokenizer = AutoTokenizer.from_pretrained('/home/user2/wns/cad-recode/Qwen2-1.5B', pad_token='<|im_end|>', padding_side='left', trust_remote_code=True)

    # Model - Load with quantization
    model = CADRecode.from_pretrained(
        model_id,
        # quantization_config=bnb_config,
        torch_dtype=torch.bfloat16, # Load in compute dtype
        attn_implementation="flash_attention_2" if torch.cuda.is_available() else None,
        device_map={'': torch.cuda.current_device()}, # Automatically distribute model layers
    )

    model_ref = None

    # Prepare model for K-bit training (important for QLoRA)
    model = prepare_model_for_kbit_training(model)
    # Enable gradient checkpointing in the base model
    #model.gradient_checkpointing_enable()

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

    dpo_features = Features({
        'uuid': Value('string'),
        'point_cloud': Array2D(dtype="float32", shape=(NUM_POINT_TOKENS, 3)), # Or Sequence(Sequence('float32')) if preferred
        'prompt': Value('string'), # Placeholder for <|im_start|>
        'chosen': Value('string'),
        'rejected': Value('string'),
        "winner_code": Value('string'),
        "loser_code": Value('string'),
    })
    train_dataset = Dataset.from_generator(
        dpo_generator,
        features=dpo_features,
        gen_kwargs={ # Pass arguments to your generator function
            "data_root": "/home/user2/wns/cad-recode/dpo_data",
            "split": "train",
            "num_points": NUM_POINT_TOKENS,
            "num_pre_points": 8192 # Or pass your actual num_pre_points
        }
    )
    # Evaluation with DPO is complex. Often skipped or done post-hoc.
    eval_dataset = None # Or create using split="test"

    print(f"Converted dataset features: {train_dataset.features}")
    print(f"Number of samples: {len(train_dataset)}")

    # Data Collator
    data_collator = DataCollatorForDPOCADRecode(
        tokenizer=tokenizer,
        max_length=MAX_SEQ_LENGTH, # Pass max sequence length
        pad_to_multiple_of=8, # Optional: for efficiency
        num_point_tokens=NUM_POINT_TOKENS,
    )

    # Trainer Args
    lr = 1e-5
    training_args = DPOConfig(
        output_dir=f"cad-recode-dpo-lr{lr}",
        num_train_epochs=3,
        per_device_train_batch_size=1, # Adjust based on GPU memory
        per_device_eval_batch_size=1,
        gradient_accumulation_steps=16, # Effective batch size = 8 * 2 = 16
        gradient_checkpointing=True, # Already enabled in model, TRL uses it too
        # optim="paged_adamw_32bit", # Paged optimizer for QLoRA
        learning_rate=lr, # Adjust as needed
        lr_scheduler_type="cosine", # Cosine scheduler is common
        logging_steps=10,
        save_strategy="steps",
        save_steps=100,
        save_total_limit=2, # Keep only the best and the latest checkpoint
        beta=dpo_beta,                     # DPO beta
        loss_type=dpo_loss_type,           # DPO loss type
        bf16=True, # Use bfloat16
        tf32=True, # Use TF32 on Ampere+ GPUs
        max_grad_norm=0.3,
        warmup_ratio=0.03,
        weight_decay=0.01, # Added weight decay
        push_to_hub=False, # Set to True to push checkpoints to HF Hub
        report_to="tensorboard", #"tensorboard"
        gradient_checkpointing_kwargs={"use_reentrant": False},
        # dataset_text_field="", # Not needed with custom collator handling everything
        # dataset_kwargs={"skip_prepare_dataset": True}, # Crucial
        remove_unused_columns=False, # Important: Keep point_cloud column
    )

    # wandb.init(
    #     project="CADRecodeDPO",
    #     name="cad-recode-dpo-logs",
    #     config=training_args,
    # )

    trainer = CADRecodeDPOTrainer(
        model=model,
        ref_model=model_ref,  # Let trainer handle creation if None
        args=training_args,
        train_dataset=train_dataset,
        eval_dataset=eval_dataset,  # Pass None if not evaluating
        processing_class=tokenizer,  # Necessary for the internal DPO impl logic
        data_collator=data_collator, # Use the custom collator
    )

    print("Starting training...")
    train_result = trainer.train()
    trainer.log_metrics("train", train_result.metrics)
    trainer.save_metrics("train", train_result.metrics)
    trainer.save_state()

    # Save the final adapter model
    print("Saving final adapter model...")
    trainer.save_model(f"cad-recode-dpo-lr{lr}-final")
    tokenizer.save_pretrained(f"cad-recode-dpo-lr{lr}-final")

    # wandb.finish()
    print("DPO Training Finished.")