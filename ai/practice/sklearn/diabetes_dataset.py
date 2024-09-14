# https://www.geeksforgeeks.org/sklearn-diabetes-dataset/

import pandas as pd
from sklearn.datasets import load_diabetes

# Load the diabetes dataset
diabetes_sklearn = load_diabetes()

# Convert the dataset to a DataFrame
diabetes_df = pd.DataFrame(data=diabetes_sklearn.data,
                           columns=diabetes_sklearn.feature_names)
print(diabetes_df.head())
# print(diabetes_df.shape)
print("Shape of Sklearn Diabetes Data:", diabetes_df.shape)

# Add target variable to the DataFrame
diabetes_df['target'] = diabetes_sklearn.target

print(diabetes_df.head())
print(diabetes_df.shape)
# print(diabetes_df)

# Print the shape of the feature matrix and target vector
print("Shape of Sklearn Diabetes Data with target:", diabetes_df.shape)

diabetes_df.to_csv('diabetes.csv')


