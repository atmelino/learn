# conda activate jh_class

# https://www.kaggle.com/code/kutaykutlu/resnet50-transfer-learning-cifar-10-beginner/notebook

# Run with keras version 2 meaning tensorflow <=2.15

import os, re, time, json
import PIL.Image, PIL.ImageFont, PIL.ImageDraw
import numpy as np
import tensorflow as tf
from tensorflow.keras.applications.resnet50 import ResNet50
from matplotlib import pyplot as plt
import tensorflow_datasets as tfds
import pickle

print("Tensorflow version " + tf.__version__)

BATCH_SIZE = 32
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

# Create folders
model_path="../../../../../local_data/practice/keras/models/resnet_02"
os.system("mkdir -p "+model_path)

# Matplotlib config
plt.rc("image", cmap="gray")
plt.rc("grid", linewidth=0)
plt.rc("xtick", top=False, bottom=False, labelsize="large")
plt.rc("ytick", left=False, right=False, labelsize="large")
plt.rc("axes", facecolor="F8F8F8", titlesize="large", edgecolor="white")
plt.rc("text", color="a8151a")
plt.rc("figure", facecolor="F0F0F0")  # Matplotlib fonts
MATPLOTLIB_FONT_DIR = os.path.join(os.path.dirname(plt.__file__), "mpl-data/fonts/ttf")


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
    filename=model_path+"/resnet_02_"+title+".png"
    fig.savefig(filename)


def preprocess_image_input(input_images):
    input_images = input_images.astype("float32")
    output_ims = tf.keras.applications.resnet50.preprocess_input(input_images)
    return output_ims



"""
Feature Extraction is performed by ResNet50 pretrained on imagenet weights. 
Input size is 224 x 224.
"""


def feature_extractor(inputs):

    feature_extractor = tf.keras.applications.resnet.ResNet50(
        input_shape=(224, 224, 3), include_top=False, weights="imagenet"
    )(inputs)
    return feature_extractor


"""
Defines final dense layers and subsequent softmax layer for classification.
"""


def classifier(inputs):
    x = tf.keras.layers.GlobalAveragePooling2D()(inputs)
    x = tf.keras.layers.Flatten()(x)
    x = tf.keras.layers.Dense(1024, activation="relu")(x)
    x = tf.keras.layers.Dense(512, activation="relu")(x)
    x = tf.keras.layers.Dense(10, activation="softmax", name="classification")(x)
    return x


"""
Since input image size is (32 x 32), first upsample the image by factor of (7x7) to transform it to (224 x 224)
Connect the feature extraction and "classifier" layers to build the model.
"""


def final_model(inputs):

    resize = tf.keras.layers.UpSampling2D(size=(7, 7))(inputs)

    resnet_feature_extractor = feature_extractor(resize)
    classification_output = classifier(resnet_feature_extractor)

    return classification_output


"""
Define the model and compile it. 
Use Stochastic Gradient Descent as the optimizer.
Use Sparse Categorical CrossEntropy as the loss function.
"""


def define_compile_model():
    inputs = tf.keras.layers.Input(shape=(32, 32, 3))

    classification_output = final_model(inputs)
    model = tf.keras.Model(inputs=inputs, outputs=classification_output)

    model.compile(
        optimizer="SGD", loss="sparse_categorical_crossentropy", metrics=["accuracy"]
    )

    return model


(training_images, training_labels), (validation_images, validation_labels) = (
    tf.keras.datasets.cifar10.load_data()
)

train_X = preprocess_image_input(training_images)
valid_X = preprocess_image_input(validation_images)

display_images(training_images, training_labels, training_labels, "TrainingData")
display_images(
    validation_images, validation_labels, validation_labels, "ValidationData"
)



model = define_compile_model()

model.summary()

EPOCHS = 3
history = model.fit(
    train_X,
    training_labels,
    epochs=EPOCHS,
    validation_data=(valid_X, validation_labels),
    batch_size=64,
)

# list all data in history
print(history.history.keys())

# save entire network to HDF5 (save everything, suggested) and history
model.save(model_path+"/resnet_02.h5")
model.save(model_path+"/resnet_02.keras")
with open(model_path+'/resnet_02.pkl', 'wb') as file_pi:
    pickle.dump(history.history, file_pi)


