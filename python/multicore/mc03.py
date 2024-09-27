
# https://forums.raspberrypi.com/viewtopic.php?t=347773

import numpy as np
size = 10000
a = np.random.random_sample((size,size))
b = np.random.random_sample((size,size))
print("starting matrix multiply")
c = np.dot(a,b)

