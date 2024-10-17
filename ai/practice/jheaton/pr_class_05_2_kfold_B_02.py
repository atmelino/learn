import pandas as pd
from scipy.stats import zscore
import os
import numpy as np
from sklearn import metrics
from sklearn.model_selection import StratifiedKFold
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation
import pprint

# pp = pprint.PrettyPrinter(indent=4,depth=None)
np.set_printoptions(linewidth=np.inf)
np.set_printoptions(threshold=np.inf)
np.set_printoptions(precision=4, suppress=True)


pd.set_option("display.max_rows", None)
pd.set_option("display.float_format", lambda x: f"{x:.3f}")

print("class_05_2_kfold_B")

# Options for this run
shuffle = False
print_fold = True
run_model = False
length = 2000
folds = 5
length = 200
folds = 3
length = 400
folds = 3
length = 80
folds = 2


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

EPOCHS = 500

# np.argmax(pred,axis=1)
# Cross-validate
# Use for StratifiedKFold classification
kf = StratifiedKFold(folds, shuffle=True, random_state=42)
oos_id = []
oos_y = []
oos_pred = []
fold = 0
# Must specify y StratifiedKFold for
for train, test in kf.split(x, df["product"]):
    fold += 1
    print(f"Fold #{fold}")
    if print_fold == True:
        # print(f"  Train: index={train}")
        # print(f"  Test:  index={test}")
        print(f"  Train: index={train} size={train.shape}")
        print(f"  Test:  index={test} size={test.shape}")

    myarr1 = []
    myarr2 = []
    for i in test:
        # print(i,df["product"][i])
        myarr1.append(i)
        myarr2.append(df["product"][i])
    col_id = pd.DataFrame(myarr1, columns=["id"])
    col_p = pd.DataFrame(myarr2, columns=["product"])
    # print(col_p)

    x_train = np.asarray(x[train]).astype(np.float32)
    y_train = np.asarray(y[train]).astype(np.float32)
    x_test = np.asarray(x[test]).astype(np.float32)
    y_test = np.asarray(y[test]).astype(np.float32)

    model = Sequential()
    # Hidden 1
    model.add(Dense(50, input_dim=x.shape[1], activation="relu"))
    model.add(Dense(25, activation="relu"))  # Hidden 2
    model.add(Dense(y.shape[1], activation="softmax"))  # Output
    model.compile(loss="categorical_crossentropy", optimizer="adam")
    model.fit(
        x_train, y_train, validation_data=(x_test, y_test), verbose=0, epochs=EPOCHS
    )

    pred = model.predict(x_test)
    print("shape of pred", pred.shape)
    print("Prediction:")
    # print(pred)
    # pp.pprint(pred)
    dfpred = pd.DataFrame(pred)
    # pp.pprint(dfpred)
    # print(dfpred)

    col_y_test = pd.DataFrame(y_test, columns=["a", "b", "c", "d", "e", "f"])
    col_pred = pd.DataFrame(pred, columns=["a", "b", "c", "d", "e", "f"])
    fold_pred = pd.concat([col_id, col_y_test, col_p, col_pred], axis=1)
    print(fold_pred)

    oos_id.append(myarr1)

    oos_y.append(y_test)
    # raw probabilities to chosen class (highest probability)
    pred = np.argmax(pred, axis=1)

    oos_pred.append(pred)

    # Measure this fold's accuracy
    y_compare = np.argmax(y_test, axis=1)  # For accuracy calculation
    score = metrics.accuracy_score(y_compare, pred)
    print(f"Fold score (accuracy): {score}")


# Build the oos prediction list and calculate the error.
oos_id = np.concatenate(oos_id)
print("oos_id after concatenate:")
print(oos_id)
oos_y = np.concatenate(oos_y)
oos_pred = np.concatenate(oos_pred)
print("oos_pred after concatenate:")
print(oos_pred)
oos_y_compare = np.argmax(oos_y, axis=1)  # For accuracy calculation
score = metrics.accuracy_score(oos_y_compare, oos_pred)
print(f"Final score (accuracy): {score}")

# Write the cross-validated prediction
oos_id = pd.DataFrame(oos_id)
oos_y = pd.DataFrame(oos_y)
oos_pred = pd.DataFrame(oos_pred)
# df_part = df.drop(columns=['income', 'aspect','subscriptions'])
oosDF = pd.concat([oos_id, oos_y, oos_pred], axis=1)
filename_write = "./output/class_5_2_kfold_B.csv"
oosDF.to_csv(filename_write, index=False)

print("test vs predicted\n", oosDF)
