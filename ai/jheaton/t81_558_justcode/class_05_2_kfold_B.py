import pandas as pd
from scipy.stats import zscore

original = True

pd.set_option("display.max_rows", None)


if original == True:
    df = pd.read_csv(
        "./input/jh-simple-dataset.csv",
        na_values=["NA", "?"],
    )
else:
    df = pd.read_csv(
        "./input/jh-simple-dataset_short100.csv",
        na_values=["NA", "?"],
    )
# print(df.head())
# print("original data set\n", df)
print("dataset original size:\n", df.shape)

# Generate dummies for job
df = pd.concat([df,pd.get_dummies(df['job'],prefix="job")],axis=1)
df.drop('job', axis=1, inplace=True)
# Generate dummies for area
df = pd.concat([df,pd.get_dummies(df['area'],prefix="area")],axis=1)
df.drop('area', axis=1, inplace=True)
# Missing values for income
med = df['income'].median()
df['income'] = df['income'].fillna(med)
# Standardize ranges
df['income'] = zscore(df['income'])
df['aspect'] = zscore(df['aspect'])
df['save_rate'] = zscore(df['save_rate'])
df['age'] = zscore(df['age'])
df['subscriptions'] = zscore(df['subscriptions'])
# Convert to numpy - Classification
x_columns = df.columns.drop('product').drop('id')
x = df[x_columns].values
dummies = pd.get_dummies(df['product']) # Classification
products = dummies.columns
y = dummies.values



