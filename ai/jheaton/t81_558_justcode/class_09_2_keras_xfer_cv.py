import tensorflow_datasets as tfds
import tensorflow as tf
import logging, os

# logging.basicConfig(level=logging.INFO)
logging.basicConfig(level=logging.DEBUG)

BASE_PATH = "../../../../local_data/jheaton/"
DATA_PATH = "../../../../local_data/tfds/dogsvscats/dataset/"
OUTPUT_PATH = BASE_PATH+"class_09_2_keras_xfer_cv/"
os.system("mkdir -p " + OUTPUT_PATH)

# tfds.core.get_tfds_path('cats_vs_dogs')

# exit()
# tfds.disable_progress_bar()

train_ds, validation_ds = tfds.load("cats_vs_dogs",split=["train[:40%]", "train[40%:50%]"],as_supervised=True, )# Include labels
# train_ds, validation_ds = tfds.load("cats_vs_dogs",data_dir=DATA_PATH,split=["train[:40%]", "train[40%:50%]"],as_supervised=True, )# Include labels
# train_ds, validation_ds = tfds.load('cats_vs_dogs', data_dir=data_dir, split='train', shuffle_files=True)

# dataset = tfds.load('cats_vs_dogs', data_dir=data_dir, split='train', shuffle_files=True)


num_train = tf.data.experimental.cardinality(train_ds)
num_test = tf.data.experimental.cardinality(validation_ds)
print(f"Number of training samples: {num_train}")
print(f"Number of validation samples: {num_test}")

import matplotlib.pyplot as plt



fig = plt.figure(figsize=(10, 10))
plt.title("title")
plt.yticks([])
plt.xticks([])
for i, (image, label) in enumerate(train_ds.take(9)):
    ax = plt.subplot(3, 3, i + 1)
    plt.imshow(image)
    plt.title(int(label))
    plt.axis("off")
filename=OUTPUT_PATH+"plot_init.png"
fig.savefig(filename)
plt.close(fig)

# fig = plt.figure(figsize=(20, 4))
# plt.title(title)
# plt.yticks([])
# plt.xticks([])

# for i in range(10):
#     ax = fig.add_subplot(1, 10, i + 1)
#     class_index = n_predictions[i]

#     plt.xlabel(classes[class_index])
#     plt.xticks([])
#     plt.yticks([])
#     plt.imshow(n_digits[i])

# plt.show()
# filename=model_path+"/resnet_02_"+title+".png"
# fig.savefig(filename)








size = (150, 150)
train_ds = train_ds.map(lambda x, y: (tf.image.resize(x, size), y))
validation_ds = validation_ds.map(lambda x, y: \
(tf.image.resize(x, size), y))








