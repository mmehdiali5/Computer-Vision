import numpy as np
import imageio as io
import matplotlib.pyplot as plt
import cv2 as cv
import random

img=cv.imread('original.png',0)
img = np.pad(img, 1, mode='constant', constant_values=0)

plt.imshow(img,cmap="gray")
plt.show()
plt.close()


impulse_noise=np.zeros(img.shape,dtype=np.uint8)

r,c=img.shape
prob_noise=0.01
thresh=1-prob_noise

for i in range(r):
    for j in range(c):
        ran_no=random.random()
       
        if ran_no<prob_noise:
            impulse_noise[i][j]=0
           
        elif ran_no>thresh:
            impulse_noise[i][j]=255
            
        else:
            impulse_noise[i][j]=img[i][j]
            
       
           
plt.imshow(impulse_noise,cmap="gray")
plt.show()
plt.close()


medianMask=np.arange(9).reshape(3,3)
r2,c2=medianMask.shape
removeNoise=np.zeros(img.shape,dtype=np.uint8)

for i in range (1,r-1):
    for j in range (1,c-1):
        i1=i-1
        for k in range (r2):
            j1=j-1
            for l in range (c2):
                medianMask[k,l]=impulse_noise[i1,j1]
                j1=j1+1
            i1=i1+1
        removeNoise[i,j]=np.median(medianMask)



plt.imshow(removeNoise,cmap="gray")
plt.title("Median without salt pepper")
plt.show()
plt.close()




