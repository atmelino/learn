import os
import pandas as pd
import numpy as np

pd.set_option('display.expand_frame_repr', False)


df = pd.DataFrame({'cost': [250, 150, 100],
                   'revenue': [100, 250, 300]})
print(df)

#Interesting: assignment of non-existing, named column adds a column

df['new']=    {0: 'North America', 1: 'Europe', 2: 'Asia'}
print(df)

df['new2']=    {0: 'bagel', 1: 'pizza', 2: 'sushi'}
print(df)

#do it again, no additional one
df['new2']=    {0: 'burger', 1: 'pizza', 2: 'sushi'}
print(df)
