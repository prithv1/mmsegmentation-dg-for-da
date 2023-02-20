# 
from . import CityscapesDataset
from .builder import DATASETS
from .custom import CustomDataset

id_to_ignore_or_group = {}
ignore_label = 255
@DATASETS.register_module()
class MapillaryDataset(CustomDataset):
    CLASSES = CityscapesDataset.CLASSES
    PALETTE = CityscapesDataset.PALETTE

    def __init__(self, **kwargs):
        assert kwargs.get('split') in [None, 'train']
        if 'split' in kwargs:
            kwargs.pop('split')
        self.gen_ids_to_ignore()
        super(MapillaryDataset, self).__init__(
            img_suffix='.jpg',
            seg_map_suffix='.png',
            split=None,
            **kwargs)

    #The following function was borrowed from the PASTA_robustnet repository
    #https://github.com/ksarangmath/PASTA_robustnet/blob/049c59908c1b10cc504d89d5183eb018d810267d/datasets/mapillary.py#L36
    def gen_ids_to_ignore(self):
        global id_to_ignore_or_group
        for i in range(66):
            id_to_ignore_or_group[i] = ignore_label

        ### Convert each class to cityscapes one
        ### Road
        # Road
        id_to_ignore_or_group[13] = 0
        # Lane Marking - General
        id_to_ignore_or_group[24] = 0
        # Manhole
        id_to_ignore_or_group[41] = 0

        ### Sidewalk
        # Curb
        id_to_ignore_or_group[2] = 1
        # Sidewalk
        id_to_ignore_or_group[15] = 1

        ### Building
        # Building
        id_to_ignore_or_group[17] = 2

        ### Wall
        # Wall
        id_to_ignore_or_group[6] = 3

        ### Fence
        # Fence
        id_to_ignore_or_group[3] = 4

        ### Pole
        # Pole
        id_to_ignore_or_group[45] = 5
        # Utility Pole
        id_to_ignore_or_group[47] = 5

        ### Traffic Light
        # Traffic Light
        id_to_ignore_or_group[48] = 6

        ### Traffic Sign
        # Traffic Sign
        id_to_ignore_or_group[50] = 7

        ### Vegetation
        # Vegitation
        id_to_ignore_or_group[30] = 8

        ### Terrain
        # Terrain
        id_to_ignore_or_group[29] = 9

        ### Sky
        # Sky
        id_to_ignore_or_group[27] = 10

        ### Person
        # Person
        id_to_ignore_or_group[19] = 11

        ### Rider
        # Bicyclist
        id_to_ignore_or_group[20] = 12
        # Motorcyclist
        id_to_ignore_or_group[21] = 12
        # Other Rider
        id_to_ignore_or_group[22] = 12

        ### Car
        # Car
        id_to_ignore_or_group[55] = 13

        ### Truck
        # Truck
        id_to_ignore_or_group[61] = 14

        ### Bus
        # Bus
        id_to_ignore_or_group[54] = 15

        ### Train
        # On Rails
        id_to_ignore_or_group[58] = 16

        ### Motorcycle
        # Motorcycle
        id_to_ignore_or_group[57] = 17

        ### Bicycle
        # Bicycle
        id_to_ignore_or_group[52] = 18

    
    def get_classes_and_palette(self, classes=None, palette=None):
        self.custom_classes = True 
        self.label_map = id_to_ignore_or_group
        return self.CLASSES, self.PALETTE