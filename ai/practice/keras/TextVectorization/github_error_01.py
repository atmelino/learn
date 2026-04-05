
# https://github.com/tensorflow/tensorflow/issues/62963
# up to tensorflow 2.20: error
# tensorflow/core/framework/local_rendezvous.cc:407] Local rendezvous is aborting with status: OUT_OF_RANGE: End of sequence
# tensorflow 2.21: no error



import tensorflow as tf
print(f"Tensor Flow Version: {tf.__version__}")


import tensorflow as tf

def dataset_test():
 
    dataset = tf.data.Dataset.from_tensor_slices(["apple", "banana", "cherry"])
    # dataset = tf.data.TextLineDataset(["file1.txt", "file2.txt"]).range(10)             # same output
    # dataset = tf.data.TFRecordDataset(["file1.tfrecords", "file2.tfrecords"]).range(10) # same output
    # dataset = tf.data.Dataset.from_tensors([1,2,3]).range(10)                           # same output

    print(list(dataset.as_numpy_iterator()))

if __name__ == "__main__":
    dataset_test()


import tensorflow as tf

range_ds = tf.data.Dataset.range(10)

for d in range_ds:
   print(d)