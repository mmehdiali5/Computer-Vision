import numpy as np
import imageio as io
import matplotlib.pyplot as plt
import cv2 as cv

img_c=cv.imread("g1.png",0)
img_c_r=cv.resize(img_c,(64,64))

cv.imshow("Display Window Name",img_c_r)
cv.waitKey(0)
cv.destroyAllWindows()

img = io.imread('g1.png')

plt.hist(img.ravel(),bins=100)
plt.ylabel("Frequency")
plt.xlabel("Intesity")
plt.show()
plt.close()


plt.imshow(img,cmap="gray")
plt.axis("off")
plt.show()
plt.close()

cv.imwrite("resizedg1.bmp",img_c_r)
