import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Input, Activation
import numpy as np
import matplotlib.pyplot as plt

x=np.array([1,2,3,4,5,6,7,8,9])
y=np.array([4,6,8,10,12,14,16 ,18,20])

plot=True
if plot==True:
    plt.plot(x, y)
    plt.ylabel('x')
    plt.xlabel('y')
    plt.show()

model=Sequential()
model.add(Dense(1,input_shape=(1,)))
model.compile(optimizer='sgd', loss="mean_absolute_error")
model.fit(x,y,epochs=100)
p=model.predict(x=[10])
print(p)

newx = [1,2,3,10]
y_pred = model.predict(newx)
for idx in range(len(newx)):
    print(f"Input: {x[idx]} prediction: {y_pred[idx]}")

p2=model.predict(x=[10])
print(p2)


def plot_data(x_data, y_data, x, y, title=None):
    plt.figure(figsize=(15,5))
    plt.scatter(x_data, y_data, label='Ground Truth', color='green', alpha=0.5)
    plt.plot(x, y, color='k', label='Model Predictions')
    plt.xlim([3,9])
    plt.ylim([0,60])
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(title)
    plt.grid(True)
    plt.legend()
    plt.show()

plot=False
if plot==True:
    plot_data(X_test, y_test, x, y, title='Test Dataset')
