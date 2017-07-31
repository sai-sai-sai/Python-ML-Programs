# -*- coding: utf-8 -*-
"""
Created on Thu May 25 21:47:03 2017

@author: Sai_Chedemala
"""

#Feature Selection

#Univariate Selection. - Statisctical method called Chi 2


from pandas import read_csv
from pandas import set_option as so
#SKB
from sklearn.feature_selection import SelectKBest as skb
from sklearn.feature_selection import chi2
#RFE 
from sklearn.feature_selection import RFE 
from sklearn.linear_model import LogisticRegression
import pandas as pd
#
from sklearn.decomposition import PCA

filename = "pima-indians-diabetes.data.csv" 
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
df_data = pd.read_csv(filename, names=names)
df_data.shape
df_data.columns
dataframe = read_csv(filename, names=names)
array = dataframe.values 
X = array[:,0:8] 
y = array[:,8]

l = [1,4,5,7]
X_4cols = X[:,l]


#Select K best using Chi 2
obj = skb(score_func = chi2, k = 5)
fit1 = obj.fit(X,y)
fit1.scores_  # actual chi values for each feature - need to calculate and check
fit1.pvalues_ # p values for each feature
New_X = best_5_features = fit1.transform(X)

#RFE 
model = LogisticRegression()
rfe = RFE(model,3)
fit = rfe.fit(X,y)
print("Num Features: %d") % fit.n_features_ 
print("Selected Features: %s") % fit.support_ 
print("Feature Ranking: %s") % fit.ranking_
#Num Features: 3 
#Selected Features: [ True False False False False True True False] 
#Feature Ranking: [1 2 3 5 6 1 1 4]




# feature extraction
pca = PCA(n_components = 5)
fit = pca.fit(X)
# summarize components
print("Explained Variance: %s") % fit.explained_variance_ratio_ #(5 ratios 1/component)
#Explained Variance: [ 0.88854663  0.06159078  0.02579012  0.01308614  0.00744094]

print(fit.components_) #Array    
#(5 X 8) So the rows are reduced from 768 to just 5 rows,same number of columns
fit.components_.shape 
#[[ -2.02176587e-03   9.78115765e-02   1.60930503e-02 ...,   1.40108085e-02
#    5.37167919e-04  -3.56474430e-03]
# [ -2.26488861e-02  -9.72210040e-01  -1.41909330e-01 ...,  -4.69729766e-02
#   -8.16804621e-04  -1.40168181e-01]
# [ -2.24649003e-02   1.43428710e-01  -9.22467192e-01 ...,  -1.32444542e-01
#   -6.39983017e-04  -1.25454310e-01]
# [ -4.90459604e-02   1.19830016e-01  -2.62742788e-01 ...,   1.92801728e-01
#    2.69908637e-03  -3.01024330e-01]
# [  1.51612874e-01  -8.79407680e-02  -2.32165009e-01 ...,   2.14744823e-02
#    1.64080684e-03   9.20504903e-01]]









