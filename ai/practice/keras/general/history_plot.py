# https://keras.io/2.18/api/datasets/boston_housing/
# https://machinelearningmastery.com/display-deep-learning-model-training-history-in-keras/
# code from AI search result "Boston Housing price regression dataset code keras"
# Requires keras version 2

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.datasets import boston_housing
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

(x_train, y_train), (x_test, y_test) = boston_housing.load_data(
    test_split=0.2, seed=113
)

scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

model = Sequential(
    [Dense(64, activation="relu", input_shape=(x_train.shape[1],)), Dense(1)]
)

model.compile(optimizer="rmsprop", loss="mse", metrics=["mae"])
# model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

model.summary()

history = model.fit(x_train, y_train, epochs=20, batch_size=1, validation_split=0.2)

test_mse_score, test_mae_score = model.evaluate(x_test, y_test)

print("test_mse_score=", test_mse_score)


# list all data in history
print(history.history.keys())

# summarize history for mae
plt.plot(history.history['mae'])
plt.plot(history.history['mae'])
plt.title('model mae')
plt.ylabel('mae')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()
# # summarize history for accuracy
# plt.plot(history.history['accuracy'])
# plt.plot(history.history['val_accuracy'])
# plt.title('model accuracy')
# plt.ylabel('accuracy')
# plt.xlabel('epoch')
# plt.legend(['train', 'test'], loc='upper left')
# plt.show()

# summarize history for loss
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()



