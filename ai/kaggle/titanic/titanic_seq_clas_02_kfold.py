# Based on jheaton class class_08_2_keras_ensembles_bio_rank
# and jheaton class 
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
import time
import logging
from sklearn.model_selection import StratifiedKFold

# logging.basicConfig(level=logging.INFO)
logging.basicConfig(level=logging.DEBUG)

# Options for this run
shuffle = False
print_fold = True
run_model = False
length = 2000
number_of_folds = 5
length = 200
number_of_folds = 3
length = 400
number_of_folds = 3
length = 80
number_of_folds = 2
length = 100
number_of_folds = 2


BASE_PATH = "../../../../local_data/kaggle/titanic/"
DATA_PATH = os.path.join(BASE_PATH, "input/")
OUTPUT_PATH = os.path.join(BASE_PATH, "titanic_seq_clas_jh_82/")
os.system("mkdir -p " + OUTPUT_PATH)

df_train = pd.read_csv(DATA_PATH + "train.csv", na_values=["NA", "?"])
# print("df_train=\n",df_train)
logging.debug(df_train)



#  PassengerId	Survived	Pclass	Name	Sex	Age	SibSp	Parch	Ticket	Fare	Cabin	Embarked

features = ["Pclass", "Sex", "SibSp","Fare"]
features = ["Pclass", "Sex", "SibSp","Fare", "Parch"]
features = ["Pclass"]          # Validation accuracy score: 0.6995515695067265
features = ["Sex"]                                  # 0.7847533632286996   
features = ["SibSp"]                                # 0.6591928251121076
features = ["Fare"]                                 # 0.6860986547085202    
features = ["Parch"]                                # 0.6053811659192825
features = ["Pclass", "Sex"]                        # 0.7847533632286996
features = ["Sex", "SibSp"]                         # 0.8071748878923767
features = ["Sex", "Fare"]                          # 0.7847533632286996
features = ["Sex", "Parch"]                         # 0.7847533632286996
features = ["Sex", "Fare", "Parch"]                 # 0.7847533632286996
features = ["Sex", "SibSp","Parch","Age"]           # 0.8071748878923767
features = ["Sex", "SibSp","Parch"]                 # 0.8071748878923767


x_columns =df_train[features]
logging.debug(x_columns)

if "Pclass" in features:
    x_columns = pd.concat([x_columns,pd.get_dummies(x_columns['Pclass'],prefix="Pclass")],axis=1)
    x_columns.drop('Pclass', axis=1, inplace=True)

if "Sex" in features:
    x_columns = pd.concat([x_columns,pd.get_dummies(x_columns['Sex'],prefix="Sex")],axis=1)
    x_columns.drop('Sex', axis=1, inplace=True)

if "Age" in features:
    # Missing values for income
    print("Age column before fillna\n",x_columns["Age"])
    med = x_columns["Age"].median()
    x_columns["Age"] = x_columns["Age"].fillna(med)
    print("Age column after fillna\n",x_columns["Age"])
    age_bins=pd.qcut(x_columns["Age"],10,duplicates='drop')
    print("age_bins\n",age_bins)
    df_age_bins=pd.DataFrame(age_bins,columns=["Age"])
    df_age_bins=pd.DataFrame(age_bins)
    df_age_bins = df_age_bins.rename(columns={'age_bins': 'Age'})
    print("df_age_bins\n",df_age_bins)
    x_columns = pd.concat([x_columns,pd.get_dummies(df_age_bins['Age'],prefix="Age")],axis=1)
    x_columns.drop('Age', axis=1, inplace=True)

if "SibSp" in features:
    x_columns = pd.concat([x_columns,pd.get_dummies(x_columns['SibSp'],prefix="SibSp")],axis=1)
    x_columns.drop('SibSp', axis=1, inplace=True)

if "Parch" in features:
    x_columns = pd.concat([x_columns,pd.get_dummies(x_columns['Parch'],prefix="Parch")],axis=1)
    x_columns['Parch9'] = False
    x_columns.drop('Parch', axis=1, inplace=True)

if "Fare" in features:
    fare_bins=pd.qcut(df_train["Fare"],5)
    # print("fare_bins\n",fare_bins)
    df_fare_bins=pd.DataFrame(fare_bins,columns=["Fare"])
    # df_fare_bins=pd.DataFrame(fare_bins)
    df_fare_bins = df_fare_bins.rename(columns={'fare_bins': 'Fare'})
    # print("df_fare_bins\n",df_fare_bins)
    x_columns = pd.concat([x_columns,pd.get_dummies(df_fare_bins['Fare'],prefix="Fare")],axis=1)
    x_columns.drop('Fare', axis=1, inplace=True)

