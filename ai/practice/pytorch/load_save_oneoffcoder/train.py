# https://learn-pytorch.oneoffcoder.com/model-persistence.html

from torchvision import datasets, models, transforms
import torch.optim as optim
import torch.nn as nn
from torchvision.transforms import *
from torch.utils.data import DataLoader
import torch
import numpy as np
import os

os.system("mkdir -p ./output")

basepath="../../../../../local_data/oneoffcoder"

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
pretrained=True
num_classes = 3
num_epochs = 20

transform = transforms.Compose([Resize(224), ToTensor()])
image_folder = datasets.ImageFolder(basepath+'/shapes/train', transform=transform)
dataloader = DataLoader(image_folder, batch_size=4, shuffle=True, num_workers=4)

model = models.resnet18(pretrained=pretrained)
model.fc = nn.Linear(model.fc.in_features, num_classes)
model = model.to(device)

criterion = nn.CrossEntropyLoss()
optimizer = optim.Rprop(model.parameters(), lr=0.01)
scheduler = optim.lr_scheduler.StepLR(optimizer, step_size=1)

train(dataloader, model, criterion, optimizer, scheduler, num_epochs=num_epochs)

torch.save(model.state_dict(), './output/resnet18-model.pt')


