from tensorflow.keras.callbacks import LambdaCallback
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import LSTM
from tensorflow.keras.optimizers import RMSprop
from tensorflow.keras.utils import get_file
import numpy as np
import random
import sys
import io
import requests
import re
import os

BASE_PATH = "../../../../local_data/jheaton/"
DATA_PATH = BASE_PATH + "class_10_3_text_generation/"
OUTPUT_PATH = BASE_PATH + "class_10_3_text_generation/"

os.system("mkdir -p " + OUTPUT_PATH)


# r = requests.get("https://data.heatonresearch.com/data/t81-558/text/treasure_island.txt")

# response = session.get('file:///path/to/your/file.txt')

filepath="file:///"+DATA_PATH+"treasure_island.txt"
print(filepath)
r = requests.get(DATA_PATH+"treasure_island.txt")
raw_text = r.text
print(raw_text[0:1000])





