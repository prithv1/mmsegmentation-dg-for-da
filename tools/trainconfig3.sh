#!/bin/bash
#SBATCH --job-name=mapillaryCheck
#SBATCH -o /srv/hoffman-lab/share4/bgoyal7/mmseg/mapillaryFinal.o
#SBATCH --error=/srv/hoffman-lab/share4/bgoyal7/mmseg/mapillaryFinal.err
#SBATCH --gres=gpu:4
#SBATCH -c 16
#SBATCH --partition=short
#SBATCH -p overcap
#SBATCH -A overcap


export PYTHONUNBUFFERED=TRUE
export MASTER_ADDR=$(srun --ntasks=1 hostname 2>&1 | tail -n1)

source /srv/flash1/testnvme/bgoyal77/miniconda3/etc/profile.d/conda.sh

conda activate mmseg




# source /srv/flash1/testnvme/bgoyal77/miniconda3/etc/profile.d/conda.sh

set -x
#python ~/mmsegmentation-dg-for-da/tools/test.py ~/mmsegmentation-dg-for-da/configs/deeplabv3plus/test_config.py $COC/latest.pth --eval mIoU --launcher pytorch
#~/mmsegmentation-dg-for-da/tools/dist_test.sh ~/mmsegmentation-dg-for-da/configs/deeplabv3plus/test_config.py $COC/latest.pth 1 --eval mIoU ECE

srun ~/mmsegmentation-dg-for-da/tools/dist_test.sh ~/mmsegmentation-dg-for-da/configs/deeplabv3plus/test_config.py $COC/latest.pth 4 --eval mIoU





#!/bin/bash