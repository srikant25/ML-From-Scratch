# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 02:00:37 2018

@author: srikant nayak
"""

import numpy as np
from zs import normalization
import math
import time
#start = time.time()

my_data=np.genfromtxt('data1.csv',delimiter=',')
#out = normalization(my_data)
my_data=np.insert(my_data,0,1,axis=1)
num1,num2=my_data.shape
train=math.ceil(.7*num1)
test= num1-train
np.random.shuffle(my_data)
training, testing = my_data[:train,:], my_data[train:,:]
x_train=training[0:,0:-1]

x_test=testing[0:,0:-1]
y_train=training[:,-1]
y_test=testing[:,-1]

def ridge_regression1(x_train,y_train,eps,alpha,lamda):
    column=x_train.shape[1]
    w=np.zeros(x_train.shape[1])
    w_nxt=np.zeros(x_train.shape[1])
    
   
    while(1):
        w_t=w.transpose()
        b=np.dot(x_train,w_t)
        diff=np.subtract(y_train,b)
        
        w_nxt[0]=w[0]+alpha*np.sum(diff)
        mul=alpha*lamda*w
        subs_w=np.subtract(w,mul)
        w[0]=w_nxt[0]
        
    
        for j in range(1,column):
            
            muli=np.dot(diff.T,x_train[:,j])
            w_nxt[j]=subs_w[j]+alpha*(muli)
            #.....................................
        
    
        w_diff=np.subtract(w,w_nxt)
        err=np.linalg.norm(w_diff)
    
        w=np.copy(w_nxt)
        if(err<eps):
          break
    
  
  
    
        
    return(w)
     
w_train=ridge_regression1(x_train,y_train,eps=.00001,alpha=.001,lamda=.00390)
yp=np.dot(x_test,w_train)
error=np.subtract(yp,y_test)
error=np.sum(error)
error2 = (error**2)/test
rms=np.sqrt(error2)




          
     
