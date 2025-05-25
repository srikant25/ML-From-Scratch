# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 04:13:25 2018

@author: srikant nayak
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 14:05:41 2018

@author: srikant nayak
"""
import numpy as np
import math
from rms import rms_value
from ridge_regression import ridge_regression1


my_data=np.genfromtxt('data1.csv',delimiter=',')
my_data=np.insert(my_data,0,1,axis=1)
num1,num2=my_data.shape
train=math.ceil(.7*num1)
test= num1-train
np.random.shuffle(my_data)
training, testing = my_data[:train,:], my_data[train:,:]
main_x=training[0:,0:-1]
main_y=training[:,-1]
rows,columns=training.shape
k=10 #no of fold
l=int(rows/k)
alpha=np.array([.000001,.00001,.0001,.001,.01])
lamda=np.array([.00003,.00006,.000144,.000244,.000488,.0009776,.00195,.00396,.00781,.0156,.03125,.0625,.125])
rms_array=np.array([])

aal=alpha.size
lam=lamda.size
#print(aal)
eps=1e-5

rms_min=99
sum5=0.0
for j in range(aal):
    for m in range(lam):
        
        for i in range(k):
            x_test=main_x[:l]
            x_train=main_x[l:rows]
            y_test=main_y[:l]
            y_train=main_y[l:rows]
            
            w_train=ridge_regression(x_train,y_train,eps,alpha[j],lamda[m])
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
    
