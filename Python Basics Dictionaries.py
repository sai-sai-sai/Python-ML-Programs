# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 18:13:55 2017

@author: Sai_Chedemala
"""
import pandas as pd
#Series
s = pd.Series(np.random.randn(3),index = (['a','b','c'])  )
s1 = pd.Series(pd.Series(['Test0','Test1','Test2','Test3','Test4','Test5']),
               index = ([0,1,2,3,4]))
s1.get_values()
s1.get_value(4)

#Dictionaries
grades = {'Ana':'B','John':'A+','Denise':'A','Katy':'A'}
doc_term_dict={('d1','t1'):12, ('d2','t3'):10, ('d3','t2'):5}
print(doc_term_dict.keys())
#indexes/Keys are Ana , John , Denise , Katy
#Keys -> Have to be immutable int ,float,str , basic types , unique
#No order of keys 
#values -> can by anything u can imagine , duplicate
del(grades(['Ana']))
print(grades.keys()) #dict_keys(['Ana', 'John', 'Denise', 'Katy'])
print(grades.values()) #dict_values(['B', 'A+', 'A', 'A'])
print(doc_term_dict.keys()) #dict_keys([('d1', 't1'), ('d2', 't3'), ('d3', 't2')])
print(doc_term_dict.values()) #dict_values([12, 10, 5])


grades['Justin'] = 'A'
print(grades)


#1st create a dictiornary
#Another way with series
d = {
     'name': pd.Series( ['Sai','Vij','Kris'] ,index = (['a','b','c'])  ),
     'age' : pd.Series( ['33','22','12']     ,index = (['a','b','c'])  ), 
    }

d['name']['a'] #Sai
d['age']['a'] #33
d.keys()#dict_keys(['name', 'age'])
d.values()# a sai b Vij c Kris 
          # a 33 b 22 c 12
# defining dictionary with lists
dl = {
       'Lcol1':[1,2,3] ,  
       'Lcol2':[11,21,31]   
     }