import tensorflow_hub as hub

# embed = hub.Module("https://tfhub.dev/google/"
# "universal-sentence-encoder/1")
# embedding = embed([
# "The quick brown fox jumps over the lazy dog."])

# print(embedding)



# embed = hub.Module("https://kaggle.com/models/google/universal-sentence-encoder/frameworks/TensorFlow1/variations/universal-sentence-encoder/versions/1")
# embeddings = embed([
#     "The quick brown fox jumps over the lazy dog.",
#     "I am a sentence for which I would like to get its embedding"])

# print(session.run(embeddings))

# The following are example embedding output of 512 dimensions per sentence
# Embedding for: The quick brown fox jumps over the lazy dog.
# [-0.016987282782793045, -0.008949815295636654, -0.0070627182722091675, ...]
# Embedding for: I am a sentence for which I would like to get its embedding.
# [0.03531332314014435, -0.025384284555912018, -0.007880025543272495, ...]


import tensorflow_hub as hub
import tensorflow as tf

english_sentences = tf.constant(["dog", "Puppies are nice.", "I enjoy taking long walks along the beach with my dog."])

preprocessor = hub.KerasLayer(
    "https://kaggle.com/models/tensorflow/bert/TensorFlow2/en-uncased-preprocess/3")
encoder = hub.KerasLayer(
    "https://www.kaggle.com/models/google/universal-sentence-encoder/TensorFlow2/cmlm-en-base/1")

english_embeds = encoder(preprocessor(english_sentences))["default"]

print (english_embeds)