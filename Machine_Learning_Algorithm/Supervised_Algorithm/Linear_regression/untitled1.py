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

zz=my_data[:,2]
xt=my_data[:,:-1]
ys=my_data[:,1]
xs=my_data[:,0]
wbest=ridge_regression1(x_train,y_train,eps=.00001,alpha=.01,lamda=3e-05)

#ax.scatter(x,y,z)
#ax.plot3D(x,y,z)

x2=int(wbest[1])
x1=int(wbest[2])
x0=int(wbest[0])
x, y = symbols('x y')
eq = x2*x + x1*y + x0

p1=plot3d(eq)
for i in range(1,len(ys)):
 p1._backend.ax.scatter(xs[i],ys[i],zz[i])

p1._backend.save('im2.png')