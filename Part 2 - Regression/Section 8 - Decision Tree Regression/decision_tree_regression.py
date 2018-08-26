# -*- coding: utf-8 -*-
"""
Created on Sun Aug 26 22:35:06 2018

@author: Hrishika
"""

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Position_Salaries.csv')

"""
Since we want the input to be a matrix of features we specify 1:2 rather than just 1
Theoretically the code 1:2 means all columns from 1 excluding 2 which works out the same logically
as simply selecting 1. 
However when we write 1:2 Python treats it as a matrix, rather than as a vector when its given 1 alone
"""
X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values

#Since we dont have a large dataset we wont be splitting it into a training and test set
#Also feature scaling is not reqiured since the linear regression library handles feature scaling
#Build the regressor
from sklearn.tree import DecisionTreeRegressor
regressor = DecisionTreeRegressor(random_state=0)
regressor.fit(X,y)

#Predict a result
regressor.predict(6.5)

#Plot the results of the polynomial regression
X_grid = np.arange(min(X), max(X),0.01)
X_grid = X_grid.reshape(len(X_grid),1)
plt.scatter(X,y,color = 'Blue')
plt.plot(X_grid, regressor.predict(X_grid), color = 'Red')
plt.xlabel('Position Levels')
plt.ylabel('Salaries')
plt.title('Salaries based on position predictor')
plt.show()