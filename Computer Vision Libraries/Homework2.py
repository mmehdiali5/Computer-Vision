import numpy as np
import imageio as io
import matplotlib.pyplot as plt
import cv2 as cv
import random
from skimage.util import random_noise


img=cv.imread('original.png',0)

img_b=np.zeros(img.shape,dtype=np.uint8)
thresh=150
Ret,img_b=cv.threshold(img,thresh,255,cv.THRESH_BINARY+cv.THRESH_OTSU)

# MY NOISE
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

#IMAGE ENHANCEMENT AND BINARIZING

#CONTRAST ENHANCEMENT

img2=cv.imread('original.png',0)
r,c=img2.shape
for i in range(r):
    for j in range(c):
        img2[i,j]=255-img2[i,j]

img_b2=np.zeros(img2.shape,dtype=np.uint8)
thresh=150
Ret,img_b2=cv.threshold(img2,thresh,255,cv.THRESH_BINARY+cv.THRESH_OTSU)        


#CONTRAST STRETCHING
img3=cv.imread('original.png',0)
MP=255
a=157
b=215
R=b-a
r,c=img3.shape
for i in range(r):
    for j in range(c):
        img3[i,j]=round(((img3[i,j]-a)/R)*MP)
        
img_b3=np.zeros(img3.shape,dtype=np.uint8)
thresh=150
Ret,img_b3=cv.threshold(img3,thresh,255,cv.THRESH_BINARY+cv.THRESH_OTSU) 
    
#EQUALIZE HISTOGRAM 
img4=cv.imread('original.png',0)
cv.equalizeHist(img4)
img_b4=np.zeros(img4.shape,dtype=np.uint8)
thresh=150
Ret,img_b4=cv.threshold(img4,thresh,255,cv.THRESH_BINARY+cv.THRESH_OTSU) 



plt.subplot(241), plt.axis('off'), plt.imshow(img,cmap='gray'), plt.title('Original')
plt.subplot(242), plt.axis('off'), plt.imshow(img2,cmap='gray'), plt.title('ENHANCE')
plt.subplot(243), plt.axis('off'), plt.imshow(img3,cmap='gray'), plt.title('STRETCH')
plt.subplot(244), plt.axis('off'), plt.imshow(img4,cmap='gray'), plt.title('EQ_HIST')
plt.subplot(245), plt.axis('off'), plt.imshow(img_b,cmap='gray'), plt.title('Org_Bin')
plt.subplot(246), plt.axis('off'), plt.imshow(img_b2,cmap='gray'), plt.title('ENHANCE_BIN')
plt.subplot(247), plt.axis('off'), plt.imshow(img_b3,cmap='gray'), plt.title('STRETCH_BIN')
plt.subplot(248), plt.axis('off'), plt.imshow(img_b4,cmap='gray'), plt.title('EQ_BIN')


plt.show()
plt.close()




