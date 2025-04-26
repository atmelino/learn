# Use conda deoldify environment
print("conda environment for this program:")
print("conda activate deoldify")

import sys

sys.path.insert(0, "../../../../local_data//DeOldify")
# sys.path.insert(0, "../../../../local_data//stylegan3")
# NOTE: This must be the first call in order to work properly!
from deoldify import device
from deoldify.device_id import DeviceId

# choices: CPU, GPU0...GPU7
device.set(device=DeviceId.GPU0)
import fastai
from deoldify.visualize import *
import warnings
from urllib.parse import urlparse
import os


print("class_07_4_deoldify")

outputdir = "../../../../local_data/jheaton/class_07_4_deoldify"
os.makedirs(outputdir, exist_ok=True)


warnings.filterwarnings(
    "ignore", category=UserWarning, message=".*?Your .*? set is empty.*?"
)

before_file = "../../../../local_data/jheaton/images/scooby_family.jpg"


RENDER_FACTOR = 35
WATERMARK = False
colorizer = get_image_colorizer(artistic=True)
# The file ColorizeArtistic_gen.pth needs to be in the models subdirectory of the directory this program is run from.
# attempts to point to a different location have been unsuccessful so far.

# model_path = "../../../../local_data/jheaton/models/ColorizeArtistic_gen.pth"
# colorizer = get_image_colorizer(artistic=True, weights_path=model_path)
# colorizer = get_image_colorizer(artistic=True, root_folder =root_path)


after_image = colorizer.get_transformed_image(
    before_file, render_factor=RENDER_FACTOR, watermarked=WATERMARK
)

after_image.save(outputdir + "/class_07_4_deoldify.png")

# print("Starting image:")
