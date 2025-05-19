# https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.KFold.html#


import numpy as np
from sklearn.model_selection import StratifiedKFold

x = np.array([[1.1, 1.2], [2.1, 2.2], [3.1, 3.2], [4.1, 4.2], [5.1,5.2], [6.1, 6.2]])
y = np.array(["cat", "rabbit", "rabbit", "cat", "rabbit", "cat"])
kf = StratifiedKFold(n_splits=2)
kf.get_n_splits(x)
print(kf)
for i, (train_index, test_index) in enumerate(kf.split(x,y)):
    print(f"Fold {i}:")
    print(f"  Train: index={train_index}")
    print("x values=\n", x[train_index])
    print("y values=\n", y[train_index])
    print(f"  Test:  index={test_index}")
    print("x values=\n", x[test_index])
    print("y values=\n", y[test_index])
