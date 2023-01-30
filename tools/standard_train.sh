#!/bin/bash
#SBATCH --job-name=segformer-viper-4g-4s-4w
#SBATCH -o /srv/hoffman-lab/share4/bgoyal7/mmseg/samplelog.o
#SBATCH --error=logs4g-4s-4w.err
#SBATCH --gres=gpu:4
#SBATCH -c 1
#SBATCH --partition=short
#SBATCH -p overcap
#SBATCH -A overcap

source ~/.bashrc

export MASTER_ADDR=$(srun --ntasks=1 hostname 2>&1 | tail -n1)

conda activate mmseg
cd ~/mmsegmentation-dg-for-da/

set -x
srun python tools/train.py configs/segformer/segformer_mit-b4_8x1_1024x1024_160k_cityscapes.py --launcher="slurm"
