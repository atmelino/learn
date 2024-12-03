from scipy.stats import zscore
from sklearn.model_selection import train_test_split
import pandas as pd
import os
import numpy as np
import time
import statistics
from sklearn import metrics
from sklearn.model_selection import StratifiedKFold
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation
from tensorflow.keras import regularizers
from tensorflow.keras.callbacks import EarlyStopping
from sklearn.model_selection import StratifiedShuffleSplit

print("class_05_5_bootstrap_B")


# Nicely formatted time string
def hms_string(sec_elapsed):
    h = int(sec_elapsed / (60 * 60))
    m = int((sec_elapsed % (60 * 60)) / 60)
    s = sec_elapsed % 60
    return "{}:{:>02}:{:>05.2f}".format(h, m, s)


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
# Missing values for income
med = df["income"].median()
df["income"] = df["income"].fillna(med)
# Standardize ranges
df["income"] = zscore(df["income"])
df["aspect"] = zscore(df["aspect"])
df["save_rate"] = zscore(df["save_rate"])
df["age"] = zscore(df["age"])
df["subscriptions"] = zscore(df["subscriptions"])
# Convert to numpy - Classification
x_columns = df.columns.drop("product").drop("id")
x = df[x_columns].values
dummies = pd.get_dummies(df["product"])  # Classification
products = dummies.columns
y = dummies.values

SPLITS = 50

# Bootstrap
boot = StratifiedShuffleSplit(n_splits=SPLITS, test_size=0.1, random_state=42)

# Track progress
mean_benchmark = []
epochs_needed = []
num = 0

# Loop through samples
for train, test in boot.split(x, df["product"]):
    start_time = time.time()
    num += 1

    # Split train and test
    # x_train = x[train]
    # y_train = y[train]
    # x_test = x[test]
    # y_test = y[test]

    x_train = np.asarray(x[train]).astype(np.float32)
    y_train = np.asarray(y[train]).astype(np.float32)
    x_test = np.asarray(x[test]).astype(np.float32)
    y_test = np.asarray(y[test]).astype(np.float32)


    # Construct neural network
    model = Sequential()
    model.add(Dense(50, input_dim=x.shape[1], activation="relu"))  # Hidden 1
    model.add(Dense(25, activation="relu"))  # Hidden 2
    model.add(Dense(y.shape[1], activation="softmax"))  # Output
    model.compile(loss="categorical_crossentropy", optimizer="adam")
    monitor = EarlyStopping(
        monitor="val_loss",
        min_delta=1e-3,
        patience=25,
        verbose=0,
        mode="auto",
        restore_best_weights=True,
    )
    # Train on the bootstrap sample
    model.fit(
        x_train,
        y_train,
        validation_data=(x_test, y_test),
        callbacks=[monitor],
        verbose=0,
        epochs=1000,
    )
    epochs = monitor.stopped_epoch
    epochs_needed.append(epochs)
    # Predict on the out of boot (validation)
    pred = model.predict(x_test)
    # Measure this bootstrap's log loss
    y_compare = np.argmax(y_test, axis=1)  # For log loss calculation
    score = metrics.log_loss(y_compare, pred)
    mean_benchmark.append(score)
    m1 = statistics.mean(mean_benchmark)
    m2 = statistics.mean(epochs_needed)
    mdev = statistics.pstdev(mean_benchmark)
    # Record this iteration
    time_took = time.time() - start_time
    print(
        f"#{num}: score={score:.6f}, mean score={m1:.6f},"
        + f"stdev={mdev:.6f}, epochs={epochs}, mean epochs={int(m2)},"
        + f" time={hms_string(time_took)}"
    )
