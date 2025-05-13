import pandas as pd
import os
import numpy as np
from sklearn import metrics
from scipy.stats import zscore
from sklearn.model_selection import KFold
from IPython.display import HTML, display


URL = "https://data.heatonresearch.com/data/t81-558/kaggle/"

df_train = pd.read_csv(URL + "bio_train.csv", na_values=["NA", "?"])
df_test = pd.read_csv(URL + "bio_test.csv", na_values=["NA", "?"])

activity_classes = df_train["Activity"]
