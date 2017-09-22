# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 19:52:01 2017

@author: Sai_Chedemala
"""

import pandas as pd
from sklearn.naive_bayes import GaussianNB as GNB
#from sklearn.cross_validation import train_test_split as tts -- depricated cv

from sklearn.model_selection import train_test_split as tts

filename = 'pima.csv'
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
df = pd.read_csv(filename, names = names)
array = df.values
X = array[:,0:8]
y = array[:,8]
seed = 7

X_train, X_test, y_train, y_test = tts(X, y, random_state=4)
X_train.shape
X_test.shape
y_train.shape
y_test.shape

model = GNB()#priors  = default better to leave
model.fit(X_train,y_train)

