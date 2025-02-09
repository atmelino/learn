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
import pprint
import tables as tb
from termcolor import colored
import tabulate

pp = pprint.PrettyPrinter(indent=4,compact=False,width=20)
float_formatter = "{:+1.5f}".format
np.set_printoptions(formatter={"float_kind": float_formatter})
os.system("mkdir -p ./output")

with open('./config/load.json') as json_data:
    d = json.load(json_data)
    # print(d)

# print(d['selected'])
name=d['selected']
config=d[name]
# print(config)
print(name)
pp.pprint(config)


fname = "./models/discriminator.h5"
with tb.open_file(fname, "r") as h5file:
    node = h5file.get_node("/")
    table = h5file.root.training_config.config
    # print(table)
    # print(table.row)
    n_epochs=table.col('n_epochs')[0]
    n_batch=table.col('n_batch')[0]
    acc_real=table.col('acc_real')[0]
    x_max=table.col('x_max')[0]

    print("n_epochs=",n_epochs)
    print("n_batch=",n_batch)
    print("acc_real=",acc_real)
    print("x_max=",x_max)

    h5file.close()



# width=x_max-x_min

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
        xval=i*x_max/10
        yval=j*(x_max*x_max)/100
        # print(xval,yval)
        xinput.append([xval,yval])
    pred = model.predict(xinput)
    # pred_df=pd.DataFrame(pred,columns=[str(xval)])
    pred_df=pd.DataFrame(pred,columns=[str(xval)])
    pred_dfs = pd.concat([pred_dfs, pred_df], axis=1)


xinput_np = np.array(xinput)
firstcol=pd.DataFrame(xinput_np[:,[1]],columns=["y\p/x"])
pred_dfs = pd.concat([firstcol,pred_dfs], axis=1)

# print(pred_dfs.to_string(index=False))
pred_dfs.to_csv("./output/disc.csv",index=False)

# headers=['0.0','0.1']
headers=pred_dfs.columns
for header in headers:
    nl3 = pred_dfs[header].nlargest(3).values
    # print(nl3)
    # # nl4 = pred_dfs.Col4.nlargest(3).values
    pred_dfs[header] = pred_dfs[header].apply(lambda x: colored(x, "red") if x in nl3 else x)
    # # pred_dfs.Col4 = pred_dfs.Col4.apply(lambda x: colored(x, "red") if x in nl4 else x)
print(tabulate.tabulate(pred_dfs, headers=pred_dfs.columns))




