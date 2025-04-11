import os.path

print("matrix mul")
import tensorflow as tf
# Create a Constant op that produces a 1x2 matrix.  The op is
# added as a node to the default graph.
#
# The value returned by the constructor represents the output
# of the Constant op.
matrix1 = tf.constant([[3., 3.]])
# Create another Constant that produces a 2x1 matrix.
matrix2 = tf.constant([[2.],[2.]])
# Create a Matmul op that takes 'matrix1' and 'matrix2' as inputs.
# The returned value, 'product', represents the result of the matrix
# multiplication.
product = tf.matmul(matrix1, matrix2)
print(product)
print(float(product))
print()


print("matrix const subtract")
import tensorflow as tf
x = tf.Variable([1.0, 2.0])
a = tf.constant([3.0, 3.0])
# Add an op to subtract 'a' from 'x'.  Run it and print the result
sub = tf.subtract(x, a)
print(sub)
print(sub.numpy())
# ==> [-2. -1.]
print()

print("matrix variable assign")
x.assign([4.0, 6.0])
print(x)
print(x.numpy())
sub = tf.subtract(x, a)
print(sub)
print(sub.numpy())
print()



# print(x.shape)
# print(y.shape)

# print("model.fit")
# print()

# pred = model.predict(x)
# print(f"Shape: {pred.shape}")
# print(pred[0:10])

# # Measure RMSE error.  RMSE is common for regression.
# score = np.sqrt(metrics.mean_squared_error(pred,y))
# print(f"Final score (RMSE): {score}")


# # Sample predictions
# for i in range(10):
#     print(f"{i+1}. Car name: {cars[i]}, MPG: {y[i]}, " 
#           + f"predicted MPG: {pred[i]}")








