# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 19:33:34 2018

@author: SRIKANT
"""




a=[1,2,3,4,5]
b=[3,4,5,6,7]
sat=a[0]
satt=b[0]
c=[]
rowa = len(a)
rowb = len(b)
for i in range(0,rowa):
     for j in range(0,rowb):
         if (a[i]==b[j]):
             c.append(a[i])
print('These are common elements of the given two arrays-{}'.format(c))             
