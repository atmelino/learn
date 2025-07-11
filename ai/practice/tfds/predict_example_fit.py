import tensorflow as tf
import tensorflow_datasets as tfds
import logging, os
import pandas as pd
import time
from sklearn import metrics

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


# Apply data augmentation
def augment(image, label):
    image = tf.image.random_flip_left_right(image)
    image = tf.image.random_brightness(image, 0.1)
    return image, label

train_dataset = train_dataset.map(augment)


# Model prediction
model = tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(32, (3,3), activation='relu', input_shape=(256, 256, 3)),
    tf.keras.layers.MaxPooling2D(2,2),
    tf.keras.layers.Conv2D(64, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(512, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
epochs=1
model.fit(train_dataset, epochs=epochs)

score = metrics.accuracy_score(y_test, pred)
print("Validation accuracy score: {}".format(score))


timestr = time.strftime("%Y%m%d-%H%M%S")
# filename = f"acc_{score:.3f}_date_{timestr}.h5"
filename = f"epochs_{epochs:.3f}_date_{timestr}.h5"
fullpath = f"{OUTPUT_PATH}{filename}"
print("Saving model to ", filename)
model.save(fullpath)


# Make predictions
predictions = model.predict(test_dataset[0:100])
print(predictions)

for images, labels in test_dataset:
    collabels = pd.DataFrame(labels, columns=["l"])
    # print(collabels)
    preds = model.predict(images)
    colpred = pd.DataFrame(preds, columns=["p0"])
    # print(colpred)
    compare = pd.concat([collabels, colpred], axis=1)
    # print(compare)
    # print("labels\n",labels)
    # print("preds\n",preds)
    
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
