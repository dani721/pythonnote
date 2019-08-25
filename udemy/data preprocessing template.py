# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 11:43:26 2019

@author: 721da
"""

# Data preprocessing template
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# importing the dataset
dataset = pd.read_csv('data.csv') #change data
x = dataset.iloc[:,1].values
y = dataset.iloc[:,3].values # depends on how many variables

# splitting the dataset into the training set and test set
from sklearn.cross_validation import train_test_split
x_trian, x_test, y_train,y_test = train_test_split(x,y,test_size = 0.2,random_state = 0)

#feature scaling
"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
x_train = sc_x.fit_transform(x_train)
x_test = sc_x.transform(x_test)"""