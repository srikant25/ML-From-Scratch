# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 16:56:21 2018

@author: srikant nayak
"""
#def gradient_assent(xtrain,ytrain,alpha,eps):
import numpy as np
import math
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
my_data=np.genfromtxt('data1.csv',delimiter=',')
np.random.shuffle(my_data)
my_data=np.insert(my_data,0,1,axis=1)
row,col=my_data.shape
train=math.ceil(.7*row)
test=row-train
training,testing=my_data[:train,:],my_data[train:,:]
xtrain=training[0:,0:-1]
xtest=testing[0:,0:-1]
ytest=testing[0:,-1]
column=xtrain.shape[1]
ytrain=training[0:,-1]
alpha=.0001
eps=.00001
w=np.zeros(xtrain.shape[1])
w_nxt=np.zeros(xtrain.shape[1])
j=0
while(1):
    w_t=w.transpose()
    b=np.dot(xtrain,w_t)
    f=(1 / (1 + np.exp(-b)))
    diff=np.subtract(ytrain,f)
    for j in range(column):
        
        mul=np.dot(diff.T,xtrain[:,j])
        w_nxt[j]=w[j]+alpha*(mul)

    w_diff=np.subtract(w,w_nxt)
    err=np.linalg.norm(w_diff)
    print(err)
    w=np.copy(w_nxt)
    if(err<eps):
        break
    #return(w_nxt)
fig = plt.figure()
#ax = fig.gca(projection='2d')
plt.scatter(b,f,c='green')   
#np.save('w_data4.csv',w)     
    
    
    
    
    
    
    
    
    







            
            
        



