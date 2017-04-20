# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 12:06:35 2017

@author: Sai_Chedemala
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
#Dataframe - 2 d , different dtyp cols , like an excel or itab , with a key
#Generic form
#   Dictionary = {
#                'Column_name1' :pd.Series([PyList1])
#                'Column_name2' :pd.Series([PyList2])
#                    .
#                    .
#                    .
#                'Column_namen' :pd.Series([PyListn])
#                }
#df = pd.DataFrame(Above Dictionary)

#or 
dict = { 'Col1':[10,20],'Col2':[1,2]}

#1st create a dictiornary with different cols
d = {
     'name': pd.Series( ['Sai','Vij','Kris'] ,index = (['a','b','c'])  ),
     'age' : pd.Series( ['33','22','12']     ,index = (['a','b','c'])  ), 
    }

d['name']['a'] #Sai
d['age']['a'] #33

d.keys()#dict_keys(['name', 'age'])
d.values()# a sai b Vij c Kris a 33 b 22 c 12
#then create a df out of the dictionary with different cols
df = pd.DataFrame(d)   
#  age name
#a  33  Sai
#b  22  Vij
#c  12  abc     

df['name']


d1 = {
     'name': pd.Series( ['Sai','Vij','Kris']   ),
     'age' : pd.Series( ['33','22','12']       ), 
     }
df1 = pd.DataFrame(d1)   # auto indexed with number indexes starting at 0 as usual
df1['newcol'] = ['a','b','c']
#  age  name
#0  33   Sai
#1  22   Vij
#2  12  Kris

rf = pd.read_csv('CleansedData.csv',names=['RepID','RepCols'],index_col = 0)
rf_X = rf['RepCols'] 
l = rf['RepID']




