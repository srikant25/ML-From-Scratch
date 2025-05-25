# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 15:49:31 2018

@author: srikant nayak
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 14:05:06 2018

@author: srikant nayak
"""


import numpy as np
import math
from gd_assent import gradient_assent
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from sympy.plotting import plot3d
from sympy import symbols
import time
start = time.time()
my_data=np.genfromtxt('data1.csv',delimiter=',')
my_data=np.insert(my_data,0,1,axis=1)
np.random.shuffle(my_data)
xtrain=my_data[0:,0:-1]
ytrain=my_data[:,-1]
p=ytrain.shape

num1,num2=my_data.shape
train=math.ceil(.7*num1)
test= num1-train
training, testing = my_data[:train,:], my_data[train:,:]
x_train=training[0:,0:-1]
x_test=testing[0:,0:-1]


i=0
alpha=.001
eps=.0001
w0=np.zeros(x_train.shape[1])
w=gradient_assent(xtrain,ytrain,alpha=.001,eps=.0001)
y=np.dot(xtrain,w)
y_train=y[:train]
y_test=y[train:]




while(1):
    x_t=x_train.transpose()
    b=np.dot(x_t,y_train)
    xtx = np.dot(x_t,x_train)
    
    
      
    trans2=np.dot(xtx,w0)
        
    Djw=np.subtract(trans2,b)    
    intermediate=alpha*Djw
    w_train = np.subtract(w0,intermediate)
    
    i=i+1
    diff= np.subtract(w_train,w0)
    err=np.linalg.norm(diff,2)
    
    w0= np.copy(w_train)
    #calculate error based one w
    if(err<eps):
        break
    
yp=np.dot(x_test,w_train)
error=np.subtract(yp,y_test)
error=np.sum(error)
error2 = (error**2)/test
rms=np.sqrt(error2)
print(rms)

np.savetxt('w_.csv',w_train ,delimiter=',')
end = time.time()
print('Time taken in direct method is {}'.format(end-start))


#plotting
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
    if ytrain[i]==0:
      ax.scatter(A1[i],A2[i],c='green')
    else:
      ax.scatter(A1[i],A2[i],c='blue')















'''
x, y = symbols('x y')
eq = w0[1]*x + w0[2]*y + w0[0]

p1=plot3d(eq)
fig = plt.figure()
ax = fig.gca(projection='3d')
xx=my_data[:,1]
yy=my_data[:,2]



for i in range(train):
    if ytrain[i]==0:
      p1.backend.ax.scatter(xx[i],yy[i],c='green')
    else:
      p1.backend.ax.scatter(xx[i],yy[i],c='blue')




surf = ax.plot_surface(xx, yy, z, rstride=1, cstride=1, cmap='hot', linewidth=0, antialiased=False)
fig.colorbar(surf, shrink=0.5, aspect=5)
plt.show()
'''












