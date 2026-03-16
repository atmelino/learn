import pandas as pd
import os
from tensorflow import keras
from tensorflow.keras import layers

BASE_PATH = "../../../../local_data/jheaton/"
DATA_PATH = BASE_PATH + "class_10_5_keras_transformers/"
OUTPUT_PATH = BASE_PATH + "class_10_5_keras_transformers/"

os.system("mkdir -p " + OUTPUT_PATH)

names = ["year", "month", "day", "dec_year", "sn_value", "sn_error", "obs_num", "extra"]
datafile = DATA_PATH + "SN_d_tot_V2.0.csv"
# datafile = "https://data.heatonresearch.com/data/t81-558/SN_d_tot_V2.0.csv"

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

# Find the last zero and move one beyond
start_id = max(df[df["obs_num"] == 0].index.tolist()) + 1
print(start_id)
df = df[start_id:]  # Trim the rows that have missing observations

df["sn_value"] = df["sn_value"].astype(float)
df_train = df[df["year"] < 2000]
df_test = df[df["year"] >= 2000]
spots_train = df_train["sn_value"].tolist()
spots_test = df_test["sn_value"].tolist()
print("Training set has {} observations.".format(len(spots_train)))
print("Test set has {} observations.".format(len(spots_test)))

import numpy as np


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
print("Shape of training y: {}".format(y_train.shape))
print("Shape of test set: {}".format(x_test.shape))


# print(x_train)
x_tr = np.reshape(x_train, (55150, 10))
print(x_tr)
x_te = np.reshape(x_test, (6381, 10))
print(x_te)


def transformer_encoder(inputs, head_size, num_heads, ff_dim, dropout=0):
    # Normalization and Attention
    x = layers.LayerNormalization(epsilon=1e-6)(inputs)
    x = layers.MultiHeadAttention(
        key_dim=head_size, num_heads=num_heads, dropout=dropout
    )(x, x)
    x = layers.Dropout(dropout)(x)
    res = x + inputs
    # Feed Forward Part
    x = layers.LayerNormalization(epsilon=1e-6)(res)
    x = layers.Conv1D(filters=ff_dim, kernel_size=1, activation="relu")(x)
    x = layers.Dropout(dropout)(x)
    x = layers.Conv1D(filters=inputs.shape[-1], kernel_size=1)(x)
    return x + res


def build_model(
    input_shape,
    head_size,
    num_heads,
    ff_dim,
    num_transformer_blocks,
    mlp_units,
    dropout=0,
    mlp_dropout=0,
):
    inputs = keras.Input(shape=input_shape)
    x = inputs
    for _ in range(num_transformer_blocks):
        x = transformer_encoder(x, head_size, num_heads, ff_dim, dropout)

    x = layers.GlobalAveragePooling1D(data_format="channels_first")(x)

    for dim in mlp_units:
        x = layers.Dense(dim, activation="relu")(x)
        x = layers.Dropout(mlp_dropout)(x)
    outputs = layers.Dense(1)(x)
    return keras.Model(inputs, outputs)


input_shape = x_train.shape[1:]
model = build_model(
    input_shape,
    head_size=256,
    num_heads=4,
    ff_dim=4,
    num_transformer_blocks=4,
    mlp_units=[128],
    mlp_dropout=0.4,
    dropout=0.25,
)
model.compile(
    loss="mean_squared_error", optimizer=keras.optimizers.Adam(learning_rate=1e-4)
)
# model.summary()
callbacks = [keras.callbacks.EarlyStopping(patience=10, restore_best_weights=True)]
model.fit(
    x_train,
    y_train,
    validation_split=0.2,
    epochs=200,
    batch_size=64,
    callbacks=callbacks,
)
model.evaluate(x_test, y_test, verbose=1)
