import numpy as np
import imageio as io
import matplotlib.pyplot as plt
import cv2 as cv

img=cv.imread('original.png',0)

plt.imshow(img,cmap="gray")
plt.show()
plt.close()

noisy_img=np.random.normal(0,3,img.shape)
plt.hist(noisy_img.ravel(),bins=100)
plt.show()
plt.close()

# img=img.astype('float64')
noisy_img=noisy_img.astype('uint8')

img_gauss=cv.add(img,noisy_img)



plt.imshow(img_gauss,cmap="gray")
plt.show()
plt.close()

