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

# Rank the features
def perturbation_rank(model, x, y, names, regression):
    errors = []

    for i in range(x.shape[1]):
        hold = np.array(x[:, i])
        np.random.shuffle(x[:, i])

        if regression:
            pred = model.predict(x)
            error = metrics.mean_squared_error(y, pred)
        else:
            pred = model.predict(x)
            error = metrics.log_loss(y, pred)

        errors.append(error)
        x[:, i] = hold

    max_error = np.max(errors)
    importance = [e / max_error for e in errors]

    data = {"name": names, "error": errors, "importance": importance}
    result = pd.DataFrame(data, columns=["name", "error", "importance"])
    result.sort_values(by=["importance"], ascending=[0], inplace=True)
    result.reset_index(inplace=True, drop=True)
    return result


BASE_PATH = "../../../../local_data/jheaton"
OUTPUT_PATH = os.path.join(BASE_PATH, "class_08_2_keras_ensembles_bio")
os.system("mkdir -p " + OUTPUT_PATH)

# URL = "https://data.heatonresearch.com/data/t81-558/kaggle/"
URL = "../../../../local_data/jheaton/input/"

df_train = pd.read_csv(URL + "bio_train.csv", na_values=["NA", "?"])
df_test = pd.read_csv(URL + "bio_test.csv", na_values=["NA", "?"])
print("df_train.shape: ", df_train.shape)
print("df_test.shape: ", df_test.shape)

# activity_classes = df_train["Activity"]


# Encode feature vector
# Convert to numpy - Classification
x_columns = df_train.columns.drop("Activity")
x = df_train[x_columns].values
y = df_train["Activity"].values  # Classification
x_submit = df_test[x_columns].values.astype(np.float32)

print("x.shape: ", x.shape)
print("y.shape: ", y.shape)
print("x_submit.shape: ", x_submit.shape)

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
submit_df.to_csv(OUTPUT_PATH+"/submit.csv", index=False)

# Rank the features
from IPython.display import display, HTML
names = list(df_train.columns) # x+y column names
names.remove("Activity") # remove the target(y)
rank = perturbation_rank(model, x_test, y_test, names, False)
display(rank[0:10])
rank.to_csv(OUTPUT_PATH+"/rank.csv", index=False)
