# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 10:51:24 2018

@author: srikant nayak
"""

import numpy as np
from zs import normalization
from gradient_def import gradient_descent
import math
import time

my_data=np.genfromtxt('data3.csv',delimiter=',')
x=my_data[0:,0:-1]
y=my_data[:,-1]
out=normalization(x)

x_input=np.insert(out,0,1,axis=1)
np.random.shuffle(my_data)

x1=x_input[:,1]**2

x_input[:,1]=x1
x2=out[:,0]*out[:,1]
x_input[:,2]=x2
x3=out[:,1]**2
x_input=np.insert(x_input,3,x3,axis=1)
num1,num2=x_input.shape
train=math.ceil(.7*num1)
test= num1-train

xtrain, xtest = x_input[:train,:], x_input[train:,:]
ytrain= y[0:train]
ytest= y[train:]
w_old=np.zeros((xtrain.shape[1]))
w_new=np.zeros((xtrain.shape[1]))
alpha=1e-4
epslon=1e-2
i=5
while(i):
    i-=1
    xtx=np.dot(xtrain.T,xtrain)
    xtxw=np.dot(w_old,xtx)

    xty=np.dot(xtrain.T,ytrain)

    gradient=np.subtract(xtxw,xty)

    w_new=w_old-alpha*gradient

    diff=np.subtract(w_new,w_old)

    error=np.linalg.norm(diff)

    w_old=np.copy(w_new)
    print(error)
    if error<epslon:
        break

xw=np.matmul(xtest,w_new)
diff=np.subtract(xw,ytest)
diff_sum=np.sum(diff)
error=math.sqrt(((diff_sum)**2)/(xtrain.shape[0]))
print("RMSE:",error)
#wtrain=gradient_descent(xtrain,ytrain,eps=.00001,alpha=.001)
#print(wtrain)


    
    

