
from torchvision import datasets, models, transforms
import torch.optim as optim
import torch.nn as nn
from torchvision.transforms import *
from torch.utils.data import DataLoader
import torch
import pandas as pd #For Data Frame Making


num_classes = 3
pretrained=True
basepath="../../../../../../../local_data/oneoffcoder"
modelpath='./output/resnet18-model.pt'

device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')

checkpoint = torch.load('./output/resnet18-checkpoint1.pt', map_location=device)

model = models.resnet18(pretrained=pretrained)
model.fc = nn.Linear(model.fc.in_features, num_classes)
model = model.to(device)

def validate(val_loader):

    # filelist=[]

    # for inputs, labels,img_path in val_loader:
    #     # print(img_path)
    #     for i in range(len(img_path)):
    #         filelist.append([img_path[i]])

    # filelist_df = pd.DataFrame(filelist, columns=['path'])
    # print(filelist_df.sort_values('path').to_string())

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

# train(dataloader, model, criterion, optimizer, scheduler, num_epochs=num_epochs)

