print("conda environment for this program:")
print("conda activate jh_class")

# Additional packages
# conda install -c conda-forge xgboost
# conda install -c conda-forge lightgbm
# conda install -c conda-forge catboost


# import
import numpy as np
import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt
import re
import os
import logging

from sklearn.metrics import accuracy_score, roc_auc_score, precision_score, recall_score, f1_score
from sklearn.model_selection import train_test_split
from sklearn.model_selection import StratifiedKFold
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import OrdinalEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import VotingClassifier
from sklearn.ensemble import RandomForestRegressor 
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import GradientBoostingClassifier
from xgboost import XGBClassifier
from lightgbm import LGBMClassifier
from catboost import CatBoostClassifier

# logging.basicConfig(level=logging.INFO)
logging.basicConfig(level=logging.DEBUG)

BASE_PATH = "../../../../local_data/kaggle/titanic/"
DATA_PATH = os.path.join(BASE_PATH, "input/")
OUTPUT_PATH = os.path.join(BASE_PATH, "polar_snow09/")
os.system("mkdir -p " + OUTPUT_PATH)

# load train and test data
train = pd.read_csv(DATA_PATH + "train.csv")
test = pd.read_csv(DATA_PATH + "test.csv")

logging.debug("missing in train",train.isnull().sum())
logging.debug("missing in test")
logging.debug(test.isnull().sum())

# name : name => name title 
def extract_title(name):
    title_search = re.search(' ([A-Za-z]+)\.', name)
    if title_search:
        return title_search.group(1)
    return ""

train['Title'] = train['Name'].apply(extract_title)
test['Title'] = test['Name'].apply(extract_title)

# Name drop 
train.drop('Name', axis=1, inplace=True)
test.drop('Name', axis=1, inplace=True)

# Pclass + Sex
train['Pclass_Sex'] = train['Pclass'].astype(str) + '_' + train['Sex'].astype(str)
test['Pclass_Sex'] = test['Pclass'].astype(str) + '_' + test['Sex'].astype(str)

# Sex categorize to number
sex_name = ['male', 'female']

for i in range(len(sex_name)):
    train.loc[train['Sex']==sex_name[i], 'Sex'] = i
    test.loc[test['Sex']==sex_name[i], 'Sex'] = i

logging.debug(train['Sex'].value_counts())

# Age null value : Age prediction
def preprocess_age(df):
    age_df = df[['Age', 'Pclass', 'Sex', 'SibSp', 'Parch', 'Fare']]
    age_df_not_null = age_df.dropna()
    age_df_null = age_df[age_df['Age'].isnull()]
    return age_df_not_null, age_df_null

train_age_not_null, train_age_null = preprocess_age(train.copy())
test_age_not_null, test_age_null = preprocess_age(test.copy())

X_train_age = train_age_not_null.drop('Age', axis=1)
y_train_age = train_age_not_null['Age']

rf_age = RandomForestRegressor(n_estimators=100, random_state=42)
rf_age.fit(X_train_age, y_train_age)

predicted_ages_train = rf_age.predict(train_age_null.drop('Age', axis=1))
train.loc[train['Age'].isnull(), 'Age'] = predicted_ages_train

predicted_ages_test = rf_age.predict(test_age_null.drop('Age', axis=1))
test.loc[test['Age'].isnull(), 'Age'] = predicted_ages_test

# Age categorize 
def age_categorize(age):
    age = age // 10 * 10
    return age

Age_s = train.Age.apply(age_categorize)
train.insert(4, 'Age_s', Age_s)

Age_s = test.Age.apply(age_categorize)
test.insert(3, 'Age_s', Age_s)

logging.debug(test.head(3))

def create_family_role(df):
    df['FamilySize'] = df['SibSp'] + df['Parch'] + 1
    df['IsAlone'] = (df['FamilySize'] == 1).astype(int)

    def get_role(passenger):
        if passenger['IsAlone']:
            return 'Alone'
        elif passenger['Parch'] > 0:
            return 'Parent'
        else:
            return 'Sibling/Spouse'
        return 'Other'

    df['FamilyRole'] = df.apply(get_role, axis=1)
    df.drop(['FamilySize', 'IsAlone'], axis=1, inplace=True)
    return df

train = create_family_role(train.copy())
test = create_family_role(test.copy())

# Fare categorize
train['Fare'].value_counts()

train['Fare_category'] = pd.qcut(train['Fare'], q=4, labels=['Low', 'Mid', 'High', 'Highest'])
test['Fare_category'] = pd.qcut(test['Fare'], q=4, labels=['Low', 'Mid', 'High', 'Highest'])

# test data : Fill 'null values' with most frequent value
test['Fare'].fillna(test['Fare'].mode()[0], inplace=True)
test['Fare_category'].fillna(test['Fare_category'].mode()[0], inplace=True)

# Fare Log
train['Fare_Log'] = np.log1p(train['Fare'])
test['Fare_Log'] = np.log1p(test['Fare'])

