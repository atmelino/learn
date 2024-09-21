import pandas as pd
from scipy.stats import zscore
from sklearn.model_selection import train_test_split
import os
import numpy as np
from sklearn import metrics
from scipy.stats import zscore
from sklearn.model_selection import KFold
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation

pd.set_option("display.max_rows", None)

# Read the data set
# df = pd.read_csv(
#     "./input/jh-simple-dataset_short100.csv",
#     na_values=["NA", "?"],
# )
df = pd.read_csv(
    "./input/jh-simple-dataset.csv",
    na_values=["NA", "?"],
)
# print(df.head())
# print("original data set\n", df)

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

print("Table after feature vector encoding\n",df.head())

# Convert to numpy - Classification
x_columns = df.columns.drop("age").drop("id")
x = df[x_columns].values
y = df["age"].values

EPOCHS = 500
# EPOCHS = 100


# Cross-Validate
kf = KFold(5, shuffle=True, random_state=42)  # Use for KFold classification
# kf = KFold(2)  # Use for KFold classification
print(kf)
oos_y = []
oos_pred = []

fold = 0
for train, test in kf.split(x):
    fold += 1
    print(f"Fold #{fold}")
    print(f"  Train: index={train}")
    print(f"  Test:  index={test}")
    # x_train = x[train]
    # y_train = y[train]
    # x_test = x[test]
    # y_test = y[test]

    x_train = np.asarray(x[train]).astype(np.float32)
    y_train = np.asarray(y[train]).astype(np.float32)
    x_test = np.asarray(x[test]).astype(np.float32)
    y_test = np.asarray(y[test]).astype(np.float32)

    model = Sequential()
    model.add(Dense(20, input_dim=x.shape[1], activation="relu"))
    model.add(Dense(10, activation="relu"))
    model.add(Dense(1))
    model.compile(loss="mean_squared_error", optimizer="adam")

    model.fit(
        x_train, y_train, validation_data=(x_test, y_test), verbose=0, epochs=EPOCHS
    )

    pred = model.predict(x_test)

    oos_y.append(y_test)
    oos_pred.append(pred)

    # Measure this fold's RMSE
    score = np.sqrt(metrics.mean_squared_error(pred, y_test))
    print(f"Fold score (RMSE): {score}")

# Build the oos prediction list and calculate the error.
oos_y = np.concatenate(oos_y)
oos_pred = np.concatenate(oos_pred)
score = np.sqrt(metrics.mean_squared_error(oos_pred, oos_y))
print(f"Final, out of sample score (RMSE): {score}")

# Write the cross-validated prediction
print("Write the cross-validated prediction to file")
oos_y = pd.DataFrame(oos_y)
oos_pred = pd.DataFrame(oos_pred)
oosDF = pd.concat([df, oos_y, oos_pred], axis=1)
filename_write="./output/kfold_5_2.csv"
oosDF.to_csv(filename_write,index=False)
# , sep=","
