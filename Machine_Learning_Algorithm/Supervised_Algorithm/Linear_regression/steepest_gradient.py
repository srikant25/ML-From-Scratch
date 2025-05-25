# -direct method of  -*-
"""
Created on Fri Aug 17 15:23:00 2018

@author: SRIKANT
"""

import numpy as np
import math
import time

from zs import normalization
start = time.time()
my_data=np.genfromtxt('Data1.csv',delimiter=',')
my_data=normalization(my_data)
my_data=np.insert(my_data,0,1,axis=1)
num1,num2=my_data.shape
train=math.ceil(.7*num1)
test= num1-train


np.random.shuffle(my_data)
training, testing = my_data[:train,:], my_data[train:,:]


x_train=training[0:,0:-1]
x_test=testing[0:,0:-1]
y_train=training[:,-1]
y_test=testing[:,-1]

w_train=np.array([0 for i in range(x_train.shape[1])])
trans = np.dot(x_train.T,x_train)
inverse =np.linalg.inv(trans)
trans2=np.dot(x_train.T,y_train)
w_train=np.dot(inverse,trans2)
print(w_train)

yp=np.dot(x_test,w_train)
error=np.subtract(yp,y_test)
error=np.sum(error)
error2 = (error**2)/test

rms=np.sqrt(error2)
end = time.time()
print('Time taken in direct method is {}'.format(end-start))
print(rms)

np.savetxt('w_data2.csv',w_train ,delimiter=',')





##print("training",training.shape)
#print("test",test.shape)
