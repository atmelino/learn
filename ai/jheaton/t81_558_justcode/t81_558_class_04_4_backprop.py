# %matplotlib inline

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation
from tensorflow.keras.callbacks import EarlyStopping
from scipy.stats import zscore
from sklearn.model_selection import train_test_split
import pandas as pd
import matplotlib.pyplot as plt


# Regression chart.
def chart_regression(pred, y, sort=True):
    t = pd.DataFrame({"pred": pred, "y": y.flatten()})
    if sort:
        t.sort_values(by=["y"], inplace=True)
    plt.plot(t["y"].tolist(), label="expected")
    plt.plot(t["pred"].tolist(), label="prediction")
    plt.xlabel("index of value")
    plt.ylabel("prediction vs actual")
    plt.legend()
    plt.show()
    # plt.savefig('t81_558_class_04_4_backprop.png')


# Read the data set
df = pd.read_csv(
    "https://data.heatonresearch.com/data/t81-558/jh-simple-dataset.csv",
    na_values=["NA", "?"],
)
df.to_csv("jh-simple-dataset_01.csv", sep=",")


# Generate dummies for job
df = pd.concat([df, pd.get_dummies(df["job"], prefix="job")], axis=1)
df.drop("job", axis=1, inplace=True)
df.to_csv("jh-simple-dataset_02.csv", sep=",")

# Generate dummies for area
df = pd.concat([df, pd.get_dummies(df["area"], prefix="area")], axis=1)
df.drop("area", axis=1, inplace=True)
df.to_csv("jh-simple-dataset_03.csv", sep=",")

# Generate dummies for product
df = pd.concat([df, pd.get_dummies(df["product"], prefix="product")], axis=1)
df.drop("product", axis=1, inplace=True)
df.to_csv("jh-simple-dataset_04.csv", sep=",")

# Missing values for income
med = df["income"].median()
df["income"] = df["income"].fillna(med)
df.to_csv("jh-simple-dataset_05.csv", sep=",")

# Standardize ranges
df["income"] = zscore(df["income"])
df["aspect"] = zscore(df["aspect"])
df["save_rate"] = zscore(df["save_rate"])
df["subscriptions"] = zscore(df["subscriptions"])
df.to_csv("jh-simple-dataset_06.csv", sep=",")

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
model.compile(loss="mean_squared_error", optimizer="adam")  # Modify here
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
# chart_regression(pred.flatten(),y_test)

print(y_test.shape)
print(pred.shape)

# print(y_test)
# print(pred)

col1 = pd.DataFrame(y_test, columns=["y_test"])
col2 = pd.DataFrame(pred, columns=["pred"])
diff = col1["y_test"] - col2["pred"]
# print(col1)
# print(col2)
# print(diff)
compare = pd.concat([col1, col2, diff], axis=1)
compare.columns=["y_test","pred","diff"]
print(compare)

# diff=compare['y_test'] - compare['pred']
# print(compare['y_test'] - compare['pred'])

# compare = pd.concat([col1, col2, diff], axis=1)
# print(compare)


# compare2=pd.DataFrame(y_test,pred,y_test-pred)
# print(compare2)
