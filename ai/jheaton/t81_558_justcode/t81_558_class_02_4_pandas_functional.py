import os
import pandas as pd
import numpy as np

pd.set_option('display.expand_frame_repr', False)

df = pd.read_csv(
    "https://data.heatonresearch.com/data/t81-558/auto-mpg.csv", 
    na_values=['NA', '?'])

pd.set_option('display.max_columns', 7)
pd.set_option('display.max_rows', 5)

print(df)


# Apply the map
df['origin_name'] = df['origin'].map(
    {1: 'North America', 2: 'Europe', 3: 'Asia'})

# Shuffle the data, so that we hopefully see
# more regions.
df = df.reindex(np.random.permutation(df.index)) 

# Display
pd.set_option('display.max_columns', 7)
pd.set_option('display.max_rows', 10)
print(df)

#Why does it add the column to the dataframe?
print(df['origin'])
print(df['origin'].map(
    {1: 'North America', 2: 'Europe', 3: 'Asia'}))


#do it again, no additional one
df['origin_name'] = df['origin'].map(
    {1: 'North America', 2: 'Europe', 3: 'Asia'})
print(df)

df['test'] = df['cylinders'].map(
    {3: 'small', 4: 'regular', 5: 'bigger'})
print(df)


df = pd.DataFrame({'cost': [250, 150, 100],
                   'revenue': [100, 250, 300]})
print(df)

df['new']=    {0: 'North America', 1: 'Europe', 2: 'Asia'}
print(df)

#Interesting: assignment of nomn-existing, named column adds a column
df['new2']=    {0: 'bagel', 1: 'pizza', 2: 'sushi'}
print(df)
