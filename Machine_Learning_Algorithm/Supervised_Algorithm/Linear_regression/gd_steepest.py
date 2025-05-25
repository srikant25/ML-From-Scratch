# -*- coding: utf-8 -*-
"""
Created on Sun Sep  2 15:56:01 2018

@author: srikant nayak
"""

def gradient_descent(eps=1e-5,alpha=.001):
    import numpy as np
    from zs import normalization
    import math
    import time
    #start = time.time()
    #my_data1=np.genfromtxt('Data3.csv',delimiter=',')
    my_data=np.genfromtxt('Data1.csv',delimiter=',')
    out = normalization(my_data)
    
    #out = np.delete(out,0,1)
    my_data=np.insert(out,0,1,axis=1)
    num1,num2=my_data.shape
    train=math.ceil(.7*num1)
    test= num1-train
    
    
    np.random.shuffle(my_data)
    training, testing = my_data[:train,:], my_data[train:,:]
    
    
    
    x_train=training[0:,0:-1]
    
    x_test=testing[0:,0:-1]
    y_train=training[:,-1]
    y_test=testing[:,-1]
    #print(x_train)
    #print(y_train)
    i=0
    w=np.zeros(x_train.shape[1])
    x_t=x_train.transpose()
    b=np.dot(x_t,y_train)
    xtx = np.dot(x_t,x_train)
    while(1):
        #gradient descent code    
        #print(x_t)   
        trans2=np.dot(xtx,w)
        #print(trans2)    
        Djw=np.subtract(trans2,b)    
        intermediate=alpha*Djw
        w_train = np.subtract(w,intermediate)
        
        i=i+1
        diff= np.subtract(w_train,w)
        err=np.linalg.norm(diff,2)
        #print(err)
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
    return(rms)
    np.savetxt('w_winequality.csv',w_train ,delimiter=',')
#end = time.time()
#print('Time taken in direct method is {}'.format(end-start))
gradient_descent(1e-5,.001)
#print(rms)
    
#np.savetxt('w_winequality.csv',w_train ,delimiter=',')