

import torch
from torch import nn
from torchvision import datasets, models, transforms


num_classes = 3


model = models.resnet18(pretrained=True) #Or Any Other Model


filepath='./output/dogsvscats_model_weights.pth'


# model.load_state_dict(torch.load(filepath))

model = models.resnet18(pretrained=True)
model.fc = nn.Linear(model.fc.in_features, num_classes)
PATH='./output/dogsvscats_model_weights.pth'
model.load_state_dict(torch.load(PATH))


model.eval()


