# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 16:48:35 2018

@author: srikant nayak
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 16:08:15 2018

@author: srikant nayak
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 13:02:11 2018

@author: srikant nayak
"""

import numpy as np 
import math
import pandas as pd


def discretize(X,k,size):
    
    import pandas as pd
    df[k] = pd.cut(X[k],size)
    df[k] = df[k].apply(lambda x: x.mid).astype('float64')
    
    
    
    
df = pd.read_csv('adultdata.csv',header=None)
discretize(df,0,20)
discretize(df,2,20)
discretize(df,4,20)
discretize(df,10,20)
discretize(df,11,20)
discretize(df,12,20)

#df = df.drop([0],axis=1)
#df =df.replace('?',np.nan)
#df=df.fillna(method='ffill')
#df[6]=df[6].astype(int)
my_data = df.values

row,col=my_data.shape
train=math.ceil(.7*row)
test=row-train
training,testing=my_data[:train,:],my_data[train:,:]
xtrain=training[0:,0:-1]
xtest=testing[0:,0:-1]
ytest=testing[0:,-1]
column=xtrain.shape[1]
ytrain=training[0:,-1]
pos=[]
neg=[]
for i in range(xtrain.shape[0]):
    if(ytrain[i]==1):
      pos.append(xtrain[i])
    else:
      neg.append(xtrain[i])
pos=np.asarray(pos)
neg=np.asarray(neg)
p=pos.shape[0]
p1=pos.shape[1]
n=neg.shape[0]
py1=p/train
py0=n/train
arr1=[]
arr0=[]
for j in range(p1):
    data=np.unique(pos[:,j],return_index=False, return_inverse=False,return_counts=True,axis=None)
    data = list(data)
    arr1.append(data)
for k in range(neg.shape[1]):
    data1=np.unique(neg[:,k],return_index=False, return_inverse=False,return_counts=True,axis=None)
    data1 = list(data1)
    arr0.append(data1)

for j in range(xtrain.shape[1]):
    diff=set(arr1[j][0]) ^ set(arr0[j][0])
   
    for k in diff:
        if k not in (arr1[j])[0]:
            (arr1[j])[0]=np.insert((arr1[j])[0],0,k)
            (arr1[j])[1]=np.insert((arr1[j])[1],0,0)
            
        else:
            (arr0[j])[0]=np.insert((arr0[j])[0],0,k)
            (arr0[j])[1]=np.insert((arr0[j])[1],0,0)

for i in range(xtrain.shape[1]):
    a=arr1[i]
    b=a[1]
    for j in range(len(b)):
        ((arr1[i])[1])[j]=1+((arr1[i])[1])[j]
        ((arr0[i])[1])[j]=1+((arr0[i])[1])[j]

     
y_pred=np.zeros(xtest.shape[0])
tp=0
tn=0
fp=0
fn=0
for i in range(xtest.shape[0]):
    prob1=1
    prob2=1
    for j in range(xtest.shape[1]):
        value=xtest[i,j]
        if(value in (arr1[j])[0]):
            ind=list((arr1[j])[0]).index(value)
            num=((arr1[j])[1])[ind]
            dino=p+len((arr1[j])[0])
            print("Positive: count and deno for attribute {} :{},{}".format(j,num,dino))
        else:
            num=1
            dino=p+len((arr1[j])[0])+1
            print("Positive: count and deno for attribute {} :{},{}".format(j,num,dino))
        prob1=prob1*(num/dino)
        
        if(value in (arr0[j])[0]):
            ind=list((arr0[j])[0]).index(value)
            num=((arr0[j])[1])[ind]
            dino=n+len((arr0[j])[0])
            print("Negative: count and deno for attribute {} :{},{}".format(j,num,dino))
       
        else:
            num=1
            dino=n+len((arr0[j])[0])+1
            print("Negative: count and deno for attribute {} :{},{}".format(j,num,dino))
       
        prob2=prob2*(num/dino)
    py1x=py1*prob1
    py0x=py0*prob2
    #print(py1x,py0x)
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
