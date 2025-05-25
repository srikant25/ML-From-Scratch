# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 02:45:25 2018

@author: srikant nayak
"""

import numpy as np
import math
from scipy.spatial import distance


my_data=np.genfromtxt('data4.csv',delimiter=',')
np.random.shuffle(my_data)
row,col=my_data.shape
train=math.ceil(.7*row)
test=row-train
training,testing=my_data[:train,:],my_data[train:,:]
xtrain=training[0:,0:-1]
xtest=testing[0:,0:-1]
ytest=testing[0:,-1]
column=xtrain.shape[1]
ytrain=training[0:,-1]

def euclidean_distance(x,y):
    dis=distance.euclidean(x,y)
    return(dis)
    
def mahalanobis_distance(x,y,inv_cov):
    
    dis=distance.mahalanobis(x,y,inv_cov)
    return(dis)
    
def manhattan_distance(xtrain,xtest):
    distan = abs(xtrain[0] - xtest[0]) + abs(xtrain[1] - xtest[1])
    return(distan)
    
    
    
    
    
def knn(xtrain,ytrain,xtest,k):
    kn=10
    y_knn=np.array([])
    for i in range(0,test):
        
        dis=np.array([])
        covarience=np.cov(xtrain.T)
        inv_cov=np.linalg.inv(covarience)
    
        for k in range(0,train):
            
            #dist=euclidean_distance(xtrain[k],xtest[i])
            #dist=manhattan_distance(xtrain[k],xtest[i])
            dist=mahalanobis_distance(xtrain[k],xtest[i],inv_cov)
            
            dis=np.append(dis,dist)
            
        zipped=zip(dis,ytrain)
        sorted_zipped=sorted(zipped,key=lambda x: x[0])
        k1,y_train=zip(*sorted_zipped)
        knn=y_train[0:kn]
        j=max(set(knn), key = knn.count)
            
        y_knn=np.append(y_knn,j)
    return(y_knn)
y_test=knn(xtrain,ytrain,xtest,k=5)
tp,tn,fp,fn=0,0,0,0
for i in range(0,test):
    
    if(y_test[i]==ytest[i]==1):
        tp=tp+1
    elif(y_test[i]==1 and ytest[i]==-1):
        fp=fp+1    
    elif(y_test[i]==-1 and ytest[i]==-1):
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

                
    




    

    
        
        
              