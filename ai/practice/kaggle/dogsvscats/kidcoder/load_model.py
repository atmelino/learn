

import torch
from torchvision import datasets, models, transforms




model = models.resnet18(pretrained=True) #Or Any Other Model


filepath='./output/dogsvscats_model_weights.pth'

#Later to restore:
model.load_state_dict(torch.load(filepath))
model.eval()


