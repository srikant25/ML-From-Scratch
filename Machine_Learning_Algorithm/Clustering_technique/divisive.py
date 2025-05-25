# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 08:02:13 2018

@author: srikant nayak
"""

import numpy as np
from scipy.spatial import distance
import matplotlib.pyplot as plt
from k_mean import k_mean
import pylab
#import random
my_data=np.genfromtxt('data2.csv',delimiter=',')
def euclidean_distance(x,y):
    dis=distance.euclidean(x,y)
    return(dis)
    
def cost(m,data):   
    cost=0
    for i in range(len(data)):
       dist=euclidean_distance(m,data[i])
       cost=cost+dist
    return(cost)
       
# k_mean......for k=2...............    
kn=4
cluster=[[] for x in range(kn)]
mean= [[] for x in range(kn)]
i=0
k=0
cluster[k],cluster[k+1],mean[k],mean[k+1] = k_mean(my_data)

while(1):
    
   
    cost_dist=[]
    
    for i in range(k+1):
       cost1=cost(mean[i],cluster[i])
       cost_dist.append(cost1)
    a=cost_dist.index(max(cost_dist))
    cluster[a],cluster[k+2],mean[a],mean[k+2]=k_mean(cluster[a])
    k=k+1
    if (kn==k+2):
        break
  
for i in range(kn):
    list1=list(zip(*cluster[i]))
    pylab.scatter(list(list1[0]),list(list1[1]))
pylab.show()

      
      
    
