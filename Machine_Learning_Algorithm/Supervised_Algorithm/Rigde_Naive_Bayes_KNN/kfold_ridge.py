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
import matplotlib.pyplot as plt


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
lamda=np.array([.00003,.00006,.000144,.000244,.000488,.0009776])
rms_array=np.array([])

aal=alpha.size
lam=lamda.size
#print(aal)
eps=1e-5

rms_min=0
rms_min2=0
Rms_test=np.array([])
rms_train=np.array([])
sum5=0.0
sum6=0.0
for m in range(lam):
    #np.random.shuffle(my_data)
    for j in range(aal):
        
        for i in range(k):
            x_test=main_x[:l]
            x_train=main_x[l:rows]
            y_test=main_y[:l]
            y_train=main_y[l:rows]
            
            w_train=ridge_regression1(x_train,y_train,eps,alpha[j],lamda[m])
            rms1=rms_value(x_test,y_test,w_train,test)
            rms2=rms_value(x_train,y_train,w_train,train)
            sum5=sum5+rms1
            sum6=sum6+rms2
            x_temp=np.concatenate((x_train,x_test))
            y_temp=np.concatenate((y_train,y_test))
            main_x=np.copy(x_temp)
            main_y=np.copy(y_temp)
            
            
            
        rms_avg=sum5/k
        rms_avg1=sum6/k
        #print("avg",rms_avg)
    
        
        if(rms_min<rms_avg):
            rms_min=rms_avg
            alpha_min=alpha[j]
            lamda_min=lamda[m]
        if(rms_min2<rms_avg1):
            rms_min2=rms_avg1
            
        
        
    print('rms_min',rms_min)
    Rms_test=np.append(Rms_test,rms_min)
    #rms_train=np.append(rms_train,rms_min2)
    print('alpha_min',alpha_min)
    
    print(lamda_min)
    
'''
plt.plot(lamda,Rms_test,c='red')
plt.plot(lamda,rms_train,c='blue')
plt.show()
#np.sort(Rms)
'''