# requires keras 2 meaning tensorflow version <= 2.15 

import pandas as pd
import os
from keras_preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import load_model

print("class_06_3_resnet_load")

BASE_PATH = "../../../../local_data/jheaton"
DATA_PATH = os.path.join(BASE_PATH, "clips/paperclips")
OUTPUT_PATH = os.path.join(BASE_PATH, "class_06_3_resnet")

validation_datagen = ImageDataGenerator(rescale=1.0 / 255)

model = load_model(os.path.join(OUTPUT_PATH, "class_06_3_resnet.h5"))

df_test = pd.read_csv(
    os.path.join(DATA_PATH,"test.csv"),
    na_values=['NA', '?'])

df_test['filename']="clips-"+df_test["id"].astype(str)+".jpg"

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
df_submit.to_csv(os.path.join(OUTPUT_PATH,"class_06_3_resnet.csv"),index=False)

print(df_submit)

