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



def load_model_and_tokenizer(original_cad_recode_path, dpo_adapter_dir,tokenizer_path):
    """
    Load the CAD-Recode model and tokenizer
    
    Args:
        original_cad_recode_path: Path to the original CAD-Recode model
        dpo_adapter_dir: Path to the DPO adapter directory
    
    Returns:
        tuple: (model, tokenizer, device)
    """
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    attn_implementation = 'flash_attention_2' if torch.cuda.is_available() else None

    print(f"Loading DPO fine-tuned model...")
    print(f"Original CAD-Recode model: {original_cad_recode_path}")
    print(f"DPO adapter directory: {dpo_adapter_dir}")

    # 1. 加载 tokenizer - 使用函数参数而不是未定义的全局变量
    try:
        tokenizer = AutoTokenizer.from_pretrained(
            tokenizer_path,
            pad_token='<|im_end|>',
            padding_side='left',
            trust_remote_code=True
        )
        print(f"Tokenizer loaded from: {tokenizer_path}")
    except Exception as e:
        print(f"Error loading tokenizer: {e}")
        raise

    # 2. 加载原始的 CAD-Recode 模型（包含预训练的 linear encoder）
    try:
        print(f"Loading original CAD-Recode model (with trained linear encoder)...")
        model = CADRecode.from_pretrained(
            original_cad_recode_path,
            torch_dtype=torch.bfloat16,
            attn_implementation=attn_implementation,
            trust_remote_code=True
        )
        print("Original CAD-Recode model loaded (including trained linear encoder).")
    except Exception as e:
        print(f"Error loading CAD-Recode model: {e}")
        raise

    # 3. 定义 PEFT LoRA 配置
    # 确保 target_modules 只包含 Qwen2 的线性层，排除 point_encoder/linear_encoder
    peft_config = LoraConfig(
        r=64,  # 根据你的 DPO 训练配置调整
        lora_alpha=16,  # 根据你的 DPO 训练配置调整
        target_modules=[
            # Qwen2 的注意力层
            "q_proj", "k_proj", "v_proj", "o_proj", 
            # Qwen2 的 MLP 层
            "gate_proj", "up_proj", "down_proj"
        ], 
        lora_dropout=0.1,
        bias="none",
        task_type="CAUSAL_LM",
    )

    # 4. 将 CAD-Recode 模型应用 PEFT LoRA
    try:
        print("Applying PEFT LoRA to CAD-Recode model (only Qwen2 LLM layers)...")
        model = get_peft_model(model, peft_config)
        print("CAD-Recode model wrapped with PEFT (PeftModelForCausalLM).")
    except Exception as e:
        print(f"Error applying PEFT LoRA: {e}")
        raise

    # # 5. 加载 DPO 训练后的 LoRA adapter 权重
    # print(f"Loading DPO LoRA adapters from: {dpo_adapter_dir}")
    
    # # 检查 adapter 文件是否存在
    # adapter_files = [
    #     "adapter_model.safetensors",
    #     "adapter_model.bin"
    # ]
    
    # adapter_found = False
    # for adapter_file in adapter_files:
    #     if os.path.exists(os.path.join(dpo_adapter_dir, adapter_file)):
    #         adapter_found = True
    #         break
    
    # if adapter_found:
    #     try:
    #         model.load_adapter(dpo_adapter_dir, adapter_name="default")
    #         print("DPO LoRA adapters loaded successfully.")
    #     except Exception as e:
    #         print(f"Error loading DPO adapters: {e}")
    #         raise
    # else:
    #     print(f"Warning: No adapter files found in {dpo_adapter_dir}")
    #     if os.path.exists(dpo_adapter_dir):
    #         print("Available files:", os.listdir(dpo_adapter_dir))
    #     else:
    #         print("DPO adapter directory does not exist!")
    #         raise FileNotFoundError(f"DPO adapter directory not found: {dpo_adapter_dir}")

    # 6. 验证模型结构
    print("\nModel structure verification:")
    print(f"Model type: {type(model)}")
    print(f"Base model type: {type(model.base_model.model)}")

    # 检查 linear encoder 是否存在且未被 LoRA 化
    encoder_found = False
    if hasattr(model.base_model.model, 'point_encoder'):
        encoder = model.base_model.model.point_encoder
        print(f"Point encoder type: {type(encoder)}")
        print(f"Point encoder parameters: {sum(p.numel() for p in encoder.parameters())}")
        encoder_found = True
    elif hasattr(model.base_model.model, 'linear_encoder'):
        encoder = model.base_model.model.linear_encoder
        print(f"Linear encoder type: {type(encoder)}")
        print(f"Linear encoder parameters: {sum(p.numel() for p in encoder.parameters())}")
        encoder_found = True
    else:
        print("Warning: No encoder found in model")
        # 打印模型属性以便调试
        print("Available attributes in base model:")
        print([attr for attr in dir(model.base_model.model) if not attr.startswith('_')])

    # # 检查 LoRA adapter 是否正确加载
    # try:
    #     print(f"Active adapters: {model.active_adapters}")
    #     print(f"PEFT config keys: {list(model.peft_config.keys())}")
    # except Exception as e:
    #     print(f"Warning: Could not access PEFT config: {e}")

    # 7. 将模型移动到设备并设置为评估模式
    try:
        model = model.eval().to(device)
        print(f"\nFull model ready for inference on {device}")
        print("Components:")
        print("- Original CAD-Recode with trained linear encoder ✓" if encoder_found else "- Original CAD-Recode with trained linear encoder ✗")
        # print("- Qwen2 LLM with DPO LoRA adapters ✓" if adapter_found else "- Qwen2 LLM with DPO LoRA adapters ✗")
    except Exception as e:
        print(f"Error moving model to device: {e}")
        raise

    return model, tokenizer, device

class Fusion360EvalDataset(torch.utils.data.Dataset):
    def __init__(self, fusion360_root: str, num_points: int = 128, num_pre_points: int = 8192) -> None:
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
    MODEL_PATH="/remote-home1/jjchen/2025CG-PJ_/cad-recode-full-dpo-lr5e-06-final"
    TOKENIZER_PATH="/remote-home1/jjchen/2025CG-PJ_/Qwen2-1.5B"
    model, tokenizer, device = load_model_and_tokenizer(MODEL_PATH,"", TOKENIZER_PATH)

    fusion360_dataset = Fusion360EvalDataset("/remote-home1/jjchen/2025CG-PJ_/r1.0.1")
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

    eval_report = {
        "console_output": [
            "======== Summary ========",
            f"CD mean: {np.mean(CDs)}",
            f"CD median: {np.median(CDs)}",
            f"IoU mean: {np.mean(IoUs)}",
            f"Invalid preds: {invalid_pred_num} / {len(fusion360_dataset)} (within which {invalid_gt_num} GTs are invalid)"
        ],
        "detailed_results": eval_summary  # 包含原有的详细结果
    }

    with open("eval_results_nolora_128.json", "w") as f:
        json.dump(eval_report, f, indent=4)