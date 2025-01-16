# https://github.com/ultralytics/yolov5

URL = "https://github.com/jeffheaton/t81_558_deep_learning/raw/master/photos/jeff_cook.jpg"
LOCAL_IMG_FILE = "./not_on_github/images/jeff_cook.jpg"

cmd="python3 /not_on_github/yolov5/detect.py --weights yolov5s.pt --img 1024 --conf 0.25 --source /not_on_github/images/"


import torch
import pandas as pd

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



