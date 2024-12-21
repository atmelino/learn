import os
import tensorflow as tf
import keras_preprocessing
from keras_preprocessing import image
from keras_preprocessing.image import ImageDataGenerator
from tensorflow.keras.callbacks import EarlyStopping
from sklearn.metrics import accuracy_score
import numpy as np

print("class_06_2_cnn_B")
# this program requires the file structure to exist, that is created by running class_06_2_cnn_B_prepare.py

# Options for this run
train=False


PATH = "./not_on_github"
EXTRACT_TARGET = os.path.join(PATH, "iris")
SOURCE = EXTRACT_TARGET  # In this case its the same, no subfolder

training_datagen = ImageDataGenerator(
    rescale=1.0 / 255,
    horizontal_flip=True,
    vertical_flip=True,
    width_shift_range=[-200, 200],
    rotation_range=360,
    fill_mode="nearest",
)

train_generator = training_datagen.flow_from_directory(
    directory=SOURCE,
    target_size=(256, 256),
    class_mode="categorical",
    batch_size=32,
    shuffle=True,
)

validation_datagen = ImageDataGenerator(rescale=1.0 / 255)

validation_generator = validation_datagen.flow_from_directory(
    directory=SOURCE,
    target_size=(256, 256),
    class_mode="categorical",
    batch_size=32,
    shuffle=True,
)

# print(validation_generator)
print(validation_generator.samples)

class_count = len(train_generator.class_indices)
print("number of classes=",class_count)
print(train_generator.class_indices)
print(train_generator.filenames)

if train==True:

    model = tf.keras.models.Sequential(
        [
            # Note the input shape is the desired size of the image
            # 300x300 with 3 bytes color
            # This is the first convolution
            tf.keras.layers.Conv2D(
                16, (3, 3), activation="relu", input_shape=(256, 256, 3)
            ),
            tf.keras.layers.MaxPooling2D(2, 2),
            # The second convolution
            tf.keras.layers.Conv2D(32, (3, 3), activation="relu"),
            tf.keras.layers.Dropout(0.5),
            tf.keras.layers.MaxPooling2D(2, 2),
            # The third convolution
            tf.keras.layers.Conv2D(64, (3, 3), activation="relu"),
            tf.keras.layers.Dropout(0.5),
            tf.keras.layers.MaxPooling2D(2, 2),
            # The fourth convolution
            tf.keras.layers.Conv2D(64, (3, 3), activation="relu"),
            tf.keras.layers.MaxPooling2D(2, 2),
            # The fifth convolution
            tf.keras.layers.Conv2D(64, (3, 3), activation="relu"),
            tf.keras.layers.MaxPooling2D(2, 2),
            # Flatten the results to feed into a DNN
            tf.keras.layers.Flatten(),
            tf.keras.layers.Dropout(0.5),
            # 512 neuron hidden layer
            tf.keras.layers.Dense(512, activation="relu"),
            # Only 1 output neuron. It will contain a value from 0-1
            tf.keras.layers.Dense(class_count, activation="softmax"),
        ]
    )
    model.summary()

    model.compile(loss="categorical_crossentropy", optimizer="adam")

    model.fit(train_generator, epochs=50, steps_per_epoch=10, verbose=1)


    validation_generator.reset()
    pred = model.predict(validation_generator)

    print(pred)

    predict_classes = np.argmax(pred, axis=1)
    expected_classes = validation_generator.classes

    correct = accuracy_score(expected_classes, predict_classes)
    print(f"Accuracy: {correct}")
