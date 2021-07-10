import numpy as np
import imageio as io
import matplotlib.pyplot as plt
import cv2 as cv

img=cv.imread('original.png',0)

img_b=np.zeros(img.shape,dtype=np.uint8)
img_b1=np.zeros(img.shape,dtype=np.uint8)
img_b2=np.zeros(img.shape,dtype=np.uint8)
img_b3=np.zeros(img.shape,dtype=np.uint8)
img_b4=np.zeros(img.shape,dtype=np.uint8)



plt.imshow(img,cmap="gray")
plt.show()
plt.close()

# plt.hist(img.ravel(),bins=100)
# plt.show()
# plt.close()

hist,bins=np.histogram(img,bins=100)
print(hist)
print(bins)

thresh=187

Ret,img_b=cv.threshold(img,thresh,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
Ret,img_b1=cv.threshold(img,thresh,255,cv.THRESH_BINARY)

Thresh_img= cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 189, 2)
img_eq=cv.equalizeHist(img)

# Ret,img_b1=cv.threshold(img,thresh,255,cv.THRESH_BINARY_INV)
# Ret,img_b2=cv.threshold(img,thresh,255,cv.THRESH_TRUNC)
# Ret,img_b3=cv.threshold(img,thresh,255,cv.THRESH_TOZERO)
# Ret,img_b4=cv.threshold(img,thresh,255,cv.THRESH_TOZERO_INV)


# r,c=img.shape
# for i in range(r):
#     for j in range(c):
#         if(img[i,j]<=thresh):
#             img_b[i,j]=0
#         else:
#              img_b[i,j]=255   

plt.imshow(img_b,cmap="gray")
plt.show()
plt.close()

# plt.imshow(img_b1,cmap="gray")
# plt.show()
# plt.close()

plt.imshow(Thresh_img,cmap="gray")
plt.show()
plt.close()

# plt.imshow(img_b2,cmap="gray")
# plt.show()
# plt.close()

# plt.imshow(img_b3,cmap="gray")
# plt.show()
# plt.close()

# plt.imshow(img_b4,cmap="gray")
# plt.show()
# plt.close()

plt.imshow(img_eq,cmap="gray")
plt.show()
plt.close()


