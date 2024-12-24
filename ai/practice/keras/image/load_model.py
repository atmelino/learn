import os

from tensorflow.keras.models import load_model



load_path = "../not_on_github/catdogsavemodel"
model2 = load_model(os.path.join(load_path,"catdog01.h5"))


