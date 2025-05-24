# HIDE OUTPUT
import tensorflow as tf
import tensorflow.keras
from transformers import pipeline
import pandas as pd
from urllib.request import urlopen

print(f"Tensor Flow Version: {tf.__version__}")
# print(f"Keras Version: {tensorflow.keras.__version__}")

#pip install transformers
#pip install transformers[sentencepiece]


## Sentiment Analysis

# Read sample text, a poem
URL = "https://data.heatonresearch.com/data/t81-558/"\
    "datasets/sonnet_18.txt"
f = urlopen(URL)
text = f.read().decode("utf-8")
print(text)


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


translator = pipeline("translation_en_to_de",
                      model="Helsinki-NLP/opus-mt-en-de")
outputs = translator(text, clean_up_tokenization_spaces=True,
                     min_length=100)
print(outputs[0]['translation_text'])


text2 = """
An apple is an edible fruit produced by an apple tree (Malus domestica). 
Apple trees are cultivated worldwide and are the most widely grown species 
in the genus Malus. The tree originated in Central Asia, where its wild 
ancestor, Malus sieversii, is still found today. Apples have been grown 
for thousands of years in Asia and Europe and were brought to North America 
by European colonists. Apples have religious and mythological significance 
in many cultures, including Norse, Greek, and European Christian tradition.
"""
summarizer = pipeline("summarization")
outputs = summarizer(text2, max_length=45,
                     clean_up_tokenization_spaces=True)
print(outputs[0]['summary_text'])


generator = pipeline("text-generation")
outputs = generator(text, max_length=400)
print(outputs[0]['generated_text'])
