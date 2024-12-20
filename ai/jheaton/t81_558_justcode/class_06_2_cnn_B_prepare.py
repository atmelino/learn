import os



do_download=False
do_mkdir=False


URL = "https://github.com/jeffheaton/data-mirror/releases/"
DOWNLOAD_SOURCE = URL+"download/v1/iris-image.zip"
print(DOWNLOAD_SOURCE)
DOWNLOAD_NAME = DOWNLOAD_SOURCE[DOWNLOAD_SOURCE.rfind('/')+1:]

PATH = "./not_on_github"
EXTRACT_TARGET = os.path.join(PATH,"iris")
SOURCE = EXTRACT_TARGET # In this case its the same, no subfolder
ZIPFILE=os.path.join(PATH, DOWNLOAD_NAME)


if do_download==True:
    # cmd = "wget --directory-prefix=./input "+DOWNLOAD_SOURCE
    cmd = "wget --directory-prefix="+PATH+" "+DOWNLOAD_SOURCE
    print(cmd)
    # result: wget --directory-prefix=./not_on_github https://github.com/jeffheaton/data-mirror/releases/download/v1/paperclips.zip
    # os.system(cmd)


if do_mkdir==True:
    cmd1="mkdir -p "+ SOURCE

    print(cmd1)

    os.system(cmd1)

