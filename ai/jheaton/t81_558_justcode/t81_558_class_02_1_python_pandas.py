# Simple dataframe
import os
import pandas as pd

pd.set_option('display.max_columns', 8)
df = pd.read_csv(
    "https://data.heatonresearch.com/data/t81-558/auto-mpg.csv")
print(df[0:5])



# pd.set_option('display.max_columns', 8)
# print(df)


# pd.set_option('display.max_rows', 5)
# print(df)

