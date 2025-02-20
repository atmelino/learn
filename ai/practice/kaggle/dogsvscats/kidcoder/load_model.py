

import torch
from torch import nn
from torchvision import datasets, models, transforms

print("load model dogs vs cats")

num_classes = 3
pretrained=True
basepath="../../../../../../local_data/kaggle/dogsvscats_short"
modelpath='./output/dogsvscats_model_weights.pth'

device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')


model = models.resnet18(pretrained=pretrained)
model.fc = nn.Linear(model.fc.in_features, num_classes)
model = model.to(device)

model.load_state_dict(torch.load(modelpath, map_location=device))

# Validation
transform = transforms.Compose([Resize(224), ToTensor()])
val_image_folder = datasets.ImageFolder(basepath+"/working/train/train", transform=transform)
val_loader = DataLoader(val_image_folder, batch_size=4, shuffle=False)











# num_classes = 3
# model = models.resnet18(pretrained=True) #Or Any Other Model
# filepath='./output/dogsvscats_model_weights.pth'
# # model.load_state_dict(torch.load(filepath))
# model = models.resnet18(pretrained=True)
# model.fc = nn.Linear(model.fc.in_features, num_classes)
# PATH='./output/dogsvscats_model_weights.pth'
# model.load_state_dict(torch.load(PATH))




