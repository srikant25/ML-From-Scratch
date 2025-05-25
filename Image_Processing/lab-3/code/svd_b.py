# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 18:11:39 2018

@author: srikant nayak
"""

#Show the different stages of SVD of the following image:
#3rd question SVD (b)
import numpy as np
from sklearn.preprocessing import normalize  
img=[
[255, 255, 255, 255, 255, 255, 255, 255],
[255 ,255 ,255 ,100 ,100 ,100 ,255 ,255],
[255, 255, 100, 150, 150, 150, 100, 255],
[255 ,255 ,100 ,150 ,200 ,150 ,100 ,255],
[255, 255, 100, 150, 150, 150, 100, 255],
[255 ,255 ,255 ,100 ,100 ,100 ,255 ,255],
[255, 255, 255, 255, 50,  255, 255, 255],
[50 , 50 , 50 , 50 , 255 ,255 ,255 ,255]
]

a=np.array(img)
eigen_value , eigen_vector=(np.linalg.eig(a))
sort_eigen_value=np.sort(abs(eigen_value))
sqrt_eigen_value=list()
for i in range(len(sort_eigen_value)):
   sqrt_eigen_value.append(math.sqrt(sort_eigen_value[i]))

norm_eigen_vector=list()
for i in range(8):
   norm_eigen_vector.append(np.linalg.norm(eigen_vector[:,i]))
#here norm values for each column c1,c2,....c8 = 1
U=abs(eigen_vector) # U matrix
v=list()
for i in range(8):
   v.append(abs(np.dot(a.T,U[:,i])))
V=np.asarray(v)
j=-1
for i in range(8):
   i1=np.outer(U[:,i],V[:,i])
   im1=np.dot(sqrt_eigen_value[-1],i1)
   scipy.misc.imsave('SVD_image{0}.jpg'.format(i),im1)
   j-=1