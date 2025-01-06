# https://keras.io/api/datasets/california_housing/
# requires keras version 3
# code from AI search result "California Housing price regression dataset code keras"

import numpy as np
import pandas as pd
from keras.datasets import california_housing
from keras.models import Sequential
from keras.layers import Dense


(x_train, y_train), (x_test, y_test) = california_housing.load_data()

print(x_train.shape)
print(y_train.shape)

