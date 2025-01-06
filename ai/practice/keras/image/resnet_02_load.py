import os
import tensorflow as tf
from tensorflow.keras.models import load_model




load_path = "../not_on_github/models"
model = load_model(os.path.join(load_path, "resnet_02.h5"))

model.summary()




