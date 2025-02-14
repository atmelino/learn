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

extract=False

projecfoldername="../../../../local_data/kaggle/statefarm"
trainfoldername=os.path.join(projecfoldername, "imgs/train")
datasetfoldername=os.path.join(projecfoldername, "dataset/")

if extract==True:
    splitfolders.ratio(trainfoldername, output=datasetfoldername, seed=32, ratio=(0.7, 0.15, 0.15))

model = YOLO('yolo11s-cls.pt')

results = model.train(data = datasetfoldername, epochs = 150, batch=32, imgsz=640,degrees=10, patience=8,seed=42)


