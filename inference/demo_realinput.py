import open3d
import trimesh
import skimage.io
import numpy as np
import cadquery as cq
import matplotlib.pyplot as plt
from scipy.spatial import cKDTree

import torch
from torch import nn
from transformers import (
    AutoTokenizer, Qwen2ForCausalLM, Qwen2Model, PreTrainedModel)
from transformers.modeling_outputs import CausalLMOutputWithPast
from pytorch3d.ops import sample_farthest_points


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

# --- 模型加载 (保持不变) ---
device = 'cuda' if torch.cuda.is_available() else 'cpu'
attn_implementation = 'flash_attention_2' if torch.cuda.is_available() else None
tokenizer = AutoTokenizer.from_pretrained(
    '/home/user2/wns/cad-recode/Qwen2-1.5B',
    pad_token='<|im_end|>',
    padding_side='left')
model = CADRecode.from_pretrained(
    '/home/user2/wns/cad-recode/cad-recode-v1.5',
    torch_dtype='auto',
    attn_implementation=attn_implementation).eval().to(device)

# --- 修改点云输入部分 ---

def load_and_sample_point_cloud(ply_file_path, n_points=None):
    """
    从PLY文件加载点云，并进行采样或使用全部点。
    
    Args:
        ply_file_path (str): PLY文件的路径。
        n_points (int, optional): 如果指定，则使用Farthest Point Sampling 采样n_points个点。
                                  如果为None，则返回PLY文件中所有点。
    Returns:
        np.ndarray: 采样或加载后的点云，形状为 (N, 3)。
    """
    pcd = open3d.io.read_point_cloud(ply_file_path)
    if not pcd.has_points():
        raise ValueError(f"PLY file {ply_file_path} contains no points.")
    
    # 原始点云数据
    original_points = np.asarray(pcd.points)

    center = np.mean(original_points, axis=0)
    centered_points = original_points - center

    extents = np.max(centered_points, axis=0) - np.min(centered_points, axis=0)
    scale_factor = 2.0 / np.max(extents) if np.max(extents) > 1e-6 else 1.0 # 避免除以0
    scaled_points = centered_points * scale_factor
    
    if n_points is not None and len(scaled_points) > n_points:
        points_tensor = torch.tensor(scaled_points, dtype=torch.float32).unsqueeze(0)
        _, ids = sample_farthest_points(points_tensor, K=n_points)
        sampled_points = scaled_points[ids[0].numpy()]
        print(f"Sampling {n_points} points from {len(original_points)} points.")
        return sampled_points
    else:
        print(f"Using all {len(original_points)} points from the PLY file.")
        return scaled_points


ply_file_path = './output.ply' 

# 可以指定采样的点数，例如256。如果设置为None，将使用PLY文件中的所有点。
num_input_points = None 


try:
    point_cloud = load_and_sample_point_cloud(ply_file_path, n_points=num_input_points)
except Exception as e:
    print(f"Error loading or processing point cloud: {e}")
    exit() 

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
print("Generated CadQuery Code:\n", py_string)

try:
    exec(py_string, globals())
    compound = globals()['r'].val()
    vertices, faces = compound.tessellate(0.001, 0.1)
    mesh = trimesh.Trimesh([(v.x, v.y, v.z) for v in vertices], faces)
    
    # 导出STL文件
    output_stl_path = './generated_model.stl' 
    mesh.export(output_stl_path)
    print(f"Successfully generated and exported STL model to: {output_stl_path}")

    output_step_path = './generated_model.step' 
    cq.exporters.export(compound, output_step_path)
    print(f"Successfully exported STEP model to: {output_step_path}")

except Exception as e:
    print(f"Error executing generated CadQuery code or exporting model: {e}")