# Use the first letter 'Cabin' : 'Cabin_deck' 
# 'Cabin' null value setting: 'Unknown'
train['Cabin_Deck'] = train['Cabin'].str[0].fillna('Unknown')
test['Cabin_Deck'] = test['Cabin'].str[0].fillna('Unknown')

#'Embarked' : Fill 'null values' with most frequent value
train['Embarked'].fillna(train['Embarked'].mode()[0], inplace=True)
test['Embarked'].fillna(test['Embarked'].mode()[0], inplace=True)

# Ticket => TicketGroupSize 
train_ticket_counts = train['Ticket'].value_counts()
test_ticket_counts = test['Ticket'].value_counts()

train['TicketGroupSize'] = train['Ticket'].map(train_ticket_counts)
test['TicketGroupSize'] = test['Ticket'].map(test_ticket_counts).fillna(1)

# Ticket => TicketPrefix('PC', 'STON/O', 'SOTON'...)
def extract_ticket_prefix(ticket):
    import re
    match = re.search(r'([A-Za-z./]+)', ticket)
    if match:
        return match.group(1)
    return None

train['TicketPrefix'] = train['Ticket'].apply(extract_ticket_prefix)
test['TicketPrefix'] = test['Ticket'].apply(extract_ticket_prefix)

train['TicketPrefix'] = train['TicketPrefix'].fillna('UNK')
test['TicketPrefix'] = test['TicketPrefix'].fillna('UNK')

train['Embarked'] = train['Embarked'].astype(str)
train['Cabin_Deck'] = train['Cabin_Deck'].astype(str)
train['Title'] = train['Title'].astype(str)
train['FamilyRole'] = train['FamilyRole'].astype(str)
train['Pclass_Sex'] = train['Pclass_Sex'].astype(str)

# 'Embarked', 'Cabin_Deck': One-Hot Encoding
categorical_cols = ['Embarked', 'Cabin_Deck', 'Title', 'FamilyRole', 'Pclass_Sex', 'Sex', 'TicketPrefix']

encoder = OneHotEncoder(handle_unknown='ignore', sparse_output=False)

# train data
encoder.fit(train[categorical_cols])

encoded_train = encoder.transform(train[categorical_cols])
encoded_train_columns = encoder.get_feature_names_out(categorical_cols)
encoded_train_df = pd.DataFrame(encoded_train, columns=encoded_train_columns)
train = pd.concat([train.drop(categorical_cols, axis=1).reset_index(drop=True), encoded_train_df], axis=1)

logging.debug(train.columns)

# test data
encoded_test_data = encoder.transform(test[categorical_cols])
encoded_test_columns = encoder.get_feature_names_out(categorical_cols)
encoded_test_df = pd.DataFrame(encoded_test_data, columns=encoded_test_columns)
test = pd.concat([test.drop(categorical_cols, axis=1).reset_index(drop=True), encoded_test_df], axis=1)

logging.debug(test.columns)

# 'Fare_category': Ordinal Encoding
ordinal_col = 'Fare_category'
categories = [['Low', 'Mid', 'High', 'Highest']]

encoder = OrdinalEncoder(categories=categories, handle_unknown='error')

encoder.fit(train[[ordinal_col]])

# train data
train[ordinal_col + '_Encoded'] = encoder.transform(train[[ordinal_col]])

# test data
test[ordinal_col + '_Encoded'] = encoder.transform(test[[ordinal_col]])

train = train.drop(columns = ['Fare_category', 'Cabin'], axis=1)
test = test.drop(columns = ['Fare_category', 'Cabin'], axis=1)

train['Age_Pclass'] = train['Age_s'] * train['Pclass']
test['Age_Pclass'] = test['Age_s'] * test['Pclass']

train['Fare_Pclass'] = train['Fare'] * train['Pclass']
test['Fare_Pclass'] = test['Fare'] * test['Pclass']

train['FamilySize'] = train['SibSp'] + train['Parch'] + 1
test['FamilySize'] = test['SibSp'] + test['Parch'] + 1
train['FamilySize_Pclass'] = train['FamilySize'] * train['Pclass']
test['FamilySize_Pclass'] = test['FamilySize'] * test['Pclass']

train['Age_Male'] = train['Age_s'] * train['Sex_0']
test['Age_Male'] = test['Age_s'] * test['Sex_0']
train['Age_Female'] = train['Age_s'] * train['Sex_1']
test['Age_Female'] = test['Age_s'] * test['Sex_1']

train_grouped_fare = train.groupby('Ticket')['Fare'].mean().to_dict()
test_grouped_fare = test.groupby('Ticket')['Fare'].mean().to_dict()
train['Group_Fare_Mean'] = train['Ticket'].map(train_grouped_fare)
test['Group_Fare_Mean'] = test['Ticket'].map(test_grouped_fare)

# Ticket drop 
train = train.drop('Ticket', axis=1)
test = test.drop('Ticket', axis=1)

X_train = train.drop('Survived', axis=1)
y_train = train['Survived']

X_test = test 

# normalization train, test data
numerical_cols = ['Age', 'Fare', 'SibSp', 'Parch', 'TicketGroupSize']

