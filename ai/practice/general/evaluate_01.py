# %matplotlib inline

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation
from tensorflow.keras.callbacks import EarlyStopping
from scipy.stats import zscore
from sklearn.model_selection import train_test_split
import pandas as pd
import matplotlib.pyplot as plt
import os


os.makedirs("./output", exist_ok=True)

# Read the data set
df = pd.read_csv(
    "https://data.heatonresearch.com/data/t81-558/jh-simple-dataset.csv",
    na_values=["NA", "?"],
)

# Generate dummies for job
df = pd.concat([df, pd.get_dummies(df["job"], prefix="job")], axis=1)
df.drop("job", axis=1, inplace=True)
df.to_csv("./output/class_04_4_jh-simple-dataset_02.csv", sep=",")

# Generate dummies for area
df = pd.concat([df, pd.get_dummies(df["area"], prefix="area")], axis=1)
df.drop("area", axis=1, inplace=True)
df.to_csv("./output/class_04_4_jh-simple-dataset_03.csv", sep=",")

# Generate dummies for product
df = pd.concat([df, pd.get_dummies(df["product"], prefix="product")], axis=1)
df.drop("product", axis=1, inplace=True)
df.to_csv("./output/class_04_4_jh-simple-dataset_04.csv", sep=",")

# Missing values for income
med = df["income"].median()
df["income"] = df["income"].fillna(med)
df.to_csv("./output/class_04_4_jh-simple-dataset_05.csv", sep=",")

# Standardize ranges
df["income"] = zscore(df["income"])
df["aspect"] = zscore(df["aspect"])
df["save_rate"] = zscore(df["save_rate"])
df["subscriptions"] = zscore(df["subscriptions"])
df.to_csv("./output/class_04_4_jh-simple-dataset_06.csv", sep=",")

# print("Table after feature vector encoding\n", df.head())
print("dataset size after feature vector encoding:\n", df.shape)

# Convert to numpy - Classification
x_columns = df.columns.drop("age").drop("id")
x = df[x_columns].values
y = df["age"].values

x = x.astype("float32")
y = y.astype("float32")


# Create train/test
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.01, random_state=42
)

# Build the neural network
model = Sequential()
model.add(Dense(25, input_dim=x.shape[1], activation="relu"))  # Hidden 1
model.add(Dense(10, activation="relu"))  # Hidden 2
model.add(Dense(1))  # Output
model.compile(loss="mean_squared_error", optimizer="adam", metrics=["accuracy"])  # Modify here
# model.compile(loss='mean_squared_error', optimizer='sgd') # Modify here
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
    callbacks=[monitor],
    verbose=0,
    epochs=1000,
)

# Plot the chart
pred = model.predict(x_test)

print(y_test.shape)
print(pred.shape)

col1 = pd.DataFrame(y_test, columns=["y_test"])
col2 = pd.DataFrame(pred, columns=["pred"])
diff = col1["y_test"] - col2["pred"]
compare = pd.concat([col1, col2, diff], axis=1)
compare.columns=["y_test","pred","diff"]
print(compare)


# test_loss, test_acc = model.evaluate(x_test, y_test,verbose=2)
# print(f'Test loss: {test_loss}   Test accuracy: {test_acc}')

# scores = model.evaluate(x_test, y_test,verbose=2)
# print("%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
# print(scores)


# evaluate the model

print("model.metrics_names",model.metrics_names)

# scores = model.evaluate(x_test, y_test, verbose=0)
# print("%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
# cvscores.append(scores[1] * 100)


