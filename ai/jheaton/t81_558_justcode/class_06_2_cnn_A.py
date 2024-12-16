import pandas as pd
import os
import tensorflow as tf
import keras_preprocessing
from keras_preprocessing import image
from keras_preprocessing.image import ImageDataGenerator
from tensorflow.keras.callbacks import EarlyStopping
import time

print("class_06_2_cnn_A")
# this program requires the file structure to exist, that is created by running class_06_1_python_images_F.py

# Nicely formatted time string
def hms_string(sec_elapsed):
    h = int(sec_elapsed / (60 * 60))
    m = int((sec_elapsed % (60 * 60)) / 60)
    s = sec_elapsed % 60
    return f"{h}:{m:>02}:{s:>05.2f}"

PATH = "./not_on_github"
EXTRACT_TARGET = os.path.join(PATH, "clips")
SOURCE = os.path.join(PATH, "clips/paperclips")
TARGET = os.path.join(PATH, "clips-processed")


df = pd.read_csv(os.path.join(SOURCE, "train.csv"), na_values=["NA", "?"])

df["filename"] = "clips-" + df["id"].astype(str) + ".jpg"
print(df)

TRAIN_PCT = 0.9
TRAIN_CUT = int(len(df) * TRAIN_PCT)
df_train = df[0:TRAIN_CUT]
df_validate = df[TRAIN_CUT:]
print(f"Training size: {len(df_train)}")
print(f"Validate size: {len(df_validate)}")

training_datagen = ImageDataGenerator(
    rescale=1.0 / 255, horizontal_flip=True, vertical_flip=True, fill_mode="nearest"
)

train_generator = training_datagen.flow_from_dataframe(
    dataframe=df_train,
    directory=SOURCE,
    x_col="filename",
    y_col="clip_count",
    target_size=(256, 256),
    batch_size=32,
    class_mode="other",
)
validation_datagen = ImageDataGenerator(rescale=1.0 / 255)
val_generator = validation_datagen.flow_from_dataframe(
    dataframe=df_validate,
    directory=SOURCE,
    x_col="filename",
    y_col="clip_count",
    target_size=(256, 256),
    class_mode="other",
)


model = tf.keras.models.Sequential(
    [
        # Note the input shape is the desired size of the image 150x150
        # with 3 bytes color.
        # This is the first convolution
        tf.keras.layers.Conv2D(
            64, (3, 3), activation="relu", input_shape=(256, 256, 3)
        ),
        tf.keras.layers.MaxPooling2D(2, 2),
        # The second convolution
        tf.keras.layers.Conv2D(64, (3, 3), activation="relu"),
        tf.keras.layers.MaxPooling2D(2, 2),
        tf.keras.layers.Flatten(),
        # 512 neuron hidden layer
        tf.keras.layers.Dense(512, activation="relu"),
        tf.keras.layers.Dense(1, activation="linear"),
    ]
)
model.summary()
epoch_steps = 250  # needed for 2.2
validation_steps = len(df_validate)
model.compile(loss="mean_squared_error", optimizer="adam")
monitor = EarlyStopping(
    monitor="val_loss",
    min_delta=1e-3,
    patience=10,
    verbose=1,
    mode="auto",
    restore_best_weights=True,
)
start_time = time.time()
history = model.fit(
    train_generator,
    verbose=1,
    validation_data=val_generator,
    callbacks=[monitor],
    epochs=25
)

print(history)

elapsed_time = time.time() - start_time
print("Elapsed time: {}".format(hms_string(elapsed_time)))

df_test = pd.read_csv(
    os.path.join(SOURCE,"test.csv"),
    na_values=['NA', '?'])

df_test['filename']="clips-"+df_test["id"].astype(str)+".jpg"

test_datagen = ImageDataGenerator(rescale = 1./255)

test_generator = validation_datagen.flow_from_dataframe(
    dataframe=df_test,
    directory=SOURCE,
    x_col="filename",
    batch_size=1,
    shuffle=False,
    target_size=(256, 256),
    class_mode=None)

test_generator.reset()
pred = model.predict(test_generator,steps=len(df_test))

df_submit = pd.DataFrame({'id':df_test['id'],'clip_count':pred.flatten()})
df_submit.to_csv(os.path.join(PATH,"submit.csv"),index=False)

print(df_submit)




