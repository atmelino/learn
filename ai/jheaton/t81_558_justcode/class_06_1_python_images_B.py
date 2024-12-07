from PIL import Image
import numpy as np

w, h = 64, 64
data = np.zeros((h, w, 3), dtype=np.uint8)
# Yellow
for row in range(32):
    for col in range(32):
        data[row,col] = [255,255,0]
# Red
for row in range(32):
    for col in range(32):
        data[row+32,col] = [255,0,0]
# Green
for row in range(32):
    for col in range(32):
        data[row+32,col+32] = [0,255,0]
# Blue
for row in range(32):
    for col in range(32):
        data[row,col+32] = [0,0,255]

img = Image.fromarray(data, 'RGB')
img.save("./output/class_06_1_B.png")
