# -*- coding: utf-8 -*-
"""
Created on Wed May 31 21:05:49 2017

@author: Sai_Chedemala
"""

import pandas as pd
from sklearn.linear_model import LogisticRegression as LoR
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LdA
from sklearn.neighbors import KNeighborsClassifier as KnC
from sklearn.naive_bayes import GaussianNB as GNB
from sklearn.tree import DecisionTreeClassifier as DTC
from sklearn.svm import SVC as svc
from sklearn.ensemble import RandomForestClassifier as rf


from sklearn.model_selection import cross_val_score 



from sklearn.model_selection import KFold
filename = 'pima-indians-diabetes.data.csv'
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']

df = pd.read_csv(filename, names = names)
array = df.values
X = array[:,0:8]
y = array[:,8]
seed = 7

#Kfold
num_folds = 10
kfold = KFold(n_splits = num_folds , random_state = seed)
model = LoR()
#model = LdA()
#model = KnC()
#model = GNB()
#model = DTC()
#model = svc()
model = rf()
results = cross_val_score(model,X,y,cv=kfold)
print(results)
print(results.mean())
print("Accuracy: %0.3f%% (%0.3f%%)") %(results.mean()*100 , results.std()*100.0)