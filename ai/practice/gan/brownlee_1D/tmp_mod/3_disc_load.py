# Use conda jh_class environment
# https://machinelearningmastery.com/how-to-develop-a-generative-adversarial-network-for-a-1-dimensional-function-from-scratch-in-keras/

import os
from numpy.random import rand
import numpy as np
from tensorflow.keras.utils import plot_model
from numpy.random import randn
from tensorflow.keras.models import load_model
import pandas as pd
import json

float_formatter = "{:+1.3f}".format
np.set_printoptions(formatter={"float_kind": float_formatter})
os.system("mkdir -p ./output")

with open('./config/config.json') as json_data:
    d = json.load(json_data)
    print(d)

n_epochs=d['n_epochs']
n_batch=d['n_batch']
x_min=d['x_min']
x_max=d['x_max']
func_range=d['func_range']
width=x_max-x_min


# load the discriminator model
load_path = "./models"
model = load_model(os.path.join(load_path, "disc_mod.h5"))

# summarize the model
model.summary()
# plot the model
# plot_model(model, to_file='discriminator_plot.png', show_shapes=True, show_layer_names=True)


# Predict

xinput = [
    [0.2, 0.00],
    [0.2, 0.01],
    [0.2, 0.04],
    [0.2, 0.08],
    [0.2, 0.09],
]
xinput = [
    [1, 1],
    [2, 4],
    [3, 9],
    [4, 16],
    [5, 25],
]

df1s=[]
# df_xvalues=pd.DataFrame(range(0,100))
# dfs=pd.DataFrame(range(0,100),columns=["x"])
df1s=pd.DataFrame()
for i in range(0,10):
    xinput=[]
    for j in range(0,100):
        xval=i*width/2/10
        yval=j/func_range/100
        # print(xval,yval)
        xinput.append([xval,yval])
    pred = model.predict(xinput)
    df1=pd.DataFrame(pred,columns=[str(xval)])
    # print(df1)
    df1s = pd.concat([df1s, df1], axis=1)

    # dfs.append( pd.DataFrame(pred,columns=["pred"]))


xinput_np = np.array(xinput)
# print(xinput_np)
# print(xinput_np[:,[1]])
df2=pd.DataFrame(xinput_np[:,[1]],columns=["x"])
# print(df2)
# exit()
dfs = pd.concat([df2,df1s], axis=1)

pd.options.display.float_format = '{:,.3f}'.format
# print(dfs)
print(dfs.to_string(index=False))
dfs.to_csv("./output/disc.csv",index=False)


# pred=model.predict([[0.5,0.25]])
# pred = model.predict(xinput)

# inp =  pd.DataFrame(xinput)
# pred_df = pd.DataFrame(pred,columns=["pred"])
# DF = pd.concat([inp, pred_df], axis=1)
# DF.to_csv("./output/disc.csv",index=False)
# print(DF)
# print(DF.to_string())


