# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 19:22:17 2018

@author: SRIKANT
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 09:30:17 2018

@author: Student

"""
#maximum and minimum element of matrix along with their location

a=[[1,2,3,4,5],
   [3,4,5,6,7],
   [1,4,5,6,7],
   [5,6,7,4,3]]

maximum =a[0][0]
minimum = a[0][0]

row = len(a)
col = len(a[0])
max_r,max_c = 0,0
min_r,min_c =0,0

for i in range(0,row) :
    for j in range(0, col):
       
        if (a[i][j]>maximum):
            maximum = a[i][j]
            max_r,max_c = i,j
        if (a[i][j]<minimum):
            minimum = a[i][j]
            min_r,min_c =i,j

print('maximum element of given matrix - {}'.format(maximum))
print('index of maximum element - {} {}'.format(max_r,max_c))
print('minimum element of given matrix - {}'.format(minimum))
print('index of minimum element - {} {}'.format(min_r,min_c))






##a=[1,2,3,4,5]
#b=[3,4,5,6,7]
#sat=a[0]
#satt=b[0]
#c=[]
#rowa = len(a)
#rowb = len(b)
#for i in range(0,rowa):
     #for j in range(0,rowb):
        # if (a[i]==b[j]):
             #c.append(a[i])
#print(c)             

   

