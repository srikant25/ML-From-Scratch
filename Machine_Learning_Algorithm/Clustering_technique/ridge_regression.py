# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 02:00:37 2018

@author: srikant nayak
"""

import numpy as np
from sklearn.model_selection import train_test_split
from zs import normalization
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

my_data=np.genfromtxt('data1.csv',delimiter=',')

x_data=my_data[0:,0:-1]
x_norm=normalization(x_data)
x=np.insert(x_norm,0,1,axis=1)

y=my_data[:,-1]
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3,stratify=y)
#def ridge_regression1(x_train,y_train,eps,alpha,lamda):
column=x.shape[1]
w=np.zeros(x.shape[1])
w_nxt=np.zeros(x.shape[1])
eps=.00001
alpha=.001
lamda=.00390
iteration=0
while(1):
    iteration=iteration+1
    w_t=w.transpose()
    b=np.dot(x_train,w_t)
    f=(1 / (1 + np.exp(-b)))
    diff=np.subtract(y_train,f)
    
    w_nxt[0]=w[0]+alpha*np.sum(diff)
    mul=alpha*lamda*w
    subs_w=np.subtract(w,mul)
    w[0]=w_nxt[0]
    for j in range(1,column):
        
        muli=np.dot(diff.T,x_train[:,j])
        w_nxt[j]=subs_w[j]+alpha*(muli)
        #.....................................
    

    w_diff=np.subtract(w,w_nxt)
    err=np.linalg.norm(w_diff)

    w=np.copy(w_nxt)
    if(err<eps):
      break
    if(iteration>200):
      break
  

#w_train=ridge_regression1(x_train,y_train,eps=.00001,alpha=.001,lamda=.00390)

h=np.zeros(x_test.shape[0])
y_pred=np.zeros(x_test.shape[0])
tp=0
tn=0
fp=0
fn=0
for i in range(x_test.shape[0]):
    h[i]=np.dot(x_test[i],w.T)
    if(h[i]>0):
        y_pred[i]=1
        if(y_test[i]==y_pred[i]==1):
            tp=tp+1
        else:fp=fp+1
        
    else:
        y_pred[i]=-1
        if(y_test[i]==y_pred[i]==-1):
            tn=tn+1
        else:fn=fn+1

print(tp)
print(tn)
print(fp)
print(fn)   
sensitivity=(tp/(tp+fn)) 
accuracy=((tp+tn)/x_test.shape[0])
specificity=(tn/(tn+fp))
precision=(tp/(tp+fp))
Fmeasure=(2*precision*sensitivity)/(precision+sensitivity)
print('the sensitivity is {}'.format(sensitivity))
print('the accuracy is {}'.format(accuracy))
print('the specificity is {}'.format(specificity))
print('the precision is {}'.format(precision))
print('the Fmeasure is {}'.format(Fmeasure))






#hyperplane...............
A1=x[:,1]
A2=x[:,2]

for i in range(y_train.shape[0]):
    if y_train[i]==1:
      plt.scatter(A1[i],A2[i],c='green')
    else:
      plt.scatter(A1[i],A2[i],c='blue')
  
p = np.linspace(-2,2,500)
plt.plot(p,-(w[0]/w[2])- (w[1]/w[2])*p)
plt.show()



          
     
