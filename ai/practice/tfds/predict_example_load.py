import tensorflow as tf
import tensorflow_datasets as tfds
import logging, os
import pandas as pd
import time
from tensorflow.keras.models import load_model

BASE_PATH = "../../../../local_data/practice/tfds/"
DATA_PATH = "../../../../local_data/tfds/"
OUTPUT_PATH = BASE_PATH+"predict_example_01/"
os.system("mkdir -p " + OUTPUT_PATH)


# Load the dataset
(train_dataset, test_dataset), metadata = tfds.load(
    'cats_vs_dogs',
    data_dir=DATA_PATH,
    split=['train[:80%]', 'train[80%:]'],
    with_info=True,
    as_supervised=True
)

# Preprocess the data
def preprocess(image, label):
    image = tf.cast(image, tf.float32)
    image = tf.image.resize(image, [256, 256])
    image = image / 255.0
    return image, label

train_dataset = train_dataset.map(preprocess)
test_dataset = test_dataset.map(preprocess)

batch_size = 32
train_dataset = train_dataset.cache().batch(batch_size).prefetch(buffer_size=10)
test_dataset = test_dataset.cache().batch(batch_size).prefetch(buffer_size=10)


filename = "epochs_5.000_date_20250708-215035.h5"


fullpath = f"{OUTPUT_PATH}{filename}"
model = load_model(fullpath)
model.summary()



# Make predictions
predictions = model.predict(test_dataset)
print(predictions)

allpred=[]
alllabels=[]

for images, labels in test_dataset:
    # collabels = pd.DataFrame(labels, columns=["l"])
    # print(collabels)
    preds = model.predict(images)
    # colpred = pd.DataFrame(preds, columns=["p0"])
    # print(colpred)
    # compare = pd.concat([collabels, colpred], axis=1)
    # print(compare)
    # print("labels\n",labels)
    # print("preds\n",preds)
    allpred.append(preds)
    alllabels.append(labels)


collabels = pd.DataFrame(allpred, columns=["l"])
colpred = pd.DataFrame(alllabels, columns=["p0"])

compare = pd.concat([collabels, colpred], axis=1)
compare.to_csv(OUTPUT_PATH + "pred_test.csv", index=False)    



# ds = train_ds.take(20)
# print("type(image), type(label), label,info.features['label'].names[label]=")
# for image, label in tfds.as_numpy(ds):
#   print(type(image), type(label), label,info.features["label"].names[label])




# for images, labels in train_dataset:
#     preds = model.predict(images)
#     print(preds)
    # Compare preds with labels

# Explanation of prediction output when activation is sigmoid:
# https://forum.freecodecamp.org/t/model-predict-output/470349
