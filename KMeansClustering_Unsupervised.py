''' 

Use Case  : Analyze any new report that is planned to be developed / existing reports planned 
            to be changed, to find similar report already available to save time and cost
Approach  : 1) Cluster the reports data using KMeans clustering algorithm
            2) Train and store the random forest supervised learning model using KMeans clustering output
            3) Predict the cluster a new report might belong using trained random forest learning model
            4) Plot the dendogram to identify the similar report id

This python code will address the step#1 of the above approach

Author(s) : Sai Krishna Chedemala and Kiran Muppala for Reports Rationalization Proof of Concept
Date      : 1-Mar-2017

'''

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer , TfidfVectorizer
from sklearn.cluster import KMeans

## Read cleaned reports data that contains report id and report column names / report heading
rf = pd.read_csv('CleansedReportsData_0.csv',names=['RepID','RepCols'],skiprows=[0],header=None)
rf_X = rf['RepCols']

## Vectorize the report details to feed into KMeans clustering algorithm
tfidf_vectorizer = TfidfVectorizer(use_idf=False)
tfidf_matrix = tfidf_vectorizer.fit_transform(rf_X) 

## Initialize number of clusters to 5 and fit the vectorized data to KMeans clustering
num_clusters = 5
km = KMeans(n_clusters=num_clusters)
km.fit(tfidf_matrix)
clusters = km.labels_.tolist()

## Map the clusters to the actual data loaded
rf['cl_no'] = clusters

## Store the KMeans clustering output in csv file. This output will be fed into learning model in step#2
header = ["RepID","RepCols","cl_no"]
rf.to_csv('ClusteredReportsData_1.csv',columns=header,index=False)