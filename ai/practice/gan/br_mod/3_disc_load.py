# Use conda jh_class environment
# https://machinelearningmastery.com/how-to-develop-a-generative-adversarial-network-for-a-1-dimensional-function-from-scratch-in-keras/

import os
from numpy.random import rand
import numpy as np
from tensorflow.keras.utils import plot_model
from numpy.random import randn
from tensorflow.keras.models import load_model
import pandas as pd

float_formatter = "{:+1.3f}".format
np.set_printoptions(formatter={"float_kind": float_formatter})
os.system("mkdir -p ./output")


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

xinput=[]
dfs=[]
for j in range(4,9):
    for i in range(0,100):
        xinput.append([j,i])
    pred = model.predict(xinput)
    dfs.append( pd.DataFrame(pred,columns=["pred"]))



# pred=model.predict([[0.5,0.25]])
pred = model.predict(xinput)

inp =  pd.DataFrame(xinput)
pred_df = pd.DataFrame(pred,columns=["pred"])
DF = pd.concat([inp, pred_df], axis=1)
DF.to_csv("./output/disc.csv",index=False)

# print(DF)
print(DF.to_string())


