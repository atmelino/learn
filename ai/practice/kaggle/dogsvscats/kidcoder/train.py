#Torch Imports

import torch
from torch import nn
from torch import optim
from torch.utils.data import DataLoader, Dataset
import torchvision
from torchvision import datasets, models, transforms
import numpy as np #For Linear Algebra
import pandas as pd #For Data Frame Making
import matplotlib.pyplot as plt #For Visualization And Plot Making
from sklearn.model_selection import train_test_split #For Data Spliting
import zipfile #For Zip Opening
import os
from tqdm import tqdm
import shutil
from PIL import Image

os.system("mkdir -p ./output")

#Set Our Device

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Available Device : {device}")


#Set Our Hyperparameters(Prameters Of Our Model For Learning Loop)

BATCH_SIZE = 64
EPOCHS = 10
LEARNING_RATE = 0.00001


#Set Our Train And Test Path
projecfoldername="../../../../../local_data/kaggle/dogsvscats"

# train_zip_path = "/kaggle/input/dogsvscats/train.zip"
# test_zip_path = "/kaggle/input/dogsvscats/test1.zip"


# train_zip_path = "/kaggle/input/dogsvscats/train.zip"
# test_zip_path = "/kaggle/input/dogsvscats/test1.zip"
train_zip_path=os.path.join(projecfoldername, "train.zip")
test_zip_path=os.path.join(projecfoldername, "test1.zip")

#Set Where Unzipped Data Save

# unzipped_dir = "/kaggle/working/"
unzipped_dir=os.path.join(projecfoldername, "working/")

#Unzip Function

def unzip(zip_path, extract_to):
    with zipfile.ZipFile(zip_path) as zip_ref:
        zip_ref.extractall(extract_to)
    print(f"Unzip File Saved To : {extract_to}")

#Make Test And Train Folder

train_path = os.path.join(unzipped_dir, "train")
test_path = os.path.join(unzipped_dir, "test")

#Unzip Train And Test Zip Files

unzip(train_zip_path, train_path)
unzip(test_zip_path, test_path)

#Define Transformations

data_transforms = transforms.Compose([
        transforms.Resize((224,224)),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ])


#Make Our Trian And Test Custom Dataset

class TrainCustomDataset(Dataset):
    def __init__(self, root_dir, transform=None):
        self.root_dir = root_dir
        self.transform = transform
        self.cat_images = [os.path.join(root_dir, i) for i in os.listdir(root_dir) if i.split(".")[0] == "cat"]
        self.dog_images = [os.path.join(root_dir, i) for i in os.listdir(root_dir) if i.split(".")[0] == "dog"]

        self.images = self.cat_images + self.dog_images
        self.labels = [0] * len(self.cat_images) + [1] * len(self.dog_images)
        
    def __len__(self):
        return len(self.images)
        
    def __getitem__(self, idx):
        img_path = self.images[idx]
        label = self.labels[idx]
        
        with Image.open(img_path) as img:
            image = img.convert('RGB')
        
        if self.transform:
            image = self.transform(image)
        
        return image, label


#Load Dataaset

# dataset = TrainCustomDataset(root_dir="/kaggle/working/train/train", transform=data_transforms)
dataset = TrainCustomDataset(root_dir=projecfoldername+"/working/train/train", transform=data_transforms)

#Split Dataset

train_size = int(0.8 * len(dataset))
val_size = len(dataset) - train_size
train_dataset, val_dataset = torch.utils.data.random_split(dataset, [train_size, val_size])

#Make Dataloader

train_loader = DataLoader(train_dataset, batch_size=BATCH_SIZE, shuffle=True)
val_loader = DataLoader(val_dataset, batch_size=BATCH_SIZE, shuffle=False)

# image = Image.open("/kaggle/working/test/test1/10.jpg")
image = Image.open(projecfoldername+"/working/test/test1/10.jpg")
plt.imshow(image)
plt.savefig("./plot01.png")

model = models.resnet18(pretrained=True) #Or Any Other Model

#Freeze All Layers Except Last Layer

for param in model.parameters():
    param.requires_grad = False

#Modify The Final Layer For Binary Classification (2 Classes : Cat And Dog)

num_ftrs = model.fc.in_features
model.fc = nn.Linear(num_ftrs, 2)

#Move The Model To GPU If It's Available

model = model.to(device)


#Set Optimizer And Loss Function

optimizer = optim.Adam(model.fc.parameters(), lr=LEARNING_RATE)
criterion = nn.CrossEntropyLoss()

def train(model, train_loader, criterion, optimizer, epochs):
    model.train()
    for epoch in range(epochs):
        running_loss = 0.0
        for i, (inputs, labels) in enumerate(train_loader):
            inputs, labels = inputs.to(device), labels.to(device)
            
            optimizer.zero_grad()

            outputs = model(inputs)
            loss = criterion(outputs, labels)

            loss.backward()
            optimizer.step()

            running_loss += loss.item()
        print(f"Epoch : [{epoch+1} / {epochs}], Average Loss : {running_loss / len(train_loader):.4f}")


#Train Model

train(model, train_loader, criterion, optimizer, epochs=EPOCHS)

torch.save(model.state_dict(), './output/dogsvscats_model_weights.pth')



























