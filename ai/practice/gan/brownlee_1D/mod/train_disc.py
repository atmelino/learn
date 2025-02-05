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
import json

float_formatter = "{:+1.3f}".format
np.set_printoptions(formatter={"float_kind": float_formatter})
os.system("mkdir -p ./models")

with open('./config/config.json') as json_data:
    d = json.load(json_data)
    print(d)

print(d['selected'])
name=d['selected']
config=d[name]
print(config)

n_epochs=config['n_epochs']
n_batch=config['n_batch']
x_min=config['x_min']
x_max=config['x_max']
width=x_max-x_min
random_real=config['random_real']

# exit()

# generate n real samples with class labels
def generate_real_samples(n):
    if(random_real==False):
        print("sequential")
        arr = np.arange(0, n)
        X1=arr*width/n-width/2
    else:
        print("random")
        X1 = rand(n) - 0.5
    # print(X1)
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


print("real samples",generate_real_samples(n_batch))
print("fake samples",generate_fake_samples(n_batch))

exit()

# define the discriminator model
model = define_discriminator()
# summarize the model
model.summary()
# plot the model
# plot_model(model, to_file='discriminator_plot.png', show_shapes=True, show_layer_names=True)


# fit the model
train_discriminator(model, n_epochs=n_epochs, n_batch=n_batch)

# save entire network to HDF5 (save everything, suggested)
model.save("./models/discriminator.h5")
model.save("./models/discriminator.keras")

