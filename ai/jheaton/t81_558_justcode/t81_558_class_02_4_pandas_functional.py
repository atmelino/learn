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

# df['test'] = df['cylinders'].map(
#     {3: 'small', 4: 'regular', 5: 'bigger'})
# print(df)

efficiency = df.apply(lambda x: x['displacement']/x['horsepower'], axis=1)
print(efficiency[0:10])

df['efficiency'] = efficiency
print(df)


import pandas as pd

# df=pd.read_csv('https://www.irs.gov/pub/irs-soi/16zpallagi.csv')
df=pd.read_csv('jheaton/t81_558_justcode/large_csv/16zpallagi.csv')
print(df)




