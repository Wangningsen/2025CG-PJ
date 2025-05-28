import json, os
import tempfile
from typing import Dict, List, Literal, Optional, Tuple, Union
import cadquery as cq
import numpy as np
import open3d # Keeping imports as in original, but some might not be used
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
import traceback


# Constants - Adjust if needed
NUM_POINT_TOKENS = 256  # Number of points for the model input
NUM_TRIAL = 10          # Number of inference attempts per ground truth file
NUM_POINTS_FOR_EVAL_CD = 8192 # Number of points for calculating Chamfer Distance

# --- Model Definitions (Keeping as requested) ---
class FourierPointEncoder(nn.Module):
    def __init__(self, hidden_size):
        super().__init__()
        frequencies = 2.0 ** torch.arange(8, dtype=torch.float32)
        self.register_buffer('frequencies', frequencies, persistent=False)
        self.projection = nn.Linear(51, hidden_size)

    # def forward(self, points):
    #     x = points
    #     x = (x.unsqueeze(-1) * self.frequencies).view(*x.shape[:-1], -1)
    #     x = torch.cat((points, x.sin(), x.cos()), dim=-1)
    #     x = self.projection(x)
    #     return x
        # >>>>> MODIFIED forward method to handle dtype <<<<<<
    def forward(self, points):
        # points is expected to be a tensor (likely float32 on model.device from input preparation)
        # self.frequencies buffer is on the same device as points (model.device)
        # Ensure self.frequencies is float32 (already defined as such)

        # 1. Calculate Fourier features (result is float32 if inputs are float32)
        # Ensure frequencies are on the same device as points for calculation
        frequencies_on_device = self.frequencies.to(points.device)

        # Calculate the frequency multiplication part
        # points: (..., 3), frequencies_on_device: (8) -> unsqueeze_(-1) -> (8, 1)
        # (points.unsqueeze(-1) * frequencies_on_device) -> (..., 3, 8) * (8, 1) -> broadcasting -> (..., 3, 8)
        # .view -> (..., 3*8=24)
        x_fourier_mult = (points.unsqueeze(-1) * frequencies_on_device).view(*points.shape[:-1], -1) # Shape ..., 24

        # Calculate sin and cos of the frequency multiplied features
        x_fourier_sin = x_fourier_mult.sin() # Shape ..., 24
        x_fourier_cos = x_fourier_mult.cos() # Shape ..., 24

        # 2. Concatenate original points and Fourier features (result is float32)
        # Combine original points (shape ..., 3) with sin and cos features (shape ..., 24 each)
        x_combined = torch.cat((points, x_fourier_sin, x_fourier_cos), dim=-1) # Result shape ..., 3 + 24 + 24 = 51

        # 3. Cast the combined input (which is float32) to match the linear layer's weight dtype (bfloat16)
        # The projection layer's weight dtype is the same as the model's dtype (bfloat16)
        # >>>>> Explicit casting here <<<<<
        x_combined_casted = x_combined.to(self.projection.weight.dtype) # Cast to bfloat16

        # 4. Apply the linear projection layer (bfloat16 input * bfloat16 weight)
        output = self.projection(x_combined_casted) # Output is bfloat16

        return output # Return the bfloat16 output embeddings

