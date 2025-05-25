# -*- gradient descent utf-8 -*-
"""
Created on Sat Aug 18 00:19:10 2018

@author: SRIKANT
"""

import numpy as np
#def gradient_descent(x_train,y_train,eps=1e-5,alpha=1e-7,my_data):
my_data=np.genfromtxt('Data1.csv',delimiter=',')
my_data=np.insert(my_data,0,1,axis=1)
x=my_data[0:,0:-1]


y=my_data[:,-1] 
alpha= .000001
eps= .00005

w=[0 for i in range(x.shape[1])]


while(1):
    b=x.T.dot(y)
    
    trans=x.T.dot(x).dot(w)
    Djw=np.subtract(trans,b)
    w_nxt = w-alpha*(Djw)
    diff=np.subtract(w_nxt,w)
    error=np.linalg.norm(diff,2)
    w=w_nxt
    if error<=eps:
        break

            

print(w)
   
        
        
     
    
