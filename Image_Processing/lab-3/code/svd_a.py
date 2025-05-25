# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 17:58:01 2018

@author: srikant nayak
"""

#3rd  question SVD
# (a)
import numpy as np
from PIL import Image
import scipy.misc
import math
a=[
[0, 1, 0],
[1 ,0 ,1],
[0 ,1 ,0]
]
#values, vectors = scipy.sparse.linalg.eigs(a, k=1, sigma=1)


sv=np.linalg.svd(a)
eigen_sort=np.sort(sv[1][:])

sqrt_eigen=list()
for i in range(len(eigen_sort)):
   sqrt_eigen.append(math.sqrt(eigen_sort[i]))
i=0
k=-1
for j in range(3):
   e=np.outer(sv[0][:,j],sv[2][:,j])
   img=np.dot(sqrt_eigen[k],e)
   img1=Image.fromarray(img)
   scipy.misc.imsave('eigh_image{0}.png'.format(j),img1)
   k-=1
   
   