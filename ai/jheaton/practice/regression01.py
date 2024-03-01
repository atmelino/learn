print("Simple TensorFlow Regression: blood pressure - age")
from tensorflow.keras.models import Sequential
import os.path

from tensorflow.keras.layers import Dense, Activation
import pandas as pd
import numpy as np
from sklearn import metrics
import matplotlib.pyplot as plt

# df = pd.read_csv("./jheaton/practice/dataset/heart.csv", na_values=['NA', '?'])
# df = pd.read_csv("./jheaton/practice/dataset/bp_age.csv", na_values=['NA', '?'])
# print(df)


dirname=os.path.dirname(__file__)
csvname=dirname+"/dataset/bp_age.csv"
df = pd.read_csv(csvname, na_values=['NA', '?'])
print(df)



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

# plt.plot(bp, age)
# plt.show()


model = Sequential()
model.add(Dense(1, input_dim=1, activation='linear'))
model.compile(loss='mse', optimizer='rmsprop',metrics='mae')
model.fit(bp,age,verbose=0,epochs=100)

pred = model.predict(age)
print(pred[0:10])

score = np.sqrt(metrics.mean_squared_error(pred,bp))
print(f"Final score (RMSE): {score}")



