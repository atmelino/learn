from tensorflow.keras.preprocessing import sequence
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Embedding
from tensorflow.keras.layers import LSTM
import numpy as np
import pandas as pd

max_features = 4  # 0,1,2,3 (total of 4)
x = [
    [[0], [1], [1], [0], [0], [0]],
    [[0], [0], [0], [2], [2], [0]],
    [[0], [0], [0], [0], [3], [3]],
    [[0], [2], [2], [0], [0], [0]],
    [[0], [0], [3], [3], [0], [0]],
    [[0], [0], [0], [0], [1], [1]],
]
x = np.array(x, dtype=np.float32)
y = np.array([1, 2, 3, 2, 3, 1], dtype=np.int32)

# print("shape of x",x.shape)
# print(x)
array_2d = x.reshape(6, 6)
# array_2d = x.reshape(1, 36)
# print(array_2d)

df_x = pd.DataFrame(array_2d)
print("input x\n", df_x)

# Convert y2 to dummy variables
y2 = np.zeros((y.shape[0], max_features), dtype=np.float32)
# print(y2)

y2[np.arange(y.shape[0]), y] = 1.0
print("learning target\n", y2)

print("Build model...")
model = Sequential()
model.add(LSTM(128, dropout=0.2, recurrent_dropout=0.2, input_shape=(None, 1)))
model.add(Dense(4, activation="sigmoid"))
model.summary()

# exit()


# try using different optimizers and different optimizer configs
model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])
print("Train...")
model.fit(x, y2, epochs=200)

pred = model.predict(x)
print("prediction\n", pred)


predict_classes = np.argmax(pred, axis=1)
print("Predicted classes: {}", predict_classes)
print("Expected classes: {}", y)

xnew = [
    [[2], [2], [0], [0], [0], [0]],
    [[0], [0], [0], [2], [2], [0]],
    [[0], [0], [0], [0], [1], [1]],
    [[0], [3], [3], [0], [0], [0]],
    [[0], [0], [0], [2], [2], [0]],
    [[0], [0], [1], [1], [0], [0]],
]
prednew = model.predict(xnew)
print("prediction\n", prednew)
predict_classesnew = np.argmax(prednew, axis=1)
print("Predicted classes: {}", predict_classesnew)
