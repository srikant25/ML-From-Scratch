# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 15:10:44 2018

@author: srikant nayak
"""

import numpy as np
from scipy.spatial import distance
import random
import matplotlib.pyplot as plt
my_data=np.genfromtxt('data4.csv' , delimiter=',')
my=my_data.tolist()

def euclidean_distance(x,y):
    dis=distance.euclidean(x,y)
    return(dis)
radius=0.45
min_lim=3
data=np.insert(my_data,0,0,axis=1) # mark all data as unvisited
x=data.tolist()
cluster=[]
main_cluster=[]
noise=[]
while(1):
    while(1):
        p=random.choice(my)
        a=my.index(p)
        if(x[a][0]==0):
            break       
    x[a][0]=1#mark as visited    
    N=[]
    for i in range(len(x)):
        dist=np.linalg.norm(np.subtract(p,my[i]))
        if(dist<radius):
            N.append(my[i])  #neighbourhood of p
    
    if(len(N)>min_lim):
        clus=[]
        
        cluster.append(p)  #forming a new cluster
        clus.append(p)        
        for j in range(len(N)):
            b=my.index(N[j])            
            if(x[b][0]==0):
                x[b][0]=1
                N1=[]
                for k in range(len(x)):
                    dist1=np.linalg.norm(np.subtract(N[j],my[k]))
                    if(dist1<radius):
                        N1.append(my[k])
                if(len(N1)>min_lim):
                    N.extend(N1)
                flag=0
                for l in main_cluster:
                    for mk in l:
                        if(N[j] in mk):
                            flag=1
                            break
                        break
                if(flag==0):
                    cluster.append(N[j]) 
                    clus.append(N[j])
    
    else:
        noise.append(p)
    if(clus):
        main_cluster.append(clus)
    c=0
    for i in range(len(x)):
        if(x[i][0]==1):
            c+=1
    if c==len(x):
        break
#for t in range(len(x)):
    
     #plt.scatter(x[:,1][t],x[:,2][t],c='green')
                
    
a=main_cluster[0]
b=main_cluster[1]
c=main_cluster[2]
l1=[]
l2=[]
for i in range(len(a)):
    pt=a[i]
    l1.append(pt[0]) 
    l2.append(pt[1])
l3=[]
l4=[]
for i in range(len(b)):
    pt=b[i]
    l3.append(pt[0]) 
    l4.append(pt[1])
l5=[]
l6=[]
for i in range(len(c)):
    pt=c[i]
    l5.append(pt[0]) 
    l6.append(pt[1])
           
plt.scatter(l1,l2,cmap='r')     
plt.scatter(l3,l4,cmap='g')     
plt.scatter(l5,l6,cmap='b')                
                
                   
            




