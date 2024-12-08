import imageio
import glob
from tqdm import tqdm
from PIL import Image
import os

print("class_06_1_python_images_F")

do_download=False
do_fileops=False

URL = "https://github.com/jeffheaton/data-mirror/releases/"
#DOWNLOAD_SOURCE = URL+"download/v1/iris-image.zip"
DOWNLOAD_SOURCE = URL+"download/v1/paperclips.zip"
print(DOWNLOAD_SOURCE)
DOWNLOAD_NAME = DOWNLOAD_SOURCE[DOWNLOAD_SOURCE.rfind('/')+1:]

PATH = "./not_on_github"
EXTRACT_TARGET = os.path.join(PATH,"clips")
SOURCE = os.path.join(PATH, "clips/paperclips")
TARGET = os.path.join(PATH,"clips-processed")
ZIPFILE=os.path.join(PATH, DOWNLOAD_NAME)

if do_download==True:
    cmd = "wget --directory-prefix=./input "+DOWNLOAD_SOURCE
    os.system(cmd)

if do_fileops==True:
    cmd="mkdir -p "+ SOURCE
    os.system(cmd)

    cmd="mkdir -p "+ TARGET
    os.system(cmd)

    cmd="mkdir -p "+ EXTRACT_TARGET
    os.system(cmd)

    cmd="unzip -o -j -d "+SOURCE+" " +ZIPFILE+" >/dev/null "
    print(cmd)



import imageio
import glob
from tqdm import tqdm
from PIL import Image
import os
def scale(img, scale_width, scale_height):
    # Scale the image
    img = img.resize((
    scale_width,
    scale_height),
    Image.ANTIALIAS)
    return img

def standardize(image):
    rgbimg = Image.new("RGB", image.size)
    rgbimg.paste(image)
    return rgbimg

def fail_below(image, check_width, check_height):
    width, height = image.size
    assert width == check_width
    assert height == check_height

files = glob.glob(os.path.join(SOURCE,"*.jpg"))
print(files)



# for file in tqdm(files):
#     try:
#         target = ""
#         name = os.path.basename(file)
#         filename, _ = os.path.splitext(name)
#         img = Image.open(file)
#         img = standardize(img)
#         img = crop_square(img)
#         img = scale(img, 128, 128)
#         #fail_below(img, 128, 128)
#         target = os.path.join(TARGET,filename+".jpg")
#         img.save(target, quality=25)
#     except KeyboardInterrupt:
#         print("Keyboard interrupt")
#         break
#     except AssertionError:
#         print("Assertion")
#         break
#     except:
#         print("Unexpected exception while processing image source: " \
#         f"{file}, target: {target}" , exc_info=True)