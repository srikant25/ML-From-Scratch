# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 19:55:36 2018

@author: SRIKANT
"""

import numpy as np

a=int(input('number of element in array:'))


array1 = []
array2 = []
add=[]
sub=[]
mul=[]
div=[]

for i in range(a):
    p=input('input {} element of first array '.format(i+1) )
    array1.append(int(p))
    
for i in range(a):
    q=input('input {} element of second array '.format(i+1))
    array2.append(int(q))
    
print('\narray is:',array1)
print('\narray is:',array2)

for i in range(0,a):
    add.append(array2[i] + array1[i])
    sub.append(array1[i] - array2[i])
    mul.append(array1[i] * array2[i])
for i in range(0,a):
    if (array2[i] != 0):
        div.append(array1[i]/array2[i])
    else:
        div.append('nan')

                        
print('element wise addition of array 1 and 2 is-\n{}\n'.format(add))                      
print('element wise substraction of array 1 and 2 is-\n{}\n'.format(sub))                      
print('element wise multiplication of array 1 and 2 is-\n{}\n'.format(mul))                      
print('element wise division of array 1 and 2 is-\n{}\n'.format(div))                      
            

        
        
        
        