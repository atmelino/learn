# Use conda jh_class environment
# https://machinelearningmastery.com/how-to-develop-a-generative-adversarial-network-for-a-1-dimensional-function-from-scratch-in-keras/

from matplotlib import pyplot
from numpy.random import rand
from numpy import hstack
import numpy as np
from numpy import ones,zeros

# generate n real samples with class labels
def generate_real_samples(n):
    # generate inputs in [-0.5, 0.5]
    X1 = rand(n) - 0.5
    # generate outputs X^2
    X2 = X1 * X1
    # stack arrays
    X1 = X1.reshape(n, 1)
    X2 = X2.reshape(n, 1)
    X = hstack((X1, X2))
    # generate class labels
    y = ones((n, 1))
    return X, y
 

# generate n fake samples with class labels
def generate_fake_samples(n):
    # generate inputs in [-1, 1]
    X1 = -1 + rand(n) * 2
    # generate outputs in [-1, 1]
    X2 = -1 + rand(n) * 2
    # stack arrays
    X1 = X1.reshape(n, 1)
    X2 = X2.reshape(n, 1)
    X = hstack((X1, X2))
    # generate class labels
    y = zeros((n, 1))
    return X, y



float_formatter = "{:.2f}".format    
np.set_printoptions(formatter={'float_kind':float_formatter})
(reals_X, reals_y)=generate_real_samples(10)
(fakes_X, fakes_y)=generate_fake_samples(10)

print("reals",reals_X)
print("reals",fakes_X)
print(reals_X.shape)


pyplot.scatter(reals_X[:, 0], reals_X[:, 1])
pyplot.show()


# pyplot.plot(inputs, outputs)
# pyplot.show()

