# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 21:10:09 2018

@author: srikant nayak
"""

import numpy as np
from zs import normalization
from gradient_def import gradient_descent
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import pandas as pd
from sympy import plot
from sympy import symbols
my_data=np.genfromtxt('Data1.csv',delimiter=',')
my_data1=np.genfromtxt('Data1.csv',delimiter=',')
my_data1=np.insert(my_data,0,1,axis=1)

my_data= np.concatenate((normalization(my_data[:,:-1]),my_data[:,-1].reshape(my_data[:,-1].shape[0],1)),axis=1)
xx=my_data[:,:-1]
yy=my_data[:,-1]
xt=my_data1[:,:-1]
ys=my_data[:,1]
xs=my_data[:,0]


#ax.scatter(x,y,z)
#ax.plot3D(x,y,z)


x1=int(w_train[1])
x0=int(w_train[0])
x, y = symbols('x y')
eq = x1*x + x0
#eq=x**3 - 3*x*y**2
p1=plot(eq)
for i in range(1,len(yy)):
 p1._backend.ax.scatter(xx[i],yy[i])
p1._backend.save('im.png')