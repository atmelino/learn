# HIDE OUTPUT
import tensorflow as tf
import tensorflow_hub as hub
import tensorflow_datasets as tfds

train_data, test_data = tfds.load(
    name="imdb_reviews",
    split=["train", "test"],
    batch_size=-1, 
    as_supervised=True
)
# /Users/jheaton/tensorflow_datasets/imdb_reviews/plain_text/0.1.0

# print(train_data)

train_examples, train_labels = tfds.as_numpy(train_data)
test_examples, test_labels = tfds.as_numpy(test_data)

# index=5
# print(train_examples[index])
# print(train_labels[index])

# print(train_examples[:3])
# print(train_labels[:3])


hub_model = "https://tfhub.dev/google/tf2-preview/gnews-swivel-20dim/1"
hub_layer = hub.KerasLayer(
    hub_model, 
    output_shape=[20], 
    input_shape=[],
    dtype=tf.string, 
    trainable=True
)

# print(hub_layer(train_examples[:3]))
print(hub_layer(train_examples[:1]))


model = tf.keras.Sequential()
model.add(hub_layer)
model.add(tf.keras.layers.Dense(16, activation='relu'))
model.add(tf.keras.layers.Dense(1, activation='sigmoid'))
model.summary()


