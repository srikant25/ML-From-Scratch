# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 15:56:39 2018

@author: srikant nayak
"""

# -*-direct method  -*-
"""
Created on Fri Aug 17 17:46:30 2018

@author: SRIKANT
"""

import numpy as np
import math
from gradient_def import gradient_descent
from rms import rms_value
from zs import normalization


my_data=np.genfromtxt('Data2.csv',delimiter=',')

my_data= np.concatenate((normalization(my_data[:,:-1]),my_data[:,-1].reshape(my_data[:,-1].shape[0],1)),axis=1)

alpha_arr=np.array([])
#wfinal1=np.zeros((2, 1),dtype=float)
my_data=np.insert(my_data,0,1,axis=1)
for h in range(0,5):
    
    np.random.shuffle(my_data)
    num1,num2=my_data.shape
    train=math.ceil(.7*num1)
    test= num1-train
    training, testing = my_data[:train,:], my_data[train:,:]
    main_x=training[0:,0:-1]
    main_y=training[:,-1]
    rows,columns=training.shape
    k=10 #no of fold
    l=int(rows/k)
    alpha=np.array([.000001,.0001,.001])
    rms_array=np.array([])
    #w_final=np.array(([])
    aal=alpha.size
    
    eps=1e-5
    
    rms_min=99
    sum5=0.0
    for j in range(aal):
        for i in range(k):
            x_test=main_x[:l]
            x_train=main_x[l:rows]
            y_test=main_y[:l]
            y_train=main_y[l:rows]
            
            w_train=gradient_descent(x_train,y_train,eps,alpha[j])
            rms=rms_value(x_test,y_test,w_train,test)
            sum5=sum5+rms
            x_temp=np.concatenate((x_train,x_test))
            y_temp=np.concatenate((y_train,y_test))
            main_x=np.copy(x_temp)
            main_y=np.copy(y_temp)
            
        rms_avg=sum5/k
        print(alpha[j])
        print(rms_avg)
        if(rms_min>rms_avg):
            rms_min=rms_avg
            alpha_min=alpha[j]
            
    alpha_arr=np.append(alpha_arr,alpha_min)
    rms_array=np.append(rms_array,rms_min)
    
    wbest= gradient_descent(x_train,y_train,eps,alpha_min)
    
            
        
    
