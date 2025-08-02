# HIDE OUTPUT
import tensorflow as tf
import tensorflow_hub as hub
import tensorflow_datasets as tfds

train_data, test_data = tfds.load(name="imdb_reviews",
    split=["train", "test"],
    batch_size=-1, as_supervised=True
)

# print(train_data)

# print(f"Number of train samples: {train_data.cardinality()}")
# print(f"Number of test samples: {test_data.cardinality()}")

train_examples, train_labels = tfds.as_numpy(train_data)
test_examples, test_labels = tfds.as_numpy(test_data)

index=5
print(train_examples[index])
print(train_labels[index])



# /Users/jheaton/tensorflow_datasets/imdb_reviews/plain_text/0.1.0


