import tensorflow as tf
print("Num GPUs Available: ", len(tf.config.experimental.list_physical_devices('GPU')))

import os
os.environ["CUDA_VISIBLE_DEVICES"] = "0,1"  # Replace with the IDs of your available GPUs

from keras.models import Sequential
from keras.layers import Dense
from keras.datasets import mnist
from keras.utils import to_categorical
import tensorflow as tf

# Create a MirroredStrategy.
strategy = tf.distribute.MirroredStrategy()

num_gpus = 4  # Replace with the number of available GPUs

# Load a sample dataset
(x_train, y_train), (x_val, y_val) = mnist.load_data()

# Preprocess the data
x_train = x_train.reshape(-1, 784).astype('float32') / 255
x_val = x_val.reshape(-1, 784).astype('float32') / 255

# Convert class vectors to binary class matrices (one-hot encoding)
y_train = to_categorical(y_train, 10)
y_val = to_categorical(y_val, 10)

with strategy.scope():
    # Define your Keras model
    model = Sequential()
    model.add(Dense(64, input_dim=784, activation='relu'))
    model.add(Dense(10, activation='softmax'))

    # Compile the model
    model.compile(loss='categorical_crossentropy',
                  optimizer='rmsprop',
                  metrics=['accuracy'])

# Train the model on your data
model.fit(x_train, y_train,
          epochs=20,
          batch_size=128 * num_gpus,
          validation_data=(x_val, y_val))




