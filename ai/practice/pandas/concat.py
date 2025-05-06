import pandas as pd
import numpy as np

data = [
    [10, 15, 20, 25, 30, 35],
    [15, 20, 25, 30, 35, 40],
    [22, 27, 32, 37, 42, 47],
    [23, 28, 33, 38, 43, 48],
    [14, 19, 24, 31, 36, 41],
]

print(data)
print(data.shape)

df1 = pd.DataFrame(data)
print(df1)


data["Col1"] = [1, 2, 3, 4, 5, 6]
df2 = pd.DataFrame(data)
print(df2)

compare1 = pd.concat([df1, df2], axis=1)
print(compare1)


np.random.shuffle(data[:, 2])
print(data)


