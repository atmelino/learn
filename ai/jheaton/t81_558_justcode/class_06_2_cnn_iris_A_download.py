import os

do_download=True
do_mkdir=True
do_unzip=True


URL = "https://github.com/jeffheaton/data-mirror/releases/"
DOWNLOAD_SOURCE = URL+"download/v1/iris-image.zip"
print(DOWNLOAD_SOURCE)
DOWNLOAD_NAME = DOWNLOAD_SOURCE[DOWNLOAD_SOURCE.rfind('/')+1:]

BASE_PATH = "../../../../local_data/jheaton"
EXTRACT_TARGET = os.path.join(BASE_PATH,"iris")
SOURCE = EXTRACT_TARGET # In this case its the same, no subfolder
ZIPFILE=os.path.join(BASE_PATH, DOWNLOAD_NAME)

if do_download==True:
    # cmd = "wget --directory-prefix=./input "+DOWNLOAD_SOURCE
    cmd = "wget --directory-prefix="+BASE_PATH+" "+DOWNLOAD_SOURCE
    print(cmd)
    # result: wget --directory-prefix=./not_on_github https://github.com/jeffheaton/data-mirror/releases/download/v1/iris-image.zip
    # os.system(cmd)

if do_mkdir==True:
    cmd1="mkdir -p "+ SOURCE
    print(cmd1)
    os.system(cmd1)

if do_unzip==True:
    cmd="unzip -o -d "+SOURCE+" " +ZIPFILE+" >/dev/null "
    print(cmd)
    # unzip -o -d ./not_on_github/iris ./not_on_github/iris-image.zip >/dev/null 



