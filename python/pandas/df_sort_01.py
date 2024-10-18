# importing pandas library
import pandas as pd

# creating and initializing a nested list
age_list = [['Afghanistan', 1952, 8425333, 'Asia'],
            ['Australia', 1957, 9712569, 'Oceania'],
            ['Brazil', 1962, 76039390, 'Americas'],
            ['China', 1957, 637408000, 'Asia'],
            ['France', 1957, 44310863, 'Europe'],
            ['India', 1952, 3.72e+08, 'Asia'],
            ['United States', 1957, 171984000, 'Americas']]

# creating a pandas dataframe
df = pd.DataFrame(age_list, columns=['Country', 'Year',
                                     'Population', 'Continent'])

print(df)

df2=df.sort_values(by=['Year'])

print(df2)

