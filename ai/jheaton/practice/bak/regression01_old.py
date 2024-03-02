print("Simple TensorFlow Regression: blood pressure - age")
from tensorflow.keras.models import Sequential
import os.path

from tensorflow.keras.layers import Dense, Activation
import pandas as pd
import numpy as np
from sklearn import metrics
import matplotlib.pyplot as plt

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
# print(df3)

plot=True
if plot==True:
    plt.plot(bp, age)
    plt.ylabel('age')
    plt.xlabel('blood pressure')
    plt.show()


model = Sequential()
model.add(Dense(1, input_dim=1, activation='linear'))
model.compile(loss='mse', optimizer='rmsprop',metrics='mae')
model.fit(bp,age,verbose=0,epochs=1000)


pred = model.predict(bp)
# print(f"Shape: {pred.shape}")
# print(pred[0:7])

# Measure RMSE error.  RMSE is common for regression.
score = np.sqrt(metrics.mean_squared_error(pred,age))
print(f"Final score (RMSE): {score}")

# Sample predictions
for i in range(7):
    print(f"{i+1}. blood pressure: {bp[i]}, age: {age[i]}, " 
          + f"predicted age: {pred[i]}")


