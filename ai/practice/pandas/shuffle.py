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
# Split into train/test
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.25, random_state=42
)

print(x_test)


np.random.shuffle(x_test[:, 0])


print(x_test)



