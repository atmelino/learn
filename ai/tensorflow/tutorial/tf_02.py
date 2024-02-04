# https://www.tensorflow.org/tutorials/quickstart/beginner

import tensorflow as tf
import pprint
# pp = pprint.PrettyPrinter(indent=2,width=100)

pp = pprint.PrettyPrinter(width=41, compact=True)


mnist = tf.keras.datasets.mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

#print(x_train)
#print(y_train)
# print(x_test)
# print(x_test,shape)
#print(y_test)
#mnist.print()
#print(mnist.shape)

# print(x_test[0])
# print(x_test[1])

# pp.pprint(x_test[0])




pp.pprint(x_test[0][0])

pp.pprint(x_test[0][0][0])

mystring=pprint.pformat(x_test[0][0], indent=1, width=200, depth=None)
print(mystring)

