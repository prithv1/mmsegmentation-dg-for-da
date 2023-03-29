_base_ = [
    '../_base_/models/deeplabv3plus_r50-d8.py',
    '../_base_/datasets/cityscapes.py', '../_base_/default_runtime.py',
    '../_base_/schedules/schedule_40k.py'
]

# Storing Directory
#Prithvi: /coc/scratch/prithvi/dg_for_da/segmentation_dg/deeplabv3plus_r50-d8_512x1024_40k_GTAV_vanilla
#Bharat: /srv/hoffman-lab/share4/bgoyal7/mmseg/mmsegCheckpoints
work_dir='/srv/hoffman-lab/share4/bgoyal7/mmseg/mmsegCheckpoints'

# Data Pipeline Settings
img_norm_cfg = dict(
    mean=[123.675, 116.28, 103.53], std=[58.395, 57.12, 57.375], to_rgb=True)
crop_size = (512, 1024)
train_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(type='LoadAnnotations'),
    dict(type='Resize', img_scale=(1914, 1052), ratio_range=(0.5, 2.0)),
    dict(type='RandomCrop', crop_size=crop_size, cat_max_ratio=0.75),
    dict(type='RandomFlip', prob=0.5),
    dict(type='PhotoMetricDistortion'),
    dict(type='Normalize', **img_norm_cfg),
    dict(type='Pad', size=crop_size, pad_val=0, seg_pad_val=255),
    dict(type='DefaultFormatBundle'),
    dict(type='Collect', keys=['img', 'gt_semantic_seg']),
]
test_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(
        type='MultiScaleFlipAug',
        img_scale=(2048, 1024),
        # img_ratios=[0.5, 0.75, 1.0, 1.25, 1.5, 1.75],
        flip=False,
        transforms=[
            dict(type='Resize', keep_ratio=True),
            dict(type='RandomFlip'),
            dict(type='Normalize', **img_norm_cfg),
            dict(type='ImageToTensor', keys=['img']),
            dict(type='Collect', keys=['img']),
        ])
]

# Path to datasets
# Samples / Workers pGPU Specs
data = dict(
    samples_per_gpu=2,
    workers_per_gpu=2,
    train=dict(
        type='GTADataset',
        data_root='/srv/datasets/GTA5DA',
        img_dir='images',
        ann_dir='labels',
        pipeline=train_pipeline),
    val=dict(
        type='CityscapesDataset',
        data_root='/srv/datasets/cityscapesDA',
        img_dir='leftImg8bit/val',
        ann_dir='gtFine/val',
        pipeline=test_pipeline),
    test=dict(
        type='CityscapesDataset',
        data_root='/srv/datasets/cityscapesDA',
        img_dir='leftImg8bit/val',
        ann_dir='gtFine/val',
        pipeline=test_pipeline))