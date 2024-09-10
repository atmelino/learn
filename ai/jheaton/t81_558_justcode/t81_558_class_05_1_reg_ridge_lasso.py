# %matplotlib inline


import sklearn
from sklearn.linear_model import LassoCV
from sklearn.linear_model import Lasso
from sklearn.linear_model import Ridge
from sklearn.linear_model import ElasticNet
import pandas as pd
import os
import numpy as np
from sklearn import metrics
from scipy.stats import zscore
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

df = pd.read_csv(
    "https://data.heatonresearch.com/data/t81-558/auto-mpg.csv", na_values=["NA", "?"]
)

# Handle missing value
df["horsepower"] = df["horsepower"].fillna(df["horsepower"].median())

# Pandas to Numpy
names = [
    "cylinders",
    "displacement",
    "horsepower",
    "weight",
    "acceleration",
    "year",
    "origin",
]
x = df[names].values
y = df["mpg"].values  # regression

# Split into train/test
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.25, random_state=45
)


# Simple function to evaluate the coefficients of a regression
from IPython.display import display, HTML, Image


def report_coef(names, coef, intercept):
    r = pd.DataFrame({"coef": coef, "positive": coef >= 0}, index=names)
    r = r.sort_values(by=["coef"])
    print(r)
    # display(r)
    # Image(filename='./test.png')

    print(f"Intercept: {intercept}")
    r["coef"].plot(kind="barh", color=r["positive"].map({True: "b", False: "r"}))
    # plt.bar(names,r["coef"].tolist())
    plt.show()


# Linear regression without L1/L2
# Create linear regression
regressor = sklearn.linear_model.LinearRegression()

# Fit/train linear regression
regressor.fit(x_train, y_train)
# Predict
pred = regressor.predict(x_test)

# Measure RMSE error.  RMSE is common for regression.
score = np.sqrt(metrics.mean_squared_error(pred, y_test))
print(f"Final score (RMSE): {score}")

report_coef(names, regressor.coef_, regressor.intercept_)


# Linear regression with L1
# Create linear regression
regressor = Lasso(random_state=0, alpha=0.1)
# Fit/train LASSO
regressor.fit(x_train, y_train)
# Predict
pred = regressor.predict(x_test)
# Measure RMSE error. RMSE is common for regression.
score = np.sqrt(metrics.mean_squared_error(pred, y_test))
print(f"Final score (RMSE): {score}")

report_coef(names, regressor.coef_, regressor.intercept_)


# Linear regression with L2
# Create linear regression
regressor = Ridge(alpha=1)
# Fit/train Ridge
regressor.fit(x_train, y_train)
# Predict
pred = regressor.predict(x_test)
# Measure RMSE error. RMSE is common for regression.
score = np.sqrt(metrics.mean_squared_error(pred, y_test))
print("Final score (RMSE): {score}")
report_coef(names, regressor.coef_, regressor.intercept_)



# Linear regression with ElasticNet 
# Create linear regression
regressor = ElasticNet(alpha=0.1, l1_ratio=0.1)
# Fit/train LASSO
regressor.fit(x_train, y_train)
# Predict
pred = regressor.predict(x_test)
# Measure RMSE error. RMSE is common for regression.
score = np.sqrt(metrics.mean_squared_error(pred, y_test))
print(f"Final score (RMSE): {score}")
report_coef(names, regressor.coef_, regressor.intercept_)
