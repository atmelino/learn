import tensorflow_datasets as tfds
import tensorflow as tf
tfds.disable_progress_bar()
train_ds, validation_ds = tfds.load(

"cats_vs_dogs",
split=["train[:40%]", "train[40%:50%]"],
as_supervised=True, # Include labels
)

num_train = tf.data.experimental.cardinality(train_ds)
num_test = tf.data.experimental.cardinality(validation_ds)
print(f"Number of training samples: {num_train}")
print(f"Number of validation samples: {num_test}")



