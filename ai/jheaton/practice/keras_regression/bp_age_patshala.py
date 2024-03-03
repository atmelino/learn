import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Input, Activation
import numpy as np
import pandas as pd
import os.path

# x=np.array([1,2,3,4,5,6,7,8,9])
# y=np.array([4,6,8,10,12,14,16 ,18,20])

dirname=os.path.dirname(__file__)
csvname=dirname+"/dataset/bp_age.csv"
df = pd.read_csv(csvname, na_values=['NA', '?'])
# print(df)

age = df['age'].values # regression
bp = df['trestbps'].values # regression

df3 = pd.DataFrame()
df3['bp']=pd.DataFrame(bp)
df3['age']=pd.DataFrame(age)
print(df3)

model=Sequential()
model.add(Dense(1,input_shape=(1,)))
model.compile(optimizer='sgd', loss="mean_absolute_error")
model.fit(bp,age,epochs=1000,verbose=0)

w0=model.layers[0].get_weights()[0][0]
print("weight w0=",w0)

p=model.predict(x=[10])
print(p)

# newx = [70,80,90]
newx = [83,87,90]
# newx = [1,3,8]
y_pred = model.predict(newx)
for idx in range(len(newx)):
    print(f"Input: {newx[idx]} prediction: {y_pred[idx]}")

p2=model.predict(x=[10])
print(p2)
