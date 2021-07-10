import numpy as np
import imageio as io
import matplotlib.pyplot as plt

img = io.imread('color1.jpg')
r,c,d=img.shape
grayImage=np.zeros((r,c,d),dtype=np.uint8)

for i in range(r):
    for j in range(c):
         grayImage[i,j]=img[i,j,0]*0.3+img[i,j,1]*0.59+img[i,j,2]*0.11
        
plt.imshow(img)
plt.show()
plt.close()

        
plt.imshow(grayImage,cmap="gray")
plt.show()
plt.close()
