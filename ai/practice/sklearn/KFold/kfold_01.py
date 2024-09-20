# https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.KFold.html#


import numpy as np
from sklearn.model_selection import KFold

X = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [5, 6], [7, 8]])
y = np.array([1, 2, 3, 4, 5, 6])
kf = KFold(n_splits=3)
kf.get_n_splits(X)
print(kf)
for i, (train_index, test_index) in enumerate(kf.split(X)):
    print(f"Fold {i}:")
    print(f"  Train: index={train_index}")
    print(f"  Test:  index={test_index}")
