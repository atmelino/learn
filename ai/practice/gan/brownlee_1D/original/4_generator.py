# Use conda jh_class environment
# https://machinelearningmastery.com/how-to-develop-a-generative-adversarial-network-for-a-1-dimensional-function-from-scratch-in-keras/


# define the generator model
from keras.models import Sequential
from keras.layers import Dense
from tensorflow.keras.utils import plot_model
# from numpy.random import randn
# from matplotlib import pyplot
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)

# define the standalone generator model
def define_generator(latent_dim, n_outputs=2):
    model = Sequential()
    model.add(Dense(15, activation='relu', kernel_initializer='he_uniform', input_dim=latent_dim))
    model.add(Dense(n_outputs, activation='linear'))
    return model

# define the discriminator model
model = define_generator(5)

# summarize the model
model.summary()

# plot the model
plot_model(model, to_file='generator_plot.png', show_shapes=True, show_layer_names=True)


# generate points in latent space as input for the generator
def generate_latent_points(latent_dim, n):
    # generate points in the latent space
    x_input = np.random.randn(latent_dim * n)
    # print(x_input)
    # reshape into a batch of inputs for the network
    x_input = x_input.reshape(n, latent_dim)
    # print(x_input)

    return x_input

# use the generator to generate n fake examples and plot the results
def generate_fake_samples(generator, latent_dim, n):
    # generate points in latent space
    x_input = generate_latent_points(latent_dim, n)
    # predict outputs
    X = generator.predict(x_input)
    # plot the results
    size=5
    plt.xlim(-size,size)
    plt.ylim(-size,size)
    plt.scatter(X[:, 0], X[:, 1])
    plt.show()

# size of the latent space
latent_dim = 5
# define the discriminator model
model = define_generator(latent_dim)
# generate and plot generated samples
generate_fake_samples(model, latent_dim, 100)





