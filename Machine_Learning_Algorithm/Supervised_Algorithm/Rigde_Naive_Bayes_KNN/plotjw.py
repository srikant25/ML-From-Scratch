# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 05:11:55 2018

@author: srikant nayak
"""

import numpy as np
import matplotlib.pyplot as plt
from zs import normalization
from ridge_regression import ridge_regression1
import math
my_data=np.genfromtxt('data1.csv',delimiter=',')
#out = normalization(my_data)
#out = np.delete(out,0,1)
my_data=np.insert(my_data,0,1,axis=1)
num1,num2=my_data.shape
train=math.ceil(.7*num1)
test= num1-train


np.random.shuffle(my_data)
training, testing = my_data[:train,:], my_data[train:,:]



x_train=training[0:,0:-1]
#x_train=normalization(x_train)

x_test=testing[0:,0:-1]

y_train=training[:,-1]
y_test=testing[:,-1]

jw_array=np.array([])
column=x_train.shape[1]
w=np.zeros(x_train.shape[1])
w_nxt=np.zeros(x_train.shape[1])
alpha=.001
lamda=.00390
eps=.00001
   
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
    xw=np.dot(x_train,w_nxt)
    xwy=np.subtract(xw,y_train)
    norm=np.linalg.norm(xwy)
    jw=.5*pow(norm,2)
    print(jw)
    jw_array=np.append(jw_array,jw)

    w_diff=np.subtract(w,w_nxt)
    err=np.linalg.norm(w_diff)

    w=np.copy(w_nxt)
    if(err<eps):
      break

plt.plot(jw_array)
plt.show()  





