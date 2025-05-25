# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 13:26:56 2018

@author: srikant nayak
"""
import numpy as np
def rms_value(x_test,y_test,w_train,test):
    yp=np.dot(x_test,w_train)
    error=np.subtract(yp,y_test)
    error=np.sum(error)
    error2 = (error**2)/test
    
    rms=np.sqrt(error2)
    return(rms)
    
    