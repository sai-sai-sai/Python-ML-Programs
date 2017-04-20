# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 14:03:04 2017

@author: Sai_Chedemala
"""
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer
#from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy.linalg as LA

rf = pd.read_csv('Test RR.csv',names=['RepID','RepCols'],skiprows=[0],index_col = 0)
rf_X = rf['RepCols'] 
rf_X.shape
type(rf_X)

#l = rf['RepID']

#Numerical Vectoriziation of text using tfidf or just countvectorizer bow
#corpus to vector spcace


cv = CountVectorizer()
bow = cv.fit_transform(rf_X).toarray()
bow.shape
type(bow)
fn = cv.get_feature_names()
#or
tf = TfidfTransformer()
bow_tf = tf.fit_transform(bow).toarray()
bow_tf.shape
type(bow_tf)

# if not passing distance matrix behaves like single linkage
#why why?  
dist =  cosine_similarity(bow)# or 1 minus same thing
dist.shape

dist_tf =  cosine_similarity(bow_tf)# or 1 minus same thing
dist_tf.shape



import scipy.cluster.hierarchy as sch

Z = sch.linkage(dist,'ward')
Z = sch.linkage(bow,'ward')

fig, dr = plt.subplots(figsize=(25  , 30)) # set size

#linkm = ward
#dr = sch.dendrogram(sch.linkage(bow,method = 'ward'),orientation = 'top',labels= rf.index)
dr = sch.dendrogram(Z,orientation = 'top',labels= rf.index)
plt.tick_params(\
    axis= 'x',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    bottom='off',      # ticks along the bottom edge are off
    top='off',         # ticks along the top edge are off
    #labelbottom='off'
    )

plt.show() #show plot with tight layout

                
from scipy.cluster.hierarchy import cophenet
from scipy.spatial.distance import pdist

c, coph_dists = cophenet(Z, pdist(dist))




plt.savefig('hcl2.png', dpi=400) #save figure as ward_clusters
plt.close()
