# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 16:45:34 2017

@author: Sai_Chedemala
"""

import theano as th
from theano import tensor as t
import os
import inspect

#declare 2 symbolic floating point variables (tensor variables)
a = t.dscalar()
b = t.dscalar()
#Symbolic expression
c = a + b
#function 
f = th.function([a,b],c)
result = f(1.5,2.4)
type(result)
result.shape
binding = {a: 1.5, b: 2.5}
type(binding)


import tensorflow as tf    
print(os.path.dirname(inspect.getfile(tf)))
#C:\Users\sai_chedemala\AppData\Local\Continuum\Anaconda2\
#envs\devi_3.5\lib\site-packages\tensorflow

# declare two symbolic floating-point scalars
a = tf.placeholder(tf.float32) 
b = tf.placeholder(tf.float32)
# create a simple symbolic expression using the add function
add = tf.add(a, b)
# bind 1.5 to 'a', 2.5 to 'b', and evaluate 'c
sess = tf.Session()
binding_dict = {a:1.5 , b:2.5}
c = sess.run(add,feed_dict = binding_dict)
print(c)
