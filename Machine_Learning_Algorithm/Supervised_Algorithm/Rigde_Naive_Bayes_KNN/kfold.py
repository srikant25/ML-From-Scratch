# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 18:19:23 2018

@author: srikant nayak
"""

import numpy as np
from rms import rms_value
from ridge_regression import ridge_regression1
from sklearn.model_selection import train_test_split
from sklearn.model_selection import StratifiedKFold



my_data=np.genfromtxt('data1.csv',delimiter=',')
my_data=np.insert(my_data,0,1,axis=1)
x=my_data[0:,0:-1]
y=my_data[:,-1]
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3,stratify=y)
rows=x_train.shape
k=10 
l=int(rows/k)
skf=StratifiedKFold(n_splits=10,suffle=True)
skf.get_n_splits(x_train,y_train)






'''
alpha=np.array([.000001,.00001,.0001,.001,.01])
lamda=np.array([.00003,.00006,.000144,.000244,.000488,.0009776])
rms_array=np.array([])

aal=alpha.size
lam=lamda.size

eps=1e-5

rms_min=0
rms_min2=0
Rms_test=np.array([])
rms_train=np.array([])
sum5=0.0
for m in range(lam):
    
    for j in range(aal):
        skf=StratifiedKFold(n_splits=10,suffle=True)
        skf.get_n_splits(x_train,y_train)
        
        for train_index, test_index in skf.split(x_train, y_train):
            
            xtrain,xtest=x_train[train_index],x_train[test_index]
            ytrain,ytest=y_train[train_index],y_train[test_index]
            
            w_train=ridge_regression1(xtrain,ytrain,eps,alpha[j],lamda[m])
            rms1=rms_value(xtest,ytest,w_train,xtest.shape)
            
            sum5=sum5+rms1
            
            x_temp=np.concatenate((xtrain,xtest))
            y_temp=np.concatenate((ytrain,ytest))
            x_train=np.copy(x_temp)
            y_train=np.copy(y_temp)
        
        
        
    rms_avg=sum5/k
    
    #print("avg",rms_avg)

    
    if(rms_min<rms_avg):
        rms_min=rms_avg
        alpha_min=alpha[j]
        lamda_min=lamda[m]
    
        
    
    
print('rms_min',rms_min)
Rms_test=np.append(Rms_test,rms_min)

print('alpha_min',alpha_min)

print(lamda_min)
'''