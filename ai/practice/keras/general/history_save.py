# https://keras.io/2.18/api/datasets/boston_housing/
# code from AI search result "Boston Housing price regression dataset code keras"
# Requires keras version 2

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.datasets import boston_housing
from sklearn.preprocessing import StandardScaler
import pickle

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

with open('../output/general/trainHistory.pkl', 'wb') as file_pi:
    pickle.dump(history.history, file_pi)
    
    
# np.save('my_history.npy',history.history)


