import pandas as pd
import os
from keras_preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import load_model

print("class_06_2_cnn_clips_D_load")

BASE_PATH = "../../../../local_data/jheaton"
SOURCE = os.path.join(BASE_PATH, "clips/paperclips")

validation_datagen = ImageDataGenerator(rescale=1.0 / 255)

model_path = os.path.join(BASE_PATH, "models")
model = load_model(model_path+"/class_06_2_cnn_clips_C_fit.h5")

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

submit_path = os.path.join(BASE_PATH, "class_06_2_cnn_clips")
df_submit = pd.DataFrame({'id':df_test['id'],'clip_count':pred.flatten()})
df_submit.to_csv(os.path.join(submit_path+"/class_06_2_cnn_clips_D_load.csv"),index=False)

print(df_submit)

