# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 13:06:53 2018

@author: srikant nayak
"""
import numpy as np
def gradient_descent(x_train,y_train,eps,alpha):
    
    w=[0 for a in range(x_train.shape[1])]
    
     
    while(1):
        #gradient descent code
        b=x_train.T.dot(y_train)
        trans=x_train.T.dot(x_train).dot(w)
        Djw=np.subtract(trans,b)
        w_train = np.subtract(w,(alpha * Djw))
        
        diff= w_train - w
        error=np.linalg.norm(diff,2)
        w= w_train
        
        #calculate error based one w
        if(error<eps):
            break
    print(w_train)
    return(w_train)
       

