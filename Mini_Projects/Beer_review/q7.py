# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 18:38:41 2018

@author: srikant nayak
"""

import numpy as np
w=np.zeros((70,70))
img=[]
input_pattern=np.zeros((5,70))
my_data=np.array(('A.csv','B.csv','C.csv','D.csv','E.csv'))
for i in range(0,5):
    data=np.genfromtxt(my_data[i],delimiter=",")
 
    tmp=data.flatten()
    input_pattern[i]=tmp
    pattern=np.matrix(tmp)
    img.append(pattern)
    tmp=np.outer(pattern,pattern)
    w=w+tmp
 #Recall
for k in range (0,5):
    x=np.shape(input_pattern[k])[0]
    mem=np.matmul(input_pattern[k],w)
    y=np.sign(mem)
    for i in range(0,x):
        if (y[i]==0):
            y[i]=input_pattern[k][i]
    
    dist_list=[]
    for i in range(0,5):
        diff=np.abs(y[i]-img[i])
        dist=np.sum(diff)
        dist_list.append(dist)
    indx=dist_list.index(min(dist_list))
    print(indx)