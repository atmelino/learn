import keras
import tensorflow as tf

image_size = (180, 180)

img = keras.utils.load_img("6779.jpg", target_size=image_size)
img_array = keras.utils.img_to_array(img)
# img_array = keras.ops.expand_dims(img_array, 0)  # Create batch axis
img_array = tf.expand_dims(img_array, 0)  # Create batch axis


# score = float(keras.ops.sigmoid(predictions[0][0]))
score = float(tf.keras.activations.sigmoid(0.345))



