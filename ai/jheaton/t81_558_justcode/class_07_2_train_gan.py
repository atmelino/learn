from os import listdir
from os.path import isfile, join
import os
from PIL import Image
from tqdm.notebook import tqdm
IMAGE_PATH = 'not_on_github/class_07_2_train_gan/data/gan/images/dogs'
files = [f for f in listdir(IMAGE_PATH) if isfile(join(IMAGE_PATH, f))]
base_size = None
for file in tqdm(files):
    file2 = os.path.join(IMAGE_PATH,file)
    img = Image.open(file2)
    sz = img.size
    if base_size and sz!=base_size:
        print(f"Inconsistant size: {file2}")
    elif img.mode!='RGB':
        print(f"Inconsistant color format: {file2}")
    else:
        base_size = sz