import tensorflow_datasets as tfds
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import logging, os
import matplotlib.pyplot as plt
import time
from tensorflow.keras.models import load_model

logging.basicConfig(level=logging.INFO)
# logging.basicConfig(level=logging.DEBUG)

BASE_PATH = "../../../../local_data/jheaton/"
DATA_PATH = "../../../../local_data/tfds/"
OUTPUT_PATH = BASE_PATH+"class_09_2_keras_xfer_cv/"
os.system("mkdir -p " + OUTPUT_PATH)

filename = "epochs_1.000_date_20250703-133442.h5"
fullpath = f"{OUTPUT_PATH}{filename}"
model = load_model(fullpath)
model.summary()


# Predict

(train_ds, validation_ds), metadata= tfds.load(
    "cats_vs_dogs",
    data_dir=DATA_PATH,
    split=["train[:40%]", "train[40%:50%]"],
    with_info=True,
    as_supervised=True, 
)# Include labels
print(train_ds)

size = (150, 150)
train_ds = train_ds.map(lambda x, y: (tf.image.resize(x, size), y))
print(train_ds)


batch_size = 32
train_ds = train_ds.cache().batch(batch_size).prefetch(buffer_size=10)
print(train_ds)

# pred = model.predict(test_ds)
pred = model.predict(train_ds)

print(pred)