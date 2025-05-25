# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 23:56:15 2018

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
def k_mean(my_data,k):
    
    data=list(my_data)
    mean=[]
    for i in range(k):
        m1=random.choice(data)
        mean.append(m1)
    k_clust=[[] for x in range(k)]
    while(1):
        for j in range(len(data)):
            dist=[]
            for l in range(0,k):
                dist1=euclidean_distance(mean[l],data[j])
                dist.append(dist1)
            
            a=dist.index(min(dist))
            k_clust[a].append(my_data[j])
        
        mean2=[]
        for i in range(k):
            mean1=np.mean(k_clust[i],axis=0)
            mean2.append(mean1)
        #mean3=np.array(mean2)
        if np.array_equal(np.array(mean2),np.array(mean)):
                    
            break
        mean=mean2
        k_clust=[[] for x in range(k)]
    return(k_clust,mean2)
cluster,mean=k_mean(my_data,k=4)

def scatter(cluster,mean,k):
    s=[]
    for i in range(0,k):
        dist1=0
        for j in range(len(cluster[i])):
            sub=(np.subtract(cluster[i][j],mean[i]))
            nrm=np.linalg.norm(sub)
            dist=nrm**2
            dist1=dist1+dist
        p=dist1/len(cluster[i])
        z=np.sqrt(p)
        s.append(z)
    return(s)
s=scatter(cluster,mean,k=4)

def mean_distance(mean,k):
    M=[]
    for i in range(k):
        m=[]
        for j in range(k):
            dist=euclidean_distance(mean[i],mean[j])
            m.append(dist)
            max_m=max(m)
        M.append(max_m)
    return(M)
#M=mean_distance(mean,k=3)

k=4
d=0
for i in range(k):
    R=[]
    for j in range(k):
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
        
       
        

    
            
            
            
            
        
        
            
            
    
