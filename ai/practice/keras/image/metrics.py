import os
import pandas as pd
import keras
from tensorflow.keras.models import load_model
import tensorflow as tf

# Options for this run
plot = False

imagedir = "../not_on_github/PetImages"
image_size = (180, 180)

load_path = "../not_on_github/catdogsavemodel"
model = load_model(os.path.join(load_path, "catdog01.h5"))


dir_path=imagedir
# res = []
# for (dir_path, dir_names, file_names) in os.walk(dir_path):
#     res.extend(file_names)
# print(res)



res = []

dir_path=imagedir+"/Cat"
# Iterate directory
for file_path in os.listdir(dir_path):
    # check if current file_path is a file
    if os.path.isfile(os.path.join(dir_path, file_path)):
        # add filename to list
        res.append(file_path)
res=sorted(res)
# print(len(res))   
print(len(res)," items")
print(res)

catarray=[]
for name in res:
    catarray.append("/Cat/"+name)
print(catarray)

# exit()

test_images = catarray


# test_images = [
#     "/Cat/22.jpg",
#     "/Cat/24.jpg",
#     "/Cat/25.jpg",
#     "/Cat/648.jpg",
#     "/Cat/3279.jpg",
#     "/Cat/6779.jpg",
#     "/Dog/0.jpg",
#     "/Dog/189.jpg",
#     "/Dog/278.jpg",
#     "/Dog/1014.jpg",
# ]

# result_table = {}
names=[]
predictions=[]

for filename in test_images:
    img = keras.utils.load_img(imagedir + filename, target_size=image_size)

    if plot == True:
        print("show cat")
        print(imagedir + filename)
        plt.imshow(img)
        plt.show()

    img_array = keras.utils.img_to_array(img)
    img_array = keras.ops.expand_dims(img_array, 0)  # Create batch axis

    prediction = model.predict(img_array)
    score = float(keras.ops.sigmoid(prediction[0][0]))

    print(prediction)
    print(imagedir + filename)
    print(f"This image is {100 * (1 - score):.2f}% cat and {100 * score:.2f}% dog.")

    names.append(filename)
    predictions.append(prediction)
    # result_table.append({imagedir + filename, predictions, score})

# print results table
results = pd.DataFrame({'filename': names, 'pred': predictions})
print(results)
