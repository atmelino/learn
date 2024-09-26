# https://stackoverflow.com/questions/75029322/does-numpy-use-multiple-cores

import numpy as np

# Creating very large arrays
arr1 = np.random.rand(10000, 10000)
arr2 = np.random.rand(10000, 10000)

# Performing lots of math that should utilize multiple cores
result = np.dot(np.linalg.inv(arr1), arr2)

print("Finished")

