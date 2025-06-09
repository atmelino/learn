import os
import pandas as pd
from sklearn.model_selection import train_test_split
import tensorflow as tf
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation
from tensorflow.keras.callbacks import EarlyStopping


BASE_PATH = "../../../../local_data/jheaton"
DATA_PATH = os.path.join(BASE_PATH, "input/")
OUTPUT_PATH = os.path.join(BASE_PATH, "class_08_5_kaggle_project_iris/")
os.system("mkdir -p " + OUTPUT_PATH)


# df_train = pd.read_csv("https://data.heatonresearch.com/data/t81-558/datasets/"+"kaggle_iris_train.csv", na_values=['NA','?'])
df_train = pd.read_csv(DATA_PATH+ "kaggle_iris_train.csv", na_values=["NA", "?"])
print(df_train)

# Encode feature vector
df_train.drop("id", axis=1, inplace=True)
num_classes = len(df_train.groupby("species").species.nunique())
print("Number of classes: {}".format(num_classes))

# Convert to numpy - Classification
x = df_train[["sepal_l", "sepal_w", "petal_l", "petal_w"]].values
dummies = pd.get_dummies(df_train["species"])  # Classification
species = dummies.columns
y = dummies.values

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

from sklearn import metrics

# Calculate multi log loss error
pred = model.predict(x_test)
score = metrics.log_loss(y_test, pred)
print("Log loss score: {}".format(score))

# Generate Kaggle submit file
# Encode feature vector
# df_test = pd.read_csv("https://data.heatonresearch.com/data/t81-558/datasets/"+"kaggle_iris_test.csv", na_values=['NA','?'])
df_test = pd.read_csv(DATA_PATH+"kaggle_iris_test.csv", na_values=['NA','?'])

# Convert to numpy - Classification
ids = df_test['id']
df_test.drop('id', axis=1, inplace=True)
x = df_test[['sepal_l', 'sepal_w', 'petal_l', 'petal_w']].values
y = dummies.values

# Generate predictions
pred = model.predict(x)
#pred

# Create submission data set
df_submit = pd.DataFrame(pred)
df_submit.insert(0,'id',ids)
df_submit.columns = ['id','species-0','species-1','species-2']

# Write submit file locally
df_submit.to_csv(OUTPUT_PATH+"iris_submit.csv", index=False)
print(df_submit[:5])


