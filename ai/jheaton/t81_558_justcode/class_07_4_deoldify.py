import sys
sys.path.insert(0, "./not_on_github/DeOldify")
#NOTE: This must be the first call in order to work properly!
from deoldify import device
from deoldify.device_id import DeviceId
#choices: CPU, GPU0...GPU7
device.set(device=DeviceId.GPU0)
import fastai
from deoldify.visualize import *
import warnings
from urllib.parse import urlparse
import os


warnings.filterwarnings("ignore", category=UserWarning,message=".*?Your .*? set is empty.*?")

# URL = 'https://raw.githubusercontent.com/jeffheaton/t81_558_deep_learning/master/photos/scooby_family.jpg'
# !wget {URL}
# URL ='./not_on_github/images/scooby_family.jpg'
# a = urlparse(URL)
# before_file = os.path.basename(a.path)
# print(before_file)

before_file ='./not_on_github/images/scooby_family.jpg'


RENDER_FACTOR = 35
WATERMARK = False
model_path = "./not_on_github/models/ColorizeArtistic_gen.pth"
root_path="./not_on_github/"
colorizer = get_image_colorizer(artistic=True)
# colorizer = get_image_colorizer(artistic=True, weights_path=model_path)
# colorizer = get_image_colorizer(artistic=True, root_folder =root_path)

 
after_image = colorizer.get_transformed_image(
    before_file, 
    render_factor=RENDER_FACTOR,
    watermarked=WATERMARK
)

after_image.save("./output/class_07_4_deoldify.png")

#print("Starting image:")






