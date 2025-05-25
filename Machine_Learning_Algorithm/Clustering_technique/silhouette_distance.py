# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 13:40:57 2018

@author: srikant nayak
"""

import numpy as np
import random
from db_index import k_mean
from db_index import euclidean_distance
my_data=np.genfromtxt('IRIS.csv',delimiter=',')
my_data=my_data[:,1:]
my_data=np.delete(my_data,(0),axis=0)
data=list(my_data)
cluster,mean=k_mean(my_data,k=4)
k=4
A=np.array([])
for i in range(k):
    o=random.choice(cluster[i])
    s=0
    for j in range(len(cluster[i])):
        dist=euclidean_distance(cluster[i][j],o)
        s=s+dist
    a=s/len(cluster[i])
    A=np.append(A,a)

B=np.array([])
for i in range(k):
    o=random.choice(cluster[i])
    c=[]
    for m in range(k):
        if(m != i):
            s=0
            for j in range(len(cluster[m])):
        #if(data[j] not in cluster[i]):
               dist=euclidean_distance(cluster[m][j],o)
               s=s+dist
            b=s/len(cluster[m])
            c.append(b)
           
        else:
            continue
    z=min(c)
   
    B=np.append(B,z)
a_min=np.min(A)
b_min=np.min(B)

silhouette_distance=(b_min-a_min)/max(b_min,a_min)
print(silhouette_distance)

    


        
         
         
    