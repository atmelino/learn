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
import pandas as pd

BASE_PATH = "../../../../local_data/jheaton/"
DATA_PATH = BASE_PATH + "class_10_3_text_generation/"
OUTPUT_PATH = BASE_PATH + "class_10_3_text_generation/"

os.system("mkdir -p " + OUTPUT_PATH)


r = requests.get("https://data.heatonresearch.com/data/t81-558/text/treasure_island.txt")
raw_text = r.text
# print("raw text\n",raw_text[0:100])

# filepath=DATA_PATH+"treasure_island.txt"
# print(filepath)
# raw_text = open(filepath, 'r').read()
# print(raw_text[0:1000])


processed_text = raw_text.lower()
print("lowered text\n",processed_text[:100])
processed_text = re.sub(r'[^\x00-\x7f]',r'', processed_text)
# print("non ASCII removed\n",processed_text[:100])
# print('corpus length:', len(processed_text))
# print("set of text\n",set(processed_text))
chars = sorted(list(set(processed_text)))
# print("sorted list of set of text\n",chars)
print('total chars:', len(chars))

char_indices = dict((c, i) for i, c in enumerate(chars))
indices_char = dict((i, c) for i, c in enumerate(chars))

print("char_indices\n",char_indices)
# print("indices_char\n",indices_char)


# cut the text in semi-redundant sequences of maxlen characters
maxlen = 40
step = 3
sentences = []
next_chars = []
for i in range(0, len(processed_text) - maxlen, step):
    sentences.append(processed_text[i: i + maxlen])
    next_chars.append(processed_text[i + maxlen])
print('nb sequences:', len(sentences))
# for sentence in sentences[:20]:
#     print(sentence)

df_sentences = pd.DataFrame(sentences,columns=['x_train'])
# print(df_sentences)
df_next_chars= pd.DataFrame(next_chars,columns=['y'])
# print(df_next_chars)
df_combined = pd.concat([df_sentences,df_next_chars], axis=1)
print(df_combined)

print('Vectorization...')
x = np.zeros((len(sentences), maxlen, len(chars)), dtype=bool)
print(x.shape)
y = np.zeros((len(sentences), len(chars)), dtype=bool)
for i, sentence in enumerate(sentences):
    for t, char in enumerate(sentence):
        x[i, t, char_indices[char]] = 1
    y[i, char_indices[next_chars[i]]] = 1

print(x)







