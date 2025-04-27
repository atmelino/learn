# conda activate jh_class

# https://www.kaggle.com/code/kutaykutlu/resnet50-transfer-learning-cifar-10-beginner/notebook

# Run with keras version 2 meaning tensorflow <=2.15

import os
import tensorflow as tf
from tensorflow.keras.models import load_model
import numpy as np
from matplotlib import pyplot as plt
import pickle


show_history = False
classes = [
    "airplane",
    "automobile",
    "bird",
    "cat",
    "deer",
    "dog",
    "frog",
    "horse",
    "ship",
    "truck",
]


# utility to display a row of digits with their predictions
def display_images(digits, predictions, labels, title):

    n = 10

    indexes = np.random.choice(len(predictions), size=n)
    n_digits = digits[indexes]
    n_predictions = predictions[indexes]
    n_predictions = n_predictions.reshape((n,))
    n_labels = labels[indexes]

    fig = plt.figure(figsize=(20, 4))
    plt.title(title)
    plt.yticks([])
    plt.xticks([])

    for i in range(10):
        ax = fig.add_subplot(1, 10, i + 1)
        class_index = n_predictions[i]

        plt.xlabel(classes[class_index])
        plt.xticks([])
        plt.yticks([])
        plt.imshow(n_digits[i])

    plt.show()
    filename = model_path + "/resnet_02_" + title + ".png"
    print("Saving plot as ", filename)
    fig.savefig(filename)


def preprocess_image_input(input_images):
    input_images = input_images.astype("float32")
    output_ims = tf.keras.applications.resnet50.preprocess_input(input_images)
    return output_ims


(training_images, training_labels), (validation_images, validation_labels) = (
    tf.keras.datasets.cifar10.load_data()
)

valid_X = preprocess_image_input(validation_images)


model_path = "../../../../../local_data/practice/keras/models/resnet_02"
model = load_model(os.path.join(model_path, "resnet_02.h5"))

model.summary()

loss, accuracy = model.evaluate(valid_X, validation_labels, batch_size=64)

print("loss=", loss, " accuracy=", accuracy)

probabilities = model.predict(valid_X, batch_size=64)
print(probabilities)
probabilities = np.argmax(probabilities, axis=1)
print(probabilities)

# Bad predictions indicated in red
display_images(validation_images, probabilities, validation_labels, "predictions")


if show_history == True:
    # utility to display training and validation curves
    def plot_metrics(metric_name, title, ylim=5):
        plt.title(title)
        plt.ylim(0, ylim)
        plt.plot(history[metric_name], color="blue", label=metric_name)
        plt.plot(
            history["val_" + metric_name], color="green", label="val_" + metric_name
        )
        plt.show()

    with open(model_path + "/resnet_02.pkl", "rb") as file_pi:
        history = pickle.load(file_pi)

    print(history)

    # list all data in history
    print(history.keys())

    plot_metrics("loss", "Loss")
    plot_metrics("accuracy", "Accuracy")
