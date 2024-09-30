import pandas as pd

pd.set_option('display.expand_frame_repr', False)
print_number=7

pd.set_option('display.max_columns', 7) 
pd.set_option('display.max_rows', 5)

df = pd.read_csv(
    "https://data.heatonresearch.com/data/t81-558/jh-simple-dataset.csv",
    na_values=['NA','?'])

pd.set_option('display.max_columns', 9)
pd.set_option('display.max_rows', 5)

if print_number==1:
    # display(df)
    print(df)



pd.set_option('display.max_columns', 7) 
pd.set_option('display.max_rows', 5)

dummies = pd.get_dummies(df['job'],prefix="job")
print(dummies.shape)

pd.set_option('display.max_columns', 9)
pd.set_option('display.max_rows', 10)

if print_number==2:
    # display(dummies)
    print(dummies)


pd.set_option('display.max_columns', 7) 
pd.set_option('display.max_rows', 5)

df = pd.concat([df,dummies],axis=1)
df.drop('job', axis=1, inplace=True)

pd.set_option('display.max_columns', 9)
pd.set_option('display.max_rows', 10)

if print_number==3:
    # display(df)
    print(df)

pd.set_option('display.max_columns', 7) 
pd.set_option('display.max_rows', 5)

df = pd.concat([df,pd.get_dummies(df['area'],prefix="area")],axis=1)
df.drop('area', axis=1, inplace=True)

pd.set_option('display.max_columns', 9)
pd.set_option('display.max_rows', 10)

if print_number==4:
    # display(df)
    print(df)


med = df['income'].median()
df['income'] = df['income'].fillna(med)
if print_number==5:
    print(list(df.columns))


x_columns = df.columns.drop('product').drop('id')
if print_number==6:
    print(list(x_columns))


# Convert to numpy - Classification
x_columns = df.columns.drop('product').drop('id')
x = df[x_columns].values
dummies = pd.get_dummies(df['product']) # Classification
products = dummies.columns
y = dummies.values

if print_number==7:
    print(x)
    print(y)


y = df['income'].values

