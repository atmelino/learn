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
import json
import matplotlib.pyplot as plt
import pprint
import tables as tb

os.system("mkdir -p ./models")
os.system("mkdir -p ./output")
pp = pprint.PrettyPrinter(indent=4)
float_formatter = "{:+1.3f}".format
np.set_printoptions(formatter={"float_kind": float_formatter})

with open("./config/train.json") as json_data:
    d = json.load(json_data)
name = d["selected"]
config = d[name]
print(name)
pp.pprint(config)
n_epochs = config["n_epochs"]
n_batch = config["n_batch"]
x_max = config["x_max"]
width = 2 * x_max
xsquared = x_max * x_max
random_real = config["random_real"]

# exit()
# acc_real = 0


# generate n real samples with class labels
def generate_real_samples(n):
    if random_real == False:
        # print("sequential")
        arr = np.arange(0, n)
        X1 = arr * width / n - width / 2
    else:
        # print("random")
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
    if random_real == False:
        # generate inputs in double the real samples range
        X1 = 2 * (-x_max + rand(n) * width)
        X2 = 1.4 * rand(n) * xsquared - 0.2 * xsquared
    else:
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

        pred = model.predict(X_real)
        print(pred)

        vals_greater_0_5 = (pred > 0.5).sum()
        print(
            "predicted real samples=",
            vals_greater_0_5,
            "total real samples=",
            len(pred),
            "accuracy=",
            vals_greater_0_5 / len(pred),
        )

    return (acc_real, acc_fake)


def plot_initial():
    x_real, _ = generate_real_samples(n_batch)
    x_fake, _ = generate_fake_samples(n_batch)
    # print("real samples",generate_real_samples(n_batch))
    # print("fake samples",generate_fake_samples(n_batch))
    fig = plt.figure(figsize=(10, 10))
    xpadding = 0.3
    ypadding = 0.3
    plotrange = {
        "xlim0": (-1 - xpadding) * width,
        "xlim1": (1 + xpadding) * width,
        # "ylim0": ypadding * 2 * -xsquared + 0.5 * xsquared,
        # "ylim1": ypadding * 2 * xsquared + 0.5 * xsquared,
        "ylim0": (-0.5 - ypadding) * xsquared,
        "ylim1": (1.5 + ypadding) * xsquared,
    }
    print(plotrange)
    plt.xlim(plotrange["xlim0"], plotrange["xlim1"])
    plt.ylim(plotrange["ylim0"], plotrange["ylim1"])
    plt.scatter(x_real[:, 0], x_real[:, 1], color="red")
    plt.scatter(x_fake[:, 0], x_fake[:, 1], color="blue")
    plt.show()
    # filename="./output/plot%05d.png" % epoch
    filename = "./output/plot_init.png"
    fig.savefig(filename)
    plt.close(fig)


# plot_initial()

# define the discriminator model
model = define_discriminator()
# summarize the model
model.summary()
# plot the model
# plot_model(model, to_file='discriminator_plot.png', show_shapes=True, show_layer_names=True)


# fit the model
acc_real, acc_fake = train_discriminator(model, n_epochs=n_epochs, n_batch=n_batch)

# save entire network to HDF5 (save everything, suggested)
model.save("./models/discriminator.h5")
model.save("./models/discriminator.keras")


# Save additional training information
class Config(tb.IsDescription):
    name = tb.StringCol(16)  # 16-character String
    n_epochs = tb.UInt64Col()  # Signed 64-bit integer
    n_batch = tb.UInt64Col()  # Signed 64-bit integer
    x_max = tb.Float64Col()  # double (double-precision)
    acc_real = tb.Float64Col()  # double (double-precision)
    random_real = tb.BoolCol()


fname = "./models/discriminator.h5"
with tb.open_file(fname, "a") as h5file:
    node = h5file.get_node("/")

    try:
        h5file.remove_node("/training_config", recursive=True)
    except tb.NoSuchNodeError:
        print("file does not have training_config node")
    print("Create training_config node")
    group = h5file.create_group(
        "/", "training_config", "Training configurationinformation"
    )
    table = h5file.create_table(group, "config", Config, "config data")
    config = table.row
    config["name"] = f"Config name"
    config["n_epochs"] = n_epochs
    config["n_batch"] = n_batch
    config["x_max"] = x_max
    config["acc_real"] = acc_real
    config["random_real"] = random_real
    # Insert a new config record
    config.append()
    table.flush()
    h5file.close()
