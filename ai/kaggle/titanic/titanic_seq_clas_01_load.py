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
from tensorflow.keras.models import load_model

BASE_PATH = "../../../../local_data/kaggle/titanic/"
DATA_PATH = os.path.join(BASE_PATH, "input/")
OUTPUT_PATH = os.path.join(BASE_PATH, "titanic_seq_clas_01/")
os.system("mkdir -p " + OUTPUT_PATH)


# Generate Kaggle submit file
print("Generate Kaggle submit file")
df_test = pd.read_csv(DATA_PATH + "test.csv", na_values=["NA", "?"])
print(df_test)


#  PassengerId	Survived	Pclass	Name	Sex	Age	SibSp	Parch	Ticket	Fare	Cabin	Embarked

# features = ["Pclass", "Sex", "SibSp", "Parch"]
# features = ["Pclass", "Sex", "SibSp"]
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
features = ["Sex", "SibSp","Parch"]                 # 0.8071748878923767
features = ["Sex", "SibSp", "Parch", "Fare"] 
# features = ["Sex", "SibSp", "Parch", "Fare", "Age"] 


x_columns =df_test[features]
print("x_columns=\n",x_columns)

if "Pclass" in features:
    x_columns = pd.concat([x_columns,pd.get_dummies(x_columns['Pclass'],prefix="Pclass")],axis=1)
    x_columns.drop('Pclass', axis=1, inplace=True)

if "Sex" in features:
    x_columns = pd.concat([x_columns,pd.get_dummies(x_columns['Sex'],prefix="Sex")],axis=1)
    x_columns.drop('Sex', axis=1, inplace=True)

if "Age" in features:
    # Missing values for income
    print("Age column before fillna\n", x_columns["Age"])
    med = x_columns["Age"].median()
    x_columns["Age"] = x_columns["Age"].fillna(med)
    print("Age column after fillna\n", x_columns["Age"])
    age_bins = pd.qcut(x_columns["Age"], 10, duplicates="drop")
    print("age_bins\n", age_bins)
    df_age_bins = pd.DataFrame(age_bins, columns=["Age"])
    df_age_bins = pd.DataFrame(age_bins)
    df_age_bins = df_age_bins.rename(columns={"age_bins": "Age"})
    print("df_age_bins\n", df_age_bins)
    x_columns = pd.concat(
        [x_columns, pd.get_dummies(df_age_bins["Age"], prefix="Age")], axis=1
    )
    x_columns.drop("Age", axis=1, inplace=True)

if "SibSp" in features:
    x_columns = pd.concat([x_columns,pd.get_dummies(x_columns['SibSp'],prefix="SibSp")],axis=1)
    x_columns.drop('SibSp', axis=1, inplace=True)

if "Parch" in features:
    x_columns = pd.concat([x_columns,pd.get_dummies(x_columns['Parch'],prefix="Parch")],axis=1)
    x_columns.drop('Parch', axis=1, inplace=True)

if "Fare" in features:
    fare_bins=pd.qcut(x_columns["Fare"],5)
    # print("fare_bins\n",fare_bins)
    df_fare_bins=pd.DataFrame(fare_bins,columns=["Fare"])
    # df_fare_bins=pd.DataFrame(fare_bins)
    df_fare_bins = df_fare_bins.rename(columns={'fare_bins': 'Fare'})
    # print("df_fare_bins\n",df_fare_bins)
    x_columns = pd.concat([x_columns,pd.get_dummies(df_fare_bins['Fare'],prefix="Fare")],axis=1)
    x_columns.drop('Fare', axis=1, inplace=True)

print("x_columns=\n",x_columns)
# x_columns.to_csv(OUTPUT_PATH + "x_columns.csv", index=False)

X_test = x_columns.values
print("X_test=\n",X_test)

# load network in HDF5 format
filename= "acc_0.807_date_20250617-142852_sex_sib_parch.h5"
filename= "acc_0.798_date_20250617-203145.h5"
filename= "acc_0.830_date_20250617-210343.h5"
filename= "acc_0.857_date_20250617-211202.h5"
# filename= "acc_0.851_fold_6_date_20250620-194601.h5"
# filename= "acc_0.831_fold_6_date_20250620-205309.h5"
# filename= "acc_0.858_fold_6_date_20250620-210421.h5"
# filename= "acc_0.846_fold_1_date_20250620-211453.h5"
filename= "acc_0.858_loss_0.410_fold_6_date_20250620-212525.h5"


print(filename)
fullpath= f"{OUTPUT_PATH}{filename}"
print("Loading model from ", fullpath)
model = load_model(fullpath)

predictions = model.predict(X_test)
# print("submit predictions=\n",predictions)

predictions = model.predict(X_test)
# print(predictions)
predictions2 = np.round(predictions)
# print(predictions2)
predictions3=np.int_(predictions2)
# print(predictions3)


# Create submission data set
df_submit = pd.DataFrame(predictions3)
df_submit.insert(0, "PassengerId", df_test.PassengerId)
df_submit.columns = ["PassengerId", "Survived"]

df_submit.to_csv(OUTPUT_PATH + "submission.csv", index=False)
print(df_submit[:5])
print("Your submission was successfully saved!")


