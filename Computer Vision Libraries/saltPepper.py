import numpy as np
import imageio as io
import matplotlib.pyplot as plt
import cv2 as cv
import random

img=cv.imread('original.png',0)

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


                
                
