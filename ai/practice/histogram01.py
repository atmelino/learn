import numpy as np
import matplotlib.pyplot as plt

data = np.random.default_rng(123).rayleigh(1, 70)

print(data)
counts, edges, bars = plt.hist(data)

plt.bar_label(bars)
plt.show()