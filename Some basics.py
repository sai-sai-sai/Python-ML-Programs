# -*- coding: utf-8 -*-
"""
Created on Wed May 24 20:55:08 2017

@author: Sai_Chedemala
"""

mydict = {'a': (1,4,5), 'b': 2, 'c': 3} 
print("A value: %d" % mydict['a'])
mydict['a'] = 11 
print("A value: %d" % mydict['a'])
print("Keys: %s" % mydict.keys()) 
print("Values: %s" % mydict.values()) 
for key in mydict.keys(): 
    print(mydict[key])
#dictionary['name of key'] --> will print value(s) for that key
#If more than one value for a particular key , then give them as tupple

for i in range(23):
    print(i)

l = [[1,2,3,4],[12,13,14,15]]
l.append([21,22,23,24])
l[4][2]
l1 = l
l2 = l + l1
 
import numpy as np
#list to array is like converting/pasting rows to columns
a = np.array(l)
a1 = np.array(l1)
a.shape
a[1,1]
a2 = a + a1
a3 = a1 * a1
m = np.matrix(l)
mt = np.transpose(m)
    
import matplotlib.pyplot as plt
myarray = np.array([1, 22 , 23]) 
plt.plot(myarray)
plt.scatter(myarray,myarray)
plt.show()


import numpy 
import pandas 
myarray = numpy.array([1, 2, 3]) 
rownames = ['a', 'b', 'c'] 
myseries = pandas.Series(myarray, index=rownames)
