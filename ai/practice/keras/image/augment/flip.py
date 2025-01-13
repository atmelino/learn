# https://www.analyticsvidhya.com/blog/2020/08/image-augmentation-on-the-fly-using-keras-imagedatagenerator/

import keras
from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing.image import load_img
from numpy import expand_dims
import matplotlib.pyplot as plt


ncols=8
LOCAL_IMG_FILE = "../../not_on_github/images/landscape.jpg"

img = keras.utils.load_img(LOCAL_IMG_FILE)

img = expand_dims(img, 0)

# ImageDataGenerator flipping
datagen = ImageDataGenerator(horizontal_flip=True, vertical_flip=True)

# iterator
aug_iter = datagen.flow(img, batch_size=1, seed=442)

# generate samples and plot
fig, ax = plt.subplots(nrows=1, ncols=ncols, figsize=(15,15))

# generate batch of images
for i in range(ncols):

	# convert to unsigned integers
	image = next(aug_iter)[0].astype('uint8')
 
	# plot image
	ax[i].imshow(image)
	ax[i].axis('off')

plt.show()