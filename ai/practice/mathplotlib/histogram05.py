import numpy as np
import matplotlib.pyplot as plt

d = [1,1,2,4,4,4,5,6]
e = [2,1,2,4,6,4,5,6]

y_test=[2,0,2,1,0,2,3,1,0,3,5,1,2,0,1,0,1,1,2,1,4,1,1,5,1,2,3,1,0,0,2,1,1,1,1,2,2,2,1,0,1,1,0,1,1,2,0,2,1,2,2,2,1,1,1,3,1,1,2,1,2,1,1,1,1,1,1,2,2,2,2,1,1,1,2,1,1,2,1,2,3,1,1,2,1,1,1,2,1,1,1,2,5,2,2,1,1,1,1,0,1,1,1,1,1,3,2,0,1,2,3,1,1,2,2,1,1,0,2,2,1,2,2,1,1,2,2,0,1,2,1,1,5,5,1,1,2,1,1,3,2,0,1,2,1,1,1,1,3,1,1,1,2,2,1,2,2,1,1,1,1,2,2,2,2,1,1,5,5,1,1,2,1,2,1,2,1,2,1,4,1,2,1,2,1,2,1,6,2,2,1,2,1,2,2,1,1,2,2,1,5,2,2,1,2,2,1,1,2,2,5,0,2,2,1,1,2,2,1,5,1,2,1,1,2,5,4,1,1,1,1,2,1,1,2,2,2,1,1,2,2,1,1,2,1,2,1,2,2,1,1,1,2,1,1,1,1,2,2,0,1,1,1,0,0,2,1,2,2,1,1,1,1,1,1,5,2,2,1,2,0,1,1,1,1,2,1,2,2,2,1,1,1,1,1,1,2,1,1,2,1,1,2,4,2,1,1,1,1,2,2,1,1,5,1,1,0,2,1,1,1,2,1,2,2,2,2,1,1,2,1,2,2,1,2,2,0,2,2,1,2,1,1,1,0,2,1,2,1,1,1,1,2,1,5,1,2,1,3,2,2,2,1,2,1,1,2,2,1,1,2,2,1,1,1,1,1,2,1,5,2,1,2,1,5,1,2,1,1,1,2,1,1,1,5,2,1,2,1,2,1,0,1,1,0,2,2,2,5,0,1,1,1,1,5,2,6,1,1,1,2,1,1,0,2,2,2,1,3,2,0,3,2,2,2,1,2,0,1,1,2,1,2,2,1,2,1,5,2,1,2,1,1,1,1,1,1,1,2,2,2,1,2,0,1,1,1,2,1,2,1,2,1,1,1,1,4,2,1,1,1,1,1,2,4,2,2,1,0,5,2,2,2,0,1,1,0,5,2,2]
pred=[2,0,2,1,0,1,2,1,0,2,1,1,2,0,1,0,1,1,1,2,1,1,1,1,1,2,3,1,0,0,2,1,1,1,2,2,2,2,1,0,1,1,0,1,1,1,0,2,1,2,1,2,1,1,1,2,1,1,2,1,2,1,1,2,1,1,2,2,2,2,2,1,1,1,3,1,1,1,1,2,3,1,2,2,1,1,1,2,2,1,1,2,1,2,2,1,2,1,1,0,1,1,1,1,1,3,1,0,1,2,2,2,1,2,2,2,1,0,2,2,1,2,2,2,1,2,1,0,1,3,1,1,0,0,1,1,2,1,1,3,2,0,1,2,1,1,1,1,2,1,1,1,2,2,1,2,2,1,3,0,1,2,1,2,2,2,1,0,0,1,1,2,1,2,1,1,1,2,1,1,1,2,1,2,1,2,2,0,2,1,2,1,1,1,2,1,1,2,2,1,1,2,2,1,2,2,1,1,1,2,1,1,1,1,1,1,2,2,1,1,0,2,1,1,1,0,1,1,1,0,1,2,2,1,2,1,2,1,0,1,1,1,2,2,1,1,2,1,2,2,1,2,1,1,2,2,1,2,2,0,1,1,1,0,1,2,1,2,2,1,1,1,1,1,1,0,2,2,2,2,0,0,2,1,1,2,1,2,1,3,1,2,1,1,1,1,1,1,1,1,2,1,1,1,2,1,1,1,1,2,1,1,2,0,2,2,0,2,2,2,1,1,1,2,2,2,2,1,1,2,1,1,1,1,2,3,0,1,2,1,2,1,2,1,0,2,1,2,1,1,1,1,1,2,0,1,2,1,2,1,2,2,1,1,1,1,2,2,1,1,2,2,1,1,0,1,1,3,1,0,2,2,2,0,0,2,2,1,1,1,1,1,1,1,0,2,1,2,1,2,2,0,1,1,0,2,2,2,0,0,2,1,1,2,0,2,0,2,1,1,1,2,1,0,1,1,1,2,3,1,0,3,3,3,1,1,2,0,1,1,2,2,2,1,1,1,1,0,2,1,1,1,2,1,2,2,1,1,2,2,1,1,1,0,1,1,1,2,1,2,1,2,2,2,1,2,1,2,2,1,0,1,1,2,1,1,2,2,0,0,1,1,2,0,1,1,0,0,2,2]


plt.bar(*np.unique(y_test, return_counts=True), alpha=0.3)
plt.bar(*np.unique(pred, return_counts=True), alpha=0.6)
plt.show()