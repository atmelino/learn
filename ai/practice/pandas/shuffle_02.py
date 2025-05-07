import pandas as pd
import numpy as np

# n = 3
# m = 4
# arr = [*m for _ in range(n)]
x_test = [i for i in range(9)]
# d=pd.DataFrame(a)
# print(d)
rows, cols = (5, 4)
arr = [[j for i in range(cols)] for j in range(rows)]

x_test = np.array(arr)
print(x_test.shape)

x_before = pd.DataFrame(x_test, columns=["sl", "sw", "pl", "pw"],copy=True)
print(x_test)

np.random.shuffle(x_test[:, 0])

x_after = pd.DataFrame(x_test,columns=["sl", "sw", "pl", "pw"])
print(x_test)


a = [" "] * x_test.shape[0]
line = pd.DataFrame(a,columns=[' '])
compare = pd.concat([x_before, line, x_after], axis=1)
print("Before shuffle - after shuffle")
print(compare)


