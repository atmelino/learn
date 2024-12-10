import pandas as pd
import os
import tensorflow as tf
import keras_preprocessing
from keras_preprocessing import image
from keras_preprocessing.image import ImageDataGenerator

print("class_06_2_cnn_A")
# this program requires the file structure to exist, that is created by running class_06_1_python_images_F.py

PATH = "./not_on_github"
EXTRACT_TARGET = os.path.join(PATH,"clips")
SOURCE = os.path.join(PATH, "clips/paperclips")
TARGET = os.path.join(PATH,"clips-processed")


df = pd.read_csv(
    os.path.join(SOURCE,"train.csv"),
    na_values=['NA', '?'])

df['filename']="clips-"+df["id"].astype(str)+".jpg"
print(df)

TRAIN_PCT = 0.9
TRAIN_CUT = int(len(df) * TRAIN_PCT)
df_train = df[0:TRAIN_CUT]
df_validate = df[TRAIN_CUT:]
print(f"Training size: {len(df_train)}")
print(f"Validate size: {len(df_validate)}")

training_datagen = ImageDataGenerator(
    rescale = 1./255,
    horizontal_flip=True,
    vertical_flip=True,
    fill_mode='nearest')

train_generator = training_datagen.flow_from_dataframe(
    dataframe=df_train,
    directory=SOURCE,
    x_col="filename",
    y_col="clip_count",
    target_size=(256, 256),
    batch_size=32,
    class_mode='other')
validation_datagen = ImageDataGenerator(rescale = 1./255)
val_generator = validation_datagen.flow_from_dataframe(
    dataframe=df_validate,
    directory=SOURCE,
    x_col="filename",
    y_col="clip_count",
    target_size=(256, 256),
    class_mode='other')




