from tensorflow.keras.preprocessing import sequence
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Embedding
from tensorflow.keras.layers import LSTM
import numpy as np
import pandas as pd
import logging, os
from tensorflow.keras.models import load_model

BASE_PATH = "../../../../local_data/practice/jheaton/"
OUTPUT_PATH = BASE_PATH+"pr_class_10_2_lstm_simple/"
print("OUTPUT_PATH=",OUTPUT_PATH)

max_features = 4  # 0,1,2,3 (total of 4)
y = np.array([1, 2, 3, 2, 3, 1], dtype=np.int32)
# Convert y2 to dummy variables
y2 = np.zeros((y.shape[0], max_features), dtype=np.float32)
# print(y2)
y2[np.arange(y.shape[0]), y] = 1.0
print("learning target\n", y2)


filename="pr_class_10_2_lstm_simple.h5"
fullpath = f"{OUTPUT_PATH}{filename}"
model = load_model(fullpath)
model.summary()



x = [
    [[0], [1], [1], [0], [0], [0]],
    [[0], [0], [0], [2], [2], [0]],
    [[0], [0], [0], [0], [3], [3]],
    [[0], [2], [2], [0], [0], [0]],
    [[0], [0], [3], [3], [0], [0]],
    [[0], [0], [0], [0], [1], [1]],
]
x = np.array(x, dtype=np.float32)

pred = model.predict(x)
np.set_printoptions(suppress=True, precision=3)
print("prediction\n", pred)
predict_classes = np.argmax(pred, axis=1)
print("Predicted classes: {}", predict_classes)
print("Expected classes: {}", y)


exit()



def runit(model, inp):
    inp = np.array(inp,dtype=np.float32)
    pred = model.predict(inp)
    return np.argmax(pred[0])


print( runit( model,x))


pred = model.predict(x)
np.set_printoptions(suppress=True, precision=3)
print("prediction\n", pred)


predict_classes = np.argmax(pred, axis=1)
print("Predicted classes: {}", predict_classes)
print("Expected classes: {}", y)


exit()



xnew = [
    [[2], [2], [0], [0], [0], [0]],
    [[0], [0], [0], [2], [2], [0]],
    [[0], [0], [0], [0], [1], [1]],
    [[0], [3], [3], [0], [0], [0]],
    [[0], [0], [0], [2], [2], [0]],
    [[0], [0], [1], [1], [0], [0]],
]
yexpected = np.array([2, 2, 1, 3, 2, 1], dtype=np.int32)
prednew = model.predict(xnew)
print("prediction\n", prednew)
predict_classesnew = np.argmax(prednew, axis=1)
print("Predicted classes: {}", predict_classesnew)
print("Expected classes: {}", yexpected)



print( runit( model,xnew ))

print("Single number in sequence")
x2new = [
    [[0], [0], [0], [0], [0], [1]],
    [[0], [2], [0], [0], [0], [0]],
    [[0], [0], [0], [0], [2], [0]],
    [[0], [0], [3], [0], [0], [0]],
]
x2new = np.array(x2new, dtype=np.float32)
yexpected = np.array([1, 2, 2, 3,], dtype=np.int32)
prednew = model.predict(x2new)
print("prediction\n", prednew)
predict_classesnew = np.argmax(prednew, axis=1)
print("Predicted classes: {}", predict_classesnew)
print("Expected classes: {}", yexpected)



print( runit( model, [[[0],[0],[0],[0],[0],[1]]] ))
print( runit( model, [[[0],[2],[0],[0],[0],[0]]] ))
print( runit( model, [[[0],[2],[2],[0],[0],[0]]] ))
print( runit( model, [[[0],[0],[3],[0],[0],[0]]] ))
