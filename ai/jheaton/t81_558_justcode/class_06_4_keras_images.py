import os
import urllib.request
import shutil
from IPython.display import Image
from PIL import Image, ImageFile
import matplotlib.pyplot as plt
import keras
from numpy import expand_dims
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.preprocessing.image import ImageDataGenerator
from matplotlib import pyplot
import matplotlib.pyplot as plt
import numpy as np
import matplotlib

print("class_06_4_keras_images")

# URL = "https://github.com/jeffheaton/t81_558_deep_learning/blob/master/photos/landscape.jpg?raw=true"

BASE_PATH = "../../../../local_data/jheaton"
DATA_PATH = os.path.join(BASE_PATH, "images")
OUTPUT_PATH = os.path.join(BASE_PATH, "class_06_4_keras_images")
os.system("mkdir -p " + OUTPUT_PATH)
LOCAL_IMG_FILE = DATA_PATH+"/landscape.jpg"

show_original = False
plot_grid = True


def show_image():
    img = keras.utils.load_img(LOCAL_IMG_FILE)
    plt.imshow(img)
    plt.show()
    plt.savefig(OUTPUT_PATH + "/class_06_4_keras_images_original.png")


if show_original == True:
    show_image()


def analyze_image(img_file):
    # Load the requested image
    img = load_img(img_file)
    print("img")
    print(img)

    data = img_to_array(img)
    print("data")
    print("data.shape", data.shape)
    print(data)

    print("data[0]")
    print("data[0].shape", data[0].shape)
    print(data[0])
    print("data[1]")
    print("data[1].shape", data[1].shape)
    print(data[1])
    print("data[0][0]")
    print("data[0][0].shape", data[0][0].shape)
    print(data[0][0])
    print("data[0][1]")
    print("data[0][1].shape", data[0][1].shape)
    print(data[0][1])
    print(data[0][1][2])


# analyze_image(LOCAL_IMG_FILE)


def modify_image(img_file):
    # Load the requested image
    img = load_img(img_file)
    print("img")
    print(img)

    img_array0 = np.asarray(img)
    img_array = img_array0.copy()
    print("img_array")
    print("img_array.shape", img_array.shape)
    # print(img_array)

    img2 = Image.fromarray(img_array, "RGB")
    img2.save(OUTPUT_PATH + "/class_06_4_keras_images_fromarray.png")

    for row in range(0, 100):
        for col in range(0, 100):
            img_array[col][row] = [112, 25, 10]

    img2 = Image.fromarray(img_array, "RGB")
    img2.save(OUTPUT_PATH + "/class_06_4_keras_images_fromarray_mod.png")


# modify_image(LOCAL_IMG_FILE)


# exit()


def visualize_generator(img_file, gen, name):
    # Load the requested image
    img = load_img(img_file)
    data = img_to_array(img)
    samples = expand_dims(data, 0)
    # print("samples")
    # print(samples.shape)
    # print(samples)

    # Generate augumentations from the generator
    it = gen.flow(samples, batch_size=1)
    # it = gen.flow(samples, batch_size=1, seed=442)
    images = []
    for i in range(4):
        batch = it.next()
        image = batch[0].astype("uint8")
        images.append(image)

    images = np.array(images)
    # print("images array")
    # print("images array shape", images.shape)
    # print(images)

    # for i in range(4):
    #     img3 = Image.fromarray(images[i], "RGB")
    #     img3.save("./output/class_06_4_keras_images_gen_0" + str(i) + ".png")

    # Create a grid of 4 images from the generator
    index, height, width, channels = images.shape
    nrows = index // 2
    grid = (
        images.reshape(nrows, 2, height, width, channels)
        .swapaxes(1, 2)
        .reshape(height * nrows, width * 2, 3)
    )

    if plot_grid == True:
        fig = plt.figure(figsize=(10.0, 10.0))
        plt.axis("off")
        plt.imshow(grid)
        # plt.show()
        fig.savefig(OUTPUT_PATH + "/class_06_4_keras_images_" + name + ".png")


visualize_generator(
    LOCAL_IMG_FILE,
    ImageDataGenerator(horizontal_flip=True, vertical_flip=True),
    name="flip",
)

visualize_generator(
    LOCAL_IMG_FILE,
    ImageDataGenerator(height_shift_range=[-200, 200], fill_mode="nearest"),
    name="shift",
)
visualize_generator(
    LOCAL_IMG_FILE,
    ImageDataGenerator(width_shift_range=[-200, 200], fill_mode="nearest"),
    name="shift",
)

visualize_generator(
    LOCAL_IMG_FILE,
    ImageDataGenerator(brightness_range=[0.2, 1]),
    name="bright",
)

visualize_generator(
    LOCAL_IMG_FILE,
    ImageDataGenerator(shear_range=30),
    name="shear",
)

visualize_generator(
    LOCAL_IMG_FILE,
    ImageDataGenerator(rotation_range=30),
    name="rotate",
)
