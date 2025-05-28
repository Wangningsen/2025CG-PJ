# 2025 CG PJ

🤗 Models and datasets are [here](https://huggingface.co/ljbro/2025CG).

This is the repository for COMP130018.01 Computer Graph A final PJ: CAD-PrefLM: Reverse Engineering CAD Models with LLMs via Direct Preference Optimization.

## Environment Setup

Please install [pytorch3d](https://github.com/facebookresearch/pytorch3d/blob/main/INSTALL.md)，[open3d](https://pypi.org/project/open3d/) and suitable [torch](https://pytorch.org/get-started/locally/) version.

Follow the instructions below: 

```bash
conda create -n cadrecode python=3.10 -y
conda activate cadrecode
# install pytorch3d, open3d and torch by yourself
pip install -r requirements.txt
```

## Inference

Within the [`inference`](./inference/) directory, you'll find various demonstrations to help you run different inference scenarios:

- **[`demo.ipynb`](./inference/demo.ipynb)**: This notebook is designed for running the baseline Qwen2 CAD-Recode inference.
- **[`demo_qwen3_nolora.ipynb`](./inference/demo_qwen3_nolora.ipynb)**: Use this notebook to perform inference with the fine-tuned Qwen3 model that was trained *without* LoRA.
- **[`demo_qwen3_lora.ipynb`](./inference/demo_qwen3_lora.ipynb)**: This notebook is for running inference with the fine-tuned Qwen3 model that *was* trained with LoRA.
- **[`demo_realinput.py`](./inference/demo_realinput.py)**: This script directly reads reconstructed point cloud files and performs inference, simulating a real-world deployment scenario.


## Training

### SFT

We want to be transparent about our training efforts. While we've seen success with some models, we hit a significant roadblock trying to fine-tune **Qwen3 1.7B** with the **CAD-Recode v1.5 dataset** to outperform the original CAD-Recode model (which uses Qwen2 1.5B). Despite tremendous effort and numerous training epochs, our fine-tuned Qwen3 model consistently failed to generate any correct answers on the Fusion360 test set.

The training codes for the original CAD-Recode model aren't publicly available. We're sharing our findings and genuinely hope the community can help shed light on this issue. Solving this problem would be a big step forward!



In the [`train`](./train/) directory, you'll find these training scripts:

- **[`train_qwen3_full.py`](./train/train_qwen3_full.py)**: This script lets you train **Qwen3 1.7B** with full parameters, *without* LoRA.
- **[`train_qwen3_lora.py`](./train/train_qwen3_lora.py)**: Use this script to train **Qwen3 1.7B** *with* LoRA.




### DPO


#### dataset

We construct our DPO dataset utilizing [cad-recode-v1.5](https://huggingface.co/datasets/filapro/cad-recode-v1.5).

How the dataset is organized:


```
├── dpo_data
├── train_val.json
├── cadquery
│   ├── uuid1(train_batch_63_630020)_loser.py
│   ├── uuid2(train_batch_63_630020)_winner.py
│   ...
│   └── uuidN_winner.py
├── ground_truth
│   ├── uuid1(train_batch_63_630020).py
│   ...
│   └── uuidN.py
└── reconstruction
    ├── uuid1(train_batch_63_630020).stl
    ...
    └── uuidN.stl
```

`cadquery` contains all chosen-rejected pairs generated; `ground_truth` contains the CADquery codes from the original dataset; `reconstruction` contains all transferred .stl files from ground-truth codes; `train_val.json`  contains train-val split as follows:

```json
{
    "train": [
        "uuid1",
        "uuid2",
        // ...
    ],
    "validation": [
        "uuid_val1",
        "uuid_val2",
        // ...
    ]
}
```

The dataset is publicly accessible [here](https://huggingface.co/ljbro/2025CG).

In the [`train`](./train/) directory, you'll find the following scripts for DPO training:
- **[`train_dpo_full.py`](./train/train_dpo_full.py)**: Use this script to perform DPO training with the full parameters of the CAD-Recode baseline checkpoint.
- **[`train_dpo_lora.py`](./train/train_dpo_full.py)**: This script allows you to perform DPO training on the CAD-Recode baseline checkpoint using LoRA.

If you want to construct your own dataset, we provide some handful gadgets for you to quickly hands on in [`tool`](./tool/) directory:
- **[`generate_stl.py`](./tool/generate_stl.py)** can generate single .stl file for CADquery.
- **[`generate_stl_in_batch.py`](./tool/generate_stl_in_batch.py)** can generate multiple .stl files in batch.
- **[`move_dpopair.py`](./tool/move_dpopair.py)** can move a whole batch of pairs and ground-truth into corresponding directories.
- **[`check.py`](./tool/check.py)** can be used to check whether there is no corresponding pair for each ground-truth.
- **[`data_split.py`](./tool/data_split.py)**
 can scan the whole ground-truth items and split the dataset into train and val with the ratio you set.

If you wish to construct your own dataset, we offer several convenient utilities in the [`tool`](./tool/) directory to help you quickly get started:

- **[`generate_stl.py`](./tool/generate_stl.py)**: This script generates a single `.stl` file from CADquery code.
- **[`generate_stl_in_batch.py`](./tool/generate_stl_in_batch.py)**: Use this script to generate multiple `.stl` files in a batch process.
- **[`move_dpopair.py`](./tool/move_dpopair.py)**: This utility can move an entire batch of DPO pairs and their corresponding ground-truth files into designated directories.
- **[`check.py`](./tool/check.py)**: This script can be used to verify that every ground-truth entry has a corresponding pair.
- **[`data_split.py`](./tool/data_split.py)**: This script scans all ground-truth items and splits the dataset into training and validation sets based on a user-defined ratio.

## Multiple Images to Point Cloud

In the [multi-view](./multi-view/) directory, you'll find our script for converting multiple images into a point cloud. We believe that multi-view images are significantly more accessible than pre-existing 3D point cloud data. You can utilize this script to transform a set of images into a point cloud representation and then feed it to the model. Perhaps this approach will lead to successful CADquery generation!


## Relevant Repositories

- **Original Implementation**: You can find the original CAD-Recode project [here](https://github.com/filaPro/cad-recode/tree/main?tab=readme-ov-file).
- **Training Reimplementation**: A fantastic reimplementation effort for the training process is available [here](https://github.com/kakukakujirori/cad-recode?tab=readme-ov-file).
