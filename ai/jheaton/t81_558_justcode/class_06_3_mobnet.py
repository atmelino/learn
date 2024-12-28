import pandas as pd
import numpy as np
import os
import tensorflow.keras
import matplotlib.pyplot as plt
from tensorflow.keras.layers import Dense,GlobalAveragePooling2D
from tensorflow.keras.applications import MobileNet
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.mobilenet import preprocess_input
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam
from PIL import Image, ImageFile
from matplotlib.pyplot import imshow
import requests
from io import BytesIO
from IPython.display import display, HTML
from tensorflow.keras.applications.mobilenet import decode_predictions
from keras.preprocessing.image import load_img


# HIDE OUTPUT
model = MobileNet(weights='imagenet',include_top=True)

model.summary()

IMAGE_WIDTH = 224
IMAGE_HEIGHT = 224
IMAGE_CHANNELS = 3


# ROOT = "https://data.heatonresearch.com/data/t81-558/images/"
ROOT = "./not_on_github/images/"

def make_square(img):
    cols,rows = img.size
    if rows>cols:
        pad = (rows-cols)/2
        img = img.crop((pad,0,cols,cols))
    else:
        pad = (cols-rows)/2
        img = img.crop((0,pad,rows,rows))
    return img


# def classify_image(url):
#     x = []
#     ImageFile.LOAD_TRUNCATED_IMAGES = False
#     response = requests.get(url)
#     img = Image.open(BytesIO(response.content))
#     img.load()
#     img = img.resize((IMAGE_WIDTH,IMAGE_HEIGHT),Image.LANCZOS)
#     x = image.img_to_array(img)
#     x = np.expand_dims(x, axis=0)
#     x = preprocess_input(x)
#     x = x[:,:,:,:3] # maybe an alpha channel
#     pred = model.predict(x)
#     display(img)
#     print(np.argmax(pred,axis=1))
#     lst = decode_predictions(pred, top=5)
#     for itm in lst[0]:
#         print(itm)

def classify_image(path):
    x = []
    ImageFile.LOAD_TRUNCATED_IMAGES = False
    # response = requests.get(url)
    # img = Image.open(BytesIO(response.content))
    # img.load()
    img = load_img(path, target_size=(224, 224))
    img = img.resize((IMAGE_WIDTH,IMAGE_HEIGHT),Image.LANCZOS)
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    x = x[:,:,:,:3] # maybe an alpha channel
    pred = model.predict(x)
    display(img)
    print(np.argmax(pred,axis=1))
    lst = decode_predictions(pred, top=5)
    for itm in lst[0]:
        print(itm)

classify_image(ROOT+"soccer_ball.jpg")
classify_image(ROOT+"airplane.jpg")
classify_image(ROOT+"race_truck.jpg")