# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 14:05:06 2018

@author: srikant nayak
"""


import numpy as np
import math
import time
#start = time.time()
my_data=np.genfromtxt('data1.csv',delimiter=',')
my_data=np.insert(my_data,0,1,axis=1)
np.random.shuffle(my_data)
num1,num2=my_data.shape
train=math.ceil(.7*num1)
test= num1-train
training, testing = my_data[:train,:], my_data[train:,:]
x_train=training[0:,0:-1]
x_test=testing[0:,0:-1]
y_train=training[:,-1]
y_test=testing[:,-1]
i=0
alpha=.001
eps=.00001
w=np.zeros(x_train.shape[1])

while(1):
    x_t=x_train.transpose()
    b=np.dot(x_t,y_train)
    xtx = np.dot(x_t,x_train)
    
    
      
    trans2=np.dot(xtx,w)
        
    Djw=np.subtract(trans2,b)    
    intermediate=alpha*Djw
    w_train = np.subtract(w,intermediate)
    
    i=i+1
    diff= np.subtract(w_train,w)
    err=np.linalg.norm(diff,2)
    
    w= np.copy(w_train)
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
#end = time.time()
#print('Time taken in direct method is {}'.format(end-start))

#print(rms)