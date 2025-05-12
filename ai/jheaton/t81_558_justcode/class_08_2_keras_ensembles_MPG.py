from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation
from sklearn.model_selection import train_test_split
import pandas as pd
import io
import os
import requests
import numpy as np
from sklearn import metrics

save_path = "."
df = pd.read_csv(
    "https://data.heatonresearch.com/data/t81-558/auto-mpg.csv", na_values=["NA", "?"]
)
cars = df["name"]

# Handle missing value
df["horsepower"] = df["horsepower"].fillna(df["horsepower"].median())

# Pandas to Numpy
x = df[
    [
        "cylinders",
        "displacement",
        "horsepower",
        "weight",
        "acceleration",
        "year",
        "origin",
    ]
].values
y = df["mpg"].values  # regression

# Split into train/test
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.25, random_state=42
)

# Build the neural network
model = Sequential()
model.add(Dense(25, input_dim=x.shape[1], activation="relu"))  # Hidden 1
model.add(Dense(10, activation="relu"))  # Hidden 2
model.add(Dense(1))  # Output
model.compile(loss="mean_squared_error", optimizer="adam")
model.fit(x_train, y_train, verbose=2, epochs=100)

# Predict
pred = model.predict(x)


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


# Rank the features - verbose
def perturbation_rank_verbose(model, x, y, names, regression):
    errors = []
    a = [" "] * x.shape[0]

    print("x.shape ", x.shape)
    diffs = pd.DataFrame(a)
    # print(x.shape[1])
    # print(x)

    for i in range(x.shape[1]):
        print("column", i)
        hold = np.array(x[:, i])

        # print("x before shuffle")
        # print(x)
        x_before = pd.DataFrame(
            x, columns=["cy", "di", "ho", "we", "ac", "ye", "or"], copy=True
        )
        # print("x_before.shape ", x_before.shape)
        # print(x_before)

        np.random.shuffle(x[:, i])

        # print("x after shuffle")
        # print(x)
        x_after = pd.DataFrame(
            x, columns=["cy", "di", "ho", "we", "ac", "ye", "or"], copy=True
        )
        # print(x_after)

        diff_shuffle = x_after.sub(x_before)
        a = [" "] * x.shape[0]
        line = pd.DataFrame(a)

        if regression:
            pred = model.predict(x)
            error = metrics.mean_squared_error(y, pred)

            y_reshaped=y.reshape(-1, 1)
            # print("y shape ", y.shape)
            # print(y)
            # print("y_reshaped shape ", y_reshaped.shape)
            # print(y_reshaped)
            # print("pred shape ", pred.shape)
            # print( pred)

            predict_values = pred
            dp = pd.DataFrame(predict_values, columns=["pr"])
            print("dp.shape ", dp.shape)
            print(dp)

            expected_values = y_reshaped
            de = pd.DataFrame(expected_values, columns=["ex"])
            print("de.shape ", de.shape)
            print(de)

            # diff_pred = predict_values - expected_values
            # diff_pred = de.sub(dp)
            # diff_pred = de-dp
            # diff_pred = y_reshaped.sub(pred)

            diff_pred = pred - y
            print("diff_pred.shape ", diff_pred.shape)
            print(diff_pred)
            df = pd.DataFrame(diff_pred, columns=["df" + str(i)])

            diffs = pd.concat([diffs, df], axis=1)

            compare = pd.concat(
                [x_before, line, x_after, line, diff_shuffle, dp, de, df], axis=1
            )
            print("Before shuffle - after shuffle - difference")
            print(compare)

        else:
            pred = model.predict(x)
            error = metrics.log_loss(y, pred)

            predict_classes = np.argmax(pred, axis=1)
            dp = pd.DataFrame(predict_classes, columns=["pr"])

            expected_classes = np.argmax(y, axis=1)
            de = pd.DataFrame(expected_classes, columns=["ex"])

            diff_pred = predict_classes - expected_classes
            df = pd.DataFrame(diff_pred, columns=["df" + str(i)])

            diffs = pd.concat([diffs, df], axis=1)

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
    diffs.rename(
        columns={"df0": "sl", "df1": "sw", "df2": "pl", "df3": "pw"}, inplace=True
    )

    return (result, diffs)


from IPython.display import display, HTML

names = list(df.columns)  # x+y column names
# names.remove("name")
# names.remove("mpg")  # remove the target(y)
# rank = perturbation_rank(model, x_test, y_test, names, True)
# display(rank)

rank, diffs = perturbation_rank_verbose(model, x_test, y_test, names, True)
display(rank)
display(diffs)
