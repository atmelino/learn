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

# bp = df['trestbps'].values # regression
# age = df['age'].values # regression

# bp=np.array([1,2,3,4,5,6,7,8,9])
# age=np.array([4,6,8,10,12,14,16 ,18,20])

bp=np.array([82,83,85,89,92,93,95,97,98])
age=np.array([10,15,22,31,45,47,52,61,72])

bp=np.array([1,	2,	3,	4,	5,	6,	7,	8,	9,	10,])
age=np.array([8,	16,	24,	32,	40,	48,	56,	64,	72,	80,])

bp=np.array([1,	2,	3,	4,	5,	6,	7,	8,	9,	10,])
age=np.array([4,	6,	8,	10,	12,	14,	16,	18,	20,	22,])

bp=np.array([1,	2,	3,	4,	5,	6,	7,	8,	9,	10,])
age=np.array([4.5,	6.5,	8.5,	10.5,	12.5,	14.5,	16.5,	18.5,	20.5,	22.5,])

bp=np.array([1,	2,	3,	4,	5,	6,	7,	8,	9,	10,])
age=np.array([5,	7,	9,	11,	13,	15,	17,	19,	21,	23,])

bp=np.array([1,	2,	3,	4,	5,	6,	7,	8,	9,	10,])
age=np.array([12,	14,	16,	18,	20,	22,	24,	26,	28,	30,])

bp=np.array([1,	2,	3,	4,	5,	6,	7,	8,	9,	10])
age=np.array([-4,	-3,	-2,	-1,	0,	1,	2,	3,	4,	5])




df3 = pd.DataFrame()
df3['bp']=pd.DataFrame(bp)
df3['age']=pd.DataFrame(age)
# print(df3)

model=Sequential()
model.add(Dense(1,input_shape=(1,)))
model.compile(optimizer='sgd', loss="mean_absolute_error")
model.fit(bp,age,epochs=5000,verbose=1)

w0=model.layers[0].get_weights()[0]
b0=model.layers[0].get_weights()[1]
# print(model.layers[0].get_weights()[0])
print("weight w0=",w0,"bias b0=",b0)

# p=model.predict(x=[10])
# print(p)

y_pred = model.predict(bp)
for idx in range(len(bp)):
    print(f"Input: {bp[idx]} prediction: {y_pred[idx]}")


