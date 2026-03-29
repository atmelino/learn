# conda create -n tensorflow-text python=3.10
# conda activate tensorflow-text
# conda install -c conda-forge tensorflow=2.19.0 -y
# conda install -c conda-forge matplotlib -y
# conda install -c conda-forge einops -y
# pip install tensorflow-text

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
import pathlib
import pandas as pd

path_to_zip = tf.keras.utils.get_file(
    "spa-eng.zip",
    origin="http://storage.googleapis.com/download.tensorflow.org/data/spa-eng.zip",
    extract=True,
)

print("path_to_zip=",path_to_zip)
# path_to_file = pathlib.Path(path_to_zip).parent / "spa-eng/spa.txt"
path_to_file = pathlib.Path(path_to_zip) / "spa-eng/spa.txt"


def load_data(path):
    text = path.read_text(encoding="utf-8")

    lines = text.splitlines()
    pairs = [line.split("\t") for line in lines]

    context = np.array([context for target, context in pairs])
    target = np.array([target for target, context in pairs])

    return target, context


target_raw, context_raw = load_data(path_to_file)
print(context_raw[-1])
