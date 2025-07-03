import tensorflow_datasets as tfds
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import logging, os
import matplotlib.pyplot as plt
import time

logging.basicConfig(level=logging.INFO)
# logging.basicConfig(level=logging.DEBUG)

BASE_PATH = "../../../../local_data/jheaton/"
DATA_PATH = "../../../../local_data/tfds/"
OUTPUT_PATH = BASE_PATH+"class_09_2_keras_xfer_cv/"
os.system("mkdir -p " + OUTPUT_PATH)

(train_ds, validation_ds), metadata= tfds.load(
    "cats_vs_dogs",
    data_dir=DATA_PATH,
    split=["train[:40%]", "train[40%:50%]"],
    with_info=True,
    as_supervised=True, 
)# Include labels

num_train = tf.data.experimental.cardinality(train_ds)
num_test = tf.data.experimental.cardinality(validation_ds)
print(f"Number of training samples: {num_train}")
print(f"Number of validation samples: {num_test}")
print("train_ds",train_ds)

fig = plt.figure(figsize=(10, 10))
for i, (image, label) in enumerate(train_ds.take(9)):
    ax = plt.subplot(3, 3, i + 1)
    plt.imshow(image)
    plt.title(int(label))
    plt.axis("off")
filename = OUTPUT_PATH + "plot_01.png"
fig.savefig(filename)
plt.close(fig)

size = (150, 150)
# train_ds = train_ds.map(lambda x, y: (tf.image.resize(x, size)/ 255.0, y))
# validation_ds = validation_ds.map(lambda x, y: (tf.image.resize(x, size)/ 255.0, y))
train_ds = train_ds.map(lambda x, y: (tf.image.resize(x, size), y))
validation_ds = validation_ds.map(lambda x, y: (tf.image.resize(x, size), y))

num_train = tf.data.experimental.cardinality(train_ds)
num_test = tf.data.experimental.cardinality(validation_ds)
print(f"Number of training samples: {num_train}")
print(f"Number of validation samples: {num_test}")
print("train_ds",train_ds)

fig = plt.figure(figsize=(10, 10))
for i, (image, label) in enumerate(train_ds.take(9)):
    ax = plt.subplot(3, 3, i + 1)
    plt.imshow(image)
    plt.title(int(label))
    plt.axis("off")
filename = OUTPUT_PATH + "plot_02.png"
fig.savefig(filename)
plt.close(fig)

batch_size = 32
train_ds = train_ds.cache().batch(batch_size).prefetch(buffer_size=10)
validation_ds = validation_ds.cache() \
.batch(batch_size).prefetch(buffer_size=10)

import matplotlib.pyplot as plt

fig = plt.figure(figsize=(10, 10))
for i, (image, label) in enumerate(train_ds.take(9)):
    ax = plt.subplot(3, 3, i + 1)
    plt.imshow(image[i])
    # plt.imshow((image * 255).astype(np.uint8))
    plt.title(int(label[i]))
    plt.axis("off")
filename = OUTPUT_PATH + "plot_03.png"
fig.savefig(filename)
plt.close(fig)


data_augmentation = keras.Sequential(
    [layers.RandomFlip("horizontal"), layers.RandomRotation(0.1),]
)

import numpy as np
for images, labels in train_ds.take(1):
    fig = plt.figure(figsize=(10, 10))
    # first_image = images[0]*255.0
    first_image = images[0]
    # print("first_image.shape=",first_image.shape)
    for i in range(9):
        ax = plt.subplot(3, 3, i + 1)
        augmented_image = data_augmentation(
            tf.expand_dims(first_image, 0), training=True
        )
        # print("augmented_image.shape=",augmented_image.shape)
        plt.imshow(augmented_image[0].numpy().astype("int32"))
        plt.title(int(labels[0]))
        plt.axis("off")
    filename = OUTPUT_PATH + "plot_04.png"
    fig.savefig(filename)
    plt.close(fig)

base_model = keras.applications.Xception(
    weights="imagenet", # Load weights pre-trained on ImageNet.
    input_shape=(150, 150, 3),
    include_top=False,
) # Do not include the ImageNet classifier at the top.

# Freeze the base_model
base_model.trainable = False

# Create new model on top
inputs = keras.Input(shape=(150, 150, 3))
x = data_augmentation(inputs) # Apply random data augmentation

# Pre-trained Xception weights requires that input be scaled
# from (0, 255) to a range of (-1., +1.), the rescaling layer
# outputs: `(inputs * scale) + offset`
scale_layer = keras.layers.Rescaling(scale=1 / 127.5, offset=-1)
x = scale_layer(x)

# The base model contains batchnorm layers.
# We want to keep them in inference mode
# when we unfreeze the base model for fine-tuning,
# so we make sure that the
# base_model is running in inference mode here.
x = base_model(x, training=False)
x = keras.layers.GlobalAveragePooling2D()(x)
x = keras.layers.Dropout(0.2)(x) # Regularize with dropout
outputs = keras.layers.Dense(1)(x)
model = keras.Model(inputs, outputs)

model.summary()

model.compile(
    optimizer=keras.optimizers.Adam(),
    loss=keras.losses.BinaryCrossentropy(from_logits=True),
    metrics=[keras.metrics.BinaryAccuracy()],
)
epochs = 1
model.fit(train_ds, epochs=epochs, validation_data=validation_ds)

timestr = time.strftime("%Y%m%d-%H%M%S")
# filename = f"acc_{score:.3f}_date_{timestr}.h5"
filename = f"epochs_{epochs:.3f}_date_{timestr}.h5"
fullpath = f"{OUTPUT_PATH}{filename}"
print("Saving model to ", filename)
model.save(fullpath)



# Predict

test_ds, ds_info = tfds.load(
        "cats_vs_dogs",
        data_dir=DATA_PATH,
        split='train',
        with_info=True,
)
print(test_ds)


size = (150, 150)
train_ds = train_ds.map(lambda x, y: (tf.image.resize(x, size), y))
print(test_ds)


batch_size = 32
test_ds = test_ds.cache().batch(batch_size).prefetch(buffer_size=10)
print(test_ds)



# test_ds= tfds.load(
#     "cats_vs_dogs",
#     data_dir=DATA_PATH,
#     # split=["train[:40%]", "train[40%:50%]"],
#     with_info=True,
# )# Include labels


# pred = model.predict(test_ds)
pred = model.predict(train_ds)

print(pred)