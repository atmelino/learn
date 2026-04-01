# https://www.tensorflow.org/api_docs/python/tf/keras/layers/TextVectorization

from keras import layers
import tensorflow as tf
import keras

max_tokens = 5000  # Maximum vocab size.
max_len = 3  # Sequence length to pad the outputs to.
# Create the layer.
vectorize_layer = tf.keras.layers.TextVectorization(
    max_tokens=max_tokens, 
    output_mode="int", 
    output_sequence_length=max_len
)

# Now that the vocab layer has been created, call `adapt` on the
# list of strings to create the vocabulary.
vectorize_layer.adapt(["foo bar", "bar baz", "baz bada boom"])
print("Dictionary:", vectorize_layer.get_vocabulary())


# Now, the layer can map strings to integers -- you can use an
# embedding layer to map these integers to learned embeddings.
input_data = [["foo qux bar"], ["qux baz"]]
input_data = [["foo qux bar"], ["qux baz"],["foo bar"],["bar tid foo"]]
print("input data:",input_data)
vl=vectorize_layer(input_data)
print(vl)

vocab_data = ["earth", "wind", "and", "fire"]
max_len = 4  # Sequence length to pad the outputs to.
# Create the layer, passing the vocab directly. You can also pass the
# vocabulary arg a path to a file containing one vocabulary word per
# line.
vectorize_layer = keras.layers.TextVectorization(
    max_tokens=max_tokens,
    output_mode='int',
    output_sequence_length=max_len,
    vocabulary=vocab_data)

# Because we've passed the vocabulary directly, we don't need to adapt
# the layer - the vocabulary is already set. The vocabulary contains the
# padding token ('') and OOV token ('[UNK]')
# as well as the passed tokens.
print(vectorize_layer.get_vocabulary())

