# -*- coding: utf-8 -*-
"""
Created on Sun Sep  2 18:17:28 2018

@author: srikant nayak
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Sep  2 15:56:01 2018

@author: srikant nayak
"""

#def gradient_descent(eps=1e-5,alpha=1e-3):
import numpy as np
import matplotlib.pyplot as plt
from zs import normalization
import math
my_data=np.genfromtxt('Data2.csv',delimiter=',')
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
eps=.00001
alpha=.001
#print(x_train)
#print(y_train)

w=np.zeros(x_train.shape[1])
x_t=x_train.transpose()
b=np.dot(x_t,y_train)
xtx = np.dot(x_t,x_train)
#jw_array=np.empty_like(jw.shape,dtype=None)
jw_array=np.array([])

while(1):
    #gradient descent code    
    #print(x_t)   
    trans2=np.dot(xtx,w)
    #print(trans2)    
    Djw=np.subtract(trans2,b)    
    intermediate=alpha*Djw
    w_train = np.subtract(w,intermediate)
    xw=np.dot(x_train,w_train)
    xwy=np.subtract(xw,y_train)
    norm=np.linalg.norm(xwy)
    jw=.5*pow(norm,2)
    print(jw)
    jw_array=np.append(jw_array,jw)
    #print(jw_array)
    
    
    diff= np.subtract(w_train,w)
    err=np.linalg.norm(diff,2)
    #print(err)
    w= np.copy(w_train)
    #calculate error based one w
    if(err<eps):
        break
plt.plot(jw_array)
plt.show()
    
    #yp=np.dot(x_test,w_train)
    #error=np.subtract(yp,y_test)
    #error=np.sum(error)
    #error2 = (error**2)/test
    #rms=np.sqrt(error2)
    #return(rms)
#gradient_descent(1e-5,1e-3)
    
