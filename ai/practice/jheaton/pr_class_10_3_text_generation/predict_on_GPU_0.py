# https://www.tensorflow.org/guide/gpu#using_a_single_gpu_on_a_multi-gpu_system

import tensorflow as tf
print("Simple TensorFlow Regression: MPG")
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation
import pandas as pd
import io
import os
import requests
import numpy as np
from sklearn import metrics
from tensorflow.keras.models import load_model
import random
import re
import sys

BASE_PATH = "../../../../../local_data/"
DATA_PATH = BASE_PATH + "jheaton/input/"
OUTPUT_PATH = BASE_PATH + "practice/jheaton/pr_class_10_3_text_generation/"


print("Num GPUs Available: ", len(tf.config.experimental.list_physical_devices("GPU")))

# tf.debugging.set_log_device_placement(True)
tf.debugging.set_log_device_placement(False)

try:
    # Specify the GPU device
    print('Using /device:GPU:0')
    with tf.device("/device:GPU:0"):

        # Load model
        filename_static = "pr_class_10_3_text_generation.keras"
        fullpath = f"{OUTPUT_PATH}{filename_static}"
        model = load_model(fullpath)
        model.summary()


        def sample(preds, temperature=1.0):
            # print("preds shape",preds.shape)
            np.set_printoptions(linewidth=np.inf)
            np.set_printoptions(linewidth=100)
            # np.set_printoptions(precision=3)
            np.set_printoptions(floatmode='fixed')
            np.set_printoptions(suppress=True)
            # print("sample function")
            # print("original preds",preds)
            # helper function to sample an index from a probability array
            preds = np.asarray(preds).astype("float64")
            print("np array preds\n",preds)

            # preds_logs=np.log(preds)
            # print("log preds\n",preds_logs)

            preds = np.log(preds) / temperature
            # print("log and temperature preds\n",preds)

            exp_preds = np.exp(preds)
            print("exponent preds\n",exp_preds)

            print("sum of exp preds",np.sum(exp_preds))
            preds = exp_preds / np.sum(exp_preds)


            probas = np.random.multinomial(1, preds, 1)
            index= np.argmax(probas)
            print("index",index)
            return np.argmax(probas)


        def on_epoch_end():
            # Function invoked at end of each epoch. Prints generated text.
            print("******************************************************")
            print("----- Generating text" )
            start_index = random.randint(0, len(processed_text) - maxlen - 1)
            # for temperature in [0.2, 0.5, 1.0, 1.2]:
            for temperature in [0.2, 1.0]:
                print("----- temperature:", temperature)
                generated = ""
                sentence = processed_text[start_index : start_index + maxlen]
                generated += sentence
                print('----- Generating with seed: "' + sentence + '"')
                sys.stdout.write(generated)
                sys.stdout.write('\n')
                print('----- end of seed')
                
                print('----- generated text')
                for i in range(400):
                    x_pred = np.zeros((1, maxlen, len(chars)))
                    for t, char in enumerate(sentence):
                        x_pred[0, t, char_indices[char]] = 1.0
                    preds = model.predict(x_pred, verbose=0)[0]
                    next_index = sample(preds, temperature)

                    # print(next_index)

                    next_char = indices_char[next_index]
                    generated += next_char
                    sentence = sentence[1:] + next_char
                    sys.stdout.write(next_char)
                    sys.stdout.flush()
                sys.stdout.write('\n')
                print('----- end of generated text')

            print()

        filepath=DATA_PATH+"treasure_island.txt"
        print(filepath)
        raw_text = open(filepath, 'r').read()

        processed_text = raw_text.lower()
        processed_text = re.sub(r"[^\x00-\x7f]", r"", processed_text)
        chars = sorted(list(set(processed_text)))
        print("number of different characters ", len(chars))
        print("chars", chars)

        char_indices = dict((c, i) for i, c in enumerate(chars))
        indices_char = dict((i, c) for i, c in enumerate(chars))

        maxlen = 40


        on_epoch_end()


except RuntimeError as e:
    print(e)
