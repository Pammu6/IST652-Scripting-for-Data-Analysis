# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 17:19:22 2019

@author: KARTHEEK
"""

#Tuple is a collection of immutable objects/elements
# A list cannot act as a primary key in a dictionary

x=input('')

#Number of vowels
c=0
d=0
e=0
for m in x:
    if m == 'a' or m == 'e' or m == 'i' or m == 'o' or m == 'u'  :
        c=c+1
    if m != 'a' and m != 'e' and m != 'i' and m != 'o' and m != 'u' and m != ' '  :
        d=d+1
    if m == ' ':
        e=e+1
        
print('The number of consonants are' + ' ' + str(d)) 
print('The number of vowels are' + ' ' + str(c)) 
print('The number of spaces are' + ' ' + str(e))

k=[]
import collections
o = collections.Counter(x)
for key,value in o.items():
    k.append([key,value])
k=sorted(k,key=lambda x: x[-1])
maxval=max([sublist[-1] for sublist in k])
minval=min([sublist[-1] for sublist in k])
for key,value in k:
    if value == maxval:
        print('The most frequent element of the string is'+ ' '+str(key))
    if value == minval:
        print('The least frequent element of the string is'+ ' '+str(key))



p=0
while p%2 == 0:
    x[p].upper()
    p=p+1
        



  
