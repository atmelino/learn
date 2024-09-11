from sklearn.metrics import mean_squared_error
y_true = [3, -0.5, 2, 7]
y_pred = [2.5, 0.0, 2, 8]

y_true = [1,2,3,4]
y_pred = [1,2,3,5]


mse=mean_squared_error(y_true, y_pred)
print(mse)


