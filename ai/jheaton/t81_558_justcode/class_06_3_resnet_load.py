import os
import keras
from tensorflow.keras.models import load_model


print("class_06_3_resnet_load")

imagedir = "./not_on_github/clips/paperclips"
image_size = (256, 256)

load_path = "./models"
model = load_model(os.path.join(load_path, "class_06_3_resnet.h5"))

filename="clips-30002.jpg"


img = keras.utils.load_img(imagedir + filename, target_size=image_size)


exit()



