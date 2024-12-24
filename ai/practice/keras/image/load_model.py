import os
import pandas
import keras
from tensorflow.keras.models import load_model
import tensorflow as tf

# Options for this run
plot = False

imagedir = "../not_on_github/PetImages"
image_size = (180, 180)

load_path = "../not_on_github/catdogsavemodel"
model = load_model(os.path.join(load_path, "catdog01.h5"))

test_images = [
    "/Cat/22.jpg",
    "/Cat/24.jpg",
    "/Cat/25.jpg",
    "/Cat/648.jpg",
    "/Dog/0.jpg",
    "/Cat/6779.jpg",
    "/Dog/189.jpg",
]

result_table = []

for filename in test_images:
    img = keras.utils.load_img(imagedir + filename, target_size=image_size)

    if plot == True:
        print("show cat")
        print(imagedir + filename)
        plt.imshow(img)
        plt.show()

    img_array = keras.utils.img_to_array(img)
    img_array = keras.ops.expand_dims(img_array, 0)  # Create batch axis

    predictions = model.predict(img_array)
    score = float(keras.ops.sigmoid(predictions[0][0]))

    print(predictions)
    print(imagedir + filename)
    print(f"This image is {100 * (1 - score):.2f}% cat and {100 * score:.2f}% dog.")

    result_table.append(imagedir + filename, predictions, score)
