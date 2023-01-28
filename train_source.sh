# Script to train source models
# Works but DDP is slow for some reason

# Train a vanilla source model (no Augs)
./tools/dist_train.sh configs/deeplabv3plus/deeplabv3plus_r50-d8_512x1024_40k_gtav.py 4

# Train a source model with PD
./tools/dist_train.sh configs/deeplabv3plus/deeplabv3plus_r50-d8_512x1024_40k_gtav_pd.py 4

# Train a source model with PASTA + PD
./tools/dist_train.sh configs/deeplabv3plus/deeplabv3plus_r50-d8_512x1024_40k_gtav_pasta_pd.py 4