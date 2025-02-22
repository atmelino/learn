
from torchvision import datasets, models, transforms
import torch.optim as optim
import torch.nn as nn
from torchvision.transforms import *
from torch.utils.data import DataLoader
import torch
import pandas as pd #For Data Frame Making
import numpy as np


num_classes = 3
EPOCHS = 3
num_epochs = EPOCHS
pretrained=True
basepath="../../../../../../../local_data/oneoffcoder"
modelpath='./output/resnet18-model.pt'

def train(dataloader, model, criterion, optimizer, scheduler, num_epochs=20):
    for epoch in range(num_epochs):
        optimizer.step()
        scheduler.step()
        model.train()

        running_loss = 0.0
        running_corrects = 0

        n = 0
        for inputs, labels in dataloader:
            inputs = inputs.to(device)
            labels = labels.to(device)

            optimizer.zero_grad()

            with torch.set_grad_enabled(True):
                outputs = model(inputs)
                loss = criterion(outputs, labels)
                _, preds = torch.max(outputs, 1)

                loss.backward()
                optimizer.step()

            running_loss += loss.item() * inputs.size(0)
            running_corrects += torch.sum(preds == labels.data)
            n += len(labels)

        epoch_loss = running_loss / float(n)
        epoch_acc = running_corrects.double() / float(n)

        print(f'epoch {epoch}/{num_epochs} : {epoch_loss:.5f}, {epoch_acc:.5f}')

np.random.seed(37)
torch.manual_seed(37)
torch.backends.cudnn.deterministic = True
torch.backends.cudnn.benchmark = False

device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')

checkpoint = torch.load('./output/resnet18-checkpoint1.pt', map_location=device)

model = models.resnet18(pretrained=pretrained)
model.fc = nn.Linear(model.fc.in_features, num_classes)
model = model.to(device)

def validate(val_loader):

    def evaluate(model, val_loader):
        model.eval()
        correct = 0
        total = 0
        compare_data = []
        with torch.no_grad():
            for inputs, labels in val_loader:
                inputs = inputs.to(device)
                labels = labels.to(device)
                outputs = model(inputs)
                _, predicted = torch.max(outputs.data, 1)
                total += labels.size(0)
                correct += (predicted == labels).sum().item()
                # print("output\n",outputs)
                # print("inputs",inputs)
                # print("labels",labels)
                # print("predic",predicted)
                for i in range(len(labels)):
                    # compare_data.append([labels[i].item(), predicted[i].item(),img_path[i]])
                    compare_data.append([labels[i].item(), predicted[i].item()])

        accuracy = 100 * correct / total
        print(f"Validation Accuracy: {accuracy:.2f}%")
        return(compare_data)

    myresults=evaluate(model, val_loader)
    compare_df = pd.DataFrame(myresults, columns=['label', 'prediction'])
    # print(compare_df)
    print(compare_df.to_string())
    filename_write = "./output/compare_train.csv"
    compare_df.to_csv(filename_write, index=False)


# Load model

criterion = nn.CrossEntropyLoss()
optimizer = optim.Rprop(model.parameters(), lr=0.01)
scheduler = optim.lr_scheduler.StepLR(optimizer, step_size=1)

model.load_state_dict(checkpoint['model_state_dict'])
criterion.load_state_dict(checkpoint['criterion_state_dict'])
optimizer.load_state_dict(checkpoint['optimizer_state_dict'])
scheduler.load_state_dict(checkpoint['scheduler_state_dict'])

# Validation
transform = transforms.Compose([Resize(224), ToTensor()])
val_image_folder = datasets.ImageFolder(basepath+'/shapes/valid', transform=transform)
val_loader = DataLoader(val_image_folder, batch_size=4, shuffle=False)
validate(val_loader)


# Continue training
transform = transforms.Compose([Resize(224), ToTensor()])
train_image_folder = datasets.ImageFolder(basepath+'/shapes/train', transform=transform)
dataloader = DataLoader(train_image_folder, batch_size=4, shuffle=True, num_workers=4)

train(dataloader, model, criterion, optimizer, scheduler, num_epochs=num_epochs)

# Validate again
validate(val_loader)
