# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 03:04:05 2018

@author: srikant nayak
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 23:24:27 2018

@author: srikant nayak
"""

import numpy as np
from zs import normalization
from ridge_regression import ridge_regression1
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import math
from sympy import plot
from sympy.plotting import plot3d
from sympy import symbols

my_data=np.genfromtxt('data1.csv',delimiter=',')
out = normalization(my_data)
my_data=np.insert(out,0,1,axis=1)
num1,num2=my_data.shape
train=math.ceil(.7*num1)
test= num1-train
np.random.shuffle(my_data)
training, testing = my_data[:train,:], my_data[train:,:]
x_train=training[0:,0:-1]
x_test=testing[0:,0:-1]
y_train=training[:,-1]
y_test=testing[:,-1]

#my_data= np.concatenate((normalization(my_data[:,:-1]),my_data[:,-1].reshape(my_data[:,-1].shape[0],1)),axis=1)


w0=ridge_regression1(x_train,y_train,eps=.00001,alpha=.01,lamda=3e-05)
A1=my_data[:,1]
A2=my_data[:,2]
min_x=np.min(A1)
max_x=np.max(A1)
min_y=np.min(A2)
max_y=np.max(A2)
x=np.arange(min_x,max_x,.5)
y=np.arange(min_y,max_y,.5)
xx,yy=np.meshgrid(x,y)

z = w0[1]*xx + w0[2]*yy + w0[0]
fig = plt.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_surface(xx, yy, z, rstride=1, cstride=1, cmap='hot', linewidth=0, antialiased=False)
fig.colorbar(surf, shrink=0.5, aspect=5)
plt.show()
plt.show()
for i in range(train):
    
    ax.scatter(A1[i],A2[i],c='green')
