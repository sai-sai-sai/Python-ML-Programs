# -*- coding: utf-8 -*-
"""
Created on Tue May 23 15:17:35 2017

@author: Sai_Chedemala
"""

#Univariate Plots

# Univariate Histograms from matplotlib 
from matplotlib import pyplot
from pandas import read_csv
import numpy as np
filename = 'pima-indians-diabetes.data.csv' 
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class'] 
df = read_csv(filename, names=names) 
df.head()
df['mass'].median()
df['mass'].describe()

#Histogram
df['mass'].hist() 
pyplot.show()
#Density function
df['mass'].plot(kind='bar', subplots=True, layout=(3,3), sharex=False)
pyplot.show()

#Multivariate Plots
correlations = df.corr()

# plot correlation matrix 
fig = pyplot.figure()
ax = fig.add_subplot(111)
cax = ax.matshow(correlations, vmin=-1, vmax=1)
ticks = np.arange(0,9,1) 
ax.set_xticks(ticks) 
ax.set_yticks(ticks)
ax.set_xticklabels(names)
ax.set_yticklabels(names)
pyplot.show()


fig = pyplot.figure()
ax = fig.add_subplot(111)
cax = ax.matshow(correlations, vmin=-1, vmax=1)
fig.colorbar(cax)
pyplot.show()