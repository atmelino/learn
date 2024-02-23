# Simple dataframe
import os
import pandas as pd

pd.set_option('display.expand_frame_repr', False)

pd.set_option('display.max_columns', 8)
df = pd.read_csv(
    "https://data.heatonresearch.com/data/t81-558/auto-mpg.csv")
print(df[0:5])


pd.set_option('display.max_rows', 5)
print(df)

def print_statistics(df):
    # Strip non-numerics
    df = df.select_dtypes(include=['int', 'float'])
    headers = list(df.columns.values)
    fields = []
    for field in headers:
        fields.append({
            'name' : field,
            'mean': df[field].mean(),
            'var': df[field].var(),
            'sdev': df[field].std()
        })
    for field in fields:
        print(field)


print_statistics(df)

import os
import pandas as pd

df = pd.read_csv(
    "https://data.heatonresearch.com/data/t81-558/auto-mpg.csv", 
    na_values=['NA', '?'])
print(f"horsepower has na? {pd.isnull(df['horsepower']).values.any()}")
    
print("Filling missing values...")
med = df['horsepower'].median()
df['horsepower'] = df['horsepower'].fillna(med)
# df = df.dropna() # you can also simply drop NA values
                 
print(f"horsepower has na? {pd.isnull(df['horsepower']).values.any()}")



# Remove all rows where the specified column is +/- sd standard deviations
def remove_outliers(df, name, sd):
    drop_rows = df.index[(np.abs(df[name] - df[name].mean())
                          >= (sd * df[name].std()))]
    df.drop(drop_rows, axis=0, inplace=True)

import pandas as pd
import os
import numpy as np
from sklearn import metrics
from scipy.stats import zscore

df = pd.read_csv(
    "https://data.heatonresearch.com/data/t81-558/auto-mpg.csv",
    na_values=['NA','?'])

# create feature vector
med = df['horsepower'].median()
df['horsepower'] = df['horsepower'].fillna(med)

# Drop the name column
# df.drop('name',1,inplace=True)

# Drop outliers in horsepower
print("Length before MPG outliers dropped: {}".format(len(df)))
remove_outliers(df,'mpg',2)
print("Length after MPG outliers dropped: {}".format(len(df)))
print_statistics(df)

pd.set_option('display.max_columns', 0)
pd.set_option('display.max_rows', 5)
print(df)



import os
import pandas as pd

df = pd.read_csv(
    "https://data.heatonresearch.com/data/t81-558/auto-mpg.csv",
    na_values=['NA','?'])

print(f"Before drop: {list(df.columns)}")
df.drop('name', axis=1,inplace=True)
print(f"After drop: {list(df.columns)}")



