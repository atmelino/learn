# Code source: Jaques Grobler
# License: BSD 3 clause
# https://scikit-learn.org/stable/auto_examples/linear_model/plot_ols.html#sphx-glr-auto-examples-linear-model-plot-ols-py

import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd

# Load the diabetes dataset
diabetes_X_load, diabetes_y = datasets.load_diabetes(return_X_y=True)
print(diabetes_X_load.shape)

# Use only one feature
diabetes_X = diabetes_X_load[:, np.newaxis, 2]

# Split the data into training/testing sets
diabetes_X_train = diabetes_X[:-20]
diabetes_X_test = diabetes_X[-20:]

# Split the targets into training/testing sets
diabetes_y_train = diabetes_y[:-20]
diabetes_y_test = diabetes_y[-20:]

# Create linear regression object
regr = linear_model.LinearRegression()

# Train the model using the training sets
regr.fit(diabetes_X_train, diabetes_y_train)

# Make predictions using the testing set
diabetes_y_pred = regr.predict(diabetes_X_test)


# print the used dataset
diabetes_test_df = pd.DataFrame(data=diabetes_X_test,columns=["bmi"])
diabetes_test_df["diabetes_y_test"] = diabetes_y_test
diabetes_test_df["diabetes_y_pred"] = diabetes_y_pred
calculated=diabetes_X_test*regr.coef_+regr.intercept_
# print(calculated)
diabetes_test_df["calculated"] = calculated

diabetes_test_df=diabetes_test_df.sort_values(by='bmi', ascending=True)
# diabetes_test_df=diabetes_test_df.sort_values(by='diabetes_y_test', ascending=True)


print("diabetes test data\n",diabetes_test_df)
# print(a)

# The coefficients
print("Coefficients: \n", regr.coef_)
print("Intercept: \n", regr.intercept_)
# The mean squared error
print("Mean squared error: %.2f" % mean_squared_error(diabetes_y_test, diabetes_y_pred))
# The coefficient of determination: 1 is perfect prediction
print("Coefficient of determination: %.2f" % r2_score(diabetes_y_test, diabetes_y_pred))

# Plot outputs
plt.scatter(diabetes_X_test, diabetes_y_test, color="black")
plt.plot(diabetes_X_test, diabetes_y_pred, color="blue", linewidth=3)

# plt.xticks(())
# plt.yticks(())

plt.show()
