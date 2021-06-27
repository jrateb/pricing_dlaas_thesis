# https://ai.stanford.edu/~amaas/data/sentiment/
# https://arxiv.org/abs/1801.06146
# https://docs.fast.ai/tutorial.text.html
# https://docs.fast.ai/distributed.html

from fastai.text.all import *
from fastai.distributed import *

path = rank0_first(untar_data, URLs.IMDB)

dls = rank0_first(lambda: TextDataLoaders.from_folder(path, valid='test', bs=64, seed=42))
learn = rank0_first(lambda: text_classifier_learner(dls, AWD_LSTM, drop_mult=0.5, metrics=accuracy))
with learn.distrib_ctx(): learn.fit(1, 1e-3)
