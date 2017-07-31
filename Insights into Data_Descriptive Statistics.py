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
peek = df_data.tail()#1
df_data.shape#2
types = df_data.dtypes#3
type(df_data['preg'])
df_data['preg'].describe()#3
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
df_data.isnull().sum() # gives missing values per coulumn(NaN)
#Correlation --> magnitude of covariance
correlation = df_data.corr(method='pearson')    
#Skew 
skew = df_data.skew()
#Doubt-Knowing that an attribute has a skew may allow you to perform data preparation to correct the skew and later improve the accuracy of your models.
#What corrective action should we take to correct the skew , wont it affect training overfitting
