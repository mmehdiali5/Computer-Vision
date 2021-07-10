import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv


img=cv.imread('building.jpeg',0)
r,c=img.shape

plt.imshow(img,cmap="gray")
plt.title("Original")
plt.show()
plt.close()


R1=round(r/2)
C1=round(c/2)

resizedImg=np.zeros((R1,C1),dtype='float64')
Rs=0
Cs=0

if(r>R1):
    Rs=r/R1
else:
    Rs=(r-1)/R1

if(c>C1):
    Cs=c/C1
else:
    Cs=(c-1)/C1

for i in range(R1):
    for j in range(C1):
        i1=round(i*Rs)
        j1=round(j*Cs)
        resizedImg[i,j]=img[i1,j1]

plt.imshow(resizedImg,cmap="gray")
plt.title("Resized")
plt.show()
plt.close()

        

