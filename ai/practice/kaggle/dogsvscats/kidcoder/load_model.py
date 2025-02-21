import torch
from torch import nn
from torchvision import datasets, models, transforms
from torchvision.transforms import *
from torch.utils.data import DataLoader




print("load model dogs vs cats")

num_classes = 2
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
val_image_folder = datasets.ImageFolder(basepath+"/working/valid", transform=transform)
val_loader = DataLoader(val_image_folder, batch_size=4, shuffle=False)

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
filename_write = "./output/compare.csv"
compare_df.to_csv(filename_write, index=False)










# num_classes = 3
# model = models.resnet18(pretrained=True) #Or Any Other Model
# filepath='./output/dogsvscats_model_weights.pth'
# # model.load_state_dict(torch.load(filepath))
# model = models.resnet18(pretrained=True)
# model.fc = nn.Linear(model.fc.in_features, num_classes)
# PATH='./output/dogsvscats_model_weights.pth'
# model.load_state_dict(torch.load(PATH))




