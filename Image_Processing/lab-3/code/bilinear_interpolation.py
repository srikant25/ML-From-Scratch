# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 00:14:59 2018

@author: srikant nayak
"""

import numpy as np
from PIL import Image
img=Image.open('q1.bmp')
arr=np.array(img,dtype='float64')
h=arr.shape[1]
w=arr.shape[0]
out_img = np.zeros(shape=(2*w,2*h))
for j in range(w):
    for i in range(h):
        out_img[2*j][2*i] = arr[j][i]
        out_img[2*j][2*i+1]=(arr[j][i]+arr[j][i+1])/2
        out_img[2*j+1][2*i]=(arr[j][i]+arr[j+1][i])/2
        out_img[2*j+1][2*i+1]=(arr[j][i]+arr[j+1][i]+arr[j][i+1]+arr[j+1][i+1])/4
        print(out_img)
img2= Image.fromarray(out_img)
img.save("q12.bmp")
img2.show()