# print("x_columns=\n",x_columns)
x_columns.to_csv(OUTPUT_PATH + "x_columns.csv", index=False)
# print(x_columns.columns[0])
# true_count = x_columns[x_columns.columns[0]].sum()
# true_counts = [x_columns[name].sum() for name in x_columns.columns] 
# print(true_counts)

x = x_columns.values
# print("x=\n",x)
y = df_train["Survived"].values  # Classification
# print("y=\n",y)

logging.debug(x.shape)
logging.debug(y.shape)

EPOCHS = 500

kf = StratifiedKFold(number_of_folds, shuffle=True, random_state=42)
fold = 0

oos_id = []
oos_y = []
oos_pred = []
fold = 0
# Must specify y StratifiedKFold for
for train, test in kf.split(x, df_train["Survived"]):
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
        myarr1.append(i+1)
        myarr2.append(df_train["Survived"][i])
    col_id = pd.DataFrame(myarr1, columns=["PassengerId"])
    col_p = pd.DataFrame(myarr2, columns=["Survived"])
    # print(col_p)

    x_train = np.asarray(x[train]).astype(np.float32)
    y_train = np.asarray(y[train]).astype(np.float32)
    x_test = np.asarray(x[test]).astype(np.float32)
    y_test = np.asarray(y[test]).astype(np.float32)

    model = Sequential()
    # Hidden 1
    model.add(Dense(50, input_dim=x.shape[1], activation="relu"))
    model.add(Dense(25, activation="relu"))  # Hidden 2
    model.add(Dense(1, activation="sigmoid"))
    model.compile(loss="binary_crossentropy", optimizer="adam")
    model.fit(
        x_train, y_train, validation_data=(x_test, y_test), verbose=0, epochs=EPOCHS
    )

    pred = model.predict(x_test)

    col_y_test = pd.DataFrame(y_test, columns=["y_test"])
    col_pred = pd.DataFrame(pred, columns=["pred"])
    fold_pred = pd.concat([col_id, col_y_test, col_p, col_pred], axis=1)
    print("shape of pred", pred.shape)
    print("Prediction:")
    print(fold_pred)

    oos_id.append(myarr1)
    oos_y.append(y_test)
    # raw probabilities to chosen class (highest probability)
    pred = np.argmax(pred, axis=1)
    oos_pred.append(pred)

    # Measure this fold's accuracy
    # y_compare = np.argmax(y_test, axis=1)  # For accuracy calculation
    # matches=np.count_nonzero(y_compare==pred)
    # score = metrics.accuracy_score(y_compare, pred)
    score = metrics.accuracy_score(y_test, pred)
    # print(f"matches: {matches}")
    print("Validation accuracy score: {}".format(score))


















exit()

# Split into train/test
# x_train, x_test, y_train, y_test = train_test_split(
#     x, y, test_size=0.25, random_state=42
# )
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.25
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
# model.summary()

model.fit(
    x_train,
    y_train,
    validation_data=(x_test, y_test),
    callbacks=[monitor],
    verbose=0,
    epochs=1000,
)
print("Fitting done...")

# Predict
pred = model.predict(x_test).flatten()

# col1 = pd.DataFrame(y_test, columns=["y_test"])
# col2 = pd.DataFrame(pred, columns=["pred"])
# diff = col1["y_test"] - col2["pred"]
# compare = pd.concat([col1, col2, diff], axis=1)
# compare.columns=["y_test","pred","diff"]
# print(compare)

# Clip so that min is never exactly 0, max never 1
pred = np.clip(pred, a_min=1e-6, a_max=(1 - 1e-6))
print("Validation logloss: {}".format(sklearn.metrics.log_loss(y_test, pred)))

# Evaluate success using accuracy
pred = pred > 0.5  # If greater than 0.5 probability, then true

col1 = pd.DataFrame(y_test, columns=["y_test"])
col2 = pd.DataFrame(pred, columns=["pred"])
diff = col1["y_test"] - col2["pred"]
compare = pd.concat([col1, col2, diff], axis=1)
compare.columns=["y_test","pred","diff"]
print("Predictions\n",compare)
compare.to_csv(OUTPUT_PATH + "predictions.csv", index=False)

score = metrics.accuracy_score(y_test, pred)
print("Validation accuracy score: {}".format(score))

# save entire network to HDF5 (save everything, suggested)
timestr = time.strftime("%Y%m%d-%H%M%S")
# print(timestr)
# accuracy= f"{score:.3f}"
# print(accuracy)
filename= f"acc_{score:.3f}_date_{timestr}.h5"
print(filename)
fullpath= f"{OUTPUT_PATH}/{filename}"
print("Saving model to ", filename)
model.save(fullpath)




