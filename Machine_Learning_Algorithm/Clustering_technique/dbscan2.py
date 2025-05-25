# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 12:48:52 2018

@author: srikant nayak
"""

import numpy as np
import random
from scipy.spatial import distance
def euclidean_distance(x,y):
    dis=distance.euclidean(x,y)
    return(dis)
    
mydata=np.genfromtxt('data4.csv',delimiter=',')
data=mydata.tolist()
radius=.9
min_limit=5
status=np.zeros(mydata.shape[0]) # all are unvisited
#while(1):
p=random.choice(data)
a=data.index(p)
if(status[a]==0):
    status[a]=1 #mark as visited
N=[]
for i in range(len(data)):
    dist=euclidean_distance(p,data[i])
    if(dist<= radius):
        N.append(data[i])
    if(len(N)>= min_limit):
        cluster=[]
        cluster.append(p)
        '''
    for j in range(len(N)):
       b=data.index(N[j])
       if(status[b]==0):
           status[b]=1
       n1=[]
       for k in range(len(data)):
           distt=euclidean_distance(N[j],data[k])
           if (distt<=radius):
               n1.append(data[k])
           if (len(n1)>=min_limit):
               N.append(n1)
               
 '''              
           
               
        
            
            
            
    
        
    
        
    

