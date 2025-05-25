# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 07:43:24 2018

@author: srikant nayak
"""

import numpy as np
from PIL import Image

def haarMatrix(n, normalized=True):
    
    n = 2**np.ceil(np.log2(n))
    if n > 2:
        h = haarMatrix(n / 2)
    else:
        return np.array([[1, 1], [1, -1]])

    
    h_n = np.kron(h, [1, 1])
     
    if normalized:
        h_i = np.sqrt(n/2)*np.kron(np.eye(len(h)), [1, -1])
    else:
        h_i = np.kron(np.eye(len(h)), [1, -1])
    
    h = np.vstack((h_n, h_i))
    return h

a = ([255,255,255,255,255,255,255,255],
     [255,255,255,100,100,100,255,255],
     [255,255,100,150,150,150,100,255],
     [255,255,100,150,200,150,100,255],
     [255,255,100,150,150,150,100,255],
     [255,255,255,100,100,100,255,255],
     [255,255,255,255,50,255,255,255],
     [50,50,50,50,255,255,255,255])

g = np.array(a)
gimg = Image.fromarray(g.astype('uint8'))
gimg.show()
gimg.save("g.pdf")

h = haarMatrix(8)
ht = np.transpose(h)
ght = np.matmul(g,ht)
hght = np.matmul(h,ght)

haarimg = Image.fromarray(hght.astype('uint8'))
haarimg.show()
haarimg.save("haar.pdf")

a = hght
ah = np.matmul(a,h)
htah = np.matmul(ht,ah)

reimg = Image.fromarray(htah.astype('uint8'))
reimg.show()
reimg.save("reimg.pdf")
