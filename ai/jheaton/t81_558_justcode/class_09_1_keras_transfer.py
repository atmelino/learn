import pandas as pd
import io
import requests
import numpy as np
from sklearn import metrics
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation
from tensorflow.keras.callbacks import EarlyStopping
import logging, os

# logging.basicConfig(level=logging.INFO)
logging.basicConfig(level=logging.DEBUG)

BASE_PATH = "../../../../local_data/jheaton"
DATA_PATH = os.path.join(BASE_PATH, "input/")
OUTPUT_PATH = os.path.join(BASE_PATH, "class_09_1_keras_transfer/")
os.system("mkdir -p " + OUTPUT_PATH)

df = pd.read_csv(DATA_PATH + "/iris.csv", na_values=["NA", "?"])
logging.debug(df)


# Convert to numpy - Classification
x = df[["sepal_l", "sepal_w", "petal_l", "petal_w"]].values
dummies = pd.get_dummies(df["species"])  # Classification
species = dummies.columns
y = dummies.values
logging.debug(y)

# Build neural network
model = Sequential()
model.add(Dense(50, input_dim=x.shape[1], activation="relu"))  # Hidden 1
model.add(Dense(25, activation="relu"))  # Hidden 2
model.add(Dense(y.shape[1], activation="softmax"))  # Output
model.compile(loss="categorical_crossentropy", optimizer="adam")
model.fit(x, y, verbose=2, epochs=100)

from sklearn.metrics import accuracy_score
pred = model.predict(x)
predict_classes = np.argmax(pred,axis=1)
expected_classes = np.argmax(y,axis=1)
correct = accuracy_score(expected_classes,predict_classes)
print(f"Training Accuracy: {correct}")

model.summary()

model2 = Sequential()
for layer in model.layers:
    model2.add(layer)
model2.summary()

from sklearn.metrics import accuracy_score
pred = model2.predict(x)
predict_classes = np.argmax(pred,axis=1)
expected_classes = np.argmax(y,axis=1)
correct = accuracy_score(expected_classes,predict_classes)
print(f"Training Accuracy: {correct}")

df_cost = pd.read_csv(DATA_PATH + "/iris_cost.csv", na_values=["NA", "?"])
logging.debug(df_cost)


model3 = Sequential()
for i in range(2):
    layer = model.layers[i]
    layer.trainable = False
    model3.add(layer)
model3.summary()

model3.add(Dense(1)) # Output
model3.compile(loss='mean_squared_error', optimizer='adam')
model3.summary()













