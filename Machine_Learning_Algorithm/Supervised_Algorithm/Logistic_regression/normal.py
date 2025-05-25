# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 12:30:04 2018

@author: srikant nayak
"""
import numpy as np
import math
def normal_distribution(xtest,m,sigma,n):
    
    q=((2*3.14)**(n/2))
    r=np.linalg.det(sigma)
    v=r**.5
    w=q*v
    
    sub=np.subtract(xtest,m)
    
    covi=np.linalg.inv(sigma)
    cov_sub=np.dot(covi,sub)
    s=np.dot(sub.T,cov_sub)
    
    t=.5*s
   
    pxy=(1/w)*math.exp(-t)
    
    
    return(pxy)
        
    