class CADRecode(Qwen2ForCausalLM):
    def __init__(self, config):
        PreTrainedModel.__init__(self, config)
        self.model = Qwen2Model(config)
        self.vocab_size = config.vocab_size
        self.lm_head = nn.Linear(config.hidden_size, config.vocab_size, bias=False)

        # These dtype changes might be handled by transformers/accelerate now,
        # especially with quantization. Commenting out default dtype changes.
        # torch.set_default_dtype(torch.float32)
        self.point_encoder = FourierPointEncoder(config.hidden_size)
        # torch.set_default_dtype(torch.bfloat16) # Model weights dtype is set during from_pretrained


    def forward(self,
                input_ids=None,
                attention_mask=None,
                point_cloud=None, # Your custom point cloud input
                position_ids=None,
                past_key_values=None,
                inputs_embeds=None,
                labels=None,
                use_cache=None,
                output_attentions=None,
                output_hidden_states=None,
                return_dict=None,
                cache_position=None):

        # Get default return_dict based on config if not provided
        return_dict = return_dict if return_dict is not None else self.config.use_return_dict

        # For the initial forward pass (past_key_values is None or empty),
        # we combine point cloud embeddings and text embeddings.
        # In generation, this is usually the first call.
        if past_key_values is None or (hasattr(past_key_values, 'get_seq_length') and past_key_values.get_seq_length() == 0):
            assert inputs_embeds is None, "inputs_embeds should be None for the initial pass when combining point cloud and text."

            # Get text embeddings
            inputs_embeds = self.model.embed_tokens(input_ids)

            # Process point cloud through the encoder
            # Ensure point_cloud tensor has the correct dtype expected by point_encoder (usually float32)
            # The output is then cast to bfloat16 as per the original forward method
            point_embeds = self.point_encoder(point_cloud.to(self.point_encoder.frequencies.device)).bfloat16() # Ensure PE runs on correct device

            # Find where to insert point embeddings using attention_mask == -1
            # This part assumes attention_mask has -1 for point token slots
            point_mask_indices = (attention_mask == -1).nonzero(as_tuple=True)

            if point_mask_indices[0].numel() > 0: # Check if any -1 exists
                 # Insert point embeddings into the main embeddings tensor
                 # This assumes point_embeds shape (batch_size, num_point_tokens, hidden_size)
                 # and the mask correctly aligns with these slots
                 batch_size, seq_len = attention_mask.shape
                 num_points_expected = (attention_mask == -1).sum(dim=1).max().item()

                 if point_embeds.shape[1] != num_points_expected:
                      print(f"Warning: Point embeds shape {point_embeds.shape} mismatch with mask expectation {num_points_expected}")
                      # Fallback insertion if shape mismatches - less ideal, relies heavily on mask indices
                      inputs_embeds[point_mask_indices] = point_embeds.reshape(-1, point_embeds.shape[-1])
                 else:
                      # Standard insertion for correctly shaped point_embeds and mask
                      inputs_embeds[:, :num_points_expected] = point_embeds # Assuming point tokens are at the beginning

            # Update attention_mask: set -1 to 1 for the processed point token slots
            attention_mask = attention_mask.clone() # Clone to avoid modifying original mask
            attention_mask[attention_mask == -1] = 1

            # Set input_ids and position_ids to None as inputs_embeds are now used
            input_ids = None
            position_ids = None # Model's internal logic might handle position_ids from inputs_embeds

        # --- Standard Decoder Forward Pass ---
        # Pass the combined embeddings and updated attention mask to the base model
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

        # Apply language model head
        # Cast hidden_states to float32 if necessary before lm_head, then logits back to float32
        # The explicit .float() at the end ensures float32 logits
        # Depending on PyTorch/hardware, lm_head might work with bfloat16 directly
        logits = self.lm_head(hidden_states)
        logits = logits.float() # Ensure logits are float32

        loss = None
        if labels is not None:
            # Shift so that tokens < n predict n for CausalLM loss
            shift_logits = logits[..., :-1, :].contiguous()
            shift_labels = labels[..., 1:].contiguous()

            loss_fct = nn.CrossEntropyLoss()
            shift_logits = shift_logits.view(-1, self.config.vocab_size)
            shift_labels = shift_labels.view(-1)

            # Ensure labels are on the same device as logits for loss calculation
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

# --- End of Model Definitions ---


# --- Helper Functions ---

