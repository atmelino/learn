
from torchvision import datasets, models, transforms
import torch.nn as nn
from torchvision.transforms import *
from torch.utils.data import DataLoader
import torch


num_classes = 3
pretrained=True
basepath="../../../../../../../local_data/oneoffcoder"


device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')


model = models.resnet18(pretrained=pretrained)
model.fc = nn.Linear(model.fc.in_features, num_classes)
model = model.to(device)

model.load_state_dict(torch.load('./output/resnet18-model.pt', map_location=device))



# Validation
transform = transforms.Compose([Resize(224), ToTensor()])
val_image_folder = datasets.ImageFolder(basepath+'/shapes/valid', transform=transform)
val_loader = DataLoader(val_image_folder, batch_size=4, shuffle=False)


def evaluate(model, val_loader):
    model.eval()
    correct = 0
    total = 0
    with torch.no_grad():
        for inputs, labels in val_loader:
            inputs = inputs.to(device)
            labels = labels.to(device)
            outputs = model(inputs)
            _, predicted = torch.max(outputs.data, 1)
            print("output\n",outputs)
            # print("inputs",inputs)
            print("labels",labels)
            print("predic",predicted)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()
    
    accuracy = 100 * correct / total
    print(f"Validation Accuracy: {accuracy:.2f}%")

evaluate(model, val_loader)


