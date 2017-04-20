''' 

Use Case  : Analyze any new report that is planned to be developed / existing reports planned 
            to be changed, to find similar report already available to save time and cost
Approach  : 1) Cluster the reports data using KMeans clustering algorithm
            2) Train and store the random forest supervised learning model using KMeans clustering output
            3) Predict the cluster a new report might belong using trained random forest learning model
            4) Plot the dendogram to identify the similar report id

This python code will address the step#2 of the above approach

Author(s) : Kiran Muppala and Sai Krishna Chedemala for Reports Rationalization Proof of Concept
Date      : 1-Mar-2017

'''

import pandas as pd
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier

## Build the training model using clustered reports data
## Input data contains the report id, report details (headings) and cluster number based on Kmeans clustering
traindata = pd.read_csv('ClusteredReportsData_1.csv',names=['RepID','RepCols','cl_no'],skiprows=[0],header=None)
reportsdata = traindata['RepCols'] 
clustername = traindata['cl_no']

## Vectorize the reports data to feed into the training model
vect = CountVectorizer()
vect.fit(reportsdata)
rf_dtm = vect.transform(reportsdata)
rf_Ddtm = rf_dtm.toarray()

## Train the RandomForest supervised classification model
rf = RandomForestClassifier(n_estimators=100) # initialize
rf.fit(rf_Ddtm, clustername) # fit the data to the algorithm

## Store the trained model 
with open('RandomForestTrainedModel', 'wb') as f:
    pickle.dump(rf, f)

from sklearn.externals import joblib
joblib.dump(vect,  'vect.pkl')

help(import)

