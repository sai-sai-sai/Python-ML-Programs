# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
# import load_iris function from datasets module
from sklearn.datasets         import load_iris as ir
from sklearn.neighbors        import KNeighborsClassifier as knn #Knn
from sklearn.cross_validation import train_test_split as tts

from sklearn         import metrics as m
from sklearn.metrics import recall_score as recall 
from sklearn.metrics import precision_score as precision


iris = ir()
type(iris)# It is a bunch

print(iris.data)
type(iris.feature_names)
print(iris.target)
print(iris.target_names)


# store feature matrix in "X"
X = iris.data
type(X)
X.shape
# store response vector in "y"
y = iris.target
type(y)
y.shape

#150 rows , 38 for testing , 112 training 33% split
# use train/test split with different random_state values
X_train, X_test, y_train, y_test = tts(X, y, random_state=4)
print(X_train.shape,y_train.shape,X_test.shape,y_test.shape)

#Initializing our Knn clasifier object
#1st initailz ur object
kn_clf = knn(n_neighbors=5)
kn_clf.fit(X_train, y_train)
y_pred = kn_clf.predict(X_test)
print(m.confusion_matrix(y_test, y_pred))


#Accuracy -->Your total correct predictions / Actual target values
#recall_score
#precision_score
#accuracy_score

# simulate splitting a dataset of 25 observations into 5 folds
from sklearn.cross_validation import KFold
kf = KFold(25, n_folds=5, shuffle=False)
kf
print('{} {:^61} {}'.format('Iteration', 'Training set observations', 'Testing set observations'))

for iteration, data in enumerate(kf, start=1):
    print(data)
    #print('{:^9} {} {:^25}'.format(iteration, data[0], data[1]))
#
#1000 --> folds = 10 , 100 rec/fold
#1st 9 folds  train data , 10th fold = Test set
#2nd 9 folds  train data , 1st fold  = Test set
#So on....

#2.Cross Val score , Grid Search CV
from sklearn.cross_validation import cross_val_score as cvn

kn_clf_cv = knn(n_neighbors=5)
#NOt passing Xtrain and Y train 
scores = cvn(kn_clf_cv, X, y, cv=10, scoring='accuracy')
print(scores)
print(scores.mean())



# search for an optimal value of K for KNN
k_range = list(range(1, 31))
k_scores = []
for k in k_range:
    kn_clf_cv = knn(n_neighbors=k)
    scores = cvn(kn_clf_cv, X, y, cv=10, scoring='accuracy')
    k_scores.append(scores.mean())
print(k_scores)


import matplotlib.pyplot as plt
plt.plot(k_range, k_scores)
plt.xlabel('Value of K for KNN')
plt.ylabel('Cross-Validated Accuracy')

#Grid Search CV
param_grid = dict(n_neighbors=k_range)
type(param_grid)#dict

from sklearn.grid_search import GridSearchCV as gscv
kn_clf_gscv = knn()
grid = gscv(kn_clf_gscv, param_grid, cv=10, scoring='accuracy')
# fit the grid with data
grid.fit(X, y)
grid.grid_scores_

# examine the best model
print(grid.best_score_)
print(grid.best_params_)
print(grid.best_estimator_)



    












