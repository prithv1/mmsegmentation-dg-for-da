# 
from .builder import DATASETS
from .custom import CustomDataset
from . import CityscapesDataset


@DATASETS.register_module()
class BDD100Dataset(CustomDataset):
    CLASSES = CityscapesDataset.CLASSES 
#Data root: '/srv/datasets/bdd100k_DG'
#Images: images/val
#Maps: bdd100k/labels/sem_seg/colormaps/val
    PALETTE = CityscapesDataset.PALETTE 

    def __init__(self, **kwargs):
        assert kwargs.get('split') in [None, 'train']
        if 'split' in kwargs:
            kwargs.pop('split')
        super(BDD100Dataset, self).__init__(
            img_suffix='.jpg',
            seg_map_suffix='.png',
            split=None,
            **kwargs)