import sys

import matplotlib

matplotlib.use('Agg')
import matplotlib.pyplot as plt

plt.plot([1, 2, 3])
# plt.savefig(sys.stdout.buffer)
plt.savefig("./output/plot01.png")

