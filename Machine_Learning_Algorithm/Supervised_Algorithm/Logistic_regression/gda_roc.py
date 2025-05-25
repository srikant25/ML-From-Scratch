# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 15:25:52 2018

@author: srikant nayak
"""

from gd_assent import gradient_assent
import numpy as np
import matplotlib.pyplot as plt
import math

my_data=np.genfromtxt('data1.csv',delimiter=',')
w_gda=np.genfromtxt('w1_gda.csv',delimiter=',')
np.random.shuffle(my_data)
my_data=np.insert(my_data,0,1,axis=1)
row,col=my_data.shape
train=math.ceil(.8*row)
test=row-train
training,testing=my_data[:train,:],my_data[train:,:]
xtrain=training[0:,0:-1]
xtest=testing[0:,0:-1]
ytest=testing[0:,-1]
ytrain=training[0:,-1]
prob=[]
tpr=np.zeros(xtest.shape[0])
fpr=np.zeros(xtest.shape[0])
y_pred=np.zeros(xtest.shape[0])
#w=gradient_assent(xtrain,ytrain,alpha=.0001,eps=.00001)


for i in range(test):
    b=np.dot(w_gda.T,xtest[i])
    f=(1 / (1 + np.exp(-b)))
    prob.append(f)
    

#prob=np.array(prob)
zipped=zip(prob,ytest)
sorted_zipped=sorted(zipped, key=lambda x: x[0],reverse=True)
prob1,y_test=zip(*sorted_zipped)


def div(x,y):
    if (y == 0):
        return 0
    else:
        return x/y
    

def performance(prob,ytest,treshold):
    y_pred=np.zeros(len(ytest))
    tp,tn,fp,fn=0,0,0,0
    for j in range(len(y_pred)):
        if(treshold <= prob[j]):
            y_pred[j]=1
        else:
            y_pred[j]=0
        if(y_pred[j]==ytest[j]==1):
            tp=tp+1
        elif(y_pred[j]==1 and ytest[j]==0):
            fp=fp+1    
        elif(y_pred[j]==0 and ytest[j]==0):
            tn=tn+1
        else:
            fn=fn+1     
    sensitivity=div(tp,(tp+fn)) 
    specificity=div(fp,(tn+fp))
    return [sensitivity,specificity]
    
for i in range(test): 
    sensitivity,specificity =performance(prob1,y_test,prob1[i])
    tpr=np.append(tpr,sensitivity)
    fpr=np.append(fpr,specificity)
plt.plot(fpr,tpr)
plt.show()
