#Test Function

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
filename_write = "./output/compare_train.csv"
compare_df.to_csv(filename_write, index=False)

