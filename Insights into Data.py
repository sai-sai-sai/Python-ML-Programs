# -*- coding: utf-8 -*-
"""
Created on Sun May 21 21:22:35 2017

@author: Sai_Chedemala
"""

from pandas import read_csv
from pandas import set_option as so
import pandas as pd

filename = "pima-indians-diabetes.data.csv" 
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
df_data = pd.read_csv(filename, names=names)
peek = df_data.head(20)
df_data.dtypes
type(df_data)
#Describe function for descriptie stats on features
#reading/printing options with set_option
so('display.width',200)
so('precision',2)

dstats = df_data.describe()
type(dstats)
type(dstats.keys)

#check how skewed ur data is (classification)
class_counts = df_data.groupby('class').size()# how do you know the .size() f()n 
print(class_counts)
#Taking class as the index or grouping by values of class ,
#describe each of the other columns
df_data.groupby('class').describe()
#Taking class as the index or grouping by values of class (0,1) ,
#count each of the other columns
df_data.groupby('class').count()
    
#How many Missing values in each feature/column
df_data.isnull().sum() # gives missing values per coulumn

#Correlation --> magnitude of covariance
correlation = df_data.corr(method='pearson')    
#Skew +ve skew => right , -ve skew => left
skew = df_data.skew()