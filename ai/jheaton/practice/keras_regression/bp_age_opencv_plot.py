print("Simple TensorFlow Regression: blood pressure - age")
import numpy as np
import os.path
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Input, Activation
import tensorflow as tf
import pandas as pd
from sklearn import metrics
import matplotlib.pyplot as plt

SEED_VALUE = 42

# Fix seed to make training deterministic.
np.random.seed(SEED_VALUE)
tf.random.set_seed(SEED_VALUE)


dirname=os.path.dirname(__file__)
csvname=dirname+"/dataset/bp_age.csv"
df = pd.read_csv(csvname, na_values=['NA', '?'])
# print(df)

age = df['age'].values # regression
bp = df['trestbps'].values # regression
# print(age)
# print(bp)

# df2 = pd.DataFrame(bp,age)
# print(df2)

df3 = pd.DataFrame()
df3['bp']=pd.DataFrame(bp)
df3['age']=pd.DataFrame(age)
print(df3)

plot=False
if plot==True:
    plt.plot(bp, age)
    plt.ylabel('age')
    plt.xlabel('blood pressure')
    plt.show()



model = Sequential()

# Define the model consisting of a single neuron.
model.add(Dense(units=1, input_shape=(1,)))

# Display a summary of the model architecture.
model.summary()

model.compile(optimizer=tf.keras.optimizers.RMSprop(learning_rate=0.005), loss="mse")

history = model.fit(
    bp,
    age,
    batch_size=5,
    epochs=100,
    # epochs=10,
    validation_split=0.3,
    verbose=0
)

def plot_loss(history):
    print("calling plot of history")
    plt.figure(figsize=(20,5))
    plt.plot(history.history['loss'], 'g', label='Training Loss')
    plt.plot(history.history['val_loss'], 'b', label='Validation Loss')
    # plt.xlim([0, 100])
    # plt.ylim([0, 300])
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.legend()
    plt.grid(True)
    plt.show()

plot=False
if plot==True:
    plot_loss(history)

# Generate feature data that spans the range of interest for the independent variable.
x = np.linspace(60, 120, 10)

# Use the model to predict the dependent variable.
y = model.predict(x)
def plot_data(x_data, y_data, x, y, title=None):

    plt.figure(figsize=(15,5))
    plt.scatter(x_data, y_data, label='Ground Truth', color='green', alpha=0.5)
    plt.plot(x, y, color='k', label='Model Predictions')
    plt.xlim([3,9])
    plt.ylim([0,60])
    plt.xlabel('Average Number of Rooms')
    plt.ylabel('Price [$K]')
    plt.title(title)
    plt.grid(True)
    plt.legend()
    plt.show()

plot=False
if plot==True:
    plot_data(X_test_1d, y_test, x, y, title='Test Dataset')



# Predict the median price of a home with [3, 4, 5, 6, 7] rooms.
x = [80,90,100]
y_pred = model.predict(x)
for idx in range(len(x)):
    print(f"Predicted age of a person with {x[idx]} blood pressure: {y_pred[idx]}")





# model = Sequential()
# model.add(Dense(1, input_dim=1, activation='linear'))
# model.compile(loss='mse', optimizer='rmsprop',metrics='mae')
# model.fit(bp,age,verbose=0,epochs=1000)


# pred = model.predict(bp)
# print(f"Shape: {pred.shape}")
# print(pred[0:7])

# Measure RMSE error.  RMSE is common for regression.
# score = np.sqrt(metrics.mean_squared_error(pred,age))
# print(f"Final score (RMSE): {score}")

# Sample predictions
# for i in range(7):
#     print(f"{i+1}. blood pressure: {bp[i]}, age: {age[i]}, " 
#           + f"predicted age: {pred[i]}")


