# -*- coding: utf-8 -*-
"""
Created on Mon May 29 12:34:09 2017

@author: Sai_Chedemala
"""
import pandas as pd
from sklearn.linear_model import LogisticRegression as LoR

from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score 
from sklearn.model_selection import LeaveOneOut
from sklearn.model_selection import ShuffleSplit
#MEtrics
from sklearn  import metrics as m


filename = 'pima-indians-diabetes.data.csv'
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']

df = pd.read_csv(filename, names = names)
array = df.values
X = array[:,0:8]
y = array[:,8]


seed = 7


#Split the data into train and test sets
test_size = 0.33
X_train , X_test , y_train , y_test = train_test_split(X,y,test_size = test_size,
                                                       random_state = seed)
#Initialize model
model = LoR()
#Fit the model with training data
model.fit(X_train,y_train)
result = model.score(X_test, y_test)
#LoR.score method Returns the mean accuracy on the given test data and labels.
print("Accuracy: %.2f%%") %(result*100.0)

# So say you want to predict and evaluate then
y_pred = model.predict(X_test)

from sklearn  import metrics as m
print(m.confusion_matrix(y_test, y_pred))
print(m.accuracy_score(y_test, y_pred))
print(m.recall_score(y_test, y_pred))
print(m.precision_score(y_test, y_pred))
print(m.ravel())

cm = m.confusion_matrix(y_test, y_pred)
cm.shape
type(cm)



#Accuracy -->Your total correct predictions / Actual target values
#recall_score --> ?
#precision_score --> ?
#accuracy_score  --> ?

#Kfold
num_folds = 10
kfold = KFold(n_splits = num_folds , random_state = seed)
model = LoR()
results = cross_val_score(model,X,y,cv=kfold)
print(results)
print(results.mean())
print("Accuracy: %0.3f%% (%0.3f%%)") %(results.mean()*100 , results.std()*100.0)

#Loo
loocv = LeaveOneOut()
model1 = LoR()
results = cross_val_score(model1, X, y, cv=loocv)
print("Accuracy: %.3f%% (%.3f%%)") % (results.mean()*100.0, results.std()*100.0)

#Random Train Test splits
n_splits = 10
test_size = 0.33
seed = 7
kfold = ShuffleSplit(n_splits = n_splits ,  test_size = test_size , random_state = seed)
model = LoR()
results = cross_val_score(model,X,y,cv=kfold)
print("Accuracy: %.3f%% (%.3f%%)") % (results.mean()*100.0, results.std()*100.0)


