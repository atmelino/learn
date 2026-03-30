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

BASE_PATH = "../../../../../local_data/practice/keras/transformers/"
DATA_PATH = BASE_PATH + "translate_attention/"
OUTPUT_PATH = BASE_PATH + "translate_attention/"
os.system("mkdir -p " + OUTPUT_PATH)


local = False
local = True
if local == False:
    print("get dataset from Internet")
    path_to_zip = tf.keras.utils.get_file(
        "spa-eng.zip",
        origin="http://storage.googleapis.com/download.tensorflow.org/data/spa-eng.zip",
        extract=True,
    )
    # path_to_file = pathlib.Path(path_to_zip).parent / "spa-eng/spa.txt"
    path_to_file = pathlib.Path(path_to_zip) / "spa-eng/spa.txt"
else:
    print("get dataset local")
    # print("DATA_PATH=", DATA_PATH)
    myorigin = DATA_PATH + "spa-eng.zip"
    # print("origin=", myorigin)
    fullPath = os.path.abspath(myorigin)  # or similar, depending on your scenario
    print(fullPath)
    # print('file://'+fullPath)
    path_to_zip = fullPath
    path_to_file = pathlib.Path(path_to_zip).parent / "spa-eng/spa.txt"

print("path_to_zip=", path_to_zip)


def load_data(path):
    text = path.read_text(encoding="utf-8")

    lines = text.splitlines()
    pairs = [line.split("\t") for line in lines]

    context = np.array([context for target, context in pairs])
    target = np.array([target for target, context in pairs])

    return target, context


target_raw, context_raw = load_data(path_to_file)
n_lines=len(target_raw)
print("number of lines=",n_lines)
# print(context_raw[-1])
# print(target_raw[-1])

print("first ten lines")
print(context_raw[:10])
print(target_raw[:10])


BUFFER_SIZE = len(context_raw)
BATCH_SIZE = 64
BATCH_SIZE = 32


random_index=True
random_index=False
if(random_index==True):
    is_train = np.random.uniform(size=(len(target_raw),)) < 0.8
    print("is_train",is_train)
    print("len is_train",len(is_train))
else:
    is_train = np.full(n_lines, True) 
    print("is_train",is_train)

train_raw = (
    tf.data.Dataset.from_tensor_slices((context_raw[is_train], target_raw[is_train]))
    # .shuffle(BUFFER_SIZE)
    .batch(BATCH_SIZE)
)
val_raw = (
    tf.data.Dataset.from_tensor_slices((context_raw[~is_train], target_raw[~is_train]))
    # .shuffle(BUFFER_SIZE)
    .batch(BATCH_SIZE)
)

# exit()
n_items=200
print("First %d items"% n_items)
for example_context_strings, example_target_strings in train_raw.take(1):
    print(example_context_strings[:n_items])
    print()
    print(example_target_strings[:n_items])
    break
# print("next batch")
# for example_context_strings, example_target_strings in train_raw.take(1):
#     print(example_context_strings[:n_items])
#     print()
#     print(example_target_strings[:n_items])
#     break

# Convert to pandas Dataframe for viewing
# pd.set_option("display.max_columns", None)
pd.set_option("display.max_colwidth", None)

# df_train_raw = tf.data.Dataset.from_tensor_slices(
#     (context_raw[is_train], target_raw[is_train])
# )
# print(df_train_raw)
# print(train_raw.shape)
# ds = tf.data.Dataset.from_tensor_slices(train_raw)

# ds_data = [x for x in train_raw.take(5).as_numpy_iterator()]
# df = pd.DataFrame(ds_data)
# print(df.head())


for example_context_strings, example_target_strings in train_raw.take(1):
    df1 = pd.DataFrame(example_context_strings[:n_items])
    df2 = pd.DataFrame(example_target_strings[:n_items])
    break

df = pd.concat([df1, df2], axis=1)

# print(df.head())
print(df)




exit()



max_vocab_size = 5000

context_text_processor = tf.keras.layers.TextVectorization(
    standardize=tf_lower_and_split_punct,
    max_tokens=max_vocab_size,
    ragged=True)







class ShapeChecker:
    def __init__(self):
        # Keep a cache of every axis-name seen
        self.shapes = {}

    def __call__(self, tensor, names, broadcast=False):
        if not tf.executing_eagerly():
            return

        parsed = einops.parse_shape(tensor, names)

        for name, new_dim in parsed.items():
            old_dim = self.shapes.get(name, None)

            if broadcast and new_dim == 1:
                continue

            if old_dim is None:
                # If the axis name is new, add its length to the cache.
                self.shapes[name] = new_dim
                continue

            if new_dim != old_dim:
                raise ValueError(
                    f"Shape mismatch for dimension: '{name}'\n"
                    f"    found: {new_dim}\n"
                    f"    expected: {old_dim}\n"
                )
