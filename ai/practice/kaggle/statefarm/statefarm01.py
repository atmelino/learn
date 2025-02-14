# Sayed Gamal
# https://www.kaggle.com/code/sayedgamal99/in-cabin-state-farm-distracted-driver-detection

# conda activate kaggle

import ultralytics
from ultralytics import YOLO
from IPython.display import Image
from roboflow import Roboflow
# from kaggle_secrets import UserSecretsClient
import os
import splitfolders

ultralytics.checks()

datafoldername="../../../../local_data/kaggle/statefarm"

trainfoldername=os.path.join(datafoldername, "imgs/train")
datasetfoldername=os.path.join(datafoldername, "dataset/")
# splitfolders.ratio("/kaggle/input/state-farm-distracted-driver-detection/imgs/train", output="dataset", seed=32, ratio=(0.7, 0.15, 0.15))
splitfolders.ratio(trainfoldername, output=datasetfoldername, seed=32, ratio=(0.7, 0.15, 0.15))




