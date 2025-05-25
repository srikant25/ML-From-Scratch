# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 22:29:05 2018

@authr: SRIKANT
"""
impt

_descent(x_train,y_train,eps=1e-5,alpha=1e-7):

def gradien
    my_data=np.genfromtxt('Data1.csv',delimiter=',')
    my_data=np.insert(my_data,0,1,axis=1)
    x=my_data[0:,0:-1]
    p=x.shape[0]

    y=my_data[:,-1]
    
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
        
gradient_descent()