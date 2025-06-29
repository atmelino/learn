import tensorflow_datasets as tfds
import tensorflow as tf
import logging, os

logging.basicConfig(level=logging.INFO)
# logging.basicConfig(level=logging.DEBUG)

BASE_PATH = "../../../../local_data/jheaton/"
DATA_PATH = "../../../../local_data/tfds/"
OUTPUT_PATH = BASE_PATH + "class_09_2_keras_xfer_cv/"
os.system("mkdir -p " + OUTPUT_PATH)

# tfds.core.get_tfds_path('cats_vs_dogs')

# exit()
# tfds.disable_progress_bar()

# train_ds, validation_ds = tfds.load("cats_vs_dogs",split=["train[:40%]", "train[40%:50%]"],as_supervised=True, )# Include labels
train_ds, validation_ds = tfds.load(
    "cats_vs_dogs",
    data_dir=DATA_PATH,
    split=["train[:40%]", "train[40%:50%]"],
    as_supervised=True,
)  # Include labels

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
filename = OUTPUT_PATH + "plot_init1.png"
fig.savefig(filename)
plt.close(fig)

size = (150, 150)
size = (250, 250)
train_ds = train_ds.map(lambda x, y: (tf.image.resize(x, size), y))
validation_ds = validation_ds.map(lambda x, y: (tf.image.resize(x, size), y))


fig = plt.figure(figsize=(10, 10))
plt.title("title")
plt.yticks([])
plt.xticks([])
for i, (image, label) in enumerate(train_ds.take(9)):
    ax = plt.subplot(3, 3, i + 1)
    plt.imshow(image)
    plt.title(int(label))
    plt.axis("off")
filename = OUTPUT_PATH + "plot_init2.png"
fig.savefig(filename)
plt.close(fig)


# (raw_train, raw_validation, raw_test), metadata = tfds.load(
#     'cats_vs_dogs',
#     split=['train[:80%]', 'train[80%:90%]', 'train[90%:]'],
#     with_info=True,
#     data_dir=r'D:\TFProjects\catsdogscompl')


def save_dataset_as_jpegs(
    dataset,
    path,
):
    """

    saves every image to the 'path' using random name + target

    :param dataset: dataset you want to save
    :param path: where you want to store it
    :param metadata: metadata from dataset. required to get class names.
    :return: Nothing. Just saves the dataset as jpegs.
    """

    for obj in dataset:
        im, name = obj["image"], obj["image/filename"]
        serialized_im = tf.image.encode_jpeg(im)

        path_and_name = os.path.join(path, name.numpy().decode())
        tf.io.write_file(path_and_name, serialized_im)


save_dataset_as_jpegs(train_ds, "jpegs_train/")
# save_dataset_as_jpegs(raw_validation, 'jpegs_validation/')
# save_dataset_as_jpegs(raw_test, 'jpegs_test/')

# https://www.tensorflow.org/guide/data
