import numpy as np
import imageio as io
import matplotlib.pyplot as plt
import cv2 as cv

img=cv.imread('moon.jpeg',0)
plt.imshow(img,cmap="gray")
plt.show()
plt.close()

img_b=np.zeros(img.shape,dtype=np.uint8)

thresh=30

Ret,img_b1=cv.threshold(img,thresh,255,cv.THRESH_BINARY)
height,width=img.shape
result=np.zeros((height,width,3),np.uint8)
result[:,:,0]=img[:][:]
result[:,:,1]=img[:][:]
result[:,:,2]=img[:][:]

for i in range(height):
    for j in range(width):
        if (img[i,j]<thresh+20 and img[i,j]>thresh-20):
            result[i][j][0]=255
            result[i][j][1]=0
            result[i][j][2]=0
            

plt.imshow(img,cmap="gray")
plt.show()
plt.close()

plt.imshow(result,cmap="gray")
plt.show()
plt.close()


