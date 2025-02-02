# Use conda jh_class environment
# https://machinelearningmastery.com/how-to-develop-a-generative-adversarial-network-for-a-1-dimensional-function-from-scratch-in-keras/

import os
from numpy.random import rand
from numpy import hstack
from numpy import ones, zeros
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from tensorflow.keras.utils import plot_model
from numpy.random import randn
import matplotlib.pyplot as plt

float_formatter = "{:+1.3f}".format
np.set_printoptions(formatter={"float_kind": float_formatter})
os.system("mkdir -p ./models")


# generate n real samples with class labels
def generate_real_samples(n):
    # generate inputs in [-10, 10]
    X1 = 20*rand(n) - 10
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
    X1 = -10 + rand(n) * 20
    # generate outputs in [-1, 1]
    X2 = rand(n) * 100
    # stack arrays
    X1 = X1.reshape(n, 1)
    X2 = X2.reshape(n, 1)
    X = hstack((X1, X2))
    # generate class labels
    y = zeros((n, 1))
    return X, y


# define the standalone discriminator model
def define_discriminator(n_inputs=2):
    model = Sequential()
    model.add(
        Dense(
            25, activation="relu", kernel_initializer="he_uniform", input_dim=n_inputs
        )
    )
    model.add(Dense(1, activation="sigmoid"))
    # compile model
    model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])
    return model


# train the discriminator model
def train_discriminator(model, n_epochs=1000, n_batch=128):
    half_batch = int(n_batch / 2)
    # run epochs manually
    print("Epoch    acc_real    acc_fake ")
    for i in range(n_epochs):
        # generate real examples
        X_real, y_real = generate_real_samples(half_batch)
        # print("X_real",X_real)
        # update model
        model.train_on_batch(X_real, y_real)
        # generate fake examples
        X_fake, y_fake = generate_fake_samples(half_batch)
        # update model
        model.train_on_batch(X_fake, y_fake)
        # evaluate the model
        _, acc_real = model.evaluate(X_real, y_real, verbose=0)
        _, acc_fake = model.evaluate(X_fake, y_fake, verbose=0)
        # print(i, acc_real, acc_fake)
        print("epoch %3d acc_real %.3f acc_fake %.3f" % (i, acc_real, acc_fake))



# print(generate_real_samples(10))
# print(generate_fake_samples(10))

def show_samples():
    (reals_X, reals_y)=generate_real_samples(10)
    (fakes_X, fakes_y)=generate_fake_samples(10)
    print("reals",reals_X)
    print("reals",fakes_X)
    print(reals_X.shape)
    plt.xlim(-10, 10)
    plt.ylim(0, 100)
    plt.scatter(reals_X[:, 0], reals_X[:, 1])
    plt.show()
    plt.xlim(-10, 10)
    plt.ylim(0, 100)
    plt.scatter(fakes_X[:, 0], fakes_X[:, 1])
    plt.show()



# exit()

# define the discriminator model
model = define_discriminator()
# summarize the model
model.summary()
# plot the model
# plot_model(model, to_file='discriminator_plot.png', show_shapes=True, show_layer_names=True)


# fit the model
train_discriminator(model, n_epochs=1000, n_batch=128)

# save entire network to HDF5 (save everything, suggested)
model.save("./models/disc_mod.h5")
model.save("./models/disc_mod.keras")

