# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 03:40:42 2018

@author: srikant nayak
"""

import numpy as np
from sklearn.model_selection import train_test_split
from heapq import nsmallest
from sklearn.preprocessing import LabelEncoder
import math
from scipy.spatial import distance
#normalize train data.....................
def normalize(my_data,k):
   mink=min(my_data[:,k])
   maxk=max(my_data[:,k])
   my_data[:,k]= (my_data[:,k]-mink)/(maxk-mink)
   return(my_data,mink,maxk)
#normalize test data..........   
def normalizets(data,k,mink,maxk):
   data[:,k]= (data[:,k]-mink)/(maxk-mink)
   return(data)
   #type of distance measure.............
def euclidean_distance(x,y):
    dis=distance.euclidean(x,y)
    return(dis)
def manhattan_distance(xtrain,xtest):
    distan = abs(xtrain[0] - xtest[0]) + abs(xtrain[1] - xtest[1])
    return(distan)
 # knn procedure..........   
def knn(my_data,xtrain,ytrain,xtest,kn):
    
    row,col=my_data.shape
    train=math.ceil(.7*row)
    test=row-train
    y_knn=np.array([])
    for i in range(0,test):
        
        dis=np.array([])
        
        for k in range(0,train):
            z=np.zeros(x.shape[1])
            cat=[1,2,3,4,6,7,8,10,15] #nominal column
            num=[0,5,9,11,12,13,14]    #numerical column
            for b in cat:
               if(xtrain[k,b]==xtest[i,b]):
                 z[b]==0
               else:
                  z[b]==1
            for b in  num:
                z=euclidean_distance(xtrain[k,b],xtest[i,b])
                #dist=manhattan_distance(xtrain[k],xtest[i])
                #dist=mahalanobis_distance(xtrain[k],xtest[i],inv_cov)
            
                dis=np.append(dis,z)
            
        zipped=zip(dis,ytrain)
        sorted_zipped=sorted(zipped,key=lambda x: x[0])
        k1,y_train=zip(*sorted_zipped)
        knn=y_train[0:kn]
        j=max(set(knn), key = knn.count)
            
        y_knn=np.append(y_knn,j)
    return(y_knn)    
my_data=np.genfromtxt('bank.csv',delimiter=',')
my_data = np.delete(my_data, (0), axis=0)
#convert nominal attributes to binary number..............
labelencoder = LabelEncoder()
my_data[:, 1] = labelencoder.fit_transform(my_data[:, 1])
my_data[:, 2] = labelencoder.fit_transform(my_data[:, 2])
my_data[:, 3] = labelencoder.fit_transform(my_data[:, 3])
my_data[:, 4] = labelencoder.fit_transform(my_data[:, 4])
my_data[:, 6] = labelencoder.fit_transform(my_data[:, 6])
my_data[:, 7] = labelencoder.fit_transform(my_data[:, 7])
my_data[:, 8] = labelencoder.fit_transform(my_data[:, 8])
my_data[:, 10] = labelencoder.fit_transform(my_data[:, 10])
my_data[:, 15] = labelencoder.fit_transform(my_data[:, 15])
my_data[:, 16] = labelencoder.fit_transform(my_data[:, 16])

my_data = np.array(my_data, dtype=np.float64)
rows=len(my_data)                #calculate no of rows in data file
cols=len(my_data[0])
x=np.delete(my_data,cols-1,1)
y=np.delete(my_data, np.s_[0:cols-1], axis=1)
num1,num2=my_data.shape
train=math.ceil(.7*num1)
test= num1-train
np.random.shuffle(my_data)
training, testing = my_data[:train,:], my_data[train:,:]
x_train=training[0:,0:-1]

x_test=testing[0:,0:-1]
y_train=training[:,-1]
y_test=testing[:,-1]
#x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3,stratify=y)
x_train,min0,max0=normalize(x_train,0)
x_train,min5,max5=normalize(x_train,5)
x_train,min9,max9=normalize(x_train,9)
x_train,min11,max11=normalize(x_train,11)
x_train,min12,max12=normalize(x_train,12)
x_train,min13,max13=normalize(x_train,13)
x_train,min14,max14=normalize(x_train,14)
x_test=normalizets(x_test,0,min0,max0)
x_test=normalizets(x_test,5,min5,max5)
x_test=normalizets(x_test,9,min9,max9)
x_test=normalizets(x_test,11,min11,max11)
x_test=normalizets(x_test,12,min12,max12)
x_test=normalizets(x_test,13,min13,max13)
x_test=normalizets(x_test,14,min14,max14)
row,col=my_data.shape
train=math.ceil(.7*row)
test=row-train
ytest=knn(my_data,x_train,y_train,x_test,kn=5)
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


