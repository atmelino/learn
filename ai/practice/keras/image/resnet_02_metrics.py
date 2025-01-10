# https://www.kaggle.com/code/kutaykutlu/resnet50-transfer-learning-cifar-10-beginner/notebook

# Run with keras version 2 meaning tensorflow <=2.15

import os
import tensorflow as tf
from tensorflow.keras.models import load_model




# Create folders
os.system("mkdir -p ../not_on_github/models/resnet_02")


(training_images, training_labels), (validation_images, validation_labels) = (
    tf.keras.datasets.cifar10.load_data()
)


valid_X = preprocess_image_input(validation_images)


load_path = "../not_on_github/models/resnet_02"
model = load_model(os.path.join(load_path, "resnet_02.h5"))

model.summary()





