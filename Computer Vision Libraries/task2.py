import numpy as np
import imageio as io
import matplotlib.pyplot as plt

img = io.imread('g1.png')
img2=io.imread('g2.png')

print(img[1,100])

r1,c1=img.shape
r2,c2=img2.shape
rows=min(r1,r2)

mergeImage=np.zeros((rows,c1+c2+20),dtype=np.uint8)

for i in range(rows):
    for j in range(c1):
        print(i,j);
        mergeImage[i,j]=img[i,j]
        
      
for i in range(rows):
    for j in range(c1+1,c1+20):
        print(i,j)
        mergeImage[i,j]=255
             
for i in range(rows):
    m=0
    for j in range(c1+21,c1+c2+20):
        print(i,j)
        mergeImage[i,j]=img2[i,m]
        m=m+1
        

plt.imshow(img,cmap="gray")
plt.show()
plt.close()

plt.imshow(img2,cmap="gray")
plt.show()
plt.close()

plt.imshow(mergeImage,cmap="gray")
plt.show()
plt.close()
