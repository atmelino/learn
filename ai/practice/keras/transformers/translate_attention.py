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
    myorigin = DATA_PATH + "spa-eng.zip"
    path_to_zip = os.path.abspath(myorigin)  # or similar, depending on your scenario
    path_to_file = pathlib.Path(path_to_zip).parent / "spa-eng/spa.txt"


def load_data(path):
    text = path.read_text(encoding="utf-8")

    lines = text.splitlines()
    pairs = [line.split("\t") for line in lines]

    context = np.array([context for target, context in pairs])
    target = np.array([target for target, context in pairs])

    return target, context


target_raw, context_raw = load_data(path_to_file)
n_lines = len(target_raw)
# print("number of lines=",n_lines)
print("Last line in data:")
print(context_raw[-1])
print(target_raw[-1])
# print("first ten lines")
# print(context_raw[:10])
# print(target_raw[:10])

BUFFER_SIZE = len(context_raw)
BATCH_SIZE = 32
BATCH_SIZE = 64

random_index = False
random_index = True
if random_index == True:
    is_train = np.random.uniform(size=(len(target_raw),)) < 0.8
    # print("is_train",is_train)
    # print("len is_train",len(is_train))
else:
    is_train = np.full(n_lines, True)
    # print("is_train",is_train)

train_raw = (
    tf.data.Dataset.from_tensor_slices((context_raw[is_train], target_raw[is_train]))
    .shuffle(BUFFER_SIZE)
    .batch(BATCH_SIZE)
)
val_raw = (
    tf.data.Dataset.from_tensor_slices((context_raw[~is_train], target_raw[~is_train]))
    .shuffle(BUFFER_SIZE)
    .batch(BATCH_SIZE)
)

# exit()
n_items = 200
# print("First %d items"% n_items)
# for example_context_strings, example_target_strings in train_raw.take(1):
#     print(example_context_strings[:n_items])
#     print()
#     print(example_target_strings[:n_items])
#     break
# print("next batch")
# for example_context_strings, example_target_strings in train_raw.take(1):
#     print(example_context_strings[:n_items])
#     print()
#     print(example_target_strings[:n_items])
#     break

# Convert to pandas Dataframe for viewing
pd.set_option("display.max_colwidth", None)
for example_context_strings, example_target_strings in train_raw.take(1):
    df1 = pd.DataFrame(example_context_strings[:n_items])
    df2 = pd.DataFrame(example_target_strings[:n_items])
    break
df = pd.concat([df1, df2], axis=1)
# print(df.head())
print(df)

print("*** Standardization ***")
example_text = tf.constant("¿Todavía está en casa?")
# print(example_text.numpy())
# print(tf_text.normalize_utf8(example_text, 'NFKD').numpy())


def tf_lower_and_split_punct(text):
    # Split accented characters.
    text = tf_text.normalize_utf8(text, "NFKD")
    text = tf.strings.lower(text)
    # Keep space, a to z, and select punctuation.
    text = tf.strings.regex_replace(text, "[^ a-z.?!,¿]", "")
    # Add spaces around punctuation.
    text = tf.strings.regex_replace(text, "[.?!,¿]", r" \0 ")
    # Strip whitespace.
    text = tf.strings.strip(text)

    text = tf.strings.join(["[START]", text, "[END]"], separator=" ")
    return text


print(example_text.numpy().decode())
print(tf_lower_and_split_punct(example_text).numpy().decode())

print("*** Text Vectorization ***")

max_vocab_size = 5000

context_text_processor = tf.keras.layers.TextVectorization(
    standardize=tf_lower_and_split_punct, max_tokens=max_vocab_size, ragged=True
)

context_text_processor.adapt(train_raw.map(lambda context, target: context))

# Here are the first 10 words from the vocabulary:
context_text_processor.get_vocabulary()[:10]
