import pandas as pd
import os
from tensorflow.keras.preprocessing import sequence
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Embedding
from tensorflow.keras.layers import LSTM
from tensorflow.keras.datasets import imdb
from tensorflow.keras.callbacks import EarlyStopping
import numpy as np

BASE_PATH = "../../../../local_data/jheaton/"
DATA_PATH = BASE_PATH + "class_10_2_lstm_sunspots/"
OUTPUT_PATH = BASE_PATH + "class_10_2_lstm_sunspots/"

os.system("mkdir -p " + OUTPUT_PATH)


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
# datafile = "https://data.heatonresearch.com/data/t81-558/SN_d_tot_V2.0.csv"
datafile = DATA_PATH + "SN_d_tot_V2.0.csv"
df = pd.read_csv(
    datafile,
    sep=";",
    header=None,
    names=names,
    na_values=["-1"],
    index_col=False,
)
print("Starting file:")
print(df[0:10])
print("Ending file:")
print(df[-10:])

start_id = max(df[df["obs_num"] == 0].index.tolist()) + 1  # Find the last zer
print(start_id)
df = df[start_id:]  # Trim the rows that have missing observations

print("New Starting file:")
print(df[0:10])

df["sn_value"] = df["sn_value"].astype(float)
df_train = df[df["year"] < 2000]
df_test = df[df["year"] >= 2000]
spots_train = df_train["sn_value"].tolist()
spots_test = df_test["sn_value"].tolist()
print("Training set has {} observations.".format(len(spots_train)))
print("Test set has {} observations.".format(len(spots_test)))


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
print("Shape of training set: {}".format(x_train.shape))
print("Shape of test set: {}".format(x_test.shape))
# print(x_train)
array_2d = x_train.reshape(55150, 10)
# print("input x reshaped(24,6)\n",array_2d)
df_x_train = pd.DataFrame(array_2d)
print("Sliding window of 10 input x_train\n", df_x_train)
df_y_train = pd.DataFrame(y_train)
print("Sliding window of target y_train\n", df_y_train)


print("Build model...")
model = Sequential()
model.add(LSTM(64, dropout=0.0, recurrent_dropout=0.0, input_shape=(None, 1)))
model.add(Dense(32))
model.add(Dense(1))
model.compile(loss="mean_squared_error", optimizer="adam")
monitor = EarlyStopping(
    monitor="val_loss",
    min_delta=1e-3,
    patience=5,
    verbose=1,
    mode="auto",
    restore_best_weights=True,
)
print("Train...")
model.fit(
    x_train,
    y_train,
    validation_data=(x_test, y_test),
    callbacks=[monitor],
    verbose=2,
    epochs=1000,
)
