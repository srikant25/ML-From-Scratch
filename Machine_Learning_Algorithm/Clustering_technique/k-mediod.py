# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 22:35:52 2018

@author: srikant nayak
"""

import numpy as np
from scipy.spatial import distance
import matplotlib.pyplot as plt
import random
import pylab
my_data=np.genfromtxt('data3.csv',delimiter=',')
data=list(my_data)
def euclidean_distance(x,y):
    dis=distance.euclidean(x,y)
    return(dis)
def cost(m,data):   
    cost=0
    for i in range(len(data)):
        
       dist=euclidean_distance(m,data[i])
       cost=cost+dist
    return(cost)
    

k=4
med=[]
clust=[[] for x in range(k)]
for i in range(k):
    m=random.choice(data)
    med.append(m)
med1=np.array(med)
for j in range(my_data.shape[0]):
    dist=[]
    for l in range(0,k):
        dist1=euclidean_distance(med[l],my_data[j])
        dist.append(dist1)
    
    a=dist.index(min(dist))
    clust[a].append(my_data[j])
cost1=[]
for i in range(k):
    cost11=cost(med[i],clust[i])
    cost1.append(cost11)
#cost2=cost1
ww=0
while(ww==0):
   for i in range(len(clust)):
       #
       random_point=random.choice(clust[i])
       test=med
       test[i]=random_point
       
       cost2=cost(test[i],clust[i])
          
       if (cost2 < cost1[i]) :
           med=test
           for j in range(my_data.shape[0]):
                dist=[]
                for l in range(0,k):
                    dist1=euclidean_distance(med[l],my_data[j])
                    dist.append(dist1)
                
                a=dist.index(min(dist))
                clust[a].append(my_data[j])
       
       status=[]
       q=0
       while (q < len(test)):
           if(np.array_equal(test[q],med[q])):
               status.append(True)
           else:
               status.append(False)
           q+=1
       if status.count(True) == len(status):
           ww=1
           break;
for i in range(k):
    list1=list(zip(*clust[i]))
    pylab.scatter(list(list1[0]),list(list1[1]))
pylab.show()
         
        
        
        
    
        
        
        
    

    
        
        
            
       
    