def code_string_to_mesh(cq_string: str):
    """Executes a CadQuery script string and returns the resulting normalized trimesh mesh."""
    local_env = {'cq': cq} # Provide cq module in the execution environment
    cad_model = None
    tmp_script_path = None # Define outside try for finally block

    try:
        # Use a temporary file to execute the code safely is often better
        # with tempfile.NamedTemporaryFile(mode='w', suffix=".py", delete=False) as tmp_script:
        #    tmp_script.write(cq_string)
        #    tmp_script_path = tmp_script.name
        # Execute the script. This populates local_env with script variables.
        # Use a restricted execution environment
        exec_globals = {'cq': cq, '__builtins__': __builtins__} # Only provide 'cq' and minimal builtins

        # Check for common variable names ('r' or 'result') after execution
        exec(cq_string, exec_globals, exec_globals) # Execute in globals to find result vars

        cad_model = exec_globals.get('r') or exec_globals.get('result')

        if cad_model is None or not isinstance(cad_model, cq.Workplane):
            # Provide more specific error if 'r'/'result' exists but is wrong type
            if 'r' in exec_globals or 'result' in exec_globals:
                 raise RuntimeError(f"Error: Variable 'r' or 'result' found but not a CadQuery Workplane (type: {type(cad_model).__name__ if cad_model is not None else 'None'}).")
            else:
                 raise RuntimeError(f"Error: No CadQuery Workplane ('r' or 'result') found in script.")

        # Attempt to get a compound or solid from the workplane
        # Get objects from the stack
        shapes = cad_model.objects
        if not shapes:
             raise RuntimeError(f"Error: CadQuery Workplane is empty.")

        # If there's more than one shape, combine them into a compound
        if len(shapes) > 1:
             final_shape = cq.Compound.makeCompound(shapes)
        else:
             final_shape = shapes[0] # Get the single shape

        # Check if the final shape is a Solid or Compound
        if not isinstance(final_shape, (cq.Solid, cq.Compound)):
             raise RuntimeError(f"Extracted final_shape is not Solid/Compound. Type: {type(final_shape).__name__}. ")


        # Convert to a mesh using a temporary file
        with tempfile.NamedTemporaryFile(suffix=".stl", delete=True) as tmp_file:
            tmp_stl_path = tmp_file.name # Get the path before closing
            # Close the file handle before export on some OS
            tmp_file.close()
            try:
                # Use cq.exporters.export
                cq.exporters.export(final_shape, tmp_stl_path)
            except Exception as export_e:
                 # Specific error for export failure
                 raise RuntimeError(f"Error during STL export: {export_e}") from export_e


            # Check if file is empty after export
            if not os.path.exists(tmp_stl_path) or os.path.getsize(tmp_stl_path) == 0:
                raise RuntimeError(f"Exported STL file is empty or not created at {tmp_stl_path}")

            # Load the mesh with trimesh
            try:
                 mesh = trimesh.load_mesh(tmp_stl_path)
            except Exception as load_e:
                 raise RuntimeError(f"Error loading exported STL ({tmp_stl_path}) with trimesh: {load_e}") from load_e


        # Normalize mesh (as in your original code)
        # Check for valid bounds/extents before normalizing
        if mesh.bounds is None or mesh.extents is None:
             # This can happen for empty or invalid meshes
             print("Warning: Mesh bounds or extents are None. Skipping normalization.")
             # Decide how to handle: return mesh as is or raise error
             return mesh # Return potentially non-normalized mesh


        center = mesh.bounds[0] + (mesh.bounds[1] - mesh.bounds[0]) / 2.0
        mesh.apply_translation(-center)
        # Avoid division by zero if extents are zero (e.g., point or line shape)
        extents = mesh.extents
        scale = 1.0
        # Check if max extent is effectively zero
        if np.max(np.abs(extents)) > 1e-6:
             scale = 2.0 / np.max(extents)
        elif np.max(np.abs(extents)) > 0: # Handle very small non-zero extents if needed
             # This case might still lead to very large scales, potentially numerical issues
             print(f"Warning: Max extent is very small ({np.max(extents)}). Applying potentially large scale.")
             scale = 2.0 / np.max(extents)

        mesh.apply_scale(scale)

        return mesh # Return the normalized trimesh mesh

    except Exception as e:
         # Catch any other general execution or processing error
         raise RuntimeError(f"Error executing CadQuery code or processing result: {e}") from e
    finally:
        # Clean up the temporary script file if it was created
        if tmp_script_path and os.path.exists(tmp_script_path):
            os.remove(tmp_script_path)


