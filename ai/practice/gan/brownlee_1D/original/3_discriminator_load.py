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


# load the discriminator model
load_path = "./models"
model = load_model(os.path.join(load_path, "discriminator.h5"))

# summarize the model
model.summary()
# plot the model
# plot_model(model, to_file='discriminator_plot.png', show_shapes=True, show_layer_names=True)


# Predict
xinput = [
    [-0.5, -0.3], 
    [-0.5, -0.1], 
    [-0.5, 0], 
    [-0.5, 0.1], 
    [-0.5, 0.25], 
    [-0.5, 0.4],
    [0.5, -0.3], 
    [0.5, -0.1], 
    [0.5, 0], 
    [0.5, 0.1], 
    [0.5, 0.25], 
    [0.5, 0.4],
    [0.2, 0.04],
]

xinput = [
    [0.2, 0.00],
    [0.2, 0.01],
    [0.2, 0.02],
    [0.2, 0.03],
    [0.2, 0.04],
    [0.2, 0.05],
    [0.2, 0.06],
    [0.2, 0.07],
    [0.2, 0.08],
    [0.2, 0.09],
]


# pred=model.predict([[0.5,0.25]])
pred = model.predict(xinput)

inp =  pd.DataFrame(xinput)
pred_df = pd.DataFrame(pred,columns=["pred"])
DF = pd.concat([inp, pred_df], axis=1)
DF.to_csv("./output/disc.csv",index=False)

print(DF)

