import os
import keras
from tensorflow.keras.models import load_model
import tensorflow as tf

imagedir="../not_on_github/PetImages"
image_size = (180, 180)


load_path = "../not_on_github/catdogsavemodel"
model = load_model(os.path.join(load_path,"catdog01.h5"))


img = keras.utils.load_img(imagedir+"/Cat/6779.jpg", target_size=image_size)

img_array = keras.utils.img_to_array(img)
# img_array = keras.ops.expand_dims(img_array, 0)  # Create batch axis
img_array = tf.expand_dims(img_array, 0)  # Create batch axis

predictions = model.predict(img_array)
print(predictions)
