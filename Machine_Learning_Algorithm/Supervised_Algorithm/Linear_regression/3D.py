# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 23:24:27 2018

@author: srikant nayak
"""

import numpy as np
from zs import normalization
from gradient_def import gradient_descent
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import pandas as pd
from sympy import plot
from sympy.plotting import plot3d
from sympy import symbols
my_data=np.genfromtxt('Data2.csv',delimiter=',')
my_data1=np.genfromtxt('Data2.csv',delimiter=',')
my_data1=np.insert(my_data,0,1,axis=1)

my_data= np.concatenate((normalization(my_data[:,:-1]),my_data[:,-1].reshape(my_data[:,-1].shape[0],1)),axis=1)

zz=my_data[:,2]
xt=my_data1[:,:-1]
ys=my_data[:,1]
xs=my_data[:,0]


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