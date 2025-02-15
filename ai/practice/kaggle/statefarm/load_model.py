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


projecfoldername="../../../../local_data/kaggle/statefarm"
trainfoldername=os.path.join(projecfoldername, "imgs/train")
datasetfoldername=os.path.join(projecfoldername, "dataset/")


model = YOLO('yolo11s-cls.pt')

# results = model.train(data = datasetfoldername, epochs = 150, batch=32, imgsz=640,degrees=10, patience=8,seed=42)

# metrics = model.val()
# print("Validation Metrics:")
# print(metrics)

