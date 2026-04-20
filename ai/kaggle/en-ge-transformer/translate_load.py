# https://www.kaggle.com/code/lonnieqin/english-spanish-translation-transformer
# conda activate jh_class

import pandas as pd
import tensorflow as tf
from tensorflow.keras.layers import TextVectorization
import pathlib
import random
import string
import re
import numpy as np
from tensorflow import keras
from tensorflow.keras import layers
import sklearn
import os
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import load_model

print(f"Tensorflow Version:{tf.__version__}")

BASE_PATH = "../../../../local_data/kaggle/"
DATA_PATH = BASE_PATH + "en-ge-transformer/"
OUTPUT_PATH = BASE_PATH + "en-ge-transformer/"
os.system("mkdir -p " + OUTPUT_PATH)


class Config:
    vocab_size = 16000  # Vocabulary Size
    sequence_length = 20
    batch_size = 512
    validation_split = 0.15
    embed_dim = 256
    latent_dim = 256
    num_heads = 4

config = Config()

class PositionalEmbedding(layers.Layer):
    def __init__(self, sequence_length, vocab_size, embed_dim, **kwargs):
        super(PositionalEmbedding, self).__init__(**kwargs)
        self.token_embeddings = layers.Embedding(
            input_dim=vocab_size, output_dim=embed_dim, mask_zero=True
        )
        self.position_embeddings = layers.Embedding(
            input_dim=sequence_length, output_dim=embed_dim, mask_zero=True
        )
        self.sequence_length = sequence_length
        self.vocab_size = vocab_size
        self.embed_dim = embed_dim

    def call(self, inputs):
        length = tf.shape(inputs)[-1]
        positions = tf.range(start=0, limit=length, delta=1)
        embedded_tokens = self.token_embeddings(inputs)
        embedded_positions = self.position_embeddings(positions)
        return embedded_tokens + embedded_positions

    def compute_mask(self, inputs, mask=None):
        return tf.math.not_equal(inputs, 0)

class TransformerEncoder(layers.Layer):
    def __init__(self, embed_dim, num_heads, ff_dim, rate=0.1, **kwargs):
        super(TransformerEncoder, self).__init__(**kwargs)
        self.att = keras.layers.MultiHeadAttention(
            num_heads=num_heads, key_dim=embed_dim
        )
        self.ffn = keras.Sequential(
            [
                keras.layers.Dense(ff_dim, activation="relu"),
                keras.layers.Dense(embed_dim),
            ]
        )
        self.layernorm1 = keras.layers.LayerNormalization(epsilon=1e-6)
        self.layernorm2 = keras.layers.LayerNormalization(epsilon=1e-6)
        self.dropout1 = keras.layers.Dropout(rate)
        self.dropout2 = keras.layers.Dropout(rate)

    def call(self, inputs, training=False):
        attn_output = self.att(inputs, inputs)
        attn_output = self.dropout1(attn_output, training=training)
        out1 = self.layernorm1(inputs + attn_output)
        ffn_output = self.ffn(out1)
        ffn_output = self.dropout2(ffn_output, training=training)
        return self.layernorm2(out1 + ffn_output)


class TransformerDecoder(layers.Layer):
    def __init__(self, embed_dim, latent_dim, num_heads, **kwargs):
        super(TransformerDecoder, self).__init__(**kwargs)
        self.embed_dim = embed_dim
        self.latent_dim = latent_dim
        self.num_heads = num_heads
        self.attention_1 = layers.MultiHeadAttention(
            num_heads=num_heads, key_dim=embed_dim
        )
        self.attention_2 = layers.MultiHeadAttention(
            num_heads=num_heads, key_dim=embed_dim
        )
        self.dense_proj = keras.Sequential(
            [
                layers.Dense(latent_dim, activation="relu"),
                layers.Dense(embed_dim),
            ]
        )
        self.layernorm_1 = layers.LayerNormalization()
        self.layernorm_2 = layers.LayerNormalization()
        self.layernorm_3 = layers.LayerNormalization()
        self.supports_masking = True

    def call(self, inputs, encoder_outputs, mask=None):
        causal_mask = self.get_causal_attention_mask(inputs)
        if mask != None:
            padding_mask = tf.cast(mask[:, tf.newaxis, :], dtype="int32")
            padding_mask = tf.minimum(padding_mask, causal_mask)
        attention_output_1 = self.attention_1(
            query=inputs, value=inputs, key=inputs, attention_mask=causal_mask
        )

        out_1 = self.layernorm_1(inputs + attention_output_1)

        attention_output_2 = self.attention_2(
            query=out_1,
            value=encoder_outputs,
            key=encoder_outputs,
            attention_mask=padding_mask,
        )

        out_2 = self.layernorm_2(out_1 + attention_output_2)

        proj_output = self.dense_proj(out_2)
        out = self.layernorm_3(out_2 + proj_output)

        return out

    def get_causal_attention_mask(self, inputs):
        input_shape = tf.shape(inputs)
        batch_size, sequence_length = input_shape[0], input_shape[1]
        i = tf.range(sequence_length)[:, tf.newaxis]
        j = tf.range(sequence_length)
        mask = tf.cast(i >= j, dtype="int32")
        mask = tf.reshape(mask, (1, input_shape[1], input_shape[1]))
        mult = tf.concat(
            [tf.expand_dims(batch_size, -1), tf.constant([1, 1], dtype=tf.int32)],
            axis=0,
        )
        return tf.tile(mask, mult)

checkpoint_filepath = OUTPUT_PATH + "translate_fit.keras"
print("loading transformer model from",checkpoint_filepath)
transformer = load_model(
    checkpoint_filepath,
    custom_objects={
        "PositionalEmbedding": PositionalEmbedding,
        "TransformerEncoder": TransformerEncoder,
        "TransformerDecoder": TransformerDecoder,
    }
)

print(transformer.summary())


# extract german vocabulary from data file 
data_file=DATA_PATH + "data.csv"
data = pd.read_csv(data_file)
print("data file=",data_file)
print("shape of data",data.shape)
print(data.head())
print(data.iloc[51089])
data["german"] = data["german"].apply(lambda item: "[start] " + item + " [end]")
print(data.head())
strip_chars = string.punctuation + "¿"
strip_chars = strip_chars.replace("[", "").replace("]", "")
print(strip_chars)


def german_standardize(input_string):
    lowercase = tf.strings.lower(input_string)
    return tf.strings.regex_replace(lowercase, "[%s]" % re.escape(strip_chars), "")

english_vectorization = TextVectorization(
    max_tokens=config.vocab_size,
    output_mode="int",
    output_sequence_length=config.sequence_length,
)
german_vectorization = TextVectorization(
    max_tokens=config.vocab_size,
    output_mode="int",
    output_sequence_length=config.sequence_length + 1,
    standardize=german_standardize,
)
print("Starting adapt german")
english_vectorization.adapt(list(data["english"]))
german_vectorization.adapt(list(data["german"]))
print("adapt complete")

english_vocab = english_vectorization.get_vocabulary()
# print(english_vocab)
print("length of english_vocab",len(english_vocab))

def write_list(filename, data):
    content = '\n'.join(str(item) for item in data)    
    with open(filename, 'w') as file:
        file.write(content)

# write_list("english_vocab.txt", english_vocab)

# Encode the prompt
prompt_data_file=DATA_PATH + "data_short.csv"
prompt_data = pd.read_csv(prompt_data_file)
print("prompt data file=",prompt_data_file)
print("shape of prompt data",prompt_data.shape)
print(prompt_data.head())


# Translation
german_vocab = german_vectorization.get_vocabulary()
# print(german_vocab)
print("length of german_vocab",len(german_vocab))
german_index_lookup = dict(zip(range(len(german_vocab)), german_vocab))

def remove_start_and_end_token(sentence):
    return sentence.replace("[start] ", "").replace(" [end]", "")

def decode_sequence(transformer, input_sentence):
    tokenized_input_sentence = english_vectorization([input_sentence])
    decoded_sentence = "[start]"
    for i in range(config.sequence_length):
        tokenized_target_sentence = german_vectorization([decoded_sentence])[:, :-1]
        predictions = transformer([tokenized_input_sentence, tokenized_target_sentence])

        sampled_token_index = np.argmax(predictions[0, i, :])
        sampled_token = german_index_lookup[sampled_token_index]
        decoded_sentence += " " + sampled_token

        if sampled_token == "[end]":
            break
    return remove_start_and_end_token(decoded_sentence)


start_index=0
end_index=10
# for i in np.random.choice(len(data), 10):
for i in range(start_index, end_index):
    item = prompt_data.iloc[i]
    translated = decode_sequence(transformer, item["english"])
    print("English   :", remove_start_and_end_token(item["english"]))
    print("german   :", remove_start_and_end_token(item["german"]))
    print("Translated:", translated)

