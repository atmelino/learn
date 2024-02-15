# HIDE OUTPUT
import tensorflow as tf
print(f"Tensor Flow Version: {tf.__version__}")
import tensorflow.keras
# print(f"Keras Version: {tensorflow.keras.__version__}")

#pip install transformers
#pip install transformers[sentencepiece]

from urllib.request import urlopen

# Read sample text, a poem
URL = "https://data.heatonresearch.com/data/t81-558/"\
    "datasets/sonnet_18.txt"
f = urlopen(URL)
text = f.read().decode("utf-8")
print(text)

# HIDE OUTPUT
import pandas as pd
from transformers import pipeline

classifier = pipeline("text-classification")


outputs = classifier(text)
df=pd.DataFrame(outputs)
print(df)