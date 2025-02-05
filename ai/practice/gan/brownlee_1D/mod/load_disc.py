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

float_formatter = "{:+1.5f}".format
np.set_printoptions(formatter={"float_kind": float_formatter})
os.system("mkdir -p ./output")

with open('./config/config.json') as json_data:
    d = json.load(json_data)
    print(d)

print(d['selected'])
name=d['selected']
config=d[name]
print(config)

n_epochs=config['n_epochs']
n_batch=config['n_batch']
x_min=config['x_min']
x_max=config['x_max']
func_range=config['func_range']
random_real=config['random_real']
width=x_max-x_min

# load the discriminator model
load_path = "./models"
model = load_model(os.path.join(load_path, "discriminator.h5"))

# summarize the model
model.summary()
# plot the model
# plot_model(model, to_file='discriminator_plot.png', show_shapes=True, show_layer_names=True)


# Predict
pred_dfs=pd.DataFrame()
for i in range(0,10):
    xinput=[]
    for j in range(0,100):
        xval=i*width/2/10
        yval=j/func_range/100
        # print(xval,yval)
        xinput.append([xval,yval])
    pred = model.predict(xinput)
    pred_df=pd.DataFrame(pred,columns=[str(xval)])
    pred_dfs = pd.concat([pred_dfs, pred_df], axis=1)


xinput_np = np.array(xinput)
firstcol=pd.DataFrame(xinput_np[:,[1]],columns=["x"])
pred_dfs = pd.concat([firstcol,pred_dfs], axis=1)

print(pred_dfs.to_string(index=False))
pred_dfs.to_csv("./output/disc.csv",index=False)



