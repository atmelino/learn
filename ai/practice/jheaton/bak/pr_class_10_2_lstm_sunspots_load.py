from tensorflow.keras.preprocessing import sequence
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Embedding
from tensorflow.keras.layers import LSTM
import numpy as np
import pandas as pd
import logging, os
from tensorflow.keras.models import load_model
from sklearn import metrics

BASE_PATH = "../../../../local_data/practice/jheaton/"
DATA_PATH = BASE_PATH + "pr_class_10_2_lstm_sunspots/"
OUTPUT_PATH = BASE_PATH + "pr_class_10_2_lstm_sunspots/"
print("OUTPUT_PATH=", OUTPUT_PATH)


# Load model
filename_static = "pr_class_10_2_lstm_sunspots.keras"
fullpath = f"{OUTPUT_PATH}{filename_static}"
model = load_model(fullpath)
model.summary()


# Predict the original test data
names = [
    "year",
    "month",
    "day",
    "dec_year",
    "sn_value",
    "sn_error",
    "obs_num",
    "unused1",
]
# Use data file that has empty datapoints removed
datafile = DATA_PATH + "SN_d_tot_V2.0_trimmed.csv"
df = pd.read_csv(
    datafile,
    sep=";",
    header=None,
    names=names,
    na_values=["-1"],
    index_col=False,
)
print(df)

df["sn_value"] = df["sn_value"].astype(float)
df_train = df[df["year"] < 2000]
df_test = df[df["year"] >= 2000]
spots_train = df_train["sn_value"].tolist()
spots_test = df_test["sn_value"].tolist()


def to_sequences(seq_size, obs):
    x = []
    y = []
    for i in range(len(obs) - SEQUENCE_SIZE):
        # print(i)
        window = obs[i : (i + SEQUENCE_SIZE)]
        after_window = obs[i + SEQUENCE_SIZE]
        window = [[x] for x in window]
        # print("{} - {}".format(window,after_window))
        x.append(window)
        y.append(after_window)
    return np.array(x), np.array(y)

SEQUENCE_SIZE = 10
x_train, y_train = to_sequences(SEQUENCE_SIZE, spots_train)
x_test, y_test = to_sequences(SEQUENCE_SIZE, spots_test)
x_train_size=x_train.shape
x_test_size=x_test.shape
print("Shape of training set: {}".format(x_train_size))
print("Shape of test set: {}".format(x_test_size))
print(x_train[0])
print(x_train[1])
df_x_train = pd.DataFrame(x_train.reshape(x_train_size[0], 10))
print(df_x_train)
df_y_train = pd.DataFrame(y_train,columns=["y"])
print(df_y_train)
pred = model.predict(x_train)
df_pred=pd.DataFrame(pred)
print(df_pred)



exit()



# Predict training data
pred = model.predict(x_train)
print(pred)






array_2d = x_test.reshape(x_test_size[0], 10)
df_x_test = pd.DataFrame(array_2d)
# print("Sliding window of 10 input x_test\n", df_x_test)
df_y_test = pd.DataFrame(y_test,columns=["y"])
# print("Sliding window of target y_test\n", df_y_test)
pred = model.predict(x_test)
print(pred)
df_pred=pd.DataFrame(pred)
print(df_pred)

# compare = pd.concat([df_x_test, df_y_test], axis=1)
compare = pd.concat([df_x_test, df_y_test,df_pred], axis=1)
# compare.columns = ["l", "pred", "pnorm","diff"]
print("Sliding window of 10 inputs and expected y of x_test\n", compare)



exit()


print("test data prediction")
pred = model.predict(x_test)
score = np.sqrt(metrics.mean_squared_error(pred,y_test))
print("Score (RMSE): {}".format(score))
print(y_test)
print(y_test.shape)


array_2d = x_train.reshape(55150, 10)
df_x_train = pd.DataFrame(array_2d)
print("Sliding window of 10 input x_train\n", df_x_train)
df_y_train = pd.DataFrame(y_train)
print("Sliding window of target y_train\n", df_y_train)



# display expected and predicted values




exit()

print("training data prediction")
pred = model.predict(x_train)
score = np.sqrt(metrics.mean_squared_error(pred,y_train))
print("Score (RMSE): {}".format(score))

print(y_train)
print(y_train.shape)












def runit(model, inp):
    inp = np.array(inp, dtype=np.float32)
    pred = model.predict(inp)
    # return np.argmax(pred[0])
    return np.argmax(pred, axis=1)


# Predict the original training data
x_train_1 = [
    [[0], [1], [1], [0], [0], [0]],
    [[0], [0], [0], [2], [2], [0]],
    [[0], [0], [0], [0], [3], [3]],
    [[0], [2], [2], [0], [0], [0]],
    [[0], [0], [3], [3], [0], [0]],
    [[0], [0], [0], [0], [1], [1]],
]
y = np.array([1, 2, 3, 2, 3, 1], dtype=np.int32)
p = runit(model, x_train_1)
print(p, " - Prediction of training data x_train_1")
print(y, " - Expected classes")
print(f"Accuracy: {np.mean(p == y) * 100:.2f}%")

x_train_3 = [
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
    [[1], [1], [0], [0], [0], [0]],
    [[0], [1], [1], [0], [0], [0]],
    [[0], [0], [1], [1], [0], [0]],
    [[0], [0], [0], [1], [1], [0]],
    [[0], [0], [0], [0], [1], [1]],
    #
    [[2], [2], [0], [0], [0], [0]],
    [[0], [2], [2], [0], [0], [0]],
    [[0], [0], [2], [2], [0], [0]],
    [[0], [0], [0], [2], [2], [0]],
    [[0], [0], [0], [0], [2], [2]],
    [[3], [3], [0], [0], [0], [0]],
    [[0], [3], [3], [0], [0], [0]],
    [[0], [0], [3], [3], [0], [0]],
    [[0], [0], [0], [3], [3], [0]],
    [[0], [0], [0], [0], [3], [3]],
]
y = np.array(
    [
        1,
        1,
        1,
        1,
        1,
        1,
        2,
        2,
        2,
        2,
        2,
        2,
        3,
        3,
        3,
        3,
        3,
        3,
        1,
        1,
        1,
        1,
        1,
        2,
        2,
        2,
        2,
        2,
        3,
        3,
        3,
        3,
        3,
    ],
    dtype=np.int32,
)
p = runit(model, x_train_3)
print(p, " - Prediction of training data x_train3")
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
p1 = runit(model, x1)
print(p1, " - Prediction of new data")
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
