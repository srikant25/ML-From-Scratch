# 2-d convolution-*-
"""
Created on Sun Aug 19 19:34:11 2018

@author: SRIKANT
"""


from scipy import signal

x=([1,0,0],[0,0,0],[0,0,0])
h=([1,1,0],[1,0,1],[1,0,0])
convolution=signal.convolve2d(x,h)
print(convolution)