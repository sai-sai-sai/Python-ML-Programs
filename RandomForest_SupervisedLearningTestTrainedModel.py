''' 

Use Case  : Analyze any new report that is planned to be developed / existing reports planned 
            to be changed, to find similar report already available to save time and cost
Approach  : 1) Cluster the reports data using KMeans clustering algorithm
            2) Train and store the random forest supervised learning model using KMeans clustering output
            3) Predict the cluster a new report might belong using trained random forest learning model
            4) Plot the dendogram to identify the similar report id

This python code will address the step#3 of the above approach

Author(s) : Kiran Muppala and Sai Krishna Chedemala for Reports Rationalization Proof of Concept
Date      : 1-Mar-2017

'''

import pandas as pd
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.externals import joblib

## Import the trained model
with open('RandomForestTrainedModel', 'rb') as f:
    rf = pickle.load(f)
    

## Test the trained model for accuracy
## The input file contains test data - the report id, report details (headings) same as training data

## *** this model has to be tested again using random data **

testdata = pd.read_csv('Test RR.csv',names=['RepID','RepCols','cl_no'],skiprows=[0],header=None)
testArr = testdata['RepCols']

## Vectorize the reports data to feed into the training model
vect = CountVectorizer()
vect1 = joblib.load('vect.pkl')

test_rfdtm = vect1.transform(testArr).toarray()
test_rfdtm.shape

## Predict the clusters for the reports data in the test dataset using trained model
results = rf.predict(test_rfdtm)
from sklearn.metrics import confusion_matrix
#cant really do it here


## Compare the predictions with the training data side by side
testdata['predictions'] = results

## Download the predicted outcome into a csv file along with training data for comparison
header = ["RepID","RepCols","cl_no","predictions"]
testdata.to_csv('ReportsPredictionOutput_3.csv',columns=header,index=False)
