import os
import tensorflow as tf
from tensorflow.keras.models import load_model
from matplotlib import pyplot as plt
import pickle


show_history=True

def preprocess_image_input(input_images):
    input_images = input_images.astype("float32")
    output_ims = tf.keras.applications.resnet50.preprocess_input(input_images)
    return output_ims

(training_images, training_labels), (validation_images, validation_labels) = (
    tf.keras.datasets.cifar10.load_data()
)

valid_X = preprocess_image_input(validation_images)


load_path = "../not_on_github/models"
model = load_model(os.path.join(load_path, "resnet_02.h5"))

model.summary()

loss, accuracy = model.evaluate(valid_X, validation_labels, batch_size=64)

print("loss=",loss, " accuracy=",accuracy)




if show_history==True:
    # utility to display training and validation curves
    def plot_metrics(metric_name, title, ylim=5):
        plt.title(title)
        plt.ylim(0, ylim)
        plt.plot(history[metric_name], color="blue", label=metric_name)
        plt.plot(
            history["val_" + metric_name], color="green", label="val_" + metric_name
        )
        plt.show()

    with open('../not_on_github/models/resnet_02.pkl', "rb") as file_pi:
        history = pickle.load(file_pi)

    print(history)

    # list all data in history
    print(history.keys())

    plot_metrics("loss", "Loss")
    plot_metrics("accuracy", "Accuracy")






