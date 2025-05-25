# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 21:54:19 2018

@author: srikant nayak
"""

import numpy as np
weight_vector=np.zeros((144,120))
#input_pattern=np.array([-1.,  1.,  1.,  1., -1.,  1., -1., -1., -1.,  1.,  1., -1., -1.,-1.,  1.,  1., -1., -1., -1.,  1.,  1., -1., -1., -1.,  1.,  1.,-1., -1., -1.,  1., -1.,  1.,  1.,  1., -1.])
A_vector=[]
B_vector=[]
filename_1=np.array(('heli.csv','plane.csv','tank.csv'))
filename_2=np.array(('three.csv','one.csv','two.csv'))

for i in range(0,3):
    data_a=np.genfromtxt(filename_1[i],delimiter=",")
    data_b=np.genfromtxt(filename_2[i],delimiter=",")
    
    #no_row,no_clm=np.shape(data)
    tmp=data_a.flatten()
    pattern_a=np.array(tmp)
    A_vector.append(pattern_a)
    tmp2=data_b.flatten()
    pattern_b=np.array(tmp2)
    B_vector.append(pattern_b)
    tmp=np.outer(pattern_a,pattern_b)
    weight_vector=weight_vector+tmp
    
#Recall equation
data=np.genfromtxt('testdata.csv',delimiter=",")
x=data.flatten()
tmp1=np.matmul(x,weight_vector)
new_B=np.sign(tmp1)
new_B[new_B==0] = 1
first_time=0
iteration=0
limit_pts=[]
while(1):
    for i in range (0,3):
        if(new_B==B_vector[i]).all():
            print("Value corresponding to pattern index - :",i)
            break
    if(first_time !=0):
        if any((new_B == x).all() for x in limit_pts):
            print('Limit pt...')
            break
    else:
        first_time=1
    limit_pts.append(new_B)
    tmp2=np.matmul(new_B,weight_vector.T)
    update_A=np.sign(tmp2)
    update_A[update_A==0] = x[update_A==0]
    new_A=update_A
    tmp1=np.matmul(new_A,weight_vector)
    B=new_B
    new_B=np.sign(tmp1)
    new_B[new_B==0] = B[new_B==0]
    iteration=iteration +1