# Copyright (c) 2020 Sen Wu. All Rights Reserved.


from PIL import ImageEnhance

from dauphin.image_segmentation.transforms.transform import DauphinTransform
from dauphin.image_segmentation.transforms.utils import categorize_value


class Sharpness(DauphinTransform):

    value_range = (2, 4)

    def __init__(self, name=None, prob=1.0, level=0):
        super().__init__(name, prob, level)

    def transform(self, img, label=None, **kwargs):
        degree = categorize_value(self.level, self.value_range, "float")

        if label:
            return self._sharpness(img, degree), label
        else:
            return self._sharpness(img, degree)

    def _sharpness(self, img, degree):
        if isinstance(img, list):
            return [ImageEnhance.Sharpness(i).enhance(degree) for i in img]
        else:
            return ImageEnhance.Sharpness(img).enhance(degree)
