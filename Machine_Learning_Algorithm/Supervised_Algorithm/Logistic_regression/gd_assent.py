# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 20:28:24 2018

@author: srikant nayak
"""
def gradient_assent(xtrain,ytrain,alpha,eps):
    import numpy as np
    
    eps=.00001
    column=xtrain.shape[1]
    w=np.zeros(xtrain.shape[1])
    w_nxt=np.zeros(xtrain.shape[1])
    while(1):
        w_t=w.transpose()
        b=np.dot(xtrain,w_t)
        f=(1 / (1 + np.exp(-b)))
        diff=np.subtract(ytrain,f)
        for j in range(column):
            
            mul=np.dot(diff.T,xtrain[:,j])
            w_nxt[j]=w[j]+alpha*(mul)
    
        w_diff=np.subtract(w,w_nxt)
        err=np.linalg.norm(w_diff)
        
        w=np.copy(w_nxt)
        if(err<eps):
            break
    return(w)
        