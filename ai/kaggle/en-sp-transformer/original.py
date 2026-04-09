# https://www.kaggle.com/code/lonnieqin/english-spanish-translation-transformer


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
print(f"Tensorflow Version:{tf.__version__}")

BASE_PATH = "../../../../local_data/kaggle/"
DATA_PATH = BASE_PATH + "en-sp-transformer/"
OUTPUT_PATH = BASE_PATH + "en-sp-transformer/"

os.system("mkdir -p " + OUTPUT_PATH)


class Config:
    vocab_size = 16000 # Vocabulary Size
    sequence_length = 20
    batch_size = 512
    validation_split = 0.15
    embed_dim = 256
    latent_dim = 256
    num_heads = 4
    # epochs = 30 # Number of Epochs to train
    epochs = 1 # Number of Epochs to train
    # is_training = False
    is_training = True
config = Config()

# data = pd.read_csv("/kaggle/input/englishspanish-translation-dataset/data.csv")
data = pd.read_csv(DATA_PATH+"data.csv")
print(data.head())

data["spanish"] = data["spanish"].apply(lambda item: "[start] " + item + " [end]")
print(data.head())

strip_chars = string.punctuation + "¿"
strip_chars = strip_chars.replace("[", "").replace("]", "")
print(strip_chars)

def spanish_standardize(input_string):
    lowercase = tf.strings.lower(input_string)
    return tf.strings.regex_replace(lowercase, "[%s]"%re.escape(strip_chars), "")
english_vectorization = TextVectorization(
    max_tokens=config.vocab_size, 
    output_mode="int", 
    output_sequence_length=config.sequence_length,
)
spanish_vectorization = TextVectorization(
    max_tokens=config.vocab_size,
    output_mode="int",
    output_sequence_length=config.sequence_length + 1,
    standardize=spanish_standardize,
)
print("Starting adapt")
english_vectorization.adapt(list(data["english"]))
spanish_vectorization.adapt(list(data["spanish"]))
print("adapt complete")

def preprocess(english, spanish):
    english = english_vectorization(english)
    spanish = spanish_vectorization(spanish)
    return ({"encoder_inputs": english, "decoder_inputs": spanish[:, :-1]}, spanish[:, 1:])
def make_dataset(df, batch_size, mode):
    dataset = tf.data.Dataset.from_tensor_slices((list(df["english"]), list(df["spanish"])))
    if mode == "train":
       dataset = dataset.shuffle(batch_size * 4) 
    dataset = dataset.batch(batch_size)
    dataset = dataset.map(preprocess)
    dataset = dataset.prefetch(tf.data.AUTOTUNE).cache()
    return dataset

train, valid = train_test_split(data, test_size=config.validation_split, random_state=42)
print(train.shape, valid.shape)

train_ds = make_dataset(train, batch_size=config.batch_size, mode="train")
valid_ds = make_dataset(valid, batch_size=config.batch_size, mode="valid")

for batch in train_ds.take(1):
    print(batch)

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


