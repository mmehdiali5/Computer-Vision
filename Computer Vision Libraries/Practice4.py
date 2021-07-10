import numpy as np
import imageio as io
import matplotlib.pyplot as plt
import cv2 as cv

img=cv.imread('original.png',0)


plt.imshow(img,cmap="gray")
plt.show()
plt.close()

plt.hist(img.ravel(),bins=100)
plt.ylabel("Frequency")
plt.xlabel("Intesity")
plt.show()
plt.close()

# r,c=img.shape
# for i in range(r):
#     for j in range(c):
#         img[i,j]=255-img[i,j]


MP=255
a=157
b=215
R=b-a
r,c=img.shape
for i in range(r):
    for j in range(c):
        img[i,j]=round(((img[i,j]-a)/R)*MP)

plt.hist(img.ravel(),bins=100)
plt.ylabel("Frequency")
plt.xlabel("Intesity")
plt.show()
plt.close()


plt.imshow(img,cmap="gray")
plt.show()
plt.close()

