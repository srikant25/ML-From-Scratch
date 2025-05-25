# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 14:46:47 2018

@author: srikant nayak
"""

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
my_data=np.array(('heli.csv','plane.csv','tank.csv'))
data=np.array('heli.csv')

w=np.zeros((144,144))
image=[]
for i in range(0,3):
    data=np.genfromtxt(my_data[i],delimiter=",")
    tmp=data.flatten()
    pattern=np.matrix(tmp)
    image.append(pattern)
    tmp=np.outer(pattern,pattern)
    w=w+tmp
  
#Recall equation
data=np.genfromtxt('testdata.csv',delimiter=",")
input_pattern=data.flatten()
no_clm=np.shape(input_pattern)[0]
tmp1=np.matmul(input_pattern,w)
y=np.sign(tmp1)
for i in range(0,no_clm):
    if (y[i]==0):
        y[i]=input[i]
dist_list=[]
for i in range(0,3):
    sub=abs(y-image[i])
    dist=np.sum(sub)
    dist_list.append(dist)
indx=dist_list.index(min(dist_list))
print(indx)
