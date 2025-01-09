# https://www.youtube.com/watch?v=640ipvR0HhQ
# How to Load and Visualize CIFAR 10 Dataset using TensorFlow Keras

import tensorflow as tf
from tensorflow import keras

from matplotlib import pyplot as plt
import numpy as np


(training_images, training_labels), (validation_images, validation_labels) = (
    tf.keras.datasets.cifar10.load_data()
)

print("training_images shape= ",training_images.shape)
print("training_labels shape= ",training_labels.shape)

print("first training_image")
plt.imshow(training_images[0])
plt.show()

print("first training_label=",training_labels[0])



