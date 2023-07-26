# Copyright (c) 2020 Sen Wu. All Rights Reserved.


from PIL import ImageEnhance

from dauphin.image_segmentation.transforms.transform import DauphinTransform
from dauphin.image_segmentation.transforms.utils import categorize_value


class Brightness(DauphinTransform):

    value_range = (0.5, 1.5)

    def __init__(self, name=None, prob=1.0, level=0):
        super().__init__(name, prob, level)

    def transform(self, img, label=None, **kwargs):
        degree = categorize_value(self.level, self.value_range, "float")

        if label:
            return self._brightness(img, degree), label
        else:
            return self._brightness(img, degree)

    def _brightness(self, img, degree):
        if isinstance(img, list):
            return [ImageEnhance.Brightness(i).enhance(degree) for i in img]
        else:
            return ImageEnhance.Brightness(img).enhance(degree)

    def __repr__(self):
        return f"<Transform ({self.name}), prob={self.prob}, level={self.level}"
