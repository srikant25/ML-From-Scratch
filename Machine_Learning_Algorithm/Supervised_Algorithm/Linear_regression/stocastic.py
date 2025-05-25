# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 18:23:55 2018

@author: srikant nayak
"""

import numpy as np
import math
import sys
from zs import normalization
#def stocastic_gradient():
my_data=np.genfromtxt('winequality-red.csv',delimiter=',')
my_data=np.concatenate((normalization(my_data[:,:-1]),my_data[:,-1].reshape(my_data[:,-1].shape[0],1)),axis=1)
my_data=np.insert(my_data,0,1,axis=1)

num1,num2=my_data.shape
train=math.ceil(.7*num1)
test= num1-train
training, testing = my_data[:train,:], my_data[train:,:]

x_train=training[:,:-1]
y_train=training[:,-1]
x_test=testing[0:,0:-1]
y_test=testing[:,-1]


w=np.zeros(x_train.shape[1])
w=w.reshape(w.shape[0],1)
x_size=x_train.shape[0]

eps=1e-5
error=50
alpha=1e-4


while(error > eps):
    for i in range(x_size):
        x_train_i=x_train[i]
        y_train_i=y_train[i]
        x_train_i.dot(y_train_i)
        exp1 =np.dot(np.dot(x_train_i.T,x_train_i),w)
        exp2 =np.dot(x_train_i.T,y_train_i)
        w_train = w - alpha*(exp1 - exp2)
        diff = w_train - w
        error_new =np.linalg.norm(diff,2)
        error=error_new
        w=w_train
        if(error<eps):
            break
    yp=np.dot(x_test,w_train)
    error=np.subtract(yp,y_test)
    error=np.sum(error)
    error2 = (error**2)/test
    rms=np.sqrt(error2)
    print(rms)
print(w)
np.savetxt('w_winequality',w_train ,delimiter=',')      
        
    
    
