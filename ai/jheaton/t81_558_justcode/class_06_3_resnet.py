import pandas as pd
import os
import tensorflow as tf
import keras_preprocessing
from keras_preprocessing import image
from keras_preprocessing.image import ImageDataGenerator


print("class_06_3_resnet")
# this program requires the file structure to exist, that is created by running class_06_2_cnn_A_prepare.py

PATH = "./not_on_github"
EXTRACT_TARGET = os.path.join(PATH, "clips")
SOURCE = os.path.join(PATH, "clips/paperclips")
TARGET = os.path.join(PATH, "clips-processed")

df_train = pd.read_csv(os.path.join(SOURCE, "train.csv"))
df_train['filename'] = "clips-" + df_train.id.astype(str) + ".jpg"
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
    rescale = 1./255,
    horizontal_flip=True,
    #vertical_flip=True,
    fill_mode='nearest')

train_generator = training_datagen.flow_from_dataframe(
    dataframe=df_train_cut,
    directory=SOURCE,
    x_col="filename",
    y_col="clip_count",
    target_size=(HEIGHT, WIDTH),
    # Keeping the training batch size small
    # USUALLY increases performance
    batch_size=32,
    class_mode='raw')

validation_datagen = ImageDataGenerator(rescale = 1./255)

val_generator = validation_datagen.flow_from_dataframe(
    dataframe=df_validate_cut,
    directory=SOURCE,
    x_col="filename",
    y_col="clip_count",
    target_size=(HEIGHT, WIDTH),
    # Make the validation batch size as large as you
    # have memory for
    batch_size=256,
    class_mode='raw')




