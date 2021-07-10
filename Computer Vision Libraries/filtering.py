import numpy as np
import imageio as io
import matplotlib.pyplot as plt
import cv2 as cv
import random
from skimage.util import random_noise


img=cv.imread('original.png',0)
img = np.pad(img, 1, mode='constant', constant_values=0)

plt.imshow(img,cmap="gray")
plt.title("Original")
plt.show()
plt.close()

img2=np.zeros(img.shape,dtype='uint8')

win=np.arange(9).reshape(3,3)

# FOR Average Filter
# win[0][0]=1
# win[0][1]=1
# win[0][2]=1
# win[1][0]=1
# win[1][1]=1
# win[1][2]=1
# win[2][0]=1
# win[2][1]=1
# win[2][2]=1


r,c=img.shape
r2,c2=win.shape

# CORRELATION
for i in range (1,r-1):
    for j in range (1,c-1):
        i1=i-1
        for k in range (r2):
            j1=j-1
            for l in range (c2):
                img2[i,j]+=win[k,l]*img[i1,j1]
                # print(i,j,i1,j1,img[i1,j1],win[k,l],img2[i][j])
                j1=j1+1
            # img2[i,j]=(1.0/9.0)*img2[i,j]
            i1=i1+1
                

# CONVOLUTION
rotatedWin=np.rot90(win,2)
img3=np.zeros(img.shape,dtype='uint8')
for i in range (1,r-1):
    for j in range (1,c-1):
        i1=i-1
        for k in range (r2):
            j1=j-1
            for l in range (c2):
                img3[i,j]+=rotatedWin[k,l]*img[i1,j1]
                # print(i,j,i1,j1,img[i1,j1],win[k,l],img2[i][j])
                j1=j1+1
            i1=i1+1




plt.imshow(img2,cmap="gray")
plt.title("CORRELATION")
plt.show()
plt.close()

plt.imshow(img3,cmap="gray")
plt.title("CONVULUTION")
plt.show()
plt.close()

