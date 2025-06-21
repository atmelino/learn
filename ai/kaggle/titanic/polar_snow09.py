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

BASE_PATH = "../../../../local_data/kaggle/titanic/"
DATA_PATH = os.path.join(BASE_PATH, "input/")
OUTPUT_PATH = os.path.join(BASE_PATH, "titanic_seq_clas_02_kfold/")
os.system("mkdir -p " + OUTPUT_PATH)

# load train and test data
train = pd.read_csv(DATA_PATH + "train.csv")
test = pd.read_csv(DATA_PATH + "test.csv")

train.isnull().sum()

