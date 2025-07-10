# Explanation of prediction output when activation is sigmoid:
# https://forum.freecodecamp.org/t/model-predict-output/470349

import tensorflow as tf
import tensorflow_datasets as tfds
import logging, os
import pandas as pd
import time
from tensorflow.keras.models import load_model
import numpy as np

BASE_PATH = "../../../../local_data/practice/tfds/"
DATA_PATH = "../../../../local_data/tfds/"
OUTPUT_PATH = BASE_PATH+"predict_example_01/"
os.system("mkdir -p " + OUTPUT_PATH)


# Load the dataset
(train_dataset, test_dataset), metadata = tfds.load(
    'cats_vs_dogs',
    data_dir=DATA_PATH,
    # split=['train[:80%]', 'train[80%:]'],
    split=['train[:80%]', 'train[99%:]'],
    with_info=True,
    as_supervised=True
)

print(f"Number of test samples: {test_dataset.cardinality()}")


# Preprocess the data
def preprocess(image, label):
    image = tf.cast(image, tf.float32)
    image = tf.image.resize(image, [256, 256])
    image = image / 255.0
    return image, label

train_dataset = train_dataset.map(preprocess)
test_dataset = test_dataset.map(preprocess)

batch_size = 64
train_dataset = train_dataset.cache().batch(batch_size).prefetch(buffer_size=10)
test_dataset = test_dataset.cache().batch(batch_size).prefetch(buffer_size=10)

print(test_dataset)

# exit()

# alllabels=[]
# alllabels=np.empty(0)

# for images, labels in test_dataset:
#     print("labels\n",labels)
    
#     # Convert the tensor to a NumPy array
#     numpy_labels = labels.numpy()
#     print(numpy_labels)    
#     print(numpy_labels.shape)   

#     numpy_labels1=numpy_labels.reshape(numpy_labels.shape[0],1)
#     print(numpy_labels1)    
#     print(numpy_labels1.shape)   

#     alllabels = np.append(alllabels, numpy_labels)
#     print(alllabels.shape)

# print(alllabels.shape)
# collabels = pd.DataFrame(alllabels, columns=["l"])
# print(collabels)
# exit()

filename = "epochs_5.000_date_20250708-215035.h5"
filename = "epochs_1.000_date_20250708-214731.h5"


fullpath = f"{OUTPUT_PATH}{filename}"
model = load_model(fullpath)
model.summary()



# Make predictions
predictions = model.predict(test_dataset)
# print(predictions)



allpreds=np.empty(0)
alllabels=np.empty(0)

for images, labels in test_dataset:
    # print("labels\n",labels)
    numpy_labels = labels.numpy()
    # print(numpy_labels)    
    # print(numpy_labels.shape)   
    numpy_labels1=numpy_labels.reshape(numpy_labels.shape[0],1)
    # print(numpy_labels1)    
    # print(numpy_labels1.shape)   
    alllabels = np.append(alllabels, numpy_labels)
    print("alllabels.shape=",alllabels.shape)

    preds = model.predict(images)
    # print("preds\n",preds)
    print("preds.shape",preds.shape)   
    allpreds = np.append(allpreds, preds)
    print("allpreds.shape=",allpreds.shape)

print("alllabels.shape=",alllabels.shape)
collabels = pd.DataFrame(alllabels, columns=["l"])
print(collabels)

print("allpreds.shape=",allpreds.shape)
# allpred1=allpred.reshape(allpred,shape)
# print(allpred1.shape)
colpreds = pd.DataFrame( allpreds, columns=["pred"])
# print(colpred)

diff = collabels["l"] - colpreds["pred"]
print(diff)

compare = pd.concat([collabels, colpreds], axis=1)
compare = pd.concat([collabels, colpreds,diff], axis=1)
compare.columns = ["l", "pred", "diff"]
print(compare)

compare.to_csv(OUTPUT_PATH + "pred_test.csv", index=False)    


