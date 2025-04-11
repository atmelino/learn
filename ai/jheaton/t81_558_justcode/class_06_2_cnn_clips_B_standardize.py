import imageio
import glob
from tqdm import tqdm
from PIL import Image
import os

print("class_06_2_cnn_A_prepare")

def scale(img, scale_width, scale_height):
    # Scale the image
    img = img.resize((
    scale_width,
    scale_height),
    Image.LANCZOS)
    return img

def standardize(image): 
    rgbimg = Image.new("RGB", image.size)
    rgbimg.paste(image)
    return rgbimg

def fail_below(image, check_width, check_height):
    width, height = image.size
    assert width == check_width
    assert height == check_height

def crop_square(image):
    width, height = image.size
    # Crop the image, centered
    new_width = min(width,height)
    new_height = new_width
    left = (width - new_width)/2
    top = (height - new_height)/2
    right = (width + new_width)/2
    bottom = (height + new_height)/2
    return image.crop((left, top, right, bottom))

PATH = "./not_on_github"
SOURCE = os.path.join(PATH, "clips/paperclips")
TARGET = os.path.join(PATH,"clips-processed")

files = glob.glob(os.path.join(SOURCE,"*.jpg"))
# print(files)
for file in tqdm(files):
    try:
        target = ""
        name = os.path.basename(file)
        filename, _ = os.path.splitext(name)
        img = Image.open(file)
        img = standardize(img)
        img = crop_square(img)
        img = scale(img, 128, 128)
        #fail_below(img, 128, 128)
        target = os.path.join(TARGET,filename+".jpg")
        print(target)
        img.save(target, quality=25)
    except KeyboardInterrupt:
        print("Keyboard interrupt")
        break
    except AssertionError:
        print("Assertion")
        break
    except:
        print("Unexpected exception while processing image source: " \
        f"{file}, target: {target}" , exc_info=True)