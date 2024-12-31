import os
import keras
from tensorflow.keras.models import load_model


print("class_06_3_resnet_load")

imagedir = "./not_on_github/clips/paperclips/"
image_size = (256, 256)

load_path = "./models"
model = load_model(os.path.join(load_path, "class_06_3_resnet.h5"))

filename="clips-30002.jpg"



test_datagen = ImageDataGenerator(rescale = 1./255)










# for keras 3 meaning tensorflow version > 2.15
# filename="clips-30002.jpg"
# img = keras.utils.load_img(imagedir + filename, target_size=image_size)
# img_array = keras.utils.img_to_array(img)
# img_array = keras.ops.expand_dims(img_array, 0)  # Create batch axis
# prediction = model.predict(img_array)
# score = float(keras.ops.sigmoid(prediction[0][0]))
# print(prediction)




exit()



