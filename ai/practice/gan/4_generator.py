# Use conda jh_class environment
# https://machinelearningmastery.com/how-to-develop-a-generative-adversarial-network-for-a-1-dimensional-function-from-scratch-in-keras/



# define the generator model
from keras.models import Sequential
from keras.layers import Dense
from tensorflow.keras.utils import plot_model

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


