# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 17:08:41 2018

@author: Hrishika
"""

#Importing the libraries
"""
Numpy supports large multi dimensional arrays and matrices and also has a large number
of mathematical tools to support operations on these arrays and matrices
"""
import numpy as np

"""
Source Wikipedia - Matplotlib is a plotting library for the Python programming language and its
numerical mathematics extension NumPy. It provides an object-oriented API for embedding plots 
into applications using general-purpose GUI toolkits like Tkinter, wxPython, Qt, or GTK+.
"""
import matplotlib.pyplot as plt

"""
Source - Wikipedia 
pandas is a Python package providing fast, flexible, and expressive data structures designed to 
make working with “relational” or “labeled” data both easy and intuitive. It aims to be the 
fundamental high-level building block for doing practical, real world data analysis in Python
"""
import pandas as pd

dataset = pd.read_csv("Data.csv")

#Create matrix of features
X = dataset.iloc[:,:-1].values
#Create dependent variable vector
Y = dataset.iloc[:,-1].values

#Handle missing data 
from sklearn.preprocessing import Imputer
"""
Create an imputer object that will replace missing data for age and salary in the dataset with 
the mean of the values along that column. Use ctrl + I to check the Imputer info
"""
imputer = Imputer(missing_values='NaN', strategy='median', axis = 0)
#Customize the imputer to fill in missing values for columns age and salary. Columns in X
#must range from starting index to index -1 
imputer = imputer.fit(X[:, 1:3])
X[:, 1:3] = imputer.transform(X[:, 1:3])
print(X)

#Encode categorical data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X_country = LabelEncoder()
X[:,0] = labelencoder_X_country.fit_transform(X[:,0])
print(X)

"""
Since the countries are represented by numbers it may confuse the machine learning algorithm
to think that there is an inherent ordering in the countries ie France is greater than Germany
and so on. Therefore we need to create dummy variables ie make as many columns as there are 
categories so that we have 1 when we have France but 0 in the columns for Germany and Spain
"""
onehotencoder = OneHotEncoder(categorical_features=[0])
X = onehotencoder.fit_transform(X).toarray()
print(X)

#Encode the categorical variable in the output vector
labelencoder_Y_purchased = LabelEncoder()
Y = labelencoder_Y_purchased.fit_transform(Y)
print(Y)

#Split the data into a training set and a test set 
from sklearn.cross_validation import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size = 0.2, random_state = 0)

#Feature Scaling - you can use standardisation and normalization
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()

#We shouldnt be scaling the dummy variables
X_train[:,3:5] = sc_X.fit_transform(X_train[:,3:5])
X_test[:,3:5] = sc_X.transform(X_test[:,3:5])

"""
for this dataset we dont need to scale the output vector since its a classification problem
Purchased - yes and no
In case of regression where the outputs can also vary largely in range we need to scale 
"""





