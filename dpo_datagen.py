import json, os
import tempfile
from typing import Dict, List, Literal, Optional, Tuple, Union
import cadquery as cq
import numpy as np
import open3d
import skimage.io
import torch
import torch.nn as nn
import torch.nn.functional as F
import trimesh
from pytorch3d.loss import chamfer_distance
from pytorch3d.ops import sample_farthest_points
from tqdm import tqdm
from transformers import (AutoTokenizer, BitsAndBytesConfig, Qwen2ForCausalLM, PreTrainedModel,
                          Qwen2Model, TrainingArguments)
from transformers.modeling_outputs import CausalLMOutputWithPast
from transformers.tokenization_utils_base import PaddingStrategy, PreTrainedTokenizerBase


NUM_POINT_TOKENS = 256
NUM_TRIAL = 10

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


class Fusion360Dataset(torch.utils.data.Dataset):
    def __init__(self, fusion360_root: str, split: Literal["train", "test"], num_points=NUM_POINT_TOKENS, num_pre_points=8192):
        with open(os.path.join(fusion360_root, "train_test.json"), "r") as f:
            data_list = json.load(f)
        self.data_paths = [os.path.join(fusion360_root, "reconstruction", uuid + ".obj") for uuid in data_list[split]]
        self.data_paths.sort()
        self.num_points = num_points
        self.num_pre_points = num_pre_points
        # Store im_start_token string/ID for convenience
        self.im_start_token = "<|im_start|>" # Or fetch from tokenizer if it has an attribute

    def __len__(self) -> int:
        return len(self.data_paths)

    def __getitem__(self, idx: int):
        path = self.data_paths[idx]
        gt_mesh = trimesh.load_mesh(path)

        # Normalize mesh before sampling
        center = gt_mesh.bounds[0] + (gt_mesh.bounds[1] - gt_mesh.bounds[0]) / 2.0
        gt_mesh.apply_translation(-center)
        scale = 2.0 / max(gt_mesh.extents) if max(gt_mesh.extents) > 1e-6 else 1.0 # Avoid division by zero
        gt_mesh.apply_scale(scale)

        # Sample Points
        point_cloud = self.mesh_to_point_cloud(gt_mesh, self.num_points, self.num_pre_points)
        if point_cloud is None:
            RuntimeError(f"Failed to generate point cloud for: {path}")

        return {"point_cloud": point_cloud, "mesh": gt_mesh, "path": path}

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


def convert_cadquery_to_pointcloud(cq_string: str, n_points: int = 8192):
    local_env = {'cq': cq} # Provide cq module
    exec(cq_string, {'cq': cq}, local_env)
    cad_model = local_env.get('r') or local_env.get('result') # Check common variable names

    if cad_model is None or not isinstance(cad_model, cq.Workplane):
        raise RuntimeError(f"Error: No valid CadQuery Workplane ('r' or 'result') found in: {cad_code_filepath}")

    # Attempt to get a compound or solid
    final_shape = cad_model.combine().val()
    if not isinstance(final_shape, (cq.Solid, cq.Compound)):
        raise RuntimeError(f"Extracted final_shape is not Solid/Compound. Type: {type(final_shape)}. File: {cad_code_filepath}")

    # convert to a mesh
    with tempfile.NamedTemporaryFile(suffix=".stl", delete=True) as tmp_file:
        cq.exporters.export(final_shape, tmp_file.name) # Use cq.exporters
        # Check if file is empty after export
        if os.path.getsize(tmp_file.name) == 0:
            RuntimeError(f"Exported STL file is empty")
        mesh = trimesh.load_mesh(tmp_file.name)

    # normalize mesh before sampling
    center = mesh.bounds[0] + (mesh.bounds[1] - mesh.bounds[0]) / 2.0
    mesh.apply_translation(-center)
    scale = 2.0 / max(mesh.extents) if max(mesh.extents) > 1e-6 else 1.0 # Avoid division by zero
    mesh.apply_scale(scale)

    # sample points
    vertices, _ = trimesh.sample.sample_surface(mesh, n_points)

    return np.array(vertices)


def save_string(string: str, filename: str):
    with open(filename, "w") as f:
        f.write(string)


if __name__ == '__main__':
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    attn_implementation = 'flash_attention_2' if torch.cuda.is_available() else None
    tokenizer = AutoTokenizer.from_pretrained(
        'Qwen/Qwen2-1.5B',
        pad_token='<|im_end|>',
        padding_side='left')
    model = CADRecode.from_pretrained(
        'filapro/cad-recode-v1.5',
        torch_dtype='auto',
        attn_implementation=attn_implementation).eval().to(device)

    dataset = Fusion360Dataset("Fusion360/r1.0.1", "train")
    save_dir = "Fusion360/r1.0.1/cadquery"
    os.makedirs(save_dir, exist_ok=True)

    for gt_data in tqdm(dataset):
        gt_mesh, gt_path = gt_data["mesh"], gt_data["path"]

        basename = os.path.splitext(os.path.basename(gt_path))[0]
        winner_path = os.path.join(save_dir, basename + "_winner.py")
        loser_path = os.path.join(save_dir, basename + "_loser.py")
        if os.path.isfile(winner_path) and os.path.isfile(loser_path):
            continue

        results = []
        for i in range(NUM_TRIAL):
            gt_point_cloud = dataset.mesh_to_point_cloud(gt_mesh, dataset.num_points, dataset.num_pre_points)

            # inference
            input_ids = [tokenizer.pad_token_id] * len(gt_point_cloud) + [tokenizer('<|im_start|>')['input_ids'][0]]
            attention_mask = [-1] * len(gt_point_cloud) + [1]
            with torch.no_grad():
                batch_ids = model.generate(
                    input_ids=torch.tensor(input_ids).unsqueeze(0).to(model.device),
                    attention_mask=torch.tensor(attention_mask).unsqueeze(0).to(model.device),
                    point_cloud=torch.tensor(gt_point_cloud.astype(np.float32)).unsqueeze(0).to(model.device),
                    max_new_tokens=768,
                    pad_token_id=tokenizer.pad_token_id)
            py_string = tokenizer.batch_decode(batch_ids)[0]
            begin = py_string.find('<|im_start|>') + 12
            end = py_string.find('<|endoftext|>')
            py_string = py_string[begin: end]

            # chamfer distance
            try:
                chamfer_points = dataset.num_pre_points  # 8192
                pred_point_cloud_dense = convert_cadquery_to_pointcloud(py_string, chamfer_points)
                gt_point_cloud_dense = dataset.mesh_to_point_cloud(gt_mesh, chamfer_points, chamfer_points)
                dist, _ = chamfer_distance(torch.tensor(gt_point_cloud_dense).unsqueeze(0).float(), torch.tensor(pred_point_cloud_dense).unsqueeze(0).float())
            except:
                print(f"{i}th py_string caused CADQuery drawing error")
                continue

            results.append((dist, py_string))


        if len(results) < NUM_TRIAL // 2:
            continue

        results.sort()
        print(f"Chamfer distances: {[[d.item() for d, _ in results]]}")
        winner_string = results[0][1]
        loser_string = results[len(results)//2][1]

        save_string(winner_string, winner_path)
        save_string(loser_string, loser_path)