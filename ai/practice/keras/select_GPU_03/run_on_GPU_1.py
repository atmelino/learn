# https://www.tensorflow.org/guide/gpu#using_a_single_gpu_on_a_multi-gpu_system

import tensorflow as tf
print("Simple TensorFlow Regression: MPG")
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation
import pandas as pd
import io
import os
import requests
import numpy as np
from sklearn import metrics

# df = pd.read_csv(
#     "https://data.heatonresearch.com/data/t81-558/auto-mpg.csv",
#     na_values=['NA', '?'])

DATA_PATH = "../../../../../local_data/jheaton/input/"

df = pd.read_csv(DATA_PATH+"auto-mpg.csv", na_values=["NA", "?"])
print(df)

cars = df["name"]

# Handle missing value
df["horsepower"] = df["horsepower"].fillna(df["horsepower"].median())

# Pandas to Numpy
x = df[
    [
        "cylinders",
        "displacement",
        "horsepower",
        "weight",
        "acceleration",
        "year",
        "origin",
    ]
].values
# x = df[['cylinders']].values
y = df["mpg"].values  # regression
print(x)


print("Num GPUs Available: ", len(tf.config.experimental.list_physical_devices("GPU")))

# tf.debugging.set_log_device_placement(True)
tf.debugging.set_log_device_placement(False)

try:
    # Specify the GPU device
    print('Using /device:GPU:1')
    with tf.device("/device:GPU:1"):

        # Build the neural network
        model = Sequential()
        model.add(Dense(25, input_dim=x.shape[1], activation="relu"))  # Hidden 1
        model.add(Dense(10, activation="relu"))  # Hidden 2
        model.add(Dense(1))  # Output
        model.compile(loss="mean_squared_error", optimizer="adam")
        model.summary()
        model.fit(x, y, verbose=2, epochs=100)

        pred = model.predict(x)
        print(f"Shape: {pred.shape}")
        print(pred[0:10])

        # Measure RMSE error.  RMSE is common for regression.
        score = np.sqrt(metrics.mean_squared_error(pred, y))
        print(f"Final score (RMSE): {score}")

        # Sample predictions
        for i in range(10):
            print(f"{i+1}. Car name: {cars[i]}, MPG: {y[i]}, " + f"predicted MPG: {pred[i]}")

except RuntimeError as e:
    print(e)
