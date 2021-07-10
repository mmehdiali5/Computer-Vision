# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 19:31:59 2021

@author: Muhammad_Mehdi_Ali
"""

import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
import math

img=cv.imread('beforeAffine.jpeg',0)
r,c=img.shape

expectedOutput=cv.imread('afterAffine.jpeg',0)
r2,c2=expectedOutput.shape



# x1=1318
# y1=1294
# x1_=389
# y1_=323

# x2=1077
# y2=1339
# x2_=403
# y2_=397

# x3=1274
# y3=1481
# x3_=443
# y3_=337

# Correspondances
x1=18
y1=39
x1_=18
y1_=70

x2=274
y2=38
x2_=274
y2_=15

x3=275
y3=351
x3_=275
y3_=328


b=np.zeros((6,1),dtype='float64')
b[0][0]=x1_
b[1][0]=y1_
b[2][0]=x2_
b[3][0]=y2_
b[4][0]=x3_
b[5][0]=y3_

A=np.zeros((6,6),dtype='float64')
A[0][0]=x1
A[0][1]=y1
A[0][2]=1

A[1][3]=x1
A[1][4]=y1
A[1][5]=1

A[2][0]=x2
A[2][1]=y2
A[2][2]=1

A[3][3]=x2
A[3][4]=y2
A[3][5]=1

A[4][0]=x3
A[4][1]=y3
A[4][2]=1

A[5][3]=x3
A[5][4]=y3
A[5][5]=1

inverseA=np.linalg.inv(A)

parameters=inverseA.dot(b)


plt.imshow(img,cmap="gray")
plt.title("Original")
plt.show()
plt.close()

plt.imshow(expectedOutput,cmap="gray")
plt.title("ExpectedOutput")
plt.show()
plt.close()

myOutput=np.zeros((r2,c2+35),dtype='float64')
myOutput.fill(255)


for i in range (r):
    for j in range (c):
        xCoordinate=round(parameters[0][0]*i+parameters[1][0]*j+parameters[2][0])
        yCoordinate=round(parameters[3][0]*i+parameters[4][0]*j+parameters[5][0])
        myOutput[xCoordinate,yCoordinate]=img[i,j]

plt.imshow(myOutput,cmap="gray")
plt.title("MyOutput")
plt.show()
plt.close()

print(parameters)

cv.imwrite("myAffineOutput.jpeg",myOutput)
        