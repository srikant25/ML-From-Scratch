# -*- coding: utf-8 -*-
"""
Created on Wed oct 11 00:00:15 2018

@author: srikant nayak
"""
import numpy as np
#filename=np.array(('zero.csv','one.csv','two.csv','three.csv','four.csv','five.csv','six.csv','seven.csv','eight.csv','nine.csv'))
my_data=np.array(('four.csv','five.csv','six.csv','seven.csv','eight.csv','nine.csv'))
w=np.zeros((35,35))
input_pattern=np.zeros((10,35))
n=6
img_arr=[]
for i in range(0,n):
    data=np.genfromtxt(my_data[i],delimiter=",")
    
    tmp=data.flatten()
    input_pattern[i]=tmp
    pattern=np.matrix(tmp)
    img_arr.append(pattern)
    tmp=np.outer(pattern,pattern)
    w=w+tmp
    #Recall equation
for k in range (0,n):
    no_clm=np.shape(input_pattern[k])[0]
    tmp1=np.matmul(input_pattern[k],w)
    y1=np.sign(tmp1)
    for i in range(0,no_clm):
        if (y1[i]==0):
            y1[i]=input[i]
    
    dist_list=[]
    for i in range(0,n):
        sub=abs(y1-img_arr[i])
        dist=np.sum(sub)
        dist_list.append(dist)
    indx=dist_list.index(min(dist_list))
    print(indx)
