# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 23:22:30 2018

@author: srikant nayak
"""

import numpy as np
import pandas as pd
import math
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
my_data=df.values
#my_data=np.genfromtxt('data1.csv',delimiter=',')
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
alpha=.001
eps=.00001
pos=[]
neg=[]
for i in range(xtrain.shape[0]):
    if(ytrain[i]==1):
      pos.append(xtrain[i])
    else:
      neg.append(xtrain[i])
 
pos=np.asarray(pos)
neg=np.asarray(neg)    
positive=pos.shape[0]
negative=neg.shape[0]
mean1=np.mean(pos,axis=0)
mean0=np.mean(neg,axis=0)
sigma=np.cov(xtrain.T)
inverse=np.linalg.inv(sigma)
p_1=positive/train
p_0=negative/train
p=p_1/p_0
pr=math.log(p)
sub=np.subtract(mean1,mean0)
w_t=np.dot(inverse,sub)
wtx=np.dot(xtest,w_t)
m1t=np.dot(mean1.T,np.dot(inverse,mean1))
m0t=np.dot(mean0.T,np.dot(inverse,mean0))
w0=pr-(.5*m1t)+(.5*m0t)
t=wtx+w0
def div(x,y):
    if (y == 0):
        return 0
    else:
        return x/y
#w1w0=np.concatenate(w0,w_t)
#np.savetxt('w1_gda.csv',w_t,delimiter=',')
#np.savetxt('w0_gda.csv',w0,delimiter=',')
y_pred=np.zeros(xtest.shape[0])
tp=0
tn=0
fp=0
fn=0
for i in range(test):
    if(t[i]>0):
        
        y_pred[i]=1
        if(ytest[i]==y_pred[i]==1):
            tp=tp+1
        else:fp=fp+1
        
    else:
        y_pred[i]=0
        if(ytest[i]==y_pred[i]==0):
            tn=tn+1
        else:fn=fn+1

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
        




