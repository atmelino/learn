import numpy as np
import matplotlib.pyplot as plt

d = [1,1,2,4,4,4,5,6]
e = [2,1,2,4,6,4,5,6]
plt.bar(*np.unique(d, return_counts=True), alpha=0.3)
plt.bar(*np.unique(e, return_counts=True), alpha=0.6)
plt.show()
