import imageio
import glob
from tqdm import tqdm
from PIL import Image
import os

print("class_06_1_python_images_F")

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


do_download=False
do_mkdir=False
do_unzip=False
do_standardize=True

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
    # cmd = "wget --directory-prefix=./input "+DOWNLOAD_SOURCE
    cmd = "wget --directory-prefix="+PATH+" "+DOWNLOAD_SOURCE
    print(cmd)
    # result: wget --directory-prefix=./not_on_github https://github.com/jeffheaton/data-mirror/releases/download/v1/paperclips.zip
    # os.system(cmd)

if do_mkdir==True:
    cmd1="mkdir -p "+ SOURCE
    cmd2="mkdir -p "+ TARGET
    cmd3="mkdir -p "+ EXTRACT_TARGET

    print(cmd1)
    print(cmd2)
    print(cmd3)

    os.system(cmd1)
    os.system(cmd2)
    os.system(cmd3)

if do_unzip==True:
    cmd="unzip -o -j -d "+SOURCE+" " +ZIPFILE+" >/dev/null "
    print(cmd)
    # unzip -o -j -d ./not_on_github/clips/paperclips ./not_on_github/paperclips.zip >/dev/null 


if do_standardize==True:
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