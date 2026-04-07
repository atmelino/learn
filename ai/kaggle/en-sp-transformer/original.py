# https://www.kaggle.com/code/lonnieqin/english-spanish-translation-transformer


import pandas as pd
import tensorflow as tf
from tensorflow.keras.layers import TextVectorization
import pathlib
import random
import string
import re
import numpy as np
from tensorflow import keras
from tensorflow.keras import layers
import sklearn
import os
from sklearn.model_selection import train_test_split
print(f"Tensorflow Version:{tf.__version__}")

BASE_PATH = "../../../../local_data/kaggle/"
DATA_PATH = BASE_PATH + "en-sp-transformer/"
OUTPUT_PATH = BASE_PATH + "en-sp-transformer/"

os.system("mkdir -p " + OUTPUT_PATH)


class Config:
    vocab_size = 16000 # Vocabulary Size
    sequence_length = 20
    batch_size = 512
    validation_split = 0.15
    embed_dim = 256
    latent_dim = 256
    num_heads = 4
    epochs = 30 # Number of Epochs to train
    is_training = False
config = Config()

# data = pd.read_csv("/kaggle/input/englishspanish-translation-dataset/data.csv")
data = pd.read_csv(DATA_PATH+"data.csv")
data.head()









