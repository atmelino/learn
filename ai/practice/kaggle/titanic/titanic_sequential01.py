from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation
from sklearn.model_selection import train_test_split
from tensorflow.keras.callbacks import EarlyStopping
import pandas as pd
import io
import os
import requests
import numpy as np
from sklearn import metrics
from sklearn.metrics import accuracy_score

BASE_PATH = "../../../../../local_data/kaggle/titanic/"
DATA_PATH = os.path.join(BASE_PATH, "input/")
OUTPUT_PATH = os.path.join(BASE_PATH, "sequential01/")
os.system("mkdir -p " + OUTPUT_PATH)

df = pd.read_csv(DATA_PATH + "train.csv", na_values=["NA", "?"])
print(df)

# Handle missing value
# df['horsepower'] = df['horsepower'].fillna(df['horsepower'].median())
df["Sex"] = df["Sex"].str.replace("female", "1")
df["Sex"] = df["Sex"].str.replace("male", "0")
df["Sex"] = pd.to_numeric(df["Sex"])
print(df)

# exit()


# Pandas to Numpy
x = df[["Sex", "Pclass", "Fare"]].values
y = df["Survived"].values  # regression

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
monitor = EarlyStopping(
    monitor="val_loss",
    min_delta=1e-3,
    patience=5,
    verbose=1,
    mode="auto",
    restore_best_weights=True,
)
model.fit(
    x_train,
    y_train,
    validation_data=(x_test, y_test),
    verbose=2,
    callbacks=[monitor],
    epochs=1000,
)

# Predict
pred = model.predict(x_test)
print(pred)
pred2=np.round(pred)
print(pred2)


# Measure RMSE error. RMSE is common for regression.
score = np.sqrt(metrics.mean_squared_error(pred, y_test))
print("Final score (RMSE): {}".format(score))


col1 = pd.DataFrame(y_test, columns=["y_test"])
col2 = pd.DataFrame(pred, columns=["pred"])
col3 = pd.DataFrame(pred2, columns=["pred2"])
diff = col1["y_test"] - col3["pred2"]
# print(col1)
# print(col2)
# print(diff)
compare = pd.concat([col1, col2, col3, diff], axis=1)
compare.columns=["y_test","pred","pred2","diff"]
compare.to_csv(OUTPUT_PATH + "compare.csv", index=False)
print(compare)


correct = accuracy_score(pred2, y_test)
print(f"Accuracy: {correct}")

exit()


# Generate Kaggle submit file
# Encode feature vector
df_test = pd.read_csv(DATA_PATH + "test.csv", na_values=["NA", "?"])

# Convert to numpy - regression
ids = df_test["id"]
df_test.drop("id", axis=1, inplace=True)
# Handle missing value
df_test["horsepower"] = df_test["horsepower"].fillna(df["horsepower"].median())
x = df_test[
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

# Generate predictions
pred = model.predict(x)

# Create submission data set
df_submit = pd.DataFrame(pred)
df_submit.insert(0, "id", ids)
df_submit.columns = ["id", "mpg"]

# Write submit file locally
# df_submit.to_csv("auto_submit.csv", index=False)
df_submit.to_csv(OUTPUT_PATH + "auto_submit.csv", index=False)
print(df_submit[:5])
