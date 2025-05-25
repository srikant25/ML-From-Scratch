# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 05:55:36 2018

@author: srikant nayak
"""

import numpy as np
from PIL import Image
import cv2
import random
im=cv2.imread(’cameraman.tif’,0)
x=np.random.randint(255, size=(255, 255))
#x=np.asarray(x)
x=np.reshape(x,(255,255))
for i in range(len(x)):
    for j in range(x.shape[0]):
        if x[i][j]==0:
          im[i][j]=0
        elif x[i][j]==255:
             im[i][j]=255
s_and_p_image=Image.fromarray(im)
s_and_p_image.save(’s_and_p_image.png’)
