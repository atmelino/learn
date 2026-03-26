import keras
from keras import layers
import os
import matplotlib.pyplot as plt


import numpy as np
import typing
from typing import Any, Tuple
import einops
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import tensorflow as tf
import tensorflow_text as tf_text


BASE_PATH = "../../../../../local_data/practice/keras/transformers/"
DATA_PATH = BASE_PATH + "translate_attention/"
OUTPUT_PATH = BASE_PATH + "translate_attention/"

os.system("mkdir -p " + OUTPUT_PATH)

# to place datafiles in local folder:
# cd (wherever your local_data folder is)
# cd practice/keras/transformers
# wget https://raw.githubusercontent.com/hfawaz/cd-diagram/master/FordA/FordA_TRAIN.tsv
# wget https://raw.githubusercontent.com/hfawaz/cd-diagram/master/FordA/FordA_TEST.tsv

# Download the file
import pathlib

path_to_zip = tf.keras.utils.get_file(
    'spa-eng.zip', origin='http://storage.googleapis.com/download.tensorflow.org/data/spa-eng.zip',
    extract=True)

path_to_file = pathlib.Path(path_to_zip).parent/'spa-eng/spa.txt'




