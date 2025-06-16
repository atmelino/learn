# Based on jheaton class class_08_2_keras_ensembles_bio_rank

print("conda environment for this program:")
print("conda activate jh_class")

import os
import pandas as pd
import numpy as np
import sklearn
from sklearn import metrics
from sklearn.model_selection import KFold
from sklearn.model_selection import train_test_split
from scipy.stats import zscore
from IPython.display import HTML, display
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation
from tensorflow.keras.callbacks import EarlyStopping

BASE_PATH = "../../../../local_data/kaggle/titanic/"
DATA_PATH = os.path.join(BASE_PATH, "input/")
OUTPUT_PATH = os.path.join(BASE_PATH, "titanic_seq_regr_01/")
os.system("mkdir -p " + OUTPUT_PATH)

df_train = pd.read_csv(DATA_PATH + "train.csv", na_values=["NA", "?"])
print("df_train.shape: ", df_train.shape)
print("df_train=\n",df_train)

# features = ["Pclass", "Sex", "SibSp", "Parch"]
features = ["Pclass", "Sex", "SibSp"]
x_columns =df_train[features]
print("x_columns=\n",x_columns)

# for feature in features:
#     print(feature)
#     df_train = pd.concat([df_train,pd.get_dummies(df_train[feature],prefix=feature)],axis=1)
#     df_train.drop(feature, axis=1, inplace=True)
#     print("df_train=\n",df_train)

x_columns = pd.concat([x_columns,pd.get_dummies(x_columns['Pclass'],prefix="Pclass")],axis=1)
x_columns.drop('Pclass', axis=1, inplace=True)
x_columns = pd.concat([x_columns,pd.get_dummies(x_columns['Sex'],prefix="Sex")],axis=1)
x_columns.drop('Sex', axis=1, inplace=True)
x_columns = pd.concat([x_columns,pd.get_dummies(x_columns['SibSp'],prefix="SibSp")],axis=1)
x_columns.drop('SibSp', axis=1, inplace=True)
print("x_columns=\n",x_columns)

x = x_columns.values
print("x=\n",x)
y = df_train["Survived"].values  # Classification
print("y=\n",y)
# x_submit = df_test[x_columns].values.astype(np.float32)

print("x.shape: ", x.shape)
print("y.shape: ", y.shape)
# print("x_submit.shape: ", x_submit.shape)

# Split into train/test
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.25, random_state=42
)
print("Fitting/Training...")
model = Sequential()
model.add(Dense(25, input_dim=x.shape[1], activation="relu"))
model.add(Dense(10))
model.add(Dense(1, activation="sigmoid"))
model.compile(loss="binary_crossentropy", optimizer="adam")
monitor = EarlyStopping(
    monitor="val_loss", min_delta=1e-3, patience=5, verbose=1, mode="auto"
)
model.fit(
    x_train,
    y_train,
    validation_data=(x_test, y_test),
    callbacks=[monitor],
    verbose=1,
    epochs=1000,
)
print("Fitting done...")

# Predict
pred = model.predict(x_test).flatten()

# Clip so that min is never exactly 0, max never 1
pred = np.clip(pred, a_min=1e-6, a_max=(1 - 1e-6))
print("Validation logloss: {}".format(sklearn.metrics.log_loss(y_test, pred)))

# Evaluate success using accuracy
pred = pred > 0.5  # If greater than 0.5 probability, then true
score = metrics.accuracy_score(y_test, pred)
print("Validation accuracy score: {}".format(score))

# Build real submit file
pred_submit = model.predict(x_submit)

# Clip so that min is never exactly 0, max never 1 (would be a NaN score)
pred = np.clip(pred, a_min=1e-6, a_max=(1 - 1e-6))
submit_df = pd.DataFrame(
    {
        "MoleculeId": [x + 1 for x in range(len(pred_submit))],
        "PredictedProbability": pred_submit.flatten(),
    }
)
submit_df.to_csv(OUTPUT_PATH+"submit.csv", index=False)

