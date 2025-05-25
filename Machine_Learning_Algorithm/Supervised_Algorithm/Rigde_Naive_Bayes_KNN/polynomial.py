# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 08:15:33 2018

@author: srikant nayak
"""# -direct method of  -*-




from gradient_def import gradient_descent
import numpy as np
from zs import normalization
import math
from sklearn.model_selection import train_test_split
my_data=np.genfromtxt('data2.csv',delimiter=',')
import matplotlib.pyplot as plt

x=my_data[0:,0:-1]
y=my_data[:,-1]
X=np.power(x,8)
X=normalization(X)
X=np.insert(X,0,1,axis=1)

xtrain,x_test,y_train,y_test=train_test_split(X,y,test_size=0.3)

alpha=.00001
eps=.00001

w_old=np.zeros(xtrain.shape[1])
w_new=np.zeros((xtrain.shape[1]))

while(1):
    
    xtx=np.dot(xtrain.T,xtrain)
    xtxw=np.dot(xtx,w_old)

    xty=np.dot(xtrain.T,y_train)

    gradient=np.subtract(xtxw,xty)

    w_new=np.subtract(w_old,alpha*gradient)

    diff=np.subtract(w_new,w_old)

    error=np.linalg.norm(diff)

    w_old=np.copy(w_new)
    print(error)
    
    if error<eps:
        break


A1=X[:,1]
#A2=X[:,2]
y_pred=np.array([])
yp=np.dot(x_test,w_old)
error=np.subtract(yp,y_test)
error=np.sum(error)
error2 = (error**2)/x_test.shape[0]
rms=np.sqrt(error2)
print('RMSE',rms)
y_pred=np.dot(w_old.T,X.T)
#plt.plot(y_pred,x)
for i in range(X.shape[0]):
    
    plt.scatter(x[i],y_pred[i],c='green')
    plt.scatter(x[i])


