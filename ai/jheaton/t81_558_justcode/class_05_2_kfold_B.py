import pandas as pd
from scipy.stats import zscore

pd.set_option("display.max_rows", None)

# Options for this run
shuffle = False
print_fold = True
length=2000
folds=5

# Read the data set
df_original = pd.read_csv(
    "./input/jh-simple-dataset.csv",
    na_values=["NA", "?"],
)
# print(df_original.head())
# print("original data set\n", df_original)
print("dataset original size:\n", df_original.shape)

df = df_original.iloc[0:length]

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
df.to_csv("./output/class_05_2_B_jh-simple-dataset_06.csv", sep=",")

# print("Table after feature vector encoding\n", df.head())
print("dataset size after feature vector encoding:\n", df.shape)

# Convert to numpy - Classification
x_columns = df.columns.drop('product').drop('id')
x = df[x_columns].values
dummies = pd.get_dummies(df['product']) # Classification
products = dummies.columns
y = dummies.values
# print("shape of y=",y.shape)
# print("y=",y)


