# https://ai.stanford.edu/~amaas/data/sentiment/
# https://arxiv.org/abs/1801.06146
# https://docs.fast.ai/tutorial.text.html
# https://docs.fast.ai/distributed.html

from fastai.text.all import *

path = untar_data(URLs.IMDB)

dls = TextDataLoaders.from_folder(path, valid='test', bs=64, seed=42)
learn = text_classifier_learner(dls, AWD_LSTM, drop_mult=0.5, metrics=accuracy)
learn.fit(1, 1e-3)
