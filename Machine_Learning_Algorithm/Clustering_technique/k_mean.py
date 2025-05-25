# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 19:21:34 2018

@author: srikant nayak
"""

import numpy as np
from scipy.spatial import distance
import matplotlib.pyplot as plt
import random
my_data=np.genfromtxt('data2.csv',delimiter=',')

def euclidean_distance(x,y):
    dis=distance.euclidean(x,y)
    return(dis)
    
def k_mean(my_data):
    data=list(my_data)
    
    m1=random.choice(data)
    m2=random.choice(data)
    while(1):
        a=list()
        b=list()
    
        for i in range(my_data.shape[0]):
            x=euclidean_distance(m1,my_data[i])
            y=euclidean_distance(m2,my_data[i])
            if(x<y):
                a.append(my_data[i])
            else:
                b.append(my_data[i])
        a=np.array(a)
        b=np.array(b)
        mean1=np.mean(a,axis=0)
        mean2=np.mean(b,axis=0)
        if np.any(mean1 == m1):
            if np.any(mean2==m2):
                break
        m1=mean1
        m2=mean2
    return(a,b,m1,m2)
      
a,b,f,m=k_mean(my_data)

A1=a[:,0]
A2=a[:,1]
plt.scatter(A1,A2,c='green')       

B1=b[:,0]
B2=b[:,1]
plt.scatter(B1,B2,c='red')


        
        
