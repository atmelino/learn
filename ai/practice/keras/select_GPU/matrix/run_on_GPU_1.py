# https://www.tensorflow.org/guide/gpu#using_a_single_gpu_on_a_multi-gpu_system

import tensorflow as tf

print("Num GPUs Available: ", len(tf.config.experimental.list_physical_devices("GPU")))


# tf.debugging.set_log_device_placement(True)
tf.debugging.set_log_device_placement(False)

try:
    # Specify the GPU device
    print('Using /device:GPU:1')
    with tf.device("/device:GPU:1"):
        a = tf.constant([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
        b = tf.constant([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]])

        max = 2000000
        for i in range(0, max):
            # print(i)
            # print (i, end="\r")
            print(f"{i} of {max}", end="\r")

            c = tf.matmul(a, b)
except RuntimeError as e:
    print(e)
