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

因为数据集还没构建完成，DPO训练的代码我还没改。

数据集构造的代码也只是从原本的[fusion360](https://github.com/AutodeskAILab/Fusion360GalleryDataset)切换到了[cad-recode-v1.5](https://huggingface.co/datasets/filapro/cad-recode-v1.5)上。

## Inference

`demo.ipynb`可以利用现有的权重进行推理。依旧是默认无法稳定直连`huggingface`，因此需要自行clone[训练完成的模型权重](https://huggingface.co/filapro/cad-recode-v1.5)和[qwen2 1.5B](https://huggingface.co/Qwen/Qwen2-1.5B)(用来提供tokenizer)。

## relevant

原始代码：https://github.com/filaPro/cad-recode/tree/main?tab=readme-ov-file

有人尝试复现的代码：https://github.com/kakukakujirori/cad-recode?tab=readme-ov-file