# Helper function to sample points from a mesh using PyTorch3D FPS
def mesh_to_point_cloud(mesh: trimesh.Trimesh, n_points: int):
    """Samples n_points from a trimesh mesh using PyTorch3D FPS."""
    if mesh.vertices.shape[0] == 0 or (mesh.faces.shape[0] == 0 and mesh.vertices.shape[0] < n_points):
        # Handle empty mesh or mesh with insufficient vertices/faces
        print(f"Warning: Mesh has {mesh.vertices.shape[0]} vertices, {mesh.faces.shape[0]} faces. Cannot sample {n_points} points.")
        # Decide how to handle: return None, return zeros, or duplicate points
        return None # Indicate failure to sample


    # Sample more points initially than needed for better FPS distribution if the mesh is complex
    n_sample_initial = max(n_points * 2, 8192) # Sample more points first

    try:
        # sample_surface returns (vertices, face_indices)
        vertices, _ = trimesh.sample.sample_surface(mesh, n_sample_initial)
    except Exception as e:
        print(f"Error during trimesh.sample.sample_surface: {e}")
        return None


    if len(vertices) == 0:
         print("Error: trimesh.sample.sample_surface returned 0 points.")
         return None

    if len(vertices) < n_points:
        print(f"Warning: Sampled only {len(vertices)} points, requested {n_sample_initial}. Duplicating points to reach {n_points}.")
        # If not enough points are sampled initially, duplicate existing points to meet n_points
        indices = np.random.choice(len(vertices), size=n_points, replace=True)
        sampled_points = vertices[indices]
    elif len(vertices) == n_points:
         sampled_points = vertices # Use all sampled if exactly n_points
    else: # len(vertices) > n_points, use FPS to get exactly n_points
        # Ensure vertices tensor is float32 for FPS
        # Pytorch3D FPS requires batch dimension (1, num_vertices, 3)
        vertices_tensor = torch.tensor(vertices, dtype=torch.float32).unsqueeze(0)
        print(f"    DEBUG(FPS): input dtype={vertices_tensor.dtype}, device={vertices_tensor.device}, shape={vertices_tensor.shape}")
        # FPS runs on GPU if PyTorch3D is installed with CUDA, otherwise CPU
        try:
             _, ids = sample_farthest_points(vertices_tensor, K=n_points)
             ids = ids[0].cpu().numpy() # Move indices back to CPU
             sampled_points = vertices[ids]
        except Exception as e:
             print(f"Error during PyTorch3D Farthest Point Sampling: {e}. Falling back to random sampling.")
             # Fallback to random sampling if FPS fails (less ideal distribution)
             indices = np.random.choice(len(vertices), size=n_points, replace=False)
             sampled_points = vertices[indices]

    return np.asarray(sampled_points, dtype=np.float32)


# Reuse save_string function
def save_string(string: str, filename: str):
    with open(filename, "w") as f:
        f.write(string)

