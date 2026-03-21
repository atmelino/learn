# https://keras.io/examples/timeseries/timeseries_classification_transformer/

# Link to this in J. Heaton class Part 10.5: Programming Transformers with Keras

import numpy as np
import keras
from keras import layers
import os

BASE_PATH = "../../../../../local_data/practice/keras/transformers/"
DATA_PATH = BASE_PATH + "timeseries/"
OUTPUT_PATH = BASE_PATH + "timeseries/"

os.system("mkdir -p " + OUTPUT_PATH)

# to place datafiles in local folder:
# cd (wherever your local_data folder is)
# cd practice/keras/transformers
# wget https://raw.githubusercontent.com/hfawaz/cd-diagram/master/FordA/FordA_TRAIN.tsv
# wget https://raw.githubusercontent.com/hfawaz/cd-diagram/master/FordA/FordA_TEST.tsv


def readucr(filename):
    data = np.loadtxt(filename, delimiter="\t")
    y = data[:, 0]
    x = data[:, 1:]
    return x, y.astype(int)


# root_url = "https://raw.githubusercontent.com/hfawaz/cd-diagram/master/FordA/"
root_url = DATA_PATH

x_train, y_train = readucr(root_url + "FordA_TRAIN.tsv")
x_test, y_test = readucr(root_url + "FordA_TEST.tsv")

# print(x_train)
# print(y_train)

print("x_train shape before reshape",x_train.shape)
# print("x_train[0] before reshape\n",x_train[0])
# print("x_train before reshape\n",x_train)
x_train = x_train.reshape((x_train.shape[0], x_train.shape[1], 1))
x_test = x_test.reshape((x_test.shape[0], x_test.shape[1], 1))
print("x_train shape after reshape",x_train.shape)
# print("x_train[0] after reshape\n",x_train[0])
# print("x_train after reshape\n",x_train)

num_classes = len(np.unique(y_train))
# print(n_classes)

idx = np.random.permutation(len(x_train))
# print(idx)
x_train = x_train[idx]
y_train = y_train[idx]
# print("x_train after shuffling\n",x_train)


y_train[y_train == -1] = 0
y_test[y_test == -1] = 0

def make_model(input_shape):
    input_layer = keras.layers.Input(input_shape)

    conv1 = keras.layers.Conv1D(filters=64, kernel_size=3, padding="same")(input_layer)
    conv1 = keras.layers.BatchNormalization()(conv1)
    conv1 = keras.layers.ReLU()(conv1)

    conv2 = keras.layers.Conv1D(filters=64, kernel_size=3, padding="same")(conv1)
    conv2 = keras.layers.BatchNormalization()(conv2)
    conv2 = keras.layers.ReLU()(conv2)

    conv3 = keras.layers.Conv1D(filters=64, kernel_size=3, padding="same")(conv2)
    conv3 = keras.layers.BatchNormalization()(conv3)
    conv3 = keras.layers.ReLU()(conv3)

    gap = keras.layers.GlobalAveragePooling1D()(conv3)

    output_layer = keras.layers.Dense(num_classes, activation="softmax")(gap)

    return keras.models.Model(inputs=input_layer, outputs=output_layer)


model = make_model(input_shape=x_train.shape[1:])
keras.utils.plot_model(model, show_shapes=True)

