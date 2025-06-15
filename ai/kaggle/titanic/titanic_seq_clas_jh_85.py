# Based on class 8.5 iris

# conda environment for this program:
# conda activate jh_class

import os
import pandas as pd
from sklearn.model_selection import train_test_split
import tensorflow as tf
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation
from tensorflow.keras.callbacks import EarlyStopping
from sklearn import metrics
from sklearn.metrics import accuracy_score


BASE_PATH = "../../../../local_data/kaggle/titanic/"
DATA_PATH = os.path.join(BASE_PATH, "input/")
OUTPUT_PATH = os.path.join(BASE_PATH, "titanic_seq_clas_01 copy/")
os.system("mkdir -p " + OUTPUT_PATH)


# df_train = pd.read_csv("https://data.heatonresearch.com/data/t81-558/datasets/"+"kaggle_iris_train.csv", na_values=['NA','?'])
df_train = pd.read_csv(DATA_PATH+ "train.csv", na_values=["NA", "?"])
print(df_train)

# Encode feature vector
num_classes = len(df_train.groupby("Survived").Survived.nunique())
print("Number of classes: {}".format(num_classes))

# Convert to numpy - Classification
# features = ["Sex", "Pclass", "Fare"]
features = ["Pclass", "Fare"]
x = df_train[features].values
print(x)
# dummies = pd.get_dummies(df_train["Survived"])  # Classification
# y = dummies.values
y = df_train["Survived"]
print(y)

# Split into train/test
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.25, random_state=45
)

# Train, with early stopping
model = Sequential()
model.add(Dense(50, input_dim=x.shape[1], activation="relu"))
model.add(Dense(25))
model.add(Dense(y.shape[1], activation="softmax"))
model.compile(loss="categorical_crossentropy", optimizer="adam")
monitor = EarlyStopping(
    monitor="val_loss",
    min_delta=1e-3,
    patience=5,
    verbose=2,
    mode="auto",
    restore_best_weights=True,
)
model.fit(
    x_train,
    y_train,
    validation_data=(x_test, y_test),
    callbacks=[monitor],
    verbose=1,
    epochs=1000,
)


# Calculate multi log loss error
pred = model.predict(x_test)
score = metrics.log_loss(y_test, pred)
print("Log loss score: {}".format(score))

# Calculate accuracy
# col1 = pd.DataFrame(y_test, columns=["y_test"])
# col2 = pd.DataFrame(pred, columns=["pred"])
# col3 = pd.DataFrame(pred2, columns=["pred2"])
# diff = col1["y_test"] - col3["pred2"]
# print(col1)
# print(col2)
# print(diff)
# compare = pd.concat([col1, col2, col3, diff], axis=1)
# compare.columns = ["y_test", "pred", "pred2", "diff"]
# compare.to_csv(OUTPUT_PATH + "compare.csv", index=False)
# print(compare)
pred=pred.flatten()
print("pred\n",pred)
print("y_test\n",y_test)
correct = accuracy_score(pred, y_test)
print(f"Accuracy: {correct}")



# Generate Kaggle submit file
# Encode feature vector
# df_test = pd.read_csv("https://data.heatonresearch.com/data/t81-558/datasets/"+"kaggle_iris_test.csv", na_values=['NA','?'])
df_test = pd.read_csv(DATA_PATH+"kaggle_iris_test.csv", na_values=['NA','?'])

# Convert to numpy - Classification
ids = df_test['id']
df_test.drop('id', axis=1, inplace=True)
x = df_test[['sepal_l', 'sepal_w', 'petal_l', 'petal_w']].values

# Generate predictions
pred = model.predict(x)

# Create submission data set
df_submit = pd.DataFrame(pred)
df_submit.insert(0,'id',ids)
df_submit.columns = ['id','species-0','species-1','species-2']

# Write submit file locally
df_submit.to_csv(OUTPUT_PATH+"iris_submit.csv", index=False)
print(df_submit[:5])


