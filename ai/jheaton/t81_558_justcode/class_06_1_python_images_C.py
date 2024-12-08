from PIL import Image, ImageFile
import numpy as np
from matplotlib.pyplot import imshow
import requests
from io import BytesIO

# %matplotlib inline
url = "https://data.heatonresearch.com/images/jupyter/brookings.jpeg"
response = requests.get(url,headers={'User-Agent': 'Mozilla/5.0'})
img = Image.open(BytesIO(response.content))
img.load()
img_array = np.asarray(img)
rows = img_array.shape[0]
cols = img_array.shape[1]
print("Rows: {}, Cols: {}".format(rows,cols))
# Create new image
img2_array = np.zeros((rows, cols, 3), dtype=np.uint8)
for row in range(rows):
    for col in range(cols):
        t = np.mean(img_array[row,col])
        img2_array[row,col] = [t,t,t]
img2 = Image.fromarray(img2_array, 'RGB')
img2.save("./output/class_06_1_B2.png")
