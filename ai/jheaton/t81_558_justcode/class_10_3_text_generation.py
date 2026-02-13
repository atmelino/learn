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


r = requests.get("https://data.heatonresearch.com/data/t81-558/text/treasure_island.txt")
raw_text = r.text
print("raw text\n",raw_text[0:100])

# filepath=DATA_PATH+"treasure_island.txt"
# print(filepath)
# raw_text = open(filepath, 'r').read()
# print(raw_text[0:1000])


processed_text = raw_text.lower()
print("lowered text\n",processed_text[:100])
processed_text = re.sub(r'[^\x00-\x7f]',r'', processed_text)
print("non ASCII removed\n",processed_text[:100])
print('corpus length:', len(processed_text))
print("set of text\n",set(processed_text))
chars = sorted(list(set(processed_text)))
print("sorted list of set of text\n",chars)
print('total chars:', len(chars))

char_indices = dict((c, i) for i, c in enumerate(chars))
indices_char = dict((i, c) for i, c in enumerate(chars))

print("char_indices\n",char_indices)
print("indices_char\n",indices_char)
