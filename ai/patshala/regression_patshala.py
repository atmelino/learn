import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Input, Activation

import numpy as np


x=np.array([1,2,3,4,5,6,7,8,9])
y=np.array([4,6,8,10,12,14,16 ,18,20])

model=Sequential()
model.add(Dense(1,input_shape=(1,)))
model.compile(optimizer='sgd', loss="mean_absolute_error")
model.fit(x,y,epochs=100)
p=model.predict(x=[10])
print(p)