# --- Main Data Generation Script ---
if __name__ == '__main__':
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    # Use 'xpu' for Intel IPs if available and supported by PyTorch/Accelerate
    # device = 'xpu' if hasattr(torch, 'xpu') and torch.xpu.is_available() else device

    attn_implementation = 'flash_attention_2' if torch.cuda.is_available() else None
    # For other devices like XPU, check their specific implementations
    # if device == 'xpu': attn_implementation = 'xpu_attention' # Example if applicable

    # Load tokenizer
    tokenizer = AutoTokenizer.from_pretrained(
        '/home/user2/wns/cad-recode/Qwen2-1.5B', # Base tokenizer config
        pad_token='<|im_end|>', # Ensure this is the correct pad token
        padding_side='left' # Left padding is common for generation
    )
    # Ensure pad_token_id is set if it wasn't by default
    if tokenizer.pad_token_id is None:
        tokenizer.pad_token_id = tokenizer.eos_token_id # Or choose another appropriate ID

    # Load model (assuming it's CADRecode class)
    # Load your SFT trained model weights. Ensure dtype matches training.
    # If your SFT was bfloat16, load as bfloat16.
    # If using 4-bit/8-bit, load with quantization_config and device_map per device as discussed earlier.
    # For this generation script on a single machine, loading to one device is simpler if memory allows.
    # Example for loading a non-quantized bfloat16 model to a single device:
    try:
        model = CADRecode.from_pretrained(
            '/home/user2/wns/cad-recode/cad-recode-v1.5', # Path to your SFT trained model
            torch_dtype=torch.bfloat16, # Load weights in bfloat16
            attn_implementation=attn_implementation
            # No device_map='auto' here for simplicity in generation script
            # Moving the whole model to device after loading
        )
        model.eval().to(device) # Set to eval mode and move to device
        print(f"Model loaded successfully on {device}.")

    except Exception as e:
        print(f"Error loading model: {e}")
        print("Please check model path, available memory, and specified dtype/quantization settings.")
        exit()


    # --- Dataset Configuration ---
    cad_recode_root = "/home/user2/wns/cad-recode/cad-recode-v1.5-data" # Point this to your CAD Recode dataset root directory
    split = "train" # Or "val" - choose the split for data generation
    save_dir = os.path.join("/home/user2/wns/cad-recode/cad-recode-v1.5-data-origindpo", "dpo_preference_pairs_best_median", split) # Directory to save generated pairs

    os.makedirs(save_dir, exist_ok=True) # Create the save directory if it doesn't exist

    # Find all ground truth .py files in the specified split
    cad_files = []
    split_dir = os.path.join(cad_recode_root, split)
    if not os.path.exists(split_dir):
         print(f"Error: Dataset split directory not found: {split_dir}")
         exit()

    # Walk through the directory to find all .py files recursively
    for root, _, files in os.walk(split_dir):
        for file in files:
            if file.endswith(".py"):
                # Store full path to the ground truth .py file
                cad_files.append(os.path.join(root, file))

    print(f"Found {len(cad_files)} ground truth .py files in '{split}' split.")


    # --- Data Generation Loop ---
    # Iterate through each ground truth .py file found
    # >>>>>> 在这里添加计数器和限制 <<<<<<
    processing_limit = 50000 # 设定要处理的样例数量限制
    processed_count = 0      # 初始化已处理样例的计数器

    # 使用 tqdm 包装 cad_files 列表以显示进度条
    for gt_code_path in tqdm(cad_files, desc=f"Generating pairs for {split}"):

        # Increment the counter for each source file considered
        processed_count += 1

        # Check if the processing limit has been reached
        if processed_count > processing_limit:
             print(f"\nProcessing limit of {processing_limit} examples reached. Stopping traversal.")
             break # Exit the loop once the limit is exceeded

        # --- Rest of the loop body remains the same ---
        # Derive a base name for saving files, including directory structure
        try:
            relative_path = os.path.relpath(gt_code_path, cad_recode_root)
            basename = os.path.splitext(relative_path)[0].replace(os.sep, '_')
        except ValueError:
            print(f"Warning: Could not get relative path for {gt_code_path}. Using full path basename.")
            basename = os.path.splitext(os.path.basename(gt_code_path))[0]

        # Define output paths based on the 'best vs median' method
        output_basename_path = os.path.join(save_dir, basename)
        winner_path = output_basename_path + "_winner.py"
        loser_path = output_basename_path + "_loser.py"
        gt_code_copy_path = output_basename_path + "_gt_code.py"

        # Skip if pair already generated (This check happens before processing costly steps)
        # This ensures already generated files don't consume processing time,
        # but they *do* count towards the 'processed_count' as the script *considered* the source file.
        if os.path.isfile(winner_path) and os.path.isfile(loser_path) and os.path.isfile(gt_code_copy_path):
             # print(f"Skipping {relative_path}: Output files already exist.")
             continue # Skip to the next ground truth file

        # --- Process One Ground Truth Example (Only runs if not skipped) ---
        print(f"\nProcessing {relative_path}...") # Print full path when processing

        try:
            # 1. Generate Ground Truth Mesh and Dense Point Cloud (once per GT file)
            with open(gt_code_path, 'r') as f:
                gt_code_string = f.read()

            gt_mesh_normalized = code_string_to_mesh(gt_code_string)
            if gt_mesh_normalized is None:
                 raise RuntimeError("code_string_to_mesh returned None mesh for GT.")

            gt_point_cloud_for_eval_np = mesh_to_point_cloud(gt_mesh_normalized, NUM_POINTS_FOR_EVAL_CD)
            if gt_point_cloud_for_eval_np is None:
                 raise RuntimeError("mesh_to_point_cloud returned None for GT evaluation.")

            gt_point_cloud_for_eval_tensor = torch.tensor(gt_point_cloud_for_eval_np, dtype=torch.float32).unsqueeze(0)

            save_string(gt_code_string, gt_code_copy_path)

            # 2. Inference and Evaluation Loop (NUM_TRIAL times)
            results = [] # Store (cd_value, generated_code_text) for successful trials

            for i in range(NUM_TRIAL):
                # print(f"  Inference {i+1}/{NUM_TRIAL}...")
                try:
                    input_point_cloud_for_model_np = mesh_to_point_cloud(gt_mesh_normalized, NUM_POINT_TOKENS)
                    if input_point_cloud_for_model_np is None:
                         print(f"  Inference {i+1}: Failed to generate input point cloud for model from GT mesh.")
                         continue

                    input_point_cloud_for_model_tensor = torch.tensor(input_point_cloud_for_model_np.astype(np.float32)).unsqueeze(0).to(model.device)

                    initial_token_ids = [tokenizer.pad_token_id] * NUM_POINT_TOKENS + [tokenizer('<|im_start|>')['input_ids'][0]]
                    initial_attention_mask = [-1] * NUM_POINT_TOKENS + [1]
                    input_ids_tensor = torch.tensor(initial_token_ids).unsqueeze(0).to(model.device)
                    attention_mask_tensor = torch.tensor(initial_attention_mask).unsqueeze(0).to(model.device)

                    with torch.no_grad():
                        generated_ids = model.generate(
                            input_ids=input_ids_tensor,
                            attention_mask=attention_mask_tensor,
                            point_cloud=input_point_cloud_for_model_tensor,
                            max_new_tokens=768,
                            pad_token_id=tokenizer.pad_token_id,
                            do_sample=True,
                            temperature=0.7,
                            top_k=50,
                            top_p=0.95,
                            num_return_sequences=1
                        )

                    py_string_raw = tokenizer.batch_decode(generated_ids, skip_special_tokens=False)[0]

                    begin_idx = py_string_raw.find('<|im_start|>')
                    py_string = py_string_raw[begin_idx + len('<|im_start|>'):].strip() if begin_idx != -1 else py_string_raw.strip()
                    end_idx = py_string.find('<|endoftext|>')
                    py_string = py_string[:end_idx].strip() if end_idx != -1 else py_string.strip()


                    # 3. Evaluate Generated Code (Render and Calculate CD)
                    pred_mesh_normalized = code_string_to_mesh(py_string)
                    if pred_mesh_normalized is None:
                         raise RuntimeError("code_string_to_mesh returned None mesh for generated code.")

                    pred_point_cloud_dense_np = mesh_to_point_cloud(pred_mesh_normalized, NUM_POINTS_FOR_EVAL_CD)
                    if pred_point_cloud_dense_np is None:
                         raise RuntimeError("mesh_to_point_cloud returned None for predicted evaluation.")
                    print(f"    DEBUG(Before Pred Tensor Creation): mesh_to_point_cloud returned type={type(pred_point_cloud_dense_np)}, dtype={pred_point_cloud_dense_np.dtype}, shape={pred_point_cloud_dense_np.shape}")
                    pred_point_cloud_dense_tensor = torch.tensor(pred_point_cloud_dense_np).unsqueeze(0).float() # Remove
                    print(f"    DEBUG(Tensor Creation): pred_point_cloud_dense_tensor dtype={pred_point_cloud_dense_tensor.dtype}, device={pred_point_cloud_dense_tensor.device}, shape={pred_point_cloud_dense_tensor.shape}")
                    # Calculate chamfer distance on CPU to avoid GPU dtype conflicts
                    # Move tensors to CPU and ensure float32 dtype
                    gt_for_cd_cpu = gt_point_cloud_for_eval_tensor.cpu().float()
                    pred_for_cd_cpu = pred_point_cloud_dense_tensor.cpu().float()
                    print(f"    DEBUG(CD): GT input dtype={gt_for_cd_cpu.dtype}, device={gt_for_cd_cpu.device}, shape={gt_for_cd_cpu.shape}")
                    print(f"    DEBUG(CD): Pred input dtype={pred_for_cd_cpu.dtype}, device={pred_for_cd_cpu.device}, shape={pred_for_cd_cpu.shape}")
                    dist_tensor_cpu, _ = chamfer_distance(gt_for_cd_cpu, pred_for_cd_cpu)
                    dist = dist_tensor_cpu.item() # Get scalar value from CPU tensor

                    results.append((dist, py_string))

                except Exception as e:
                    print(f"  Inference {i+1}: Error during generated code execution or evaluation - {e}")
                    traceback.print_exc()
                    # Optional: Save the problematic generated code and error for debugging
                    # error_code_path = os.path.join(save_dir, f"{basename}_inference{i+1}_eval_error.py")
                    # save_string(f"# Error: {e}\n\n{py_string}", error_code_path)
                    continue


            # 4. Select Winner/Loser (Best vs Median method)
            if len(results) < NUM_TRIAL // 2:
                print(f"Prompt {basename}: Not enough successful inferences ({len(results)}/{NUM_TRIAL}). Skipping pair generation.")
                # Clean up the saved gt_code_copy_path if we skipped pair generation for this prompt
                if os.path.exists(gt_code_copy_path):
                     os.remove(gt_code_copy_path)
                continue


            results.sort(key=lambda x: x[0])

            winner_cd, winner_string = results[0]
            loser_cd, loser_string = results[len(results) // 2]

            if winner_cd >= loser_cd:
                 print(f"Warning: Winner CD ({winner_cd:.4f}) is not less than Loser CD ({loser_cd:.4f}).")
                 if len(results) <= 1 or winner_cd == loser_cd:
                      print("Cannot form a valid pair with current results. Skipping.")
                      if os.path.exists(gt_code_copy_path): os.remove(gt_code_copy_path)
                      continue
                 else:
                      if len(results) > 1 and results[0][0] == results[len(results)//2][0]:
                           print("Winner and Loser CDs are identical. Using second best as loser.")
                           loser_cd, loser_string = results[1]
                           if winner_cd >= loser_cd:
                                print("Winner and second-best CDs are also identical. Skipping pair generation.")
                                if os.path.exists(gt_code_copy_path): os.remove(gt_code_copy_path)
                                continue

            # 5. Save Winner and Loser Code Strings
            try:
                save_string(winner_string, winner_path)
                save_string(loser_string, loser_path)
                print(f"Successfully generated and saved winner/loser pair for {basename}")
            except Exception as e:
                 print(f"Error saving winner/loser files for {basename}: {e}")
                 if os.path.exists(winner_path): os.remove(winner_path)
                 if os.path.exists(loser_path): os.remove(loser_path)
                 # Keep the gt_code_copy_path


        except Exception as e:
            # Catch errors during initial GT processing for a file
            print(f"\nError processing initial GT file {gt_code_path}: {e}")
            traceback.print_exc()
            # Clean up GT copy if it was saved before the error
            if os.path.exists(gt_code_copy_path):
                 os.remove(gt_code_copy_path)
            continue # Continue to the next file


    print("\nData generation process complete.")