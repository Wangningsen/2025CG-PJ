# 2025 CG PJ

这是2025 CG PJ: CAD。

## Environment Setup

请自己手动安装[pytorch3d](https://github.com/facebookresearch/pytorch3d/blob/main/INSTALL.md)，[open3d](https://pypi.org/project/open3d/)以及适合的[torch](https://pytorch.org/get-started/locally/)版本。

我将原本的`dockerfile`转换为了`requirenments.txt`，我可以在自己的服务器上正常搭建环境，服务器设置为：

- ubuntu 22.04
- cuda 12.4
- torch 2.5.1

```bash
conda create -n cadrecode python=3.10 -y
conda activate cadrecode
# install pytorch3d, open3d and torch by yourself
pip install -r requirements.txt
```

## Training

### SFT

在`train.py`中我实现了利用[qwen3 1.7B](https://huggingface.co/Qwen/Qwen3-1.7B)进行SFT。这里我默认不能稳定直连huggingface，因此所有权重都是放在本地进行的训练。如要运行，请自己修改内部的相关路径。

### DPO

DPO训练的代码我还没改，我后面会改的。或者你有时间可以自己改改。

数据集构造的代码也只是从原本的[fusion360](https://github.com/AutodeskAILab/Fusion360GalleryDataset)切换到了[cad-recode-v1.5](https://huggingface.co/datasets/filapro/cad-recode-v1.5)上。

DPO数据生成完成，我这里有2617个对。

数据的组织形式：

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

其中`cadquery`存储了所有生成的胜败对；`ground_truth`存储了数据集中原始的gt脚本；`reconstruction`中存储有已经转换完成的stl文件，可以直接采样生成点云作为模型输入；`train_val.json`中有训练验证集的划分，如下：

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

- `generate_stl.py`可用于生成单个stl文件；
- `generate_stl_in_batch.py`可用于批量生成stl文件；
- `move_dpopair.py`可用于批量移动一整个batch生成的对和gt移动到对应的文件夹中；
- `check.py`可用于检查是否有哪个gt没有对应的胜败对。可能会有有gt无胜败对存在的情况！


## Inference

`demo.ipynb`可以利用现有的权重进行推理。依旧是默认无法稳定直连`huggingface`，因此需要自行clone[训练完成的模型权重](https://huggingface.co/filapro/cad-recode-v1.5)和[qwen2 1.5B](https://huggingface.co/Qwen/Qwen2-1.5B)(用来提供tokenizer)。

## relevant

原始代码：https://github.com/filaPro/cad-recode/tree/main?tab=readme-ov-file

有人尝试复现的代码：https://github.com/kakukakujirori/cad-recode?tab=readme-ov-file
