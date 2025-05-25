# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 04:23:54 2018

@author: srikant nayak
"""
#def meshgrid(x,y,gap):
    
from gd_assent import gradient_assent
import numpy as np

import matplotlib.pyplot as plt
import math

my_data=np.genfromtxt('data5.csv',delimiter=',')
np.random.shuffle(my_data)
my_data=np.insert(my_data,0,1,axis=1)
row,col=my_data.shape
train=math.ceil(.7*row)
test=row-train
training,testing=my_data[:train,:],my_data[train:,:]
xtrain=training[0:,0:-1]
xtest=testing[0:,0:-1]
ytest=testing[0:,-1]
ytrain=training[0:,-1]
w=gradient_assent(xtrain,ytrain,alpha=.001,eps=.0001)
A1=my_data[:,1]
A2=my_data[:,2]
min_x=np.min(A1)
max_x=np.max(A1)
min_y=np.min(A2)
max_y=np.max(A2)
x=np.arange(min_x,max_x,.5)
y=np.arange(min_y,max_y,.5)
xx,yy=np.meshgrid(x,y)
z=w[1]*xx + w[2]*yy +w[0]
fig = plt.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_surface(xx, yy, z, rstride=1, cstride=1, cmap='hot', linewidth=0, antialiased=False)
fig.colorbar(surf, shrink=0.5, aspect=5)
plt.show()
plt.show()
for i in range(train):
    if ytrain[i]==0:
      ax.scatter(A1[i],A2[i],c='green')
    else:
      ax.scatter(A1[i],A2[i],c='blue')




