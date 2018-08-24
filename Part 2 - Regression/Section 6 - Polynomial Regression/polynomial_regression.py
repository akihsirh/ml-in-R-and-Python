# -*- coding: utf-8 -*-
"""
Created on Sat Aug 25 01:06:37 2018

@author: Hrishika
"""


# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('PositionSalaries.csv')
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
from sklearn.preprocessing import PolynomialFeatures
poly_regressor = PolynomialFeatures(degree = 4)
X_nomial = poly_regressor.fit_transform(X)
"""
The new matrix in the above line is given not only a new column with degree 2 terms but also 
a column for the intercept
"""
from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(X_nomial,y)

#Plot the results of the polynomial regression
X_plot = np.arange(min(X),max(X),0.1)
X_plot = X_plot.reshape(len(X_plot),1)
plt.scatter(X,y,color = 'Blue')
plt.plot(X_plot, lin_reg.predict(poly_regressor.fit_transform(X_plot)), color = 'Red')
plt.xlabel('Position Levels')
plt.ylabel('Salaries')
plt.title('Salaries based on position predictor')

#Predict a salary for a custom position level
lin_reg.predict(poly_regressor.fit_transform(6.5))