class PositionalEmbedding(layers.Layer):
    def __init__(self, sequence_length, vocab_size, embed_dim, **kwargs):
        super(PositionalEmbedding, self).__init__(**kwargs)
        self.token_embeddings = layers.Embedding(
            input_dim=vocab_size, 
            output_dim=embed_dim,
            mask_zero=True
        )
        self.position_embeddings = layers.Embedding(
            input_dim=sequence_length, 
            output_dim=embed_dim,
            mask_zero=True
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

class TransformerDecoder(layers.Layer):
    def __init__(self, embed_dim, latent_dim, num_heads, **kwargs):
        super(TransformerDecoder, self).__init__(**kwargs)
        self.embed_dim = embed_dim
        self.latent_dim = latent_dim
        self.num_heads = num_heads
        self.attention_1 = layers.MultiHeadAttention(
            num_heads=num_heads,
            key_dim=embed_dim
        )
        self.attention_2 = layers.MultiHeadAttention(
            num_heads=num_heads,
            key_dim=embed_dim
        )
        self.dense_proj = keras.Sequential([
            layers.Dense(latent_dim, activation="relu"),
            layers.Dense(embed_dim),
        ])
        self.layernorm_1 = layers.LayerNormalization()
        self.layernorm_2 = layers.LayerNormalization()
        self.layernorm_3 = layers.LayerNormalization()
        self.supports_masking = True
        
    def call(self, inputs, encoder_outputs, mask = None):
        causal_mask = self.get_causal_attention_mask(inputs)
        if mask != None:
            padding_mask = tf.cast(mask[:, tf.newaxis, :], dtype="int32")
            padding_mask = tf.minimum(padding_mask, causal_mask)
        attention_output_1 = self.attention_1(
            query=inputs, 
            value=inputs, 
            key=inputs, 
            attention_mask=causal_mask
        )
        
        out_1 = self.layernorm_1(inputs + attention_output_1)
        
        attention_output_2 = self.attention_2(
            query=out_1, 
            value=encoder_outputs, 
            key=encoder_outputs, 
            attention_mask=padding_mask
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
            axis=0
        )
        return tf.tile(mask, mult)


def edit_distance(y_true, y_pred):
    y_true = tf.cast(y_true, tf.int32)
    y_pred = tf.argmax(y_pred, axis=-1, output_type=y_true.dtype)
    y_true_tensor =  tf.sparse.from_dense(
        y_true
    )
    y_pred_tensor = tf.sparse.from_dense(
        y_pred
    )
    metric = 1 - tf.edit_distance(y_true_tensor, y_pred_tensor, normalize=True)
    return metric

def get_transformer(config):
    encoder_inputs = keras.Input(shape=(None,), dtype="int64", name="encoder_inputs")
    x = PositionalEmbedding(config.sequence_length, config.vocab_size, config.embed_dim)(encoder_inputs)
    encoder_outputs = TransformerEncoder(config.embed_dim, config.num_heads, config.latent_dim)(x)
    encoder = keras.Model(encoder_inputs, encoder_outputs)

    decoder_inputs = keras.Input(shape=(None,), dtype="int64", name="decoder_inputs")
    encoded_seq_inputs = keras.Input(shape=(None, config.embed_dim), name="decoder_state_inputs")
    x = PositionalEmbedding(config.sequence_length, config.vocab_size, config.embed_dim)(decoder_inputs)
    x = TransformerDecoder(config.embed_dim, config.latent_dim, config.num_heads)(x, encoded_seq_inputs)
    x = layers.Dropout(0.5)(x)
    decoder_outputs = layers.Dense(config.vocab_size, activation="softmax")(x)
    decoder = keras.Model([decoder_inputs, encoded_seq_inputs], decoder_outputs)

    decoder_outputs = decoder([decoder_inputs, encoder_outputs])
    transformer = keras.Model(
        [encoder_inputs, decoder_inputs], decoder_outputs, name="transformer"
    )
    transformer.compile(
        "adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"]
    )
    return transformer

transformer = get_transformer(config)
transformer.summary()
keras.utils.plot_model(transformer, show_shapes=True)


class LossAndErrorPrintingCallback(tf.keras.callbacks.Callback):
    def on_epoch_end(self, epoch, logs=None):
        # print(f"The average loss for epoch {epoch} is {logs['loss']:.7f} "
        #       f"and mean absolute error is {logs['mean_absolute_error']:.7f}.")
        print(f"\nend of epoch {epoch}, loss= {logs['loss']:.7f} ")
# Usage in model.fit
# model.fit(x_train, y_train, epochs=2, verbose=0, 
#           callbacks=[LossAndErrorPrintingCallback()])   

if config.is_training:
    checkpoints = tf.keras.callbacks.ModelCheckpoint(
        filepath=OUTPUT_PATH+"model.tf", 
        monitor="val_accuracy", 
        mode="max", 
        save_best_only=True,
    )
    early_stop = tf.keras.callbacks.EarlyStopping(
        patience=10,
        monitor="val_loss",
        mode="min",
        restore_best_weights=True
    )
    transformer.fit(train_ds, epochs=config.epochs, validation_data=valid_ds, callbacks=[checkpoints, early_stop,LossAndErrorPrintingCallback()])
    transformer.load_weights(OUTPUT_PATH+"model.tf")
else:
    # transformer.load_weights("../input/english-spanish-translation-transformer-model/model.tf")
    transformer.load_weights(OUTPUT_PATH+"model.tf")
















