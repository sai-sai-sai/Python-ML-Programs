# -*- coding: utf-8 -*-
"""
Created on Thu May  4 13:44:57 2017

@author: Sai_Chedemala
"""

import numpy as np
import pandas as pd
import pickle as pk
#Read the data set into memory
ticketsp = pd.read_excel('E:/My Data/Adient Test Set.xlsx')
ticketsp.head()
ticketsp.shape # (219488, 27/41)
ticketsp.columns = ticketsp.columns.str.replace(' ','_')
ticketsp.rename(columns = {'ColX':'Unkown_COl'},inplace = True)

# Drop unwanted features
ticketsp.drop(['Work_Item_Description', 
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
ticketsp.drop(['SLT_Time_To_Own_Status'],axis = 1,inplace = True)
ticketsp.drop(['Assigned_to_User_Assignments'],axis = 1,inplace = True)
ticketsp.drop(['Assigned_to_User_City'],axis = 1,inplace = True)
ticketsp.drop(['Assigned_to_User_Country'],axis = 1,inplace = True)
ticketsp.drop(['Assigned_to_User'],axis = 1,inplace = True)#useful but delete for now
ticketsp.drop(['Assigned_to_User_Department'],axis = 1,inplace = True)#useful but delete for now
ticketsp.drop(['Affected_User'],axis = 1,inplace = True)#useful but delete for now
ticketsp.drop(['Web_Link'],axis = 1,inplace = True)
ticketsp.drop(['Assigned_to_User_Global_ID'],axis = 1,inplace = True)#useful but delete for now
ticketsp.drop(['Status'],axis = 1,inplace = True)
ticketsp.drop(['Status_Filter'],axis = 1,inplace = True)
# Affected_User_Global_ID has 10k - for now lets drop
ticketsp.drop(['Affected_User_Global_ID'],axis = 1,inplace = True)#useful but delete for now

ticketsp.shape           
ticketsp.set_index('Incident_#',inplace = True)

Xp = ticketsp.iloc[:,0:12]
Xdp = pd.get_dummies(Xp)#,drop_first = True)
Xdp.shape#168501, 6947

filename = 'Adie_svm.sav'
clfp = pk.load(open(filename, 'rb'))
len(clfp.support_vectors_)#same 9962
#yp_pred  = clfp.predict(Xdp)#--> Error

filename1 = 'cols'
cols_train = pk.load(open(filename1, 'rb'))
len(cols_train)

cols_test   = Xdp.columns

#remove extra columns
extracols = set(cols_test) - set(cols_train)
l = list(extracols)
Xdp.drop( l  , axis = 1 , inplace = True) 

#Add missining columns to train
missing_cols = set(cols_train) - set(cols_test)
#Add missining columns to train
for c in missing_cols:
    Xdp[c] = 0


yt_pred  = clfp.predict(Xdp)#--> Memory Error

        
        
    
b = 0
j = 'pred'
fn = " "
for a in range(0,168501,20000):
    if a != 0:
        fn = repr(a)
        fn = j + fn + '.xlsx'
        Xt_pred = Xdp.iloc[b:a,:]
        yt_pred  = clfp.predict(Xt_pred)#--> Memory Error
        #pk.dump(yt_pred, open(fn, 'wb'))
        writer1 = pd.ExcelWriter(fn)
        df_yt_pred = pd.DataFrame(data=yt_pred)  # 1st row as the column names
        df_yt_pred.to_excel(writer1,'Sheet1')#
        print(b,a,fn)
        b = a + 1
    if b == 160001:
        fn = j + repr(b) + '.xlsx'
        Xt_pred = Xdp.iloc[b:168501,:]
        yt_pred  = clfp.predict(Xt_pred)
        #pk.dump(yt_pred, open(fn, 'wb'))
        writer1 = pd.ExcelWriter(fn)
        df_yt_pred = pd.DataFrame(data=yt_pred)  # 1st row as the column names
        df_yt_pred.to_excel(writer1,'Sheet1')#
        print(b,168501,fn)



            




   