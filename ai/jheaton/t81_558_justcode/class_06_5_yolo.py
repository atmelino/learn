print("conda environment for this program:")
print("conda activate vision")

# https://github.com/ultralytics/yolov5

import os
import torch
import pandas as pd

BASE_PATH = "../../../../local_data/jheaton"
DATA_PATH = os.path.join(BASE_PATH, "images")
LOCAL_IMG_FILE = DATA_PATH+"/jeff_cook.jpg"
# URL = "https://github.com/jeffheaton/t81_558_deep_learning/raw/master/photos/jeff_cook.jpg"

pd.set_option('display.width', 1000)

# Model
yolo_model = torch.hub.load('ultralytics/yolov5', 'yolov5s')
# or yolov5n - yolov
# Inference
results = yolo_model(LOCAL_IMG_FILE)
# Results
df = results.pandas().xyxy[0]
print(df)


df2 = df[['name','class']].groupby(by=["name"]).count().reset_index()
df2.columns = ['name','count']
df2['image'] = 1
df2.pivot(index=['image'],columns='name',values='count').reset_index().fillna(0)
print(df2)



