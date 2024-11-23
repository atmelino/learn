# https://scikit-learn.org/1.5/modules/generated/sklearn.model_selection.ShuffleSplit.html

import numpy as np
from sklearn.model_selection import ShuffleSplit

X = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
y = np.array([1, 2, 1, 2, 1, 2])

# print("X= ",X)
# print("y= ",y)

print("Input x output y")
for input, output in zip(X,y):
    print(f'x = {input}, y = {output}')


rs = ShuffleSplit(n_splits=5, test_size=.25, random_state=0)
rs.get_n_splits(X)
print(rs)

for i, (train_index, test_index) in enumerate(rs.split(X)):
    # print(f"Fold {i}:")
    # print(f"  Train: index={train_index}")
    # print(f"  Test:  index={test_index}")
    print(f"Fold {i}:  Train: index={train_index}       Test:  index={test_index}")
    # print(f"  Test:  index={test_index}")
    x_train = X[train_index]
    y_train = y[train_index]
    x_test = X[test_index]
    y_test = y[test_index]   
    # print(x_train)
    for input, output in zip(x_train,y_train):
        print(f'x = {input}, y = {output}')


# Specify train and test size
print("with train size specified")
rs = ShuffleSplit(n_splits=5, train_size=0.5, test_size=.25,
                  random_state=0)
for i, (train_index, test_index) in enumerate(rs.split(X)):
    print(f"Fold {i}:")
    print(f"  Train: index={train_index}")
    print(f"  Test:  index={test_index}")


     # x_train = x[train]
    # y_train = y[train]
    # x_test = x[test]
    # y_test = y[test]   