# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 15:55:08 2017

@author: Sai_Chedemala
"""

import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer
#from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfTransformer , TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy.linalg as LA
from sklearn.cluster import KMeans

rf = pd.read_csv('CleansedData.csv',names=['RepID','RepCols'],index_col = 0)
rf_X = rf['RepCols']


tfidf_vectorizer = TfidfVectorizer(use_idf=False)
tfidf_matrix = tfidf_vectorizer.fit_transform(rf_X) #(401, 1336)
vocab = tfidf_vectorizer.get_feature_names()#1336 length

num_clusters = 5
km = KMeans(n_clusters=num_clusters)
km.fit(tfidf_matrix)
clusters = km.labels_.tolist()

#Map the clusters to the actual data loaded
rf['cl_no'] = clusters

#Visulaizations of excel download -
# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('rf clusters.xlsx', engine='xlsxwriter')
# Convert the dataframe to an XlsxWriter Excel object.
rf.to_excel(writer, sheet_name='Clusters')
# Close the Pandas Excel writer and output the Excel file.
writer.save()
