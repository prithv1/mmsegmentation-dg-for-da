_base_ = './deeplabv3plus_r50-d8_4x4_512x512_80k_vaihingen.py'
model = dict(
    pretrained='open-mmlab://resnet18_v1c',
    backbone=dict(depth=18),
    decode_head=dict(
        c1_in_channels=64,
        c1_channels=12,
        in_channels=512,
        channels=128,
    ),
    auxiliary_head=dict(in_channels=256, channels=64))
data = dict(
    samples_per_gpu=1,
    workers_per_gpu=1,
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