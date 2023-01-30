#!/bin/bash
conda create --name mmseg_dg_da python=3.8 -y
conda activate mmseg_dg_da
​
conda install pytorch==1.12.0 torchvision==0.13.0 torchaudio==0.12.0 cudatoolkit=11.3 -c pytorch -y
​
pip install -U openmim
mim install mmcv-full
mim install mmengine
​
pip install -v -e .