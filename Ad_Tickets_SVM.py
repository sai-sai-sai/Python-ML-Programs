# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 13:10:42 2017

@author: Sai_Chedemala
"""

import numpy as np
import pandas as pd
import pickle as pk


#Read the data set into memory
tickets = pd.read_excel('E:/My Data/MANA/Adient_Ticket_Dump_Latest - Copy.xlsx')
tickets.head()
tickets.shape # (219488 rows, 27/41 columns)
tickets.columns = tickets.columns.str.replace(' ','_')
tickets.rename(columns = {'ColX':'Unkown_COl'},inplace = True)
# Drop unwanted features
tickets.drop(['Work_Item_Description', 
              'Work_Item_Title','Source',
              'Remedy_ID','Assigned_to_User_Date',
              'Assigned_to_User_Time', 
              'Created_Date',#24*7hr support?
              'Created_Time',#24*7hr support?
              'Unkown_COl',
              'Resolution_Type',
              'Resolution_Item',
              'Incident_Resolution_Category', 
              'Incident_Resolution_Description',
              'Service_Request_Implementation_Results',
              'Service_Request_Implementation_Notes'],
               axis = 1,inplace = True)

#We can lamdaizing or use above
tickets.drop(['SLT_Time_To_Own_Status'],axis = 1,inplace = True)
tickets.drop(['Assigned_to_User_Assignments'],axis = 1,inplace = True)
tickets.drop(['Assigned_to_User_City'],axis = 1,inplace = True)
tickets.drop(['Assigned_to_User_Country'],axis = 1,inplace = True)
tickets.drop(['Assigned_to_User'],axis = 1,inplace = True)#useful but delete for now
tickets.drop(['Assigned_to_User_Department'],axis = 1,inplace = True)#useful but delete for now
tickets.drop(['Affected_User'],axis = 1,inplace = True)#useful but delete for now
tickets.drop(['Web_Link'],axis = 1,inplace = True)
tickets.drop(['Assigned_to_User_Global_ID'],axis = 1,inplace = True)#useful but delete for now
tickets.drop(['Status'],axis = 1,inplace = True)
tickets.drop(['Status_Filter'],axis = 1,inplace = True)
# Affected_User_Global_ID has 10k - for now lets drop
tickets.drop(['Affected_User_Global_ID'],axis = 1,inplace = True)#useful but delete for now

#Remianing             
len(tickets.columns)
'''
'Incident_#', 
'App_Group', 
'Topic_Group1',
'Topic_Group2',
'Work_Item_Type',
'Priority',
'Support_Group',
'Urgency',
'Impact',
'CTI_Cateogry',
'CTI_Type',
'CTI_Item',
'Classification',
'SLT_Resolution_Status'
'''

#Count null values per column
s2 = tickets.isnull().sum().sort_values(ascending = False)
#Numerical --> Most occuring , Mean , 

#list of columns with non zero null values
s_nz = s2.iloc[s2.values > 0] # also a series
l_nz = s_nz.keys() # get the cols into a list


# Instead of doing all at once with lambda like above
#Checking what happens when we delete for each columns
#(141643, 26) --- After removing blank Topic_Group2 s
#tickets1 = tickets1.dropna( subset = l_nz[6:10] , how ='any'  , axis = 0)
#tickets = tickets.applymap(lambda x: x != np.nan)
tickets1 = tickets.dropna( subset = ['SLT_Resolution_Status'] , how ='all'  , axis = 0)
tickets1 = tickets1.dropna( subset = ['Impact'] , how ='all'  , axis = 0)
tickets1 = tickets1.dropna( subset = ['Topic_Group2'] , how ='all'  , axis = 0)
tickets1 = tickets1.dropna( subset = ['Classification'] , how ='all'  , axis = 0)
tickets1 = tickets1.dropna( subset = ['CTI_Item'] , how ='all'  , axis = 0)
tickets1 = tickets1.dropna( subset = ['CTI_Type'] , how ='all'  , axis = 0)
tickets1 = tickets1.dropna( subset = ['Urgency'] , how ='all'  , axis = 0)
tickets1 = tickets1.dropna( subset = ['Support_Group'] , how ='all'  , axis = 0)
tickets1 = tickets1.dropna( subset = ['Priority'] , how ='all'  , axis = 0)
tickets1 = tickets1.dropna( subset = ['CTI_Cateogry'] , how ='all'  , axis = 0)
tickets1 = tickets1.dropna( subset = ['Priority'] , how ='all'  , axis = 0)
tickets1 = tickets1.dropna( subset = ['Work_Item_Type'] , how ='all'  , axis = 0)
tickets1 = tickets1.dropna( subset = ['App_Group'] , how ='all'  , axis = 0)
#tickets1 = tickets1.dropna( subset = ['Affected_User_Global_ID'] , how ='all'  , axis = 0)
#tickets1 = tickets1.dropna( subset = ['Assigned_to_User_Department'] , how ='all'  , axis = 0)


#Finally left with
tickets1.shape #(50987, 13)
#now recheck if all zeros are in s2 ie no Nans in any row , col
s2_new = tickets1.isnull().sum().sort_values(ascending = False)
tickets1.columns
tickets1.set_index('Incident_#',inplace = True)
writer = pd.ExcelWriter('output.xlsx')
tickets1.to_excel(writer,'Sheet1')
writer.save()

tickets1.head(5)
tickets1 = tickets1.loc[(tickets1.SLT_Resolution_Status == 'Met') | (tickets1.SLT_Resolution_Status == 'Breached' )]
tickets1.shape#(50806, 13)
tickets1.columns
X = tickets1.iloc[:,0:12]
X.shape
Lcols = X.columns.values
type(Lcols)#array
#unique values in each column
for col in Lcols:
    print(col,len(set(X[col])))
    
# Affected_User_Global_ID has 10k - for now lets drop
#tickets1.drop(['Affected_User_Global_ID'],axis = 1,inplace = True)    

#y = tickets1.loc[:,'SLT_Resolution_Status'] instead of this map it to dictionary
type(mapdict) = { 'Breached' : 1 , 'Met' : 0}
len(y)


X.shape # --> Still a df , or a df with multiple cols/series
y.shape #--> now a series , so each col of a Df is a series

#####################
'''
One Hot Encoder in Scikit <-----
#Codify categorical feats using le ohe
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder as ohe
type(LabelEncoder())
Xenc = X.apply(lambda x: LabelEncoder().fit_transform)
X[:,1]
tickets[:,0:1]
Xemc = X.copy()
mle_x = mle()
X = X.apply(lambda x: mle_x.fit_transform()
ohe_x = ohe()
Xc = ohe_x.fit_transform(X).toarray()
'''
####################### Giving up on LE and OHE
#Try with pandas dummies 

Xd = pd.get_dummies(X)
Xd.shape#(50806, 3077) 3066) 2554 with drop first , 2571 become 10k with global id user
Xd.head()
type(Xd)#not sparse ?
######## End of pre-processing #########
from sklearn import svm as sv

clf = sv.SVC()
clf.fit(Xd, y)  
type(Xd.columns)
len(clf.support_vectors_)#3312/21556 
clf.support_
clf.n_support_
#9962/50806 still good enough 20% ?
ypred = clf.predict(Xd)

cdf = clf.decision_function(Xd)

len(ypred)
# save the model to disk
filename = 'Adie_svm.sav'
pk.dump(clf, open(filename, 'wb'))

filename1 = 'cols'
pk.dump(Xd.columns, open(filename1, 'wb'))

l =  ypred - y



#Set Index practice demo Begin
dict = {
     'name': pd.Series( ['Sai','Vij','Kris'] ,index = (['a','b','c'])  ),
     'age' : pd.Series( ['33','22','12']     ,index = (['a','b','c'])  ), 
    }

df = pd.DataFrame(dict)
df.index
df.columns
df.set_index('name',inplace = True)
df.index
df.head()
#Set Index practice demo End

a = 0
b = 3
df.iloc[a:b,:]

flnm = 'output4.xlsx'
writer1 = pd.ExcelWriter(flnm)
df_ypred = pd.DataFrame(data=ypred)  # 1st row as the column names
df_ypred.to_excel(writer1,'Sheet1')# numpy array cant dowloand directly
