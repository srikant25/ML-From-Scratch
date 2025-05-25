# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 19:00:12 2018

@author: srikant nayak
"""

from gd_assent import gradient_assent
import pandas as pd
import numpy as np
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
my_data=np.insert(my_data,0,1,axis=1)
row,col=my_data.shape
train=math.ceil(.7*row)
test=row-train
training,testing=my_data[:train,:],my_data[train:,:]
xtrain=training[0:,0:-1]
xtest=testing[0:,0:-1]
ytest=testing[0:,-1]
ytrain=training[0:,-1]
h=np.zeros(xtest.shape[0])
y_pred=np.zeros(xtest.shape[0])
w=gradient_assent(xtrain,ytrain,alpha=.001,eps=.0001)
np.savetxt('w_logistic',w,delimiter=',')
tp=0
tn=0
fp=0
fn=0
for i in range(test):
    h[i]=np.dot(xtest[i],w.T)
    if(h[i]>0):
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
        



