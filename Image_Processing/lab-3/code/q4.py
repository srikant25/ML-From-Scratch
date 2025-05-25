# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 06:26:06 2018

@author: srikant nayak
"""

from PIL import Image
import numpy as np 
from matplotlib import pyplot as plt
A = Image.open(’D:/ml lab prog/dip/lab 3/cameraman.tif’).convert(”L”)
 plt.show(A) 
 Arr = np.array(A) 
 u, s, vh = np.linalg.svd(Arr)
sr = np.array(s[0:100]) ur = np.array(u[0:256, 0:100])
 vr = np.array(vh[0:100, 0:256])
z = np.zeros((256,256))
for i in range(0,100):
    ui = ured[0:256,0:i]
    vi = vred[0:i,0:256]
    appr = np.matmul(ui,vi)
    z = z + sred[i] * appr
    recimg = Image.fromarray(z) imshow(recimg)
    imshow(A) title(’original’)
error = Arr - z 
errorimg = Image.fromarray(error)
imshow(errorimg)
calc = 0 
 for j in range(101,256):
     calc = calc + (s[i]**2) 
     print(calc)
noise = np.random.randint(20, size=(256, 256))
imgnoise = Arr + noise nimg = Image.fromarray(imgnoise.astype(’uint8’)) 
imshow(nimg)
nArr = np.array(nimg) 
un, sn, vhn = np.linalg.svd(nAarr)
snr = np.array(s[0:100]) 
unr = np.array(u[0:256, 0:100]) 
vnr = np.array(vh[0:100, 0:256]) 
en = np.zeros((256,256))
for i in range(0,100): 
    uni = unred[0:256,0:i] 
    vni = vnred[0:i,0:256] 
    apprn = np.matmul(ui,vi) 
    en = en + snred[i] * appr
recnimg = Image.fromarray(en) 
imshow(recnimg)
err = list()
for i in range(0,256):
    k = 0
    if i==255: 
        break
    for j in range(i+1,256):
        k = k + s[j] err.append(k)
        err.append(0)
        kv = np.arange(1,257) 
plot(kv,err) 
title(’k v/s Error plot’) 
xlabel(’k’) 
ylabel(’Error’)


