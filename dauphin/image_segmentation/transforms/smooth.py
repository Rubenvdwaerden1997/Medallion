# Copyright (c) 2020 Sen Wu. All Rights Reserved.


from PIL import ImageFilter

from dauphin.image_segmentation.transforms.transform import DauphinTransform


class Smooth(DauphinTransform):
    def __init__(self, name=None, prob=1.0, level=0):
        super().__init__(name, prob, level)

    def transform(self, pil_img, label, **kwargs):
        return pil_img.filter(ImageFilter.SMOOTH), label
