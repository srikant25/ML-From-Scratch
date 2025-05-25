# direct method formula -*-
"""
Created on Thu Aug 16 16:46:22 2018

@author: SRIKANT
"""


import numpy as np

my_data=np.genfromtxt('Data1.csv',delimiter=',')
my_data=np.insert(my_data,0,1,axis=1)
x=my_data[0:,0:-1]
y=my_data[:,-1]

w=np.array([0 for i in range(x.shape[1])])
trans = np.dot(x.T,x)
inverse =np.linalg.inv(trans)
trans2=np.dot(x.T,y)
print(trans2)
w=np.dot(inverse,trans2)
print(w)

