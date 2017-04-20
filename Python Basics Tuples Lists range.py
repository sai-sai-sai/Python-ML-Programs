# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 11:07:58 2017
@author: Sai_Chedemala
"""
#***********************************************************************************#
#Tuples
x = (1,2,3)
y = (4,5,x)# nested tuple (1, 2, (1, 2, 3))
te = () #Empty tuple
tu = (2,'one',3) #tuple
#t(1)  = 5# This is ivalid Tuples are imutable
print(tu[2],)#sq.bracket used for indexes and comma at the end of a single value
#tuple actually makes it a tuple instead of just a single value
for i in tu[0:3]:
    print(i)
#***********************************************************************************#
#Tuple can be a collection of multiple tumples
def get_data(aTuple) :
    nums = ()
    words = ()
    for t in aTuple:
        nums = nums + (t[0],)
        if t[1] not in words:
            words = words + (t[1],)
    min_nums = min(nums)
    max_nums = max(nums)
    unique_words = len(words)
    return(min_nums,max_nums,unique_words)  

(small,large,words) = get_data((  (1,'one'),
                                   (2,'three'),
                                   (3,'three')   ))
print(small)
print(large)
print(words)    
#***********************************************************************************#
#Lists ,


L = [4,2,44,33,67,54,'abc',78,99,123,54,111,34] #usually homogenoues,though techincally
                                                #can mix different data types in a list
#iterate a list using indices of the elts of the list
for i in range(len(L)):
    print(L[i])
L.append(5)# only one element can be appended at a time, object.method(),()=call it
L.append([32,3]) # appeds another list to the list L,nested list
L.extend([6,7]) #Extends list with new elts , not apending a list
del(L[16]) # deletes 16th indexed elt in L
L.pop() #removes and returns last elt of the list L
L.remove(78) # removed elt with value 78

#instead of indices iterate through the elts of the list themselves        
for i in L:
    k = str(i)[0]
    if k not in ('a','b','c','d'):
     i += 1
print(L)
# L is [4, 2, 44, 33, 67, 54, 78, 99, 123, 32]
OddL = L[0:len(L):2] # [start:end:x every 2nd/xth element after the current is considered]
print(OddL)#[4, 44, 67, 78, 123] n
evenL = L[1:len(L):2]
CompleteL = OddL + evenL #concatenate
print(L)
#***********************************************************************************#
str = 'sai'
L1 = list(str)#L1 is a list with letters of str as elts of string ['s', 'a', 'i']
print(sorted(L1)) #sorted(L1) - doenst mutate L1 - ['a', 'i', 's']
print(L1) #-['s', 'a', 'i']
L1.sort() # sorts and mutates L1 itself L1 is now = ['a', 'i', 's']
print(L1) #- ['a', 'i', 's']
L1.reverse()# mutates L
#list.sort-Mutates the list, returns nothing
#sortED(list)-returns the sorted list,doesnt mutate the very list
#***********************************************************************************#
#range is like a tuple/list
for var in range(5):
    print(var) # 01234
for var in range(2,5):
    print(var) # 234
for var in range(21,2,-1):
    print(var) # all nus from 21 to 3 descending
for var in range(21,2,-2):
    print(var) # every 2nd nus from 21 to 3 descending
for var in range(2,21,2):
    print(var) # all nus from 2 to 20 ascending
# so range also generates th like a tuple , a series of elts(only nus),but only 1elt at a time
#***********************************************************************************#
#aliasing , clonning of lists
warm = ['red','yellow','orange']
hot = warm #list hot also binds/points to same memory location of warm
hot.append('pink') #also changes warm , since both point/bind to same memry , 
warm_cl = warm[:]#is clone , is a copy not alias of warm, clone has its own sep. memory area
warm_cl.append('magenta')#doesnt affect list "warm"
print(warm_cl)
#Nested lists
br_col = [warm]
br_col.append(hot)
print(br_col)# list with 2 elts , both elts are pointing to lists themselves , warm and hot
#if any of the nested lists changes br_col also cahnges
#***********************************************************************************#
#F()ns as Objects and Dictionaries
for each_elt in map(abs,[1,-2,-3,-5])          :
    print(each_elt)
A = [1,34,56,1]
B = [0,53,43,34]
for each_elt in map(min,A,B) :
    print(each_elt)#0,34,43,1

#FL = [min,abs,etc] this list of functions can iterate over actual data lists
#***********************************************************************************#


