import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Input, Activation
import tensorflow.keras.initializers
import numpy as np

choice=5
match choice:
    case 1:
        x=np.array([1,2,3,4,5,6,7,8,9])
        y=np.array([4,6,8,10,12,14,16,18,20])
        k_initializer =tensorflow.keras.initializers.Constant(2.2)
        b_initializer =tensorflow.keras.initializers.Constant(1.8)        
        xval=[3]
    case 2:
        x=np.array([1,	2,	3,	4,	5,	6,	7,	8,	9,	10,])
        y=np.array([8,	16,	24,	32,	40,	48,	56,	64,	72,	80,])
        k_initializer =tensorflow.keras.initializers.Constant(7.5)
        b_initializer =tensorflow.keras.initializers.Constant(0.2)
        xval=[3]
    case 3:
        x=np.array([82,83,85,89,92,93,95,97,98])
        y=np.array([10,15,22,31,45,47,52,61,72])
        k_initializer =tensorflow.keras.initializers.Constant(3.5)
        b_initializer =tensorflow.keras.initializers.Constant(-277)
        # k_initializer =tensorflow.keras.initializers.Constant(3.)
        # b_initializer =tensorflow.keras.initializers.Constant(-2)
        # k_initializer =tensorflow.keras.initializers.Constant(1.)
        # b_initializer =tensorflow.keras.initializers.Constant(1.)
        xval=[90]
    case 4:
        x=np.array([31,	32,	33,	34,	35,	36,	37,	38,	39,	40,])
        y=np.array([42,	44,	46,	48,	50,	52,	54,	56,	58,	60,])
        k_initializer =tensorflow.keras.initializers.Constant(2.2)
        b_initializer =tensorflow.keras.initializers.Constant(-18)
        xval=[40]
    case 5:
        x=np.array([8.27,	8.44,	8.61,	8.78,	8.95,	9.12,	9.29,	9.46,	9.63,	9.8,])
        y=np.array([12.45,	18.4,	24.35,	30.3,	36.25,	42.2,	48.15,	54.1,	60.05,	66,])
        k_initializer =tensorflow.keras.initializers.Constant(2.2)
        b_initializer =tensorflow.keras.initializers.Constant(-18)
        xval=[40]






model=Sequential()
# initializer = Ones()
# initializer =tensorflow.keras.initializers.Ones()
# model.add(Dense(1,input_shape=(1,), kernel_initializer="random_uniform"))
model.add(Dense(1,input_shape=(1,), kernel_initializer=k_initializer,bias_initializer=b_initializer))
# model.compile(optimizer='sgd', loss="mean_absolute_error")
model.compile(optimizer='Adam', loss="MeanAbsoluteError")
model.fit(x,y,epochs=30000,verbose=1)

w0=model.layers[0].get_weights()[0]
b0=model.layers[0].get_weights()[1]
# print(model.layers[0].get_weights()[0])
print("weight w0=",w0,"bias b0=",b0)

print("input=",xval, "   prediction=",model.predict(x=xval))
# p=model.predict(x=[1])
# print(p)
y_pred = model.predict(x)
for idx in range(len(x)):
    print(f"Input: {x[idx]} prediction: {y_pred[idx]}")
