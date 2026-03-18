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

print(y_train)

x_train = x_train.reshape((x_train.shape[0], x_train.shape[1], 1))
x_test = x_test.reshape((x_test.shape[0], x_test.shape[1], 1))

n_classes = len(np.unique(y_train))

idx = np.random.permutation(len(x_train))
x_train = x_train[idx]
y_train = y_train[idx]

y_train[y_train == -1] = 0
y_test[y_test == -1] = 0