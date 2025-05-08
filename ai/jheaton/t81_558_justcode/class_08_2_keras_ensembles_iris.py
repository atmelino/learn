from sklearn import metrics
import scipy as sp
import numpy as np
import math
import pandas as pd
import io
import requests
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation
from tensorflow.keras.callbacks import EarlyStopping
from sklearn.model_selection import train_test_split
from IPython.display import display, HTML
from sklearn import metrics
from sklearn import metrics
from sklearn.metrics import accuracy_score


# df = pd.read_csv(
# "https://data.heatonresearch.com/data/t81-558/iris.csv",
# na_values=['NA', '?'])
df = pd.read_csv(
    "../../../../local_data/jheaton/class_08_2_keras_ensembles/iris.csv",
    na_values=["NA", "?"],
)

# Convert to numpy - Classification
x = df[["sepal_l", "sepal_w", "petal_l", "petal_w"]].values
dummies = pd.get_dummies(df["species"])  # Classification
species = dummies.columns
y = dummies.values
# Split into train/test
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.25, random_state=42
)
# Build neural network
model = Sequential()
model.add(Dense(50, input_dim=x.shape[1], activation="relu"))  # Hidden 1
model.add(Dense(25, activation="relu"))  # Hidden 2
model.add(Dense(y.shape[1], activation="softmax"))  # Output
model.compile(loss="categorical_crossentropy", optimizer="adam")
model.fit(x_train, y_train, verbose=2, epochs=100)

pred = model.predict(x_test)
predict_classes = np.argmax(pred, axis=1)
expected_classes = np.argmax(y_test, axis=1)
correct = accuracy_score(expected_classes, predict_classes)
print(f"Accuracy: {correct}")

# Rank the features


def perturbation_rank(model, x, y, names, regression):
    errors = []

    for i in range(x.shape[1]):
        hold = np.array(x[:, i])
        np.random.shuffle(x[:, i])

        if regression:
            pred = model.predict(x)
            error = metrics.mean_squared_error(y, pred)
        else:
            pred = model.predict(x)
            error = metrics.log_loss(y, pred)

        errors.append(error)
        x[:, i] = hold

    max_error = np.max(errors)
    importance = [e / max_error for e in errors]

    data = {"name": names, "error": errors, "importance": importance}
    result = pd.DataFrame(data, columns=["name", "error", "importance"])
    result.sort_values(by=["importance"], ascending=[0], inplace=True)
    result.reset_index(inplace=True, drop=True)
    return result


# Rank the features


def perturbation_rank_verbose(model, x, y, names, regression):
    errors = []
    # print(x.shape)
    # print(x.shape[1])
    # print(x)

    for i in range(x.shape[1]):
        print("column", i)
        hold = np.array(x[:, i])

        # print("x before shuffle")
        # print(x)
        x_before = pd.DataFrame(x, columns=["sl", "sw", "pl", "pw"], copy=True)
        print(x_before.shape)
        # print(x_before)

        np.random.shuffle(x[:, i])

        # print("x after shuffle")
        # print(x)
        x_after = pd.DataFrame(x, columns=["sl", "sw", "pl", "pw"], copy=True)
        # print(x_after)

        diff_shuffle = x_after.sub(x_before)
        a = [" "] * x.shape[0]
        line = pd.DataFrame(a)

        pred = model.predict(x)
        error = metrics.log_loss(y, pred)
        # print(pred)
        predict_classes = np.argmax(pred, axis=1)
        dp = pd.DataFrame(predict_classes, columns=["pr"])

        expected_classes = np.argmax(y, axis=1)
        de = pd.DataFrame(expected_classes, columns=["ex"])

        diff_pred = predict_classes - expected_classes
        df = pd.DataFrame(diff_pred, columns=["df"])

        compare = pd.concat(
            [x_before, line, x_after, line, diff_shuffle, dp, de, df], axis=1
        )
        print("Before shuffle - after shuffle - difference")
        print(compare)

        errors.append(error)
        x[:, i] = hold

    max_error = np.max(errors)
    importance = [e / max_error for e in errors]

    data = {"name": names, "error": errors, "importance": importance}
    result = pd.DataFrame(data, columns=["name", "error", "importance"])
    result.sort_values(by=["importance"], ascending=[0], inplace=True)
    result.reset_index(inplace=True, drop=True)
    return result


names = list(df.columns)  # x+y column names
names.remove("species")  # remove the target(y)
# rank = perturbation_rank(model, x_test, y_test, names, False)
rank = perturbation_rank_verbose(model, x_test, y_test, names, False)
display(rank)
