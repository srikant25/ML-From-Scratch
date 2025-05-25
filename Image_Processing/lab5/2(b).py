# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 21:59:43 2018

@author: srikant nayak
"""

from PIL import Image
import numpy as np
img=Image.open('3_kidney.png').convert('L')
img_arr=np.array(img)
w,h=img_arr.shape
for i in range(w):
    for j in range(h):
        if (150 > img_arr[i][j] > 100):
            img_arr[i][j] = img_arr[i][j]+50

image=Image.fromarray(img_arr)
image.show()
image.save('enhance_image.png')
