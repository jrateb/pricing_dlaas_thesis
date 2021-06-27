# https://docs.fast.ai/tutorial.imagenette.html

from fastai.vision.all import *
from fastai.distributed import *

path = rank0_first(untar_data, URLs.IMAGENETTE)
dls = DataBlock(
    blocks=(ImageBlock, CategoryBlock),
    get_items=get_image_files, get_y=parent_label,
    item_tfms=Resize(460),
    batch_tfms=[*aug_transforms(size=224, min_scale=0.75),
                                Normalize.from_stats(*imagenet_stats)]
).dataloaders(path, path=path, bs=64)

learn = Learner(dls, resnet50(), metrics=accuracy)
learn.unfreeze()
with learn.distrib_ctx(): learn.fit(1, 1e-3)
