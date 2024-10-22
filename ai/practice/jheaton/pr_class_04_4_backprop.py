# %matplotlib inline

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation
from tensorflow.keras.callbacks import EarlyStopping
from scipy.stats import zscore
from sklearn.model_selection import train_test_split
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import metrics
import os

print("pr_class_04_4_backprop")
print("A loop to show the effect of the number of input data on the achieved precision of the prediction")
print("original data set has 2000 rows")

directory_path = "./output"
if not os.path.exists(directory_path):
    os.makedirs(directory_path)

# Read the data set
df_original = pd.read_csv(
    "./input/jh-simple-dataset.csv",
    na_values=["NA", "?"],
)

start = 100
stop = 2000+1
step = 100

# start = 20
# stop = 60+1
# step = 20

for length in range(start, stop, step):
    print("Using", length, "rows")

    df = df_original.iloc[0:length]

    print(df)

    if True:

        # Generate dummies for job
        df = pd.concat([df, pd.get_dummies(df["job"], prefix="job")], axis=1)
        df.drop("job", axis=1, inplace=True)
        df.to_csv("./output/jh-simple-dataset_02.csv", sep=",")

        # Generate dummies for area
        df = pd.concat([df, pd.get_dummies(df["area"], prefix="area")], axis=1)
        df.drop("area", axis=1, inplace=True)
        df.to_csv("./output/jh-simple-dataset_03.csv", sep=",")

        # Generate dummies for product
        df = pd.concat([df, pd.get_dummies(df["product"], prefix="product")], axis=1)
        df.drop("product", axis=1, inplace=True)
        df.to_csv("./output/jh-simple-dataset_04.csv", sep=",")

        # Missing values for income
        med = df["income"].median()
        df["income"] = df["income"].fillna(med)
        df.to_csv("./output/jh-simple-dataset_05.csv", sep=",")

        # Standardize ranges
        df["income"] = zscore(df["income"])
        df["aspect"] = zscore(df["aspect"])
        df["save_rate"] = zscore(df["save_rate"])
        df["subscriptions"] = zscore(df["subscriptions"])
        df.to_csv("./output/jh-simple-dataset_06.csv", sep=",")

        # Convert to numpy - Classification
        x_columns = df.columns.drop("age").drop("id")
        x = df[x_columns].values
        y = df["age"].values

        x = x.astype("float32")
        y = y.astype("float32")

        # Create train/test
        x_train, x_test, y_train, y_test = train_test_split(
            x, y, test_size=0.25, random_state=42
        )

        EPOCHS = 500

        # Build the neural network
        model = Sequential()
        model.add(Dense(25, input_dim=x.shape[1], activation="relu"))  # Hidden 1
        model.add(Dense(10, activation="relu"))  # Hidden 2
        model.add(Dense(1))  # Output
        model.compile(loss="mean_squared_error", optimizer="adam")  # Modify here
        model.fit(
            x_train, y_train, validation_data=(x_test, y_test), verbose=0, epochs=EPOCHS
        )

        pred = model.predict(x_test)
        # print(y_test.shape)
        # print(pred.shape)
        # Measure this set's RMSE
        score = np.sqrt(metrics.mean_squared_error(pred, y_test))
        # print(f"Set score (RMSE): {score}")
        print("Rows used=", length, ",   Set score (RMSE)=", score)

exit()


col1 = pd.DataFrame(y_test, columns=["y_test"])
col2 = pd.DataFrame(pred, columns=["pred"])
diff = col1["y_test"] - col2["pred"]
compare = pd.concat([col1, col2, diff], axis=1)
compare.columns = ["y_test", "pred", "diff"]
print(compare)
