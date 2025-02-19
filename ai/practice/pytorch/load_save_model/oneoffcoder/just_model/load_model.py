
from torchvision import datasets, models, transforms
import torch.nn as nn
import torch



num_classes = 3
pretrained=True
device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')




model = models.resnet18(pretrained=pretrained)
model.fc = nn.Linear(model.fc.in_features, num_classes)
model = model.to(device)

model.load_state_dict(torch.load('./output/resnet18-model.pt', map_location=device))

model.eval()



