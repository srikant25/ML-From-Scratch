"""
Created on Wed nov 11 00:00:15 2018

@author: srikant nayak
"""

import numpy as np


weight_vector=np.zeros((5,4))
A_vector=[]
B_vector=[]

def compute_hamming_dist(u,v):
    tmp=abs(u-v)
    dist=np.sum(tmp)
    return dist

def transfer_func(weight_vector,input):
    global A_vector,B_vector
    limit_pts=[]
    new_A=input
   
    tmp1=np.matmul(input,weight_vector)
    new_B=np.sign(tmp1)
    new_B[new_B==0] = -1
    first_time=0
    iteration=0
    while(1):
        for i in range (0,2):
            if(new_B==B_vector[i]).all():
                print("Value corresponding to pattern - :",i)
                print("iterations=",iteration)
                print("hammind dist from 0-",compute_hamming_dist(new_B,B_vector[0]))
                print("hammind dist from 1-",compute_hamming_dist(new_B,B_vector[1]))
                return
        if(first_time !=0):
            if any((new_B == x).all() for x in limit_pts):
                print("iterations=",iteration)
                print('Limit pt...')
                print("hammind dist from 0-",compute_hamming_dist(new_B,B_vector[0]))
                print("hammind dist from 1-",compute_hamming_dist(new_B,B_vector[1]))
                return
        else:
            first_time=1
        limit_pts.append(new_B)
        tmp2=np.matmul(new_B,weight_vector.T)
        update_A=np.sign(tmp2)
        update_A[update_A==0] = new_A[update_A==0]
        new_A=update_A
        tmp1=np.matmul(new_A,weight_vector)
        B=new_B
        new_B=np.sign(tmp1)
        new_B[new_B==0] = B[new_B==0]
        iteration=iteration +1
     
        
a1 = np.matrix([0, 1, 0, 1, 0])
a2 = np.matrix([1, 1, 0, 0, 0])
b1 = np.matrix([1, 0, 0, 1])
b2 = np.matrix([0, 1, 0, 1])
a1[a1 == 0] = -1
a2[a2 == 0] = -1
b1[b1 == 0] = -1
b2[b2 == 0] = -1
A_vector.append(a1)
B_vector.append(b1)
tmp=np.outer(a1,b1)
weight_vector=weight_vector+tmp
A_vector.append(a2)
B_vector.append(b2)
tmp=np.outer(a2,b2)
weight_vector=weight_vector+tmp
    

input_pattern=np.array([-1,1,1,1,-1])

transfer_func(weight_vector,input_pattern)

input_pattern=np.array([-1,-1,1,1,-1])

transfer_func(weight_vector,input_pattern)



