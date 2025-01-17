import pandas as pd
from scipy.stats import zscore
from sklearn.model_selection import train_test_split
import os
import numpy as np
from sklearn import metrics
from sklearn.model_selection import KFold
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation


print("class_05_2_kfold_C")

# Options for this run
length = 100
folds = 2
length = 2000
folds = 5

# Read the data set
df_original = pd.read_csv(
    "./input/jh-simple-dataset.csv",
    na_values=["NA", "?"],
)
print("dataset original size:\n", df_original.shape)
df = df_original.iloc[0:length]


# Generate dummies for job
df = pd.concat([df, pd.get_dummies(df["job"], prefix="job")], axis=1)
df.drop("job", axis=1, inplace=True)
# Generate dummies for area
df = pd.concat([df, pd.get_dummies(df["area"], prefix="area")], axis=1)
df.drop("area", axis=1, inplace=True)
# Generate dummies for product
df = pd.concat([df, pd.get_dummies(df["product"], prefix="product")], axis=1)
df.drop("product", axis=1, inplace=True)
# Missing values for income
med = df["income"].median()
df["income"] = df["income"].fillna(med)
# Standardize ranges
df["income"] = zscore(df["income"])
df["aspect"] = zscore(df["aspect"])
df["save_rate"] = zscore(df["save_rate"])
df["subscriptions"] = zscore(df["subscriptions"])
# Convert to numpy - Classification
x_columns = df.columns.drop("age").drop("id")
x = df[x_columns].values
y = df["age"].values


EPOCHS = 500

# Keep a 10% holdout
x_main, x_holdout, y_main, y_holdout = train_test_split(x, y, test_size=0.10)
# Cross-validate
kf = KFold(folds)
oos_y = []
oos_pred = []
fold = 0
for train, test in kf.split(x_main):
    fold += 1
    print(f"Fold #{fold}")

    # x_train = x_main[train]
    # y_train = y_main[train]
    # x_test = x_main[test]
    # y_test = y_main[test]
    x_train = np.asarray(x[train]).astype(np.float32)
    y_train = np.asarray(y[train]).astype(np.float32)
    x_test = np.asarray(x[test]).astype(np.float32)
    y_test = np.asarray(y[test]).astype(np.float32)
    x_holdout = np.asarray(x_holdout).astype('float32')

    model = Sequential()
    model.add(Dense(20, input_dim=x.shape[1], activation="relu"))
    model.add(Dense(5, activation="relu"))
    model.add(Dense(1))
    model.compile(loss="mean_squared_error", optimizer="adam")
    model.fit(
        x_train, y_train, validation_data=(x_test, y_test), verbose=0, epochs=EPOCHS
    )
    pred = model.predict(x_test)
    oos_y.append(y_test)
    oos_pred.append(pred)
    # Measure accuracy
    score = np.sqrt(metrics.mean_squared_error(pred,y_test))
    print(f"Fold score (RMSE): {score}")

# Build the oos prediction list and calculate the error.
oos_y = np.concatenate(oos_y)
oos_pred = np.concatenate(oos_pred)
score = np.sqrt(metrics.mean_squared_error(oos_pred,oos_y))
print()
print(f"Cross-validated score (RMSE): {score}")
# Write the cross-validated prediction (from the last neural network)
holdout_pred = model.predict(x_holdout)
score = np.sqrt(metrics.mean_squared_error(holdout_pred,y_holdout))
print(f"Holdout score (RMSE): {score}")