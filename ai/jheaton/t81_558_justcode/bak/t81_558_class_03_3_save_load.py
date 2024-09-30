from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation
import pandas as pd
import io
import os
import requests
import numpy as np
from sklearn import metrics


save=False
if save:
    save_path = "./jheaton/t81_558_justcode/models"


    df = pd.read_csv(
        "https://data.heatonresearch.com/data/t81-558/auto-mpg.csv", 
        na_values=['NA', '?'])

    cars = df['name']

    # Handle missing value
    df['horsepower'] = df['horsepower'].fillna(df['horsepower'].median())

    # Pandas to Numpy
    x = df[['cylinders', 'displacement', 'horsepower', 'weight',
        'acceleration', 'year', 'origin']].values
    y = df['mpg'].values # regression

    # Build the neural network
    model = Sequential()
    model.add(Dense(25, input_dim=x.shape[1], activation='relu')) # Hidden 1
    model.add(Dense(10, activation='relu')) # Hidden 2
    model.add(Dense(1)) # Output
    model.compile(loss='mean_squared_error', optimizer='adam')
    model.fit(x,y,verbose=2,epochs=100)

    # Predict
    pred = model.predict(x)
    print(pred[0:10])

    # Measure RMSE error.  RMSE is common for regression.
    score = np.sqrt(metrics.mean_squared_error(pred,y))
    print(f"Before save score (RMSE): {score}")

    # save neural network structure to JSON (no weights)
    model_json = model.to_json()
    with open(os.path.join(save_path,"class_03_3_save_load.json"), "w") as json_file:
        json_file.write(model_json)

    # save entire network to HDF5 (save everything, suggested)
    model.save(os.path.join(save_path,"class_03_3_save_load.h5"))

load=True
if load:
    from tensorflow.keras.models import load_model
    df2 = pd.read_csv(
        "https://data.heatonresearch.com/data/t81-558/auto-mpg.csv", 
        na_values=['NA', '?'])
    # Handle missing value
    df2['horsepower'] = df2['horsepower'].fillna(df2['horsepower'].median())
    # Pandas to Numpy
    x2 = df2[['cylinders', 'displacement', 'horsepower', 'weight',
        'acceleration', 'year', 'origin']].values
    y2 = df2['mpg'].values # regression


    load_path = "./jheaton/t81_558_justcode/models"
    model2 = load_model(os.path.join(load_path,"class_03_3_save_load.h5"))
    pred2 = model2.predict(x2)
    # Measure RMSE error.  RMSE is common for regression.
    score = np.sqrt(metrics.mean_squared_error(pred2,y2))
    print(f"After load score (RMSE): {score}")
    print(pred2[0:10])


