import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Input, Activation
import tensorflow.keras.initializers
import numpy as np

x=np.array([1,	2,	3,	4,	5,	6,	7,	8,	9,	10,])
y=np.array([8,	16,	24,	32,	40,	48,	56,	64,	72,	80,])

x=np.array([1,2,3,4,5,6,7,8,9])
y=np.array([4,6,8,10,12,14,16,18,20])


# initializer = Constant(10.)
# values = initializer(shape=(2, 2))


k_initializer =tensorflow.keras.initializers.Constant(2.2)
b_initializer =tensorflow.keras.initializers.Constant(1.8)


model=Sequential()
# initializer = Ones()
# initializer =tensorflow.keras.initializers.Ones()
# model.add(Dense(1,input_shape=(1,), kernel_initializer="random_uniform"))
model.add(Dense(1,input_shape=(1,), kernel_initializer=k_initializer,bias_initializer=b_initializer))
model.compile(optimizer='sgd', loss="mean_absolute_error")
model.fit(x,y,epochs=300,verbose=1)

w0=model.layers[0].get_weights()[0]
b0=model.layers[0].get_weights()[1]
# print(model.layers[0].get_weights()[0])
print("weight w0=",w0,"bias b0=",b0)

p=model.predict(x=[1])
print(p)