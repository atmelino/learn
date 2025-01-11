# https://www.kaggle.com/code/kutaykutlu/resnet50-transfer-learning-cifar-10-beginner/notebook

# Run with keras version 2 meaning tensorflow <=2.15

import os
import tensorflow as tf
from tensorflow.keras.models import load_model
import pandas as pd
import numpy as np


# Create folders
os.system("mkdir -p ../not_on_github/models/resnet_02")


(training_images, training_labels), (validation_images, validation_labels) = (
    tf.keras.datasets.cifar10.load_data()
)


def preprocess_image_input(input_images):
    input_images = input_images.astype("float32")
    output_ims = tf.keras.applications.resnet50.preprocess_input(input_images)
    return output_ims


valid_X = preprocess_image_input(validation_images)


load_path = "../not_on_github/models/resnet_02"
model = load_model(os.path.join(load_path, "resnet_02.h5"))

model.summary()

probabilities = model.predict(valid_X, batch_size=64)
df1 = pd.DataFrame(probabilities)
# print(df1)

predict = np.argmax(probabilities, axis=1)
df2 = pd.DataFrame(predict, columns=["pred"])
# print(df2)

print("Prediction probabilites and highest index")
df12 = pd.concat([df1, df2], axis=1)
print(df12)

print("Validation values")
df3 = pd.DataFrame(validation_labels, columns=["val"])
print(df3)

print("Validation vs. Prediction values")
df32 = pd.concat([df3, df2], axis=1)
print(df32)
filename_write = "../not_on_github/models/resnet_02/resnet_02_metrics.csv"
df32.to_csv(filename_write, index=False)
