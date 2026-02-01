from tensorflow.keras.preprocessing import sequence
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Embedding
from tensorflow.keras.layers import LSTM
import numpy as np
import pandas as pd
import logging, os
from tensorflow.keras.models import load_model

BASE_PATH = "../../../../local_data/practice/jheaton/"
OUTPUT_PATH = BASE_PATH + "pr_class_10_2_lstm_simple/"
print("OUTPUT_PATH=", OUTPUT_PATH)


# filename = "pr_class_10_2_lstm_simple.h5"
filename = "pr_class_10_2_lstm_simple.keras"
fullpath = f"{OUTPUT_PATH}{filename}"
model = load_model(fullpath)
model.summary()


def runit(model, inp):
    inp = np.array(inp, dtype=np.float32)
    pred = model.predict(inp)
    # return np.argmax(pred[0])
    return np.argmax(pred, axis=1)

# Predict the original training data
x_train = [
    [[0], [1], [1], [0], [0], [0]],
    [[0], [0], [0], [2], [2], [0]],
    [[0], [0], [0], [0], [3], [3]],
    [[0], [2], [2], [0], [0], [0]],
    [[0], [0], [3], [3], [0], [0]],
    [[0], [0], [0], [0], [1], [1]],
]
y = np.array([1, 2, 3, 2, 3, 1], dtype=np.int32)
p=runit(model, x_train)
print(p, " - Prediction")
print(y, " - Expected classes")
print(f"Accuracy: {np.mean(p == y) * 100:.2f}%")

x1 = [
    [[2], [2], [0], [0], [0], [0]],
    [[0], [0], [0], [2], [2], [0]],
    [[0], [0], [0], [0], [1], [1]],
    [[0], [3], [3], [0], [0], [0]],
    [[0], [0], [0], [2], [2], [0]],
    [[0], [0], [1], [1], [0], [0]],
]
y1 = np.array([2, 2, 1, 3, 2, 1], dtype=np.int32)
p1=runit(model, x_train)
print(p1, " - Prediction")
print(y1, " - Expected classes")
print(f"Accuracy: {np.mean(p1 == y1) * 100:.2f}%")


print("Single number in sequence")
x3 = [
    [[0], [0], [0], [0], [0], [1]],
    [[0], [2], [0], [0], [0], [0]],
    [[0], [0], [0], [0], [2], [0]],
    [[0], [0], [3], [0], [0], [0]],
]
y3 = np.array(
    [
        1,
        2,
        2,
        3,
    ],
    dtype=np.int32,
)

print(runit(model, x3), " - Prediction")
print(y3, " - Expected classes")


print(runit(model, [[[0], [0], [0], [0], [0], [1]]]))
print(runit(model, [[[0], [2], [0], [0], [0], [0]]]))
print(runit(model, [[[0], [2], [2], [0], [0], [0]]]))
print(runit(model, [[[0], [0], [3], [0], [0], [0]]]))
