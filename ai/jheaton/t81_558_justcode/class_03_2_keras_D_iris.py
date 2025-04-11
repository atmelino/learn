import os.path
import pandas as pd
import io
import requests
import numpy as np
from sklearn import metrics
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation
from tensorflow.keras.callbacks import EarlyStopping

# df = pd.read_csv(
#     "https://data.heatonresearch.com/data/t81-558/iris.csv",
#     na_values=['NA', '?'])
df = pd.read_csv("./input/iris.csv", na_values=["NA", "?"])

# Convert to numpy - Classification
x = df[["sepal_l", "sepal_w", "petal_l", "petal_w"]].values
dummies = pd.get_dummies(df["species"])  # Classification
species = dummies.columns
y = dummies.values


# Build neural network
model = Sequential()
model.add(Dense(50, input_dim=x.shape[1], activation="relu"))  # Hidden 1
model.add(Dense(25, activation="relu"))  # Hidden 2
model.add(Dense(y.shape[1], activation="softmax"))  # Output

model.compile(loss="categorical_crossentropy", optimizer="adam")
model.fit(x, y, verbose=2, epochs=100)

# Print out number of species found:

print(species)

pred = model.predict(x)
print(f"Shape: {pred.shape}")
print(pred[0:10])

np.set_printoptions(suppress=True)
print(y[0:10])

predict_classes = np.argmax(pred, axis=1)
expected_classes = np.argmax(y, axis=1)
diff = predict_classes - expected_classes
print(f"Predictions: {predict_classes}")
print(f"Expected: {expected_classes}")
print(f"diff: {diff}")

print(species[predict_classes[1:70]])

from sklearn.metrics import accuracy_score

correct = accuracy_score(expected_classes, predict_classes)
print(f"Accuracy: {correct}")

sample_flower = np.array([[5.0, 3.0, 4.0, 2.0]], dtype=float)
pred = model.predict(sample_flower)
print(pred)
pred = np.argmax(pred)
print(f"Predict that {sample_flower} is: {species[pred]}")

sample_flower = np.array([[5.0, 3.0, 4.0, 2.0], [5.2, 3.5, 1.5, 0.8]], dtype=float)
pred = model.predict(sample_flower)
print(pred)
pred = np.argmax(pred, axis=1)
print(f"Predict that these two flowers {sample_flower} ")
print(f"are: {species[pred]}")


