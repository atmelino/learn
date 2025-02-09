import pandas as pd

data = {'Col1': [10, 15, 20, 25, 30, 35], 
        'Col2': [15, 20, 25, 30, 35, 40], 
        'Col3': [22, 27, 32, 37, 42, 47],
        'Col4': [23, 28, 33, 38, 43, 48], 
        'Col5': [14, 19, 24, 31, 36, 41]
}
df = pd.DataFrame(data)
print(df)


def highlight_max(col, props=''):
    nlargest = col.nlargest(3)
    return np.where(col.isin(nlargest), props, '')

df.style.apply(highlight_max, props='color:red', subset=['Col3', 'Col4'], axis=0)

from termcolor import colored
import tabulate
df1 = pd.DataFrame(df)
nl3 = df.Col3.nlargest(3).values
nl4 = df.Col4.nlargest(3).values
df1.Col3 = df1.Col3.apply(lambda x: colored(x, "red") if x in nl3 else x)
df1.Col4 = df1.Col4.apply(lambda x: colored(x, "red") if x in nl4 else x)
print(tabulate.tabulate(df1, headers=df1.columns))




