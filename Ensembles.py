# -*- coding: utf-8 -*-
"""
Created on Sun Jun 04 20:18:49 2017

@author: Sai_Chedemala
"""

from pandas import read_csv
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedKFold
#Cart model
from sklearn.tree import DecisionTreeClassifier 

#Cart model baggers
from sklearn.ensemble import BaggingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import ExtraTreesClassifier
#Cart model Boosters
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import GradientBoostingClassifier
#Voting on Various models
from sklearn.ensemble import VotingClassifier
#Submodel1
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC


# load data 
filename = 'pima-indians-diabetes.data.csv'
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class'] 
dataframe = read_csv(filename, names=names)
array = dataframe.values 
X = array[:,0:8] 
Y = array[:,8]
#BaggingClassifier
seed = 7
num_splits = 10
kf = KFold(n_splits = num_splits, random_state = seed)
model  = DecisionTreeClassifier()
#results = cross_val_score(model,X,Y,cv=kf)-->forgot to bag ?
#Bag 1st with 100 such trees
num_trees = 100
bagger_model = BaggingClassifier(base_estimator = model , n_estimators = num_trees , random_state = seed)
#NOw use bagged model (baggermodel)
results = cross_val_score(bagger_model,X,Y,cv=kf)
print(results.mean())
type(results)
results.shape

#W/o Bagging
#Kflod will go into Cross Val Score
#model will go into Cross Val Score as model
#X,y  will go into Cross Val Score

#W/Bagging
#Kflod will go into Cross Val Score
#model will go into Bagger_Model as base esitmator
#Bagger_model will go into Cross Val Score as model (so this is more enriched ie 100 trees insteas of 1 decesion tree)
#X,y  will go into Cross Val Score

#RandomFOrestClassifier
num_trees = 100
skf = StratifiedKFold(n_splits=10,  random_state=seed)
model = RandomForestClassifier(n_estimators = num_trees, max_features = 3 )
results = cross_val_score( model , X , Y, scoring = 'accuracy' , cv = skf)
print(results.mean())# Just Kf is giving better accuracy than skf
type(results)
results.shape

#ExtraTreesClassifier
model = ExtraTreesClassifier(n_estimators = num_trees , max_features = 5)
results = cross_val_score( model , X , Y, scoring = 'accuracy' , cv = kf)
print(results.mean())
type(results)
results.shape

#################BOOSTING#####################
#AdaBoost
model = AdaBoostClassifier(n_estimators = num_trees , random_state = seed)
results = cross_val_score(model,X,Y,cv=kf)
print(results.mean())

 #Stochastic Gradient Boosting
model = GradientBoostingClassifier(n_estimators = num_trees , random_state = seed)
results = cross_val_score(model,X,Y,cv = kf)
print(results.mean())
###########################VOTING####################
#create sub models
list_of_submodels = []
submodel1 = LogisticRegression()
list_of_submodels.append(('LR',submodel1))
submodel2 = DecisionTreeClassifier()
list_of_submodels.append(('DTC',submodel2))
submodel3 = SVC()
list_of_submodels.append(('SVC',submodel3))
#now create an ensemble of the submodels
ensemble = VotingClassifier(list_of_submodels)
results = cross_val_score(ensemble,X,Y,cv = kf)
print(results.mean())
#weights for each model can be given manually or heuristcally 
#More advanced methods can learn how to best weight the predictions from sub-models, 
#but this is called stacking (stacked aggregation) and is currently not 
#provided in scikit-learn
