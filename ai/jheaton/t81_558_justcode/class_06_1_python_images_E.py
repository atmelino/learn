from PIL import Image, ImageFile
import numpy as np
from matplotlib.pyplot import imshow
import requests
from io import BytesIO

def add_noise(a):
    a2 = a.copy()
    rows = a2.shape[0]
    cols = a2.shape[1]
    s = int(min(rows,cols)/20) # size of spot is 1/20 of smallest dimension
    for i in range(100):
        x = np.random.randint(cols-s)
        y = np.random.randint(rows-s)
        a2[y:(y+s),x:(x+s)] = 0
    return a2

url = "https://data.heatonresearch.com/images/jupyter/brookings.jpeg"
response = requests.get(url,headers={'User-Agent': 'Mozilla/5.0'})
img = Image.open(BytesIO(response.content))
img.load()
img_array = np.asarray(img)
rows = img_array.shape[0]
cols = img_array.shape[1]
print("Rows: {}, Cols: {}".format(rows,cols))
# Create new image
img2_array = img_array.astype(np.uint8)
print(img2_array.shape)
img2_array = add_noise(img2_array)
img2 = Image.fromarray(img2_array, 'RGB')
img2.save("./output/class_06_1_E.png")
