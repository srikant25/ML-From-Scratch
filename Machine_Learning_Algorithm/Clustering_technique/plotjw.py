# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 20:50:05 2018

@author: srikant nayak
"""

import numpy as np
from scipy.spatial import distance
import random

import matplotlib.pyplot as plt
my_data=np.genfromtxt('data3.csv',delimiter=',')
data=list(my_data)
def euclidean_distance(x,y):
    dis=distance.euclidean(x,y)
    return(dis)
k=4
mean=[]
for i in range(k):
    m1=random.choice(data)
    mean.append(m1)
k_clust=[[] for x in range(k)]
iteration=0

j_w=np.array([])
while(1):
    
    
    
    for j in range(len(data)):
        dist=[]
        for l in range(0,k):
            dist1=euclidean_distance(mean[l],data[j])
            dist.append(dist1)
        #(m,a) = min((v,a) for a,v in enumerate(dist))
        a=dist.index(min(dist))
        k_clust[a].append(my_data[j])
    jw1=0
    print(len(mean))
    
    for j in range(len(k_clust[a])):
         
         diff=np.subtract(k_clust[a][j],mean[a])
         nrm=np.linalg.norm(diff)
         jw=nrm**2
         jw1=jw1+jw
         
        
    j_w=np.append(j_w,jw1)
    iteration=iteration+1
        
        
             
    #cluster=np.array(k_clust)
    mean2=[]
    for i in range(k):
        mean1=np.mean(k_clust[i],axis=0)
        mean2.append(mean1)
    
    
      
    if np.array_equal(np.array(mean2),np.array(mean)):
                
        break
    mean=mean2
    k_clust=[[] for x in range(k)]
   



    

#plt.plot(j_w)        
        
        



for i in range(k):
    list1=list(zip(*k_clust[i]))
    pylab.scatter(list(list1[0]),list(list1[1]))
pylab.show()

   
   