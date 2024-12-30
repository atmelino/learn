import os
from tensorflow.keras.models import load_model


print("class_06_3_resnet_load")

load_path = "./models"
model = load_model(os.path.join(load_path, "class_06_3_resnet.h5"))

exit()



