import os
import pandas as pd

# PATH = "/kaggle/input/applications-of-deep-learning-wustlspring-2023/beach/beach/"
# !conda install -y -c conda-forge keras-preprocessing

BASE_PATH = "../../../../../local_data/jheaton/"
DATA_PATH = os.path.join(BASE_PATH, "beach/beach/")
OUTPUT_PATH = os.path.join(BASE_PATH, "kaggle/simple_beach_count/")
os.system("mkdir -p " + OUTPUT_PATH)

# df = pd.read_csv(os.path.join(PATH, "train.csv"),na_values=['NA', '?'])
df = pd.read_csv(DATA_PATH+ "train.csv", na_values=["NA", "?"])
print(df)


TRAIN_PCT = 0.9
TRAIN_CUT = int(len(df) * TRAIN_PCT)

df_train = df[0:TRAIN_CUT]
df_validate = df[TRAIN_CUT:]

print(f"Training size: {len(df_train)}")
print(f"Validate size: {len(df_validate)}")

import tensorflow as tf
import keras_preprocessing
from keras_preprocessing import image
from keras_preprocessing.image import ImageDataGenerator

training_datagen = ImageDataGenerator(
  rescale = 1./255,
  horizontal_flip=True,
  vertical_flip=True,
  fill_mode='nearest')

train_generator = training_datagen.flow_from_dataframe(
        dataframe=df_train,
        directory=DATA_PATH,
        x_col="filename",
        y_col="count",
        target_size=(256, 256),
        batch_size=32,
        class_mode='other')

validation_datagen = ImageDataGenerator(rescale = 1./255)

val_generator = validation_datagen.flow_from_dataframe(
        dataframe=df_validate,
        directory=DATA_PATH,
        x_col="filename",
        y_col="count",
        target_size=(256, 256),
        class_mode='other')

from tensorflow.keras.callbacks import EarlyStopping

model = tf.keras.models.Sequential([
    # Note the input shape is the desired size of the image 150x150 with 3 bytes color
    # This is the first convolution
    tf.keras.layers.Conv2D(64, (3,3), activation='relu', input_shape=(256, 256, 3)),
    tf.keras.layers.MaxPooling2D(2, 2),
    # The second convolution
    tf.keras.layers.Conv2D(64, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),
    tf.keras.layers.Flatten(),
    # 512 neuron hidden layer
    tf.keras.layers.Dense(512, activation='relu'),
    tf.keras.layers.Dense(1, activation='linear')
])


model.summary()
epoch_steps = 250 # needed for 2.2
validation_steps = len(df_validate)
model.compile(loss = 'mean_squared_error', optimizer='adam')
monitor = EarlyStopping(monitor='val_loss', min_delta=1e-3, patience=5, verbose=1, mode='auto',
        restore_best_weights=True)
history = model.fit(train_generator,  
  verbose = 1, 
  validation_data=val_generator, callbacks=[monitor], epochs=1)


# save entire network to HDF5 (save everything, suggested)
print("Saving model to ",OUTPUT_PATH+"/simple_beach_count.h5")
model.save(OUTPUT_PATH+"/simple_beach_count.h5")
model.save(OUTPUT_PATH+"/simple_beach_count.keras")

# Generate Submission File
# df_test = pd.read_csv(os.path.join(PATH,"test.csv"),na_values=['NA', '?'])
df_test = pd.read_csv(DATA_PATH+ "test.csv",na_values=['NA', '?'])

test_datagen = ImageDataGenerator(rescale = 1./255)

test_generator = validation_datagen.flow_from_dataframe(
        dataframe=df_test,
        directory=DATA_PATH,
        x_col="filename",
        batch_size=1,
        shuffle=False,
        target_size=(256, 256),
        class_mode=None)

test_generator.reset()
pred = model.predict(test_generator,steps=len(df_test))

df_submit = pd.DataFrame({'id':df_test['id'],'clip_count':pred.flatten()})
# df_submit.to_csv("/kaggle/working/submit.csv",index=False)
df_submit.to_csv(OUTPUT_PATH+"submit.csv",index=False)






