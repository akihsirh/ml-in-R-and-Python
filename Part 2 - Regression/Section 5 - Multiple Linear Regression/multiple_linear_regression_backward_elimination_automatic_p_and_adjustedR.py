# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 23:10:14 2018

@author: Hrishika
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 20:55:03 2018

@author: Hrishika
"""

# Data Preprocessing Template

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('50_Startups.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 4].values

# Encoding categorical data
# Encoding the Independent Variable
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X = LabelEncoder()
X[:, 3] = labelencoder_X.fit_transform(X[:, 3])
onehotencoder = OneHotEncoder(categorical_features = [3])
X = onehotencoder.fit_transform(X).toarray()

#Avoiding the dummy variable trap
X = X[:,1:]
"""
Although the linear regression model takes care of dummy variables we should carry out this 
step anyways. Also since the regression library takes care of feature scaling we dont need to carry
out that either
"""

# Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

#Fit multiple linear regression model to the training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

#Test the regressor on the test data
y_pred = regressor.predict(X_test)

#Building backward elimination model
import statsmodels.formula.api as sm

"""
The statsmodel doesnt take into account the x0 constant included in the linear regression model
Hence we need to add a constant column to our matrix of features.
In the below line we use the numpy library append function to add a column of 1's to the 
matrix X
"""
X = np.append(arr = np.ones((50,1)).astype(int), values = X ,axis = 1)

def backwardElimination(x, siglev):
    numPredictors = len(x[0])
    temp = np.zeros(x.shape).astype(int)
    for i in range(0, numPredictors):
        regressor_OLS = sm.OLS(y, x).fit()
        maxVar = max(regressor_OLS.pvalues).astype(float)
        adjR_before = regressor_OLS.rsquared_adj.astype(float)
        if maxVar > siglev:
            for j in range(0, numPredictors - i):
                if (regressor_OLS.pvalues[j].astype(float) == maxVar):
                    temp[:,j] = x[:, j]
                    x = np.delete(x, j, 1)
                    tmp_regressor = sm.OLS(y, x).fit()
                    adjR_after = tmp_regressor.rsquared_adj.astype(float)
                    if (adjR_before >= adjR_after):
                        x_rollback = np.hstack((x, temp[:,[0,j]]))
                        x_rollback = np.delete(x_rollback, j, 1)
                        print (regressor_OLS.summary())
                        return x_rollback
                    else:
                        continue
    regressor_OLS.summary()
    return x
 
SL = 0.05
X_opt_P_R = X[:, [0, 1, 2, 3, 4, 5]]
X_Modeled_P_R = backwardElimination(X_opt_P_R, SL)
