# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 11:32:44 2018

@author: srikant nayak
"""

import numpy as np
from PIL import Image
def haarMatrix(n, normalized=True):
    n = 2**np.ceil(np.log2(n))
    if n > 2:
        h = haarMatrix(n / 2)
        else:
            return 
    np.array([[1, 1], [1, -1]])
    hn = np:kron(h; [1; 1])

   if normalized:
      hi = np:sqrt(n=2) * np:kron(np:eye(len(h)); [1;-1])
   else :
     hi = np:kron(np:eye(len(h)); [1;-1])
     h = np.vstack((hn; hi))
     return h
a = ([255,255,255,255,255,255,255,255], [255,255,255,100,100,100,255,255], [255,255,100,150,150,150,100,255],
[255,255,100,150,200,150,100,255], [255,255,100,150,150,150,100,255], [255,255,255,100,100,100,255,255],
[255,255,255,255,50,255,255,255], [50,50,50,50,255,255,255,255])
arr = np.array(a)
arr_img = Image.fromarray(arr.astype('uint8'))
arr_img.show()
arr_img.save("g.pdf")
h = haarMatrix(8)
h_t = np.transpose(h)
arr_h_t = np.matmul(arr,h_t)
h_arr_h_t = np.matmul(h,arr_h_t)
haar_img = Image.fromarray(h_arr_h_t.astype('uint8'))
haar_img.show()
haar_img.save("haar.pdf")
a = h_arr_h_t
ah = np.matmul(a,h)
htah = np.matmul(h_t,ah)
re_img = Image.fromarray(htah.astype('uint8'))
re_img.show()
re_img.save("reimg.pdf")
