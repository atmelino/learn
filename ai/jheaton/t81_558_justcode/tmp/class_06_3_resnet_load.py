# requires keras 2 meaning tensorflow version <= 2.15 

import os
import keras
from tensorflow.keras.models import load_model
from keras_preprocessing.image import ImageDataGenerator


print("class_06_3_resnet_load")

PATH = "./not_on_github"
SOURCE = os.path.join(PATH, "clips/paperclips")

imagedir = "./not_on_github/clips/paperclips/"
image_size = (256, 256)

load_path = "./models"
model = load_model(os.path.join(load_path, "class_06_3_resnet.h5"))

filename="clips-30002.jpg"

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
df_submit.to_csv(os.path.join(PATH,"class_06_3_resnet_load.csv"),index=False)

print(df_submit)









# for keras 3 meaning tensorflow version > 2.15
# filename="clips-30002.jpg"
# img = keras.utils.load_img(imagedir + filename, target_size=image_size)
# img_array = keras.utils.img_to_array(img)
# img_array = keras.ops.expand_dims(img_array, 0)  # Create batch axis
# prediction = model.predict(img_array)
# score = float(keras.ops.sigmoid(prediction[0][0]))
# print(prediction)




exit()



