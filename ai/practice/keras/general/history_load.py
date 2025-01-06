# Requires keras version 2

import tensorflow as tf
import pickle
import matplotlib.pyplot as plt


with open('../output/general/trainHistory.pkl', "rb") as file_pi:
    history = pickle.load(file_pi)

print(history)

# list all data in history
print(history.keys())

# summarize history for mae
plt.plot(history['mae'])
plt.plot(history['mae'])
plt.title('model mae')
plt.ylabel('mae')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()

# summarize history for loss
plt.plot(history['loss'])
plt.plot(history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()





