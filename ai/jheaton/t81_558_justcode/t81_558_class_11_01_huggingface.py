# HIDE OUTPUT
import tensorflow as tf
print(f"Tensor Flow Version: {tf.__version__}")
import tensorflow.keras
# print(f"Keras Version: {tensorflow.keras.__version__}")

#pip install transformers
#pip install transformers[sentencepiece]

from urllib.request import urlopen

## Sentiment Analysis

# Read sample text, a poem
URL = "https://data.heatonresearch.com/data/t81-558/"\
    "datasets/sonnet_18.txt"
f = urlopen(URL)
text = f.read().decode("utf-8")
print(text)

import pandas as pd
from transformers import pipeline

classifier = pipeline("text-classification")

outputs = classifier(text)
df=pd.DataFrame(outputs)
print(df)



# Entity Tagging
text2 = "Abraham Lincoln was a president who lived in the United States."

tagger = pipeline("ner", aggregation_strategy="simple")

outputs = tagger(text2)
df=pd.DataFrame(outputs)
print(df)


reader = pipeline("question-answering")
question = "What now shall fade?"

outputs = reader(question=question, context=text)
df=pd.DataFrame([outputs])
print(df)



