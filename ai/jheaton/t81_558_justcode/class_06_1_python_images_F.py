import os

do_download=False

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

cmd="mkdir -p "+ SOURCE
os.system(cmd)

cmd="mkdir -p "+ TARGET
os.system(cmd)

cmd="mkdir -p "+ EXTRACT_TARGET
os.system(cmd)

cmd="unzip -o -j -d "+SOURCE+" " +ZIPFILE+" >/dev/null "
print(cmd)

# !unzip -o -j -d {SOURCE} {os.path.join(PATH, DOWNLOAD_NAME)} >/dev/null


