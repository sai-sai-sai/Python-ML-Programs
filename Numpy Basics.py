# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 09:49:22 2017

@author: Sai_Chedemala
"""
from __future__ import division #to over come intiger division of/in nympy lists
import numpy as np # for numpy arrays
import pylab as pl # for plotting
import scipy.stats as scs#(from scipy import stats)

 
#Numpy array is just another data type like Python List

PyList1 = (1,2,3,4,5)#tupple
PyList2 = [11,12,13,14,15]
PyList3 = [11,12,13,14,15,PyList2]

print(type(PyList2))
#Numpy Array
NpList = np.array([PyList1,PyList2])
print(type(NpList))
NpList.shape

# To do Math ops on lists , you have to iterate , you cant vectorzie
# with Numpy Arrays you can vectorize
A = np.array([1,2,3,4])
B = np.array([11,12,13,14])
B2 = np.array([[11,12,13,14],[21,22,23,24]]) # - Multidim array

print(B.ndim)#1
print(B2.ndim)#2
print(np.shape(B2))#(2,4)

c = A + B # =  array([12, 14, 16, 18])
c = A * B # = array([11, 24, 39, 56])
c = A.dot(B) # = 130 , Matrix multiplication [1x4] * [4x1]
c = A@B# = 130 , At operator ,Matrix multiplication [1x4] * [4x1]
c = np.sin(A)
pl.plot(c)
# Accessing elts of an array
print(B2[0][1],B2[1,0])
#generate random numbers
r = np.random.randn(2,5) # 2x5 matrix of random numbers
Bt = B2.transpose()
F = B2.dot(Bt)
Bt1 = np.array([[11,21],[12,22],[13,23],[14,24]])
Bt1.transpose()
#Statistical operations on Python lists using Numpy
np.mean(PyList2) #will cast the python list as a numpy array
np.median(PyList2)
np.std(NpList)#directly on a numpy array

# Random Nus
a = np.random.randn(100)
np.shape(a)
np.reshape(a,4,19)

#Numpy Operations
A = np.array(([1,2],[3,4]))
Ainv = np.linalg.inv(A)
B = np.array([[9,7],[5,6]])

# Scipy - 
#Find the probability density of zero from standard normal distribution
scs.norm.pdf(0)#0.3989422804014327
# if you have a Gaussian with say mean = 5 and std.deviation = 10(scale)
scs.norm.pdf(0, loc = 5 , scale = 10)# 0.035206532676429952 smaller 
# if you want to calculate PDF for all and each individual elts in a matrix
r = np.random.randn(10)# array
scs.norm.pdf(r)
# Log of PDF
scs.norm.logpdf(r) # Log PDF is used in joint probablities and also in gausian PDF
#using Log in these cases is faster as multiplication becomes addition and exponential 
#is replacecd with log respectively
