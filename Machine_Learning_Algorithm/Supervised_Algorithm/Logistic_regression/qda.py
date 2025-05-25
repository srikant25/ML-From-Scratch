# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 12:51:37 2018

@author: srikant nayak
"""

import numpy as np
from normal import normal_distribution 
from sklearn.model_selection import train_test_split
import math
import pandas as pd

df = pd.read_csv('data5.csv',header=None)

my_data = df.values
#np.random.shuffle(my_data)
X=my_data[0:,0:-1]
y=my_data[:,-1]


xtrain, xtest, ytrain, ytest = train_test_split(X, y, test_size = 0.3, stratify=y,)
pos=[]
neg=[]
train=xtrain.shape[0]
test=xtest.shape[0]
for i in range(xtrain.shape[0]):
    if(ytrain[i]==1):
      pos.append(xtrain[i])
    else:
      neg.append(xtrain[i])
pos=np.asarray(pos)
neg=np.asarray(neg)
p=pos.shape[0]
n=neg.shape[0]
py1=p/train
py0=n/train
m1=np.mean(pos,axis=0)
m0=np.mean(neg,axis=0)
sigma1=np.cov(pos.T)
sigma0=np.cov(neg.T)
n=xtest.shape[1]


     
y_pred=np.zeros(xtest.shape[0])
tp=0
tn=0
fp=0
fn=0
for i in range(xtest.shape[0]):
    
    pxy1=normal_distribution(xtest[i],m1,sigma1,n)
    pxy0=normal_distribution(xtest[i],m0,sigma0,n)
        
    py1x=py1*pxy1
    py0x=py0*pxy0
    #print(py1x)
    
    if(py1x >= py0x):
        y_pred[i]=1
    else:
        y_pred[i]=0
        
    if(y_pred[i]==ytest[i]==1):
        tp=tp+1
    elif(y_pred[i]==1 and ytest[i]==0):
        fp=fp+1    
    elif(y_pred[i]==0 and ytest[i]==0):
        tn=tn+1
    else:
        fn=fn+1
print(tp)
print(tn)
print(fp)
print(fn)   
sensitivity=(tp/(tp+fn)) 
accuracy=((tp+tn)/test)
specificity=(tn/(tn+fp))
precision=(tp/(tp+fp))
Fmeasure=(2*precision*sensitivity)/(precision+sensitivity)
print('the sensitivity is {}'.format(sensitivity))
print('the accuracy is {}'.format(accuracy))
print('the specificity is {}'.format(specificity))
print('the precision is {}'.format(precision))
print('the Fmeasure is {}'.format(Fmeasure))
