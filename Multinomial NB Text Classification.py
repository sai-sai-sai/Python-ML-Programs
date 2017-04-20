# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 11:55:14 2017

@author: Sai_Chedemala
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB 


rf = pd.read_csv('rf clusters.csv',names=['RepID','RepCols','cl_no'],skiprows=[0],index_col = 0)
rf_X = rf['RepCols'] 
cls = rf['cl_no']
vect = CountVectorizer()
vect.fit(rf_X)
dims = vect.get_feature_names()
dims.__len__()#1337

rf_dtm = vect.transform(rf_X)
rf_dtm.shape# (402, 1337) , 1 record error titles
type(rf_dtm)# scipy.sparse.csr.csr_matrix
print(rf_dtm)# non zeros locations and contents of non zeros save memory i guess?


rf_Ddtm = rf_dtm.toarray()# to dense why to do this looks like same D = dense
rf_Ddtm.shape# (402, 1337)
type(rf_Ddtm)#numpy.ndarray
print(rf_Ddtm)
df_dtm = pd.DataFrame(rf_Ddtm,columns = dims)
type(df_dtm)#pandas.core.frame.DataFrame
df_dtm.shape# (402, 1337)
print(df_dtm)

mnb = MultinomialNB()#knn not working , may be good for vertical exampls where b<l,this is fat
y_cl = mnb.fit(rf_Ddtm,cls)

#######################################################


test_rf = pd.read_csv('Test RR.csv',names=['RepID','RepCols'],skiprows=[0],index_col = 0)
test_rf.head(10)    
test_rf_X = rf['RepCols'] 
test_rfdtm = vect.transform(test_rf_X).toarray()
test_predict_y_cl = mnb.predict(test_rfdtm)
test_predict_y_cl.shape
test_predict_y_cl.__len__()

test_rf['pred_cl'] = test_predict_y_cl# 41 wrong predictions out of 402

#Visulaizations of excel download 
# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('rf pred cl.xlsx', engine='xlsxwriter')
# Convert the dataframe to an XlsxWriter Excel object.
test_rf.to_excel(writer, sheet_name='Predict')
# Close the Pandas Excel writer and output the Excel file.
writer.save()








