import os.path

simple_tf=False
if simple_tf:
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

mandelbrot=False
if mandelbrot:
  import tensorflow as tf
  import numpy as np
  import PIL.Image
  from io import BytesIO
  from IPython.display import Image, display

  def render(a):
    a_cyclic = (a*0.3).reshape(list(a.shape)+[1])
    img = np.concatenate([10+20*np.cos(a_cyclic),
                          30+50*np.sin(a_cyclic),
                          155-80*np.cos(a_cyclic)], 2)
    img[a==a.max()] = 0
    a = img
    a = np.uint8(np.clip(a, 0, 255))
    f = BytesIO()
    return PIL.Image.fromarray(a)

  #@tf.function
  def mandelbrot_helper(grid_c, current_values, counts,cycles):
    
    for i in range(cycles):
      temp = current_values*current_values + grid_c
      not_diverged = tf.abs(temp) < 4
      current_values.assign(temp),
      counts.assign_add(tf.cast(not_diverged, tf.float32))

  def mandelbrot(render_size,center,zoom,cycles):
    f = zoom/render_size[0]
    real_start = center[0]-(render_size[0]/2)*f
    real_end = real_start + render_size[0]*f 
    imag_start = center[1]-(render_size[1]/2)*f
    imag_end = imag_start + render_size[1]*f 

    real_range = tf.range(real_start,real_end,f,dtype=tf.float64)
    imag_range = tf.range(imag_start,imag_end,f,dtype=tf.float64)
    real, imag = tf.meshgrid(real_range,imag_range)
    grid_c = tf.constant(tf.complex(real, imag))
    current_values = tf.Variable(grid_c)
    counts = tf.Variable(tf.zeros_like(grid_c, tf.float32))

    mandelbrot_helper(grid_c, current_values,counts,cycles)
    return counts.numpy()

  counts = mandelbrot(
      #render_size=(3840,2160), # 4K
      #render_size=(1920,1080), # HD
      render_size=(640,480),
      center=(-0.5,0),
      zoom=4,
      cycles=200
  )  
  img = render(counts)
  print("mandelbrot", img.size)
  img

  dirname=os.path.dirname(__file__)
  imgname=dirname+"/images/mandel.png"
  img.save(imgname)
  # img.save('jheaton/t81_558_justcode/large_csv/madel01.png')



mpg=False
if mpg:
  print("Simple TensorFlow Regression: MPG")
  from tensorflow.keras.models import Sequential
  from tensorflow.keras.layers import Dense, Activation
  import pandas as pd
  import io
  import os
  import requests
  import numpy as np
  from sklearn import metrics

  df = pd.read_csv(
      "https://data.heatonresearch.com/data/t81-558/auto-mpg.csv", 
      na_values=['NA', '?'])
  print(df)

  cars = df['name']

  # Handle missing value
  df['horsepower'] = df['horsepower'].fillna(df['horsepower'].median())

  # Pandas to Numpy
  x = df[['cylinders', 'displacement', 'horsepower', 'weight',
        'acceleration', 'year', 'origin']].values
  # x = df[['cylinders']].values
  y = df['mpg'].values # regression
  print(x)


  # Build the neural network
  model = Sequential()
  model.add(Dense(25, input_dim=x.shape[1], activation='relu')) # Hidden 1
  model.add(Dense(10, activation='relu')) # Hidden 2
  model.add(Dense(1)) # Output
  model.compile(loss='mean_squared_error', optimizer='adam')
  model.summary()
  model.fit(x,y,verbose=0,epochs=100)

  pred = model.predict(x)
  print(f"Shape: {pred.shape}")
  print(pred[0:10])

  # Measure RMSE error.  RMSE is common for regression.
  score = np.sqrt(metrics.mean_squared_error(pred,y))
  print(f"Final score (RMSE): {score}")

  # Sample predictions
  for i in range(10):
      print(f"{i+1}. Car name: {cars[i]}, MPG: {y[i]}, " 
            + f"predicted MPG: {pred[i]}")



import pandas as pd
import io
import requests
import numpy as np
from sklearn import metrics
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation
from tensorflow.keras.callbacks import EarlyStopping

df = pd.read_csv(
    "https://data.heatonresearch.com/data/t81-558/iris.csv", 
    na_values=['NA', '?'])

# Convert to numpy - Classification
x = df[['sepal_l', 'sepal_w', 'petal_l', 'petal_w']].values
dummies = pd.get_dummies(df['species']) # Classification
species = dummies.columns
y = dummies.values


# Build neural network
model = Sequential()
model.add(Dense(50, input_dim=x.shape[1], activation='relu')) # Hidden 1
model.add(Dense(25, activation='relu')) # Hidden 2
model.add(Dense(y.shape[1],activation='softmax')) # Output

model.compile(loss='categorical_crossentropy', optimizer='adam')
model.fit(x,y,verbose=2,epochs=100)

# Print out number of species found:

print(species)

pred = model.predict(x)
print(f"Shape: {pred.shape}")
print(pred[0:10])

np.set_printoptions(suppress=True)
print(y[0:10])

predict_classes = np.argmax(pred,axis=1)
expected_classes = np.argmax(y,axis=1)
diff=predict_classes-expected_classes
print(f"Predictions: {predict_classes}")
print(f"Expected: {expected_classes}")
print(f"diff: {diff}")

print(species[predict_classes[1:70]])

from sklearn.metrics import accuracy_score

correct = accuracy_score(expected_classes,predict_classes)
print(f"Accuracy: {correct}")

sample_flower = np.array( [[5.0,3.0,4.0,2.0]], dtype=float)
pred = model.predict(sample_flower)
print(pred)
pred = np.argmax(pred)
print(f"Predict that {sample_flower} is: {species[pred]}")

sample_flower = np.array( [[5.0,3.0,4.0,2.0],[5.2,3.5,1.5,0.8]],\
        dtype=float)
pred = model.predict(sample_flower)
print(pred)
pred = np.argmax(pred,axis=1)
print(f"Predict that these two flowers {sample_flower} ")
print(f"are: {species[pred]}")























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








