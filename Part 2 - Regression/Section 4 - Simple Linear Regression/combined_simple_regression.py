# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 22:03:40 2018

@author: Hrishika
"""

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Salary_Data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values

# Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size = 0.8, random_state = 0)

#For simple regression the library handles feature scaling
#Import linear regression library
from sklearn.linear_model import LinearRegression
sim_reg = LinearRegression()

#Train the simple linear regressor on the training set
sim_reg.fit(X_train, y_train)

#Testing the regressor on the test set
y_predicted = sim_reg.predict(X_test)

#Plot the results test vs predicted
#Plot the training set
plt.scatter(X_train, y_train, color= 'red')
plt.plot(X_train, sim_reg.predict(X_train), color='blue')
plt.title('Salary vs Experience (Training set results)')
plt.xlabel('Experience in Years')
plt.ylabel('Salary')
plt.show()

#Plot the test set
plt.scatter(X_test, y_test, color= 'red')
plt.plot(X_train, sim_reg.predict(X_train), color='blue')
plt.title('Salary vs Experience (Test set results)')
plt.xlabel('Experience in Years')
plt.ylabel('Salary')
plt.show()

