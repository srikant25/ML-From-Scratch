# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 15:47:35 2018

@author: srikant nayak
"""

import numpy as np
from scipy.spatial import distance
import matplotlib.pyplot as plt
from k_med import cost
from k_med import mediod
import random
from db_index import euclidean_distance
from db_index import k_mean
from db_index import scatter


my_data=np.genfromtxt('data2.csv',delimiter=',')
k=[2,3,4]
for m in range(len(k)):
    
    
    cluster,mean=k_mean(my_data,k=k[m])
    s=scatter(cluster,mean,k=k[m])
    d=0
    for i in range(len(cluster)):
        R=[]
        for j in range(len(cluster)):
            if i!=j:
                num=s[i]+s[j]
                dino=euclidean_distance(mean[i],mean[j])
                Rij=num/dino
                R.append(Rij)
            else:
                continue
        Di=max(R)
        d=d+Di
        
    DB_index=d/k 
db=list(DB_index)
a=db.index(min(db))
k_best=k[a]
print(k_best)


