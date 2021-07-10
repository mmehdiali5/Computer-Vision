import numpy as np

import matplotlib.pyplot as plt
import cv2 as cv

gaussKernal=np.arange(9).reshape(3,3).astype('float64')

img=cv.imread('g2.png',0)
img = np.pad(img, 1, mode='constant', constant_values=0)

plt.imshow(img,cmap="gray")
plt.title("Original")
plt.show()
plt.close()

sigma=10
sumOfKernal=0.0
for x,i in zip(range(-1,2),range(3)):
    for y,j in zip(range(-1,2),range(3)):
          gaussKernal[i,j]=((1.0/((2.0*3.14)*(sigma)**2.0)))*(2.718**(-1.0*((x**2+y**2)/(2.0*sigma**2))))
          sumOfKernal=sumOfKernal+gaussKernal[i,j]
 
    
r,c=img.shape
r2,c2=gaussKernal.shape

blur_img=np.zeros(img.shape,dtype='uint8')
sum1=0.0

for i in range (1,r-1):
    for j in range (1,c-1):
        i1=i-1
        sum1=0.0
        for k in range (r2):
            j1=j-1
            for l in range (c2):
                sum1+=gaussKernal[k,l]*img[i1,j1]
                j1=j1+1
            i1=i1+1      
        blur_img[i,j]=(1/sumOfKernal)*sum1
        

plt.imshow(blur_img,cmap="gray")
plt.title("BLUR")
plt.show()
plt.close()  

integer=3060
integer=integer.astype('uint8')
    

              
        

        