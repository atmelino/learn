
# https://github.com/tensorflow/tensorflow/issues/62963
# up to tensorflow 2.20: error
# tensorflow/core/framework/local_rendezvous.cc:407] Local rendezvous is aborting with status: OUT_OF_RANGE: End of sequence
# tensorflow 2.21: no error



import tensorflow as tf
print(f"Tensor Flow Version: {tf.__version__}")


