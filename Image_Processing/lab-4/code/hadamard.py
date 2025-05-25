# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 11:54:59 2018

@author: srikant nayak
"""

import numpy as np
from scipy import linalg
from PIL import Image
a = ([255,255,255,255,255,255,255,255], [255,255,255,100,100,100,255,255], [255,255,100,150,150,150,100,255],
[255,255,100,150,200,150,100,255], [255,255,100,150,150,150,100,255], [255,255,255,100,100,100,255,255],
[255,255,255,255,50,255,255,255], [50,50,50,50,255,255,255,255])
arr = np.array(a)
arr_img = Image.fromarray(arr.astype('uint8'))
arr_img.show()
arr_img.save("g.pdf")
h = linalg.hadamard(8)
h_t = np.transpose(h)
arr_h_t = np.matmul(arr,h_t)
h_arr_h_t = np.matmul(h,arr_h_t)
hd_img = Image.fromarray(h_arr_h_t.astype('uint8'))
hd_img.show()
hd_img.save("hadamard.pdf")
a = h_arr_h_t
ah = np.matmul(a,h)
htah = np.matmul(h_t,ah)
hdr_img = Image.fromarray(htah.astype('uint8'))
hdr_img.show()
hdr_img.save("hadamard.pdf")