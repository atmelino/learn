import os
import pandas as pd
from scipy.stats import zscore
pd.set_option('display.expand_frame_repr', False)

df = pd.read_csv(
    "https://data.heatonresearch.com/data/t81-558/auto-mpg.csv",
    na_values=['NA','?'])

pd.set_option('display.max_columns', 7)
pd.set_option('display.max_rows', 5)

df['mpg'] = zscore(df['mpg'])
print(df)


df = df.sort_values(by='mpg', ascending=True)
print(df)

import pandas as pd

df = pd.read_csv(
    "https://data.heatonresearch.com/data/t81-558/jh-simple-dataset.csv",
    na_values=['NA','?'])

pd.set_option('display.max_columns', 7)
pd.set_option('display.max_rows', 5)

print(df)

areas = list(df['area'].unique())
print(f'Number of areas: {len(areas)}')
print(f'Areas: {areas}')

dummies = pd.get_dummies(['a','b','c','d'],prefix='area')
print(dummies)
print()
dummies = pd.get_dummies(df['area'],prefix='area')
print(dummies[0:10]) # Just show the first 10

df = pd.concat([df,dummies],axis=1)
pd.set_option('display.max_columns', 0)
pd.set_option('display.max_rows', 10)

print(df[['id','job','area','income','area_a',
                  'area_b','area_c','area_d']])



pd.set_option('display.max_columns', 0)
pd.set_option('display.max_rows', 5)

df.drop('area', axis=1, inplace=True)
print(df[['id','job','income','area_a',
                  'area_b','area_c','area_d']])

import pandas as pd 

dummies = pd.get_dummies(['a','b','c','d'],prefix='area', drop_first=True)
print(dummies)

import pandas as pd 

# Read the dataset
df = pd.read_csv(
    "https://data.heatonresearch.com/data/t81-558/jh-simple-dataset.csv",
    na_values=['NA','?'])

# encode the area column as dummy variables
dummies = pd.get_dummies(df['area'], drop_first=True, prefix='area',dtype=int)
df = pd.concat([df,dummies],axis=1)
df.drop('area', axis=1, inplace=True)

# display the encoded dataframe
pd.set_option('display.max_columns', 0)
pd.set_option('display.max_rows', 10)

print(df[['id','job','income',
                  'area_b','area_c','area_d']])


# Create a small sample dataset
import pandas as pd
import numpy as np

np.random.seed(43)
df = pd.DataFrame({
    'cont_9': np.random.rand(10)*100,
    'cat_0': ['dog'] * 5 + ['cat'] * 5,
    'cat_1': ['wolf'] * 9 + ['tiger'] * 1,
    'y': [1, 0, 1, 1, 1, 1, 0, 0, 0, 0]
})

pd.set_option('display.max_columns', 0)
pd.set_option('display.max_rows', 0)
print(df)

means0 = df.groupby('cat_0')['y'].mean().to_dict()
print(means0)
print()

print(df['y'].mean())

def calc_smooth_mean(df1, df2, cat_name, target, weight):
    # Compute the global mean
    mean = df[target].mean()

    # Compute the number of values and the mean of each group
    agg = df.groupby(cat_name)[target].agg(['count', 'mean'])
    counts = agg['count']
    means = agg['mean']

    # Compute the "smoothed" means
    smooth = (counts * means + weight * mean) / (counts + weight)

    # Replace each value by the according smoothed mean
    if df2 is None:
        return df1[cat_name].map(smooth)
    else:
        return df1[cat_name].map(smooth),df2[cat_name].map(smooth.to_dict())



WEIGHT = 5
df['cat_0_enc'] = calc_smooth_mean(df1=df, df2=None, 
    cat_name='cat_0', target='y', weight=WEIGHT)
df['cat_1_enc'] = calc_smooth_mean(df1=df, df2=None, 
    cat_name='cat_1', target='y', weight=WEIGHT)

pd.set_option('display.max_columns', 0)
pd.set_option('display.max_rows', 0)

print(df)
