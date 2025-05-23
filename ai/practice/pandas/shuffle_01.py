# Create dataframe from train_test_split, shuffle column, without copy parameter in
# pd.dataframe creation, a change in x_test will result in a change in the dataframe
# (no deep copy)

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

df = pd.read_csv(
    "../../../../local_data/jheaton/class_08_2_keras_ensembles/iris.csv",
    na_values=["NA", "?"],
)
print(df)

# Convert to numpy - Classification
x = df[["sepal_l", "sepal_w", "petal_l", "petal_w"]].values
dummies = pd.get_dummies(df["species"])  # Classification
species = dummies.columns
y = dummies.values


# without deep copy

# Split into train/test
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.1, random_state=42
)

x_before = pd.DataFrame(x_test, columns=["sl", "sw", "pl", "pw"])
print(x_test)

np.random.shuffle(x_test[:, 0])

x_after = pd.DataFrame(x_test)
print(x_test)

compare = pd.concat([x_before, x_after], axis=1)
print(compare)

# with deep copy

# Split into train/test
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.1, random_state=42
)

x_before_copy = pd.DataFrame(x_test, columns=["sl", "sw", "pl", "pw"], copy=True)
print(x_test)

np.random.shuffle(x_test[:, 0])

x_after_copy = pd.DataFrame(x_test)
print(x_test)

compare_copy = pd.concat([x_before_copy, x_after_copy], axis=1)
print(compare_copy)
