# Sayed Gamal
# https://www.kaggle.com/code/sayedgamal99/in-cabin-state-farm-distracted-driver-detection

# conda activate kaggle


# c0: normal driving
# c1: texting - right
# c2: talking on the phone - right
# c3: texting - left
# c4: talking on the phone - left
# c5: operating the radio
# c6: drinking
# c7: reaching behind
# c8: hair and makeup
# c9: talking to passenger


import ultralytics
from ultralytics import YOLO
from IPython.display import Image
from roboflow import Roboflow
# from kaggle_secrets import UserSecretsClient
import os
import splitfolders
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

ultralytics.checks()


projecfoldername="../../../../local_data/kaggle/statefarm"
trainfoldername=os.path.join(projecfoldername, "imgs/train")
datasetfoldername=os.path.join(projecfoldername, "dataset/")


# model = YOLO('yolo11s-cls.pt')
model = YOLO('./runs/classify/train/weights/best.pt')


# results = model.train(data = datasetfoldername, epochs = 150, batch=32, imgsz=640,degrees=10, patience=8,seed=42)

# metrics = model.val()
# print("Validation Metrics:")
# print(metrics)

images=[
    "c0/img_100074.jpg",
    "c6/img_100109.jpg",
    "c3/img_100139.jpg" 
]

  
test_img_path=os.path.join(datasetfoldername, "test/"+images[2])
# test_img_path=os.path.join(datasetfoldername, "test/c0/img_100074.jpg")
# test_img_path = '/kaggle/working/dataset/test/c0/img_100074.jpg'  # adjust path as needed
results = model.predict(test_img_path, imgsz=640)
print(results)
result = results[0]




plt.figure(figsize=(12, 4))
plt.subplot(1, 2, 1)
img = Image.open(test_img_path)
plt.imshow(img)
plt.title(f'Predicted: {result.names[result.probs.top1]}')
plt.axis('off')

# Show probability distribution
plt.subplot(1, 2, 2)
probs = result.probs.data.cpu().numpy()
class_names = list(result.names.values())
y_pos = np.arange(len(class_names))
plt.barh(y_pos, probs)
plt.yticks(y_pos, class_names)
plt.xlabel('Probability')
plt.title('Class Probabilities')

plt.tight_layout()
plt.show()
plt.savefig("./plot01.png")

