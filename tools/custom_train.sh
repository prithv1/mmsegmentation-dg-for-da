#!/bin/sh -l
#SBATCH -p short
#SBATCH --gres=gpu:4
#SBATCH -J DLV3+
#SBATCH -o /srv/hoffman-lab/share4/bgoyal7/mmseg/firstlog.log
#SBATCH -A overcap
#SBATCH -p overcap
hostname
srun python -u train.py ../configs/gtavExperiments/deeplabv3plus/deeplabv3plus_r18-d8_4x4_512x512_80k_vaihingen.py --launcher="slurm"
