import numpy as np

# Set precision to 3 decimal places
np.set_printoptions(precision=3)

# Create an array with mixed-scale numbers
arr = np.array([0.001, 1.234, 1e20])

# Print the array with default (maxprec) floatmode
print(arr)
# Output: [ 0.001  1.234 1.000000e+20]

# Change floatmode to fixed
np.set_printoptions(floatmode='fixed')

# Print the array again
print(arr)
# Output: [ 0.001  1.234 1000000000000000000000000]

# Change floatmode to unique
np.set_printoptions(floatmode='unique')

# Print the array again
print(arr)
# Output: [ 0.001  1.234 1.0e+20]
