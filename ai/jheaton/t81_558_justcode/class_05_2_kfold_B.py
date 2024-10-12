import pandas as pd
from scipy.stats import zscore
import os
import numpy as np
from sklearn import metrics
from sklearn.model_selection import StratifiedKFold
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation
from sklearn.model_selection import KFold
from tensorflow.keras.models import Sequential

pd.set_option("display.max_rows", None)

print("class_05_2_kfold_B")

# Options for this run
shuffle = False
print_fold = True
run_model = False
length = 2000
folds = 5
length = 400
folds = 3

# Read the data set
# df_original = pd.read_csv(
#     "./input/jh-simple-dataset.csv",
#     na_values=["NA", "?"],
# )
df_original = pd.read_csv(
    "./input/jh-simple-dataset_sorted.csv",
    na_values=["NA", "?"],
)
# print(df_original.head())
# print("original data set\n", df_original)
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
df.to_csv("./output/class_05_2_B_jh-simple-dataset_06.csv", sep=",")

# print("Table after feature vector encoding\n", df.head())
print("dataset size after feature vector encoding:\n", df.shape)

# Convert to numpy - Classification
x_columns = df.columns.drop("product").drop("id")
x = df[x_columns].values
# print(x)
dummies = pd.get_dummies(df["product"])  # Classification
products = dummies.columns
y = dummies.values

print("shape of y=", y.shape)
col1 = pd.DataFrame(df, columns=["id"])
col2 = pd.DataFrame(df, columns=["product"])
col3 = pd.DataFrame(y)
product_encoded = pd.concat([col1, col2, col3], axis=1)
print(product_encoded)

product_counts = product_encoded['product'].value_counts().reset_index()
product_counts.columns = ['product', 'counts']
product_counts['perc'] = product_counts['counts']/len(product_encoded)*100
print(product_counts)


EPOCHS = 500


# np.argmax(pred,axis=1)
# Cross-validate
# Use for StratifiedKFold classification
kf = StratifiedKFold(folds, shuffle=True, random_state=42)
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
    # print("y_test=", y_test)

    col_y_test = pd.DataFrame(y_test)

    fold_test = pd.concat([col_id, col_p, col_y_test], axis=1)
    print(fold_test)

    # count_a = fold_test["product"].value_counts()["a"]
    # count_b = fold_test["product"].value_counts()["b"]
    # count_c = fold_test["product"].value_counts()["c"]
    # count_d = fold_test["product"].value_counts()["d"]
    # count_e = fold_test["product"].value_counts()["e"]
    # count_f = fold_test["product"].value_counts()["f"]
    # print(
    #     "counts of a b c d e f:", count_a, count_b, count_c, count_d, count_e, count_f
    # )

    # product_counts = fold_test['product'].value_counts()
    product_counts = fold_test['product'].value_counts().reset_index()
    product_counts.columns = ['product', 'counts']
    product_counts['perc'] = product_counts['counts']/len(fold_test)*100
    print(product_counts)

    if run_model == True:
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
        oos_y.append(y_test)
        # raw probabilities to chosen class (highest probability)
        pred = np.argmax(pred, axis=1)
        oos_pred.append(pred)
        # Measure this fold's accuracy
        y_compare = np.argmax(y_test, axis=1)  # For accuracy calculation
        score = metrics.accuracy_score(y_compare, pred)
        print(f"Fold score (accuracy): {score}")

exit()
