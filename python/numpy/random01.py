import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
plt.hist(np.random.randn(10000), bins=100)
plt.show()

