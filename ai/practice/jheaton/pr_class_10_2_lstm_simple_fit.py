from tensorflow.keras.preprocessing import sequence
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Embedding
from tensorflow.keras.layers import LSTM
import numpy as np
import pandas as pd
import logging, os
import time

BASE_PATH = "../../../../local_data/practice/jheaton/"
OUTPUT_PATH = BASE_PATH + "pr_class_10_2_lstm_simple/"
print("OUTPUT_PATH=", OUTPUT_PATH)
os.system("mkdir -p " + OUTPUT_PATH)

max_features = 4  # 0,1,2,3 (total of 4)
set=2
if(set==1):
    print("set 1")
    x_train_1 = [
        [[0], [1], [1], [0], [0], [0]],
        [[0], [0], [0], [2], [2], [0]],
        [[0], [0], [0], [0], [3], [3]],
        [[0], [2], [2], [0], [0], [0]],
        [[0], [0], [3], [3], [0], [0]],
        [[0], [0], [0], [0], [1], [1]],
    ]
    x = np.array(x_train_1, dtype=np.float32)
    y = np.array([1, 2, 3, 2, 3, 1], dtype=np.int32)
    # print("shape of x",x.shape)
    # print("x",x)
    array_2d = x.reshape(6, 6)
    print("input x reshaped(6,6)\n",array_2d)
    # array_2d = x.reshape(1, 36)
    # print("reshaped(1,36)\n",array_2d)
    # df_x = pd.DataFrame(array_2d)
    # print("input x\n", df_x)


if(set==2):
    print("set 2")
    x_train_2 = [
        [[1], [0], [0], [0], [0], [0]],
        [[0], [1], [0], [0], [0], [0]],
        [[0], [0], [1], [0], [0], [0]],
        [[0], [0], [0], [1], [0], [0]],
        [[0], [0], [0], [0], [1], [0]],
        [[0], [0], [0], [0], [0], [1]],
        #
        [[2], [0], [0], [0], [0], [0]],
        [[0], [2], [0], [0], [0], [0]],
        [[0], [0], [2], [0], [0], [0]],
        [[0], [0], [0], [2], [0], [0]],
        [[0], [0], [0], [0], [2], [0]],
        [[0], [0], [0], [0], [0], [2]],
        #
        [[3], [0], [0], [0], [0], [0]],
        [[0], [3], [0], [0], [0], [0]],
        [[0], [0], [3], [0], [0], [0]],
        [[0], [0], [0], [3], [0], [0]],
        [[0], [0], [0], [0], [3], [0]],
        [[0], [0], [0], [0], [0], [3]],
        #
        [[0], [0], [0], [0], [1], [1]],
        [[0], [0], [0], [2], [2], [0]],
        [[0], [0], [0], [0], [3], [3]],
        [[0], [2], [2], [0], [0], [0]],
        [[0], [0], [3], [3], [0], [0]],
        [[0], [0], [0], [0], [1], [1]],
    ]
    x = np.array(x_train_2, dtype=np.float32)
    y = np.array(
        [1, 1, 1, 1, 1, 1,
        2, 2, 2, 2, 2, 2,
        3, 3, 3, 3, 3, 3,
        1, 2, 3, 2, 3, 1], dtype=np.int32)

    print("shape of x",x.shape)
    # print(x)
    array_2d = x.reshape(24, 6)
    # print("input x reshaped(24,6)\n",array_2d)
    df_x = pd.DataFrame(array_2d)
    print("input x\n", df_x)




# Convert y2 to dummy variables
y2 = np.zeros((y.shape[0], max_features), dtype=np.float32)
# print(y2)

y2[np.arange(y.shape[0]), y] = 1.0
print("learning target\n", y2)

# exit(   )

print("Build model...")
model = Sequential()
model.add(LSTM(128, dropout=0.2, recurrent_dropout=0.2, input_shape=(None, 1)))
model.add(Dense(4, activation="sigmoid"))
model.summary()

# exit()

# try using different optimizers and different optimizer configs
model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])
print("Train...")
epochs = 500
history = model.fit(x, y2, epochs=epochs)
acc = history.history["accuracy"]
# print(acc)

# Save model
timestr = time.strftime("%Y%m%d-%H%M%S")
filename_time = f"acc_{acc[-1]:.3f}_epochs_{epochs}_date_{timestr}"
filename_static = "pr_class_10_2_lstm_simple"
fullpath = f"{OUTPUT_PATH}{filename_static}"
print("Saving model to ", fullpath)
model.save(fullpath + ".h5")
model.save(fullpath + ".keras")
fullpath = f"{OUTPUT_PATH}{filename_time}"
print("Saving model to ", fullpath)
model.save(fullpath + ".h5")
model.save(fullpath + ".keras")


pred = model.predict(x)
np.set_printoptions(suppress=True, precision=3)
print("prediction\n", pred)
predict_classes = np.argmax(pred, axis=1)
print("Predicted classes: {}", predict_classes)
print("Expected classes:  {}", y)
