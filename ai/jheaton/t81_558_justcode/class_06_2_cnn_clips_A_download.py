import imageio
import glob
from tqdm import tqdm
from PIL import Image
import os

print("class_06_2_cnn_A_prepare")

URL = "https://github.com/jeffheaton/data-mirror/releases/"
DOWNLOAD_SOURCE = URL+"download/v1/paperclips.zip"
print(DOWNLOAD_SOURCE)
DOWNLOAD_NAME = DOWNLOAD_SOURCE[DOWNLOAD_SOURCE.rfind('/')+1:]
PATH = "../../../../local_data/jheaton"
EXTRACT_TARGET = os.path.join(PATH,"clips")
SOURCE = os.path.join(PATH, "clips/paperclips")
TARGET = os.path.join(PATH,"clips-processed")
ZIPFILE=os.path.join(PATH, DOWNLOAD_NAME)

# 1. Step: Download the zip file
# Run the download command on the command line.
# This code will generate the command
cmd = "wget --directory-prefix="+PATH+" "+DOWNLOAD_SOURCE
print(cmd)
# os.system(cmd)
# wget --directory-prefix=../../../../local_data/jheaton https://github.com/jeffheaton/data-mirror/releases/download/v1/paperclips.zip

# 2. Step: Create the directories
cmd1="mkdir -p "+ SOURCE
cmd2="mkdir -p "+ TARGET
cmd3="mkdir -p "+ EXTRACT_TARGET

print(cmd1)
print(cmd2)
print(cmd3)

os.system(cmd1)
os.system(cmd2)
os.system(cmd3)


# 3. Step: Unzip the files 
# Run the unzip command on the command line.
# This code will generate the command
cmd="unzip -o -j -d "+SOURCE+" " +ZIPFILE+" >/dev/null "
print(cmd)
# unzip -o -j -d ../../../../local_data/jheaton/clips/paperclips ../../../../local_data/jheaton/paperclips.zip >/dev/null 

