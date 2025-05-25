# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 21:54:19 2018

@author: srikant nayak
"""

import numpy as np
w=np.zeros((144,120))

A_vector=[]
B_vector=[]
a=np.array(('heli.csv','plane.csv','tank.csv'))
b=np.array(('three.csv','one.csv','two.csv'))

for i in range(0,3):
    data_a=np.genfromtxt(a[i],delimiter=",")
    data_b=np.genfromtxt(b[i],delimiter=",")
    tmp=data_a.flatten()
    pattern_a=np.array(tmp)
    A_vector.append(pattern_a)
    tmp2=data_b.flatten()
    pattern_b=np.array(tmp2)
    B_vector.append(pattern_b)
    tmp=np.outer(pattern_a,pattern_b)
    w=w+tmp
    
#Recall equation
data=np.genfromtxt('testdata.csv',delimiter=",")
x=data.flatten()
tmp1=np.matmul(x,w)
new_B=np.sign(tmp1)
new_B[new_B==0] = 1
first_time=0
iteration=0
limit_pts=[]
while(1):
    iteration=iteration +1
    for i in range (0,3):
        if(new_B==B_vector[i]).all():
            print("Value corresponding to pattern index - :",i)
            break
    if(first_time !=0):
        if any((new_B == x).all() for x in limit_pts):
            #print('Limit pt...')
            break
    else:
        first_time=1
    limit_pts.append(new_B)
    tmp2=np.matmul(new_B,w.T)
    update_A=np.sign(tmp2)
    update_A[update_A==0] = x[update_A==0]
    new_A=update_A
    tmp1=np.matmul(new_A,w)
    B=new_B
    new_B=np.sign(tmp1)
    new_B[new_B==0] = B[new_B==0]
print(iteration)   