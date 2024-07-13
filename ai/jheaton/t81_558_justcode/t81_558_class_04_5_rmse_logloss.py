from sklearn import metrics
import numpy as np

predicted = [1.1, 1.9, 3.4, 4.2, 4.3]
expected = [1, 2, 3, 4, 5]
score_mse = metrics.mean_squared_error(predicted, expected)
score_rmse = np.sqrt(score_mse)
print("Score (MSE): {}".format(score_mse))
print("Score (RMSE): {}".format(score_rmse))

score_mse = (
    (predicted[0] - expected[0]) ** 2
    + (predicted[1] - expected[1]) ** 2
    + (predicted[2] - expected[2]) ** 2
    + (predicted[3] - expected[3]) ** 2
    + (predicted[4] - expected[4]) ** 2
) / len(predicted)
score_rmse = np.sqrt(score_mse)
print("Score (MSE): {}".format(score_mse))
print("Score (RMSE): {}".format(score_rmse))

from sklearn import metrics

expected = [1, 1, 0, 0, 0]
predicted = [0.9, 0.99, 0.1, 0.05, 0.06]
print(metrics.log_loss(expected, predicted))


import numpy as np

score_logloss = (
    np.log(1.0 - np.abs(expected[0] - predicted[0]))
    + np.log(1.0 - np.abs(expected[1] - predicted[1]))
    + np.log(1.0 - np.abs(expected[2] - predicted[2]))
    + np.log(1.0 - np.abs(expected[3] - predicted[3]))
    + np.log(1.0 - np.abs(expected[4] - predicted[4]))
) * (-1 / len(predicted))
print(f"Score Logloss {score_logloss}")
