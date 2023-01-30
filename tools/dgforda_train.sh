#!/bin/bash
#SBATCH --job-name=deeplabtrain
#SBATCH -o /srv/hoffman-lab/share4/bgoyal7/mmseg/mmsegCheckpoints/deepLabPasta.o
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
srun train_source.sh
