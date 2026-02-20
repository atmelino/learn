# https://www.tensorflow.org/guide/gpu#using_a_single_gpu_on_a_multi-gpu_system

import tensorflow as tf
print("Num GPUs Available: ", len(tf.config.experimental.list_physical_devices('GPU')))


tf.debugging.set_log_device_placement(True)

try:
  # Specify an invalid GPU device
  with tf.device('/device:GPU:0'):
    a = tf.constant([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
    b = tf.constant([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]])

    for i in range(0,10000000):
        print(i)
        c = tf.matmul(a, b)
except RuntimeError as e:
  print(e)

