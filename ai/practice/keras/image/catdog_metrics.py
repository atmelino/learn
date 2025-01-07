# https://keras.io/examples/vision/image_classification_from_scratch/
# Requires keras version 3

import os
import pandas as pd
import keras
from tensorflow.keras.models import load_model
import tensorflow as tf

# from progressbar import ProgressBar
from progress.bar import Bar

# Options for this run
plot = False
print_in_loop = False
partial_files = False
mynfiles = 20

imagedir = "../not_on_github/PetImages"
image_size = (180, 180)

load_path = "../not_on_github/catdogsavemodel"
model = load_model(os.path.join(load_path, "catdog01.h5"))


dir_path = imagedir

filenamearray = []

dir_path = imagedir + "/Cat"
for file_path in os.listdir(dir_path):
    if os.path.isfile(os.path.join(dir_path, file_path)):
        filenamearray.append("/Cat/" + file_path)
filenamearray = sorted(filenamearray)
dir_path = imagedir + "/Dog"
for file_path in os.listdir(dir_path):
    if os.path.isfile(os.path.join(dir_path, file_path)):
        filenamearray.append("/Dog/" + file_path)
filenamearray = sorted(filenamearray)
length = len(filenamearray)
# print(len(filenamearray)," items")
# print(filenamearray)

if partial_files == True:
    nfiles = mynfiles
else:
    nfiles = length

test_images = filenamearray[0:nfiles]
names = []
predictions = []
catprobs = []
dogprobs = []

print("Total files to process: ", nfiles)
myfilename = "filename"


class SlowBar(Bar):
    message = 'Loading'

    # message = "mes %(index)d %(mymessage)s"
    suffix = "Index %(index)d ETA %(remaining_seconds)d s  File %(mymessage)s"

    @property
    def remaining_seconds(self):
        return self.eta

    @property
    def mymessage(self):
        # return "hello"
        return myfilename


# message="                    "
# bar = Bar('Processing', max=nfiles)
# bar = Bar(message, max=nfiles)
# pbar = ProgressBar(maxval=nfiles)
# pbar.start()
bar = SlowBar(max=nfiles)


for i, filename in enumerate(test_images):
    # for filename in test_images:
    # pbar.update(i)
    myfilename = filename
    bar.next()

    img = keras.utils.load_img(imagedir + filename, target_size=image_size)

    if plot == True:
        print("show cat")
        print(imagedir + filename)
        plt.imshow(img)
        plt.show()

    img_array = keras.utils.img_to_array(img)
    img_array = keras.ops.expand_dims(img_array, 0)  # Create batch axis

    prediction = model.predict(img_array, verbose=0)
    score = float(keras.ops.sigmoid(prediction[0][0]))
    catprob = 100 * (1 - score)
    dogprob = 100 * score

    if print_in_loop == True:
        # print(prediction)
        print(imagedir + filename)
        print(f"This image is {100 * (1 - score):.2f}% cat and {100 * score:.2f}% dog.")

    names.append(filename)
    predictions.append(prediction)
    catprobs.append(catprob)
    dogprobs.append(dogprob)

# print results table
# pbar.finish()
bar.finish()

results = pd.DataFrame(
    {"filename": names, "pred": predictions, "cat %": catprobs, "dog %": dogprobs}
)
filename_write = "../output/catdog.csv"
results.to_csv(filename_write, index=False)
print(results)
