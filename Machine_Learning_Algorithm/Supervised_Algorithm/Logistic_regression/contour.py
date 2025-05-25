# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 11:05:55 2018

@author: srikant nayak
"""

import numpy as np
import math
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from scipy.stats import multivariate_normal
my_data=np.genfromtxt('data3.csv',delimiter=',')
np.random.shuffle(my_data)
row,col=my_data.shape
train=math.ceil(.7*row)
test=row-train
training,testing=my_data[:train,:],my_data[train:,:]
xtrain=training[0:,0:-1]
ytrain=training[0:,-1]
pos=[]
neg=[]
for i in range(xtrain.shape[0]):
    if(ytrain[i]==1):
      pos.append(xtrain[i])
    else:
      neg.append(xtrain[i])
posi=np.asarray(pos)
neg=np.asarray(neg)    
positive=posi.shape[0]
negative=neg.shape[0]
m1=np.mean(pos,axis=0)
m0=np.mean(neg,axis=0)
covar=np.cov(xtrain.T)
A1=my_data[:,0]
A2=my_data[:,1]
min_x=np.min(A1)-20
max_x=np.max(A1)+20
min_y=np.min(A2)-20
max_y=np.max(A2)+20
x=np.linspace(min_x,max_x,200)
y=np.linspace(min_y,max_y,200)
xx,yy=np.meshgrid(x,y)

pos = np.array([xx.flatten(),yy.flatten()]).T
rv1=multivariate_normal(m0,covar)
rv2=multivariate_normal(m1,covar)
fig = plt.figure()
ax0 = fig.gca()
ax0.contour(xx,yy,rv1.pdf(pos).reshape(200,200),cmap='hot')
ax0.contour(xx,yy,rv2.pdf(pos).reshape(200,200))

plt.show()