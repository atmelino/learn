# https://www.tensorflow.org/guide/data

import tensorflow as tf
import pathlib
import os
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

np.set_printoptions(precision=4)


flowers_root = tf.keras.utils.get_file(
    'flower_photos',
    'https://storage.googleapis.com/download.tensorflow.org/example_images/flower_photos.tgz',
    untar=True)
flowers_root = pathlib.Path(flowers_root)


list_ds = tf.data.Dataset.list_files(str(flowers_root/'*/*'))

print(list_ds)
print(iter(list_ds))

file_path = next(iter(list_ds))
print(file_path)