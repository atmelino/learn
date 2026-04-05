# https://www.tensorflow.org/tutorials/load_data/text


import collections
import pathlib
import os
# import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras import layers
from tensorflow.keras import losses
from tensorflow.keras import utils
from tensorflow.keras.layers import TextVectorization
import tensorflow_datasets as tfds
import tensorflow_text as tf_text

BASE_PATH = "../../../../../local_data/practice/keras/TextVectorization/"
DATA_PATH = BASE_PATH + "Load_text/"
OUTPUT_PATH = BASE_PATH + "Load_text/"
os.system("mkdir -p " + OUTPUT_PATH)


local = False
local = True
if local == False:
    print("get dataset from Internet")
    data_url = "https://storage.googleapis.com/download.tensorflow.org/data/stack_overflow_16k.tar.gz"
    dataset_dir = utils.get_file(
        origin=data_url, untar=True, cache_dir="stack_overflow", cache_subdir=""
    )
    dataset_dir = pathlib.Path(dataset_dir).parent / "stack_overflow_16k.tar.gz"
    print(dataset_dir)
    print(list(dataset_dir.iterdir()))
else:
    print("get dataset local")
    data_url = DATA_PATH + "stack_overflow_16k.tar.gz"
    dataset_dir = utils.get_file(
        origin=data_url, untar=True, cache_dir="stack_overflow", cache_subdir=""
    )
    dataset_dir = pathlib.Path(dataset_dir).parent / "stack_overflow_16k.tar.gz"
    print(dataset_dir)
    print(list(dataset_dir.iterdir()))

train_dir = dataset_dir / "train"
print(train_dir)
print(list(train_dir.iterdir()))

sample_file = train_dir / "python/1755.txt"

with open(sample_file) as f:
    print(f.read())

batch_size = 32
seed = 42

raw_train_ds = utils.text_dataset_from_directory(
    train_dir, batch_size=batch_size, validation_split=0.2, subset="training", seed=seed
)


for text_batch, label_batch in raw_train_ds.take(1):
    for i in range(2):
        print("Question: ", text_batch.numpy()[i])
        print("Label:", label_batch.numpy()[i])
