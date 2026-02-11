from tensorflow.keras.preprocessing import sequence
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Embedding
from tensorflow.keras.layers import LSTM
import numpy as np
import pandas as pd
import logging, os
from tensorflow.keras.models import load_model
from sklearn import metrics
from numpy import array

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
# Use partial data file
datafile = DATA_PATH + "SN_d_tot_V2.0_short1.csv"
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
spots = df["sn_value"].tolist()
print(spots)

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

# Predict training data
SEQUENCE_SIZE = 10
x,y = to_sequences(SEQUENCE_SIZE, spots)
x_size=x.shape

def predict_sequence(sequence_number):
    sequence=spots[sequence_number:sequence_number+SEQUENCE_SIZE]
    print(sequence)
    sequence = array(sequence)
    x_input = sequence.reshape(1, 10, 1)
    print("reshaped input for inference\n", x_input)
    x_input_size = x_input.shape
    print("Shape of inference set: {}".format(x_input_size))
    yhat = model.predict(x_input, verbose=1)
    print("model prediction\n", yhat)

predict_sequence(0)
predict_sequence(1)




exit()
# display expected and predicted values
df_x = pd.DataFrame(x.reshape(x_size[0], 10))
print(df_x)
df_y = pd.DataFrame(y,columns=["y"])
print(df_y)
pred = model.predict(x)
df_pred=pd.DataFrame(pred,columns=["pred"])
print(df_pred)
compare = pd.concat([df_x, df_y,df_pred], axis=1)
# compare.columns = ["l", "pred", "pnorm","diff"]
print("Sliding window of 10 inputs and expected y of x_test\n", compare)





