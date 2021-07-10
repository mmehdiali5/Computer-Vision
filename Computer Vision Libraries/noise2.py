import numpy as np
import imageio as io
import matplotlib.pyplot as plt
import cv2 as cv
import random
from skimage.util import random_noise

# POISSON NOISE

# img=cv.imread('original.png',0)
# noisy_img=np.zeros(img.shape,dtype='uint8')

# poisson_noise=np.random.poisson(10,img.shape)

# poisson_noise=poisson_noise.astype('uint8')

# noisy_img=cv.add(img,poisson_noise)

# cv.imshow('Original Image',img)
# cv.waitKey(0)
# cv.destroyAllWindows()

# cv.imshow('Noisy Image',noisy_img)
# cv.waitKey(0)
# cv.destroyAllWindows()

#SPECKLE NOISE
# img=cv.imread('original.png',0)
# noisy_img=np.zeros(img.shape,dtype='uint8')

# speckle_noise=np.random.normal(0,1,img.shape)


# # noisy_img=img+img*speckle_noise
# # To reduce noise effect we multiply fraction of speckle noise

# noisy_img=img+img*(0.09*speckle_noise)
# noisy_img=noisy_img.astype('uint8') #it is in float so convert it in uint8 otherwise displayed a white screen

# cv.imshow('Original Image',img)
# cv.waitKey(0)
# cv.destroyAllWindows()

# cv.imshow('Noisy Image',noisy_img)
# cv.waitKey(0)
# cv.destroyAllWindows()

# BUILT-IN FUNCTIONS FOR NOISE
img=cv.imread('original.png',0)
gauss=random_noise(img,mode='gaussian')
salt_pepper=random_noise(img,mode='s&p')
poisson=random_noise(img,mode='poisson')
speckle=random_noise(img,mode='speckle')

noise=np.random.normal(0,3,img.shape)
noise=noise.astype('uint8')
new_noise=img*(0.01*img*noise)

plt.subplot(231), plt.axis('off'), plt.imshow(img,cmap='gray'), plt.title('Original')
plt.subplot(232), plt.axis('off'), plt.imshow(gauss,cmap='gray'), plt.title('Gaussian')
plt.subplot(233), plt.axis('off'), plt.imshow(salt_pepper,cmap='gray'), plt.title('Salt & Pepper')
plt.subplot(234), plt.axis('off'), plt.imshow(poisson,cmap='gray'), plt.title('Poisson')
plt.subplot(235), plt.axis('off'), plt.imshow(speckle,cmap='gray'), plt.title('Speckle')
plt.subplot(236), plt.axis('off'), plt.imshow(new_noise,cmap='gray'), plt.title('New Noise')

plt.show()
plt.close()