import torch
from torch import nn
from torchvision import datasets, models, transforms
from torchvision.transforms import *
from torch.utils.data import DataLoader
from torch.utils.data import DataLoader, Dataset
import os
from PIL import Image
import pandas as pd #For Data Frame Making


print("load model dogs vs cats")

num_classes = 2
BATCH_SIZE = 4
pretrained=True
basepath="../../../../../../local_data/kaggle/dogsvscats_short"
modelpath='./output/dogsvscats_model_weights.pth'

device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')


#Define Transformations

data_transforms = transforms.Compose([
        transforms.Resize((224,224)),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ])


#Make Our Train And Test Custom Dataset

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
        
        return image, label, img_path


def validate(val_loader):

    filelist=[]

    for inputs, labels,img_path in val_loader:
        # print(img_path)
        for i in range(len(img_path)):
            filelist.append([img_path[i]])

    filelist_df = pd.DataFrame(filelist, columns=['path'])
    # print(filelist_df.sort_values('path').to_string())

    model = models.resnet18(pretrained=pretrained)
    model.fc = nn.Linear(model.fc.in_features, num_classes)
    model = model.to(device)

    model.load_state_dict(torch.load(modelpath, map_location=device))

    def evaluate(model, val_loader):
        model.eval()
        correct = 0
        total = 0

        compare_data = []

        with torch.no_grad():
            for inputs, labels,img_path in val_loader:
                inputs, labels = inputs.to(device), labels.to(device)
                outputs = model(inputs)
                _, predicted = torch.max(outputs.data, 1)
                total += labels.size(0)
                correct += (predicted == labels).sum().item()
                # print("labels",labels)
                # print("predic",predicted)
                # print("labels",labels.tolist())
                # print("predic",predicted.tolist())

                for i in range(len(labels)):
                    # label = 'dog' if predicted[i].item() == 1 else 'cat'
                    compare_data.append([labels[i].item(), predicted[i].item(),img_path[i]])

        accuracy = 100 * correct / total
        print(f"Validation Accuracy: {accuracy:.2f}%")
        # print(compare_data)
        return(compare_data)

    myresults=evaluate(model, val_loader)
    compare_df = pd.DataFrame(myresults, columns=['label', 'prediction','path'])

    # print(compare_df)

    print(compare_df.to_string())
    filename_write = "./output/compare_load.csv"
    compare_df.to_csv(filename_write, index=False)



#Load Dataset
val_dataset = TrainCustomDataset(root_dir=basepath+"/working/valid", transform=data_transforms)
#Make Dataloader
val_loader = DataLoader(val_dataset, batch_size=BATCH_SIZE, shuffle=False)
validate(val_loader)
