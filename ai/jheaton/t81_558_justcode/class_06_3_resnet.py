import pandas as pd
import os
import tensorflow as tf
import keras_preprocessing
from keras_preprocessing import image
from keras_preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications.resnet50 import ResNet50
from tensorflow.keras.layers import Input
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D
from tensorflow.keras.models import Model
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.metrics import RootMeanSquaredError


print("class_06_3_resnet")
# this program requires the file structure to exist, that is created by running class_06_2_cnn_A_prepare.py

PATH = "./not_on_github"
SOURCE = os.path.join(PATH, "clips/paperclips")
# TARGET = os.path.join(PATH, "clips-processed")

df_train = pd.read_csv(os.path.join(SOURCE, "train.csv"))
df_train["filename"] = "clips-" + df_train.id.astype(str) + ".jpg"
print(df_train)

TRAIN_PCT = 0.9
TRAIN_CUT = int(len(df_train) * TRAIN_PCT)
df_train_cut = df_train[0:TRAIN_CUT]
df_validate_cut = df_train[TRAIN_CUT:]
print(f"Training size: {len(df_train_cut)}")
print(f"Validate size: {len(df_validate_cut)}")

WIDTH = 256
HEIGHT = 256

training_datagen = ImageDataGenerator(
    rescale=1.0 / 255,
    horizontal_flip=True,
    # vertical_flip=True,
    fill_mode="nearest",
)

train_generator = training_datagen.flow_from_dataframe(
    dataframe=df_train_cut,
    directory=SOURCE,
    x_col="filename",
    y_col="clip_count",
    target_size=(HEIGHT, WIDTH),
    # Keeping the training batch size small
    # USUALLY increases performance
    batch_size=32,
    class_mode="raw",
)

validation_datagen = ImageDataGenerator(rescale=1.0 / 255)

val_generator = validation_datagen.flow_from_dataframe(
    dataframe=df_validate_cut,
    directory=SOURCE,
    x_col="filename",
    y_col="clip_count",
    target_size=(HEIGHT, WIDTH),
    # Make the validation batch size as large as you
    # have memory for
    batch_size=256,
    class_mode="raw",
)


input_tensor = Input(shape=(HEIGHT, WIDTH, 3))
base_model = ResNet50(
    include_top=False, weights=None, input_tensor=input_tensor, input_shape=None
)

x = base_model.output
x = GlobalAveragePooling2D()(x)
x = Dense(1024, activation="relu")(x)
x = Dense(1024, activation="relu")(x)
model = Model(inputs=base_model.input, outputs=Dense(1)(x))


# Important, calculate a valid step size for the validation dataset
STEP_SIZE_VALID = val_generator.n // val_generator.batch_size

model.compile(
    loss="mean_squared_error",
    optimizer="adam",
    metrics=[RootMeanSquaredError(name="rmse")],
)

monitor = EarlyStopping(
    monitor="val_loss",
    min_delta=1e-3,
    patience=50,
    verbose=1,
    mode="auto",
    restore_best_weights=True,
)

history = model.fit(
    train_generator,
    epochs=100,
    steps_per_epoch=250,
    validation_data=val_generator,
    callbacks=[monitor],
    verbose=1,
    validation_steps=STEP_SIZE_VALID,
)

# save entire network to HDF5 (save everything, suggested)
model.save("./models/class_06_3_resnet.h5")
model.save("./models/class_06_3_resnet.keras")
