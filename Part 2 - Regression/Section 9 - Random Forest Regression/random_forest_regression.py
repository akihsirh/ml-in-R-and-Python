# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 00:22:08 2018

@author: Hrishika
"""

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values

#Not splitting the dataset into training and test because the dataset is too small
#Feature scaling is not required since this model does not depend on Euclidean distances

#Build the regressor
from sklearn.ensemble import RandomForestRegressor
 regressor = RandomForestRegressor(n_estimators= 300, random_state= 0)
regressor.fit(X,y)


# Predicting a new result
y_pred = regressor.predict(6.5)

# Visualising the Random Forest Regression results (higher resolution)
X_grid = np.arange(min(X), max(X), 0.01)
X_grid = X_grid.reshape((len(X_grid), 1))
plt.scatter(X, y, color = 'red')
plt.plot(X_grid, regressor.predict(X_grid), color = 'blue')
plt.title('Truth or Bluff (Random Forest Regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()