scaler = StandardScaler()
X_train[numerical_cols] = scaler.fit_transform(X_train[numerical_cols])
X_test[numerical_cols] = scaler.transform(X_test[numerical_cols])

param_grid_lr = {'C': [0.001, 0.01, 0.1]}
grid_search_lr = GridSearchCV(LogisticRegression(random_state=42), param_grid_lr, cv=3, scoring='accuracy')
grid_search_lr.fit(X_train, y_train)
best_lr = grid_search_lr.best_estimator_
print("Best Logistic Regression:", grid_search_lr.best_params_)

param_grid_rf = {'n_estimators': [50, 100], 'max_depth': [3, 5]}
grid_search_rf = GridSearchCV(RandomForestClassifier(random_state=42), param_grid_rf, cv=3, scoring='accuracy')
grid_search_rf.fit(X_train, y_train)
best_rf = grid_search_rf.best_estimator_
print("Best Random Forest:", grid_search_rf.best_params_)

param_grid_gb = {'n_estimators': [50, 100], 'learning_rate': [0.01, 0.1], 'max_depth': [2, 3]}
grid_search_gb = GridSearchCV(GradientBoostingClassifier(random_state=42), param_grid_gb, cv=3, scoring='accuracy')
grid_search_gb.fit(X_train, y_train)
best_gb = grid_search_gb.best_estimator_
print("Best Gradient Boosting:", grid_search_gb.best_params_)

param_grid_xgb = {'n_estimators': [50, 100], 'learning_rate': [0.01, 0.1], 'max_depth': [2, 3]}
grid_search_xgb = GridSearchCV(XGBClassifier(random_state=42, use_label_encoder=False, eval_metric='logloss'), param_grid_xgb, cv=3, scoring='accuracy')
grid_search_xgb.fit(X_train, y_train)
best_xgb = grid_search_xgb.best_estimator_
print("Best XGBoost:", grid_search_xgb.best_params_)

param_grid_catboost = {'iterations': [50, 100], 'learning_rate': [0.01, 0.1], 'depth': [2, 3]}
grid_search_catboost = GridSearchCV(CatBoostClassifier(random_state=42, verbose=0), param_grid_catboost, cv=3, scoring='accuracy')
grid_search_catboost.fit(X_train, y_train)
best_catboost = grid_search_catboost.best_estimator_
print("Best CatBoost:", grid_search_catboost.best_params_)

# base models
base_models = [
    ('lr', best_lr),
    ('rf', best_rf),
    ('gb', best_gb),
    ('xgb', best_xgb),
    ('catboost', best_catboost)
]

# Out-of-Fold (OOF) 
def get_oof_predictions(model, X_train, y_train, X_test, n_splits=5):
    oof_train = np.zeros((X_train.shape[0],))
    oof_test = np.zeros((X_test.shape[0],))
    oof_test_skf = np.empty((n_splits, X_test.shape[0]))
    skf = StratifiedKFold(n_splits=n_splits, shuffle=True, random_state=42)

    for fold, (train_index, val_index) in enumerate(skf.split(X_train, y_train)):
        X_train_fold, X_val_fold = X_train.iloc[train_index], X_train.iloc[val_index]
        y_train_fold, y_val_fold = y_train.iloc[train_index], y_train.iloc[val_index]

        model.fit(X_train_fold, y_train_fold)
        oof_train[val_index] = model.predict_proba(X_val_fold)[:, 1]
        oof_test_skf[fold, :] = model.predict_proba(X_test)[:, 1]

    oof_test[:] = oof_test_skf.mean(axis=0)
    return oof_train, oof_test

oof_train_predictions = {}
oof_test_predictions = {}

for name, model in base_models:
    oof_train, oof_test = get_oof_predictions(model, X_train, y_train, X_test)
    oof_train_predictions[name] = oof_train 
    oof_test_predictions[name] = oof_test  

oof_train = np.column_stack(list(oof_train_predictions.values()))
oof_test = np.column_stack(list(oof_test_predictions.values()))
y_train_meta = y_train

param_grid_gb = {
    'n_estimators': [50, 100],
    'learning_rate': [0.01, 0.1],
    'max_depth': [3, 5]
}

meta_model_gb = GradientBoostingClassifier(random_state=42)
grid_search_gb = GridSearchCV(meta_model_gb, param_grid_gb, cv=5, scoring='accuracy', n_jobs=-1)
grid_search_gb.fit(oof_train, y_train_meta)

best_params_gb = grid_search_gb.best_params_
best_score_gb = grid_search_gb.best_score_
print(f"최적 GradientBoostingClassifier 하이퍼파라미터: {best_params_gb}")
print(f"최고 검증 정확도: {best_score_gb:.4f}")

best_meta_model_gb = grid_search_gb.best_estimator_

predictions = best_meta_model_gb.predict(oof_test)

submission = pd.DataFrame({'PassengerId': test['PassengerId'], 'Survived': predictions})
submission.to_csv(OUTPUT_PATH +'submission.csv', index=False)




















































