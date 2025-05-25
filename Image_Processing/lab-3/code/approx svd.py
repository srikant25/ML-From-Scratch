# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 21:22:48 2018

@author: srikant nayak
"""

from PIL import Image
import numpy as np
from matplotlib import pyplot as plt

A = Image.open('D:/ml lab prog/dip/lab 3/cameraman.jpg').convert("L")


arr = np.array(A)
u, s, vh = np.linalg.svd(arr)


sred = np.array(s[0:100])
ured = np.array(u[0:256, 0:100])
vred = np.array(vh[0:100, 0:256])

z = np.zeros((256,256))

for i in range(0,100):
    ui = ured[0:256,0:i]
    vi = vred[0:i,0:256]
    appr = np.matmul(ui,vi)
    z = z + sred[i] * appr

r_img = Image.fromarray(z)
im.show(r_img)



error = arr - z
error_img = Image.fromarray(error)
im.show(error_img)



k = 0
#Calculation of Error
for j in range(101,256):
    k = k + (s[i]**2)
print(k)

noise = np.random.randint(20, size=(256, 256))
img_noise = arr + noise
n_img = Image.fromarray(img_noise.astype('uint8'))
im.show(n_img)

n_arr = np.array(n_img)
un, sn, vhn = np.linalg.svd(n_arr)

snred = np.array(s[0:100])
unred = np.array(u[0:256, 0:100])
vnred = np.array(vh[0:100, 0:256])
en = np.zeros((256,256))

for i in range(0,100):
    uni = unred[0:256,0:i]
    vni = vnred[0:i,0:256]
    apprn = np.matmul(ui,vi)
    en = en + snred[i] * appr

r_img = Image.fromarray(en)
im.show(r_img)

