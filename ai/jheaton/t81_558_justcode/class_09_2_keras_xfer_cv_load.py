import tensorflow_datasets as tfds
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import logging, os
import matplotlib.pyplot as plt
import time
from tensorflow.keras.models import load_model
import pandas as pd

logging.basicConfig(level=logging.INFO)
# logging.basicConfig(level=logging.DEBUG)

BASE_PATH = "../../../../local_data/jheaton/"
DATA_PATH = "../../../../local_data/tfds/"
OUTPUT_PATH = BASE_PATH+"class_09_2_keras_xfer_cv/"
os.system("mkdir -p " + OUTPUT_PATH)


(train_ds, validation_ds), info= tfds.load(
    "cats_vs_dogs",
    data_dir=DATA_PATH,
    split=["train[:40%]", "train[40%:50%]"],
    with_info=True,
    as_supervised=True, 
)# Include labels
print("train_ds=\n",train_ds,"\n")
print("info=\n",info,"\n")
print("info.features=\n",info.features,"\n")
print("info.features['label'].num_classes=\n",info.features["label"].num_classes,"\n")
print("info.features['label'].names=\n",info.features["label"].names,"\n")


ds = train_ds.take(20)
print("type(image), type(label), label,info.features['label'].names[label]=")
for image, label in tfds.as_numpy(ds):
  print(type(image), type(label), label,info.features["label"].names[label])


c1=tfds.as_dataframe(train_ds.take(20), info)
col1 = c1['label']
# col1 = pd.DataFrame(train_ds, columns=["image","train_ds"])
print(col1)

size = (150, 150)
train_ds = train_ds.map(lambda x, y: (tf.image.resize(x, size), y))
print(train_ds)

batch_size = 32
train_ds = train_ds.cache().batch(batch_size).prefetch(buffer_size=10)
print(train_ds)


filename = "epochs_1.000_date_20250703-133442.h5"
filename = "epochs_1.000_date_20250703-135646.h5"

fullpath = f"{OUTPUT_PATH}{filename}"
model = load_model(fullpath)
model.summary()


# Predict

# pred = model.predict(test_ds)
pred = model.predict(train_ds)
print(pred)

col2 = pd.DataFrame(pred[0:20], columns=["p1"])
print(col2)

compare = pd.concat([col1, col2], axis=1)
# compare.columns = ["y_test", "p1","p2","p3","p4","p5","p6","p7"]
print(compare)
compare.to_csv(OUTPUT_PATH + "pred.csv", index=False)
