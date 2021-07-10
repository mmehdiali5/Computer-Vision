import numpy as np
import random
import matplotlib.pyplot as plt
import cv2 as cv

conservativeKernal=np.arange(9).reshape(3,3).astype('float64')

img=cv.imread('original.png',0)

plt.imshow(img,cmap="gray")
plt.title("Original")
plt.show()
plt.close()


# APPLYING GAUSSIAN NOISE
noisy_img=np.random.normal(0,3,img.shape)
plt.hist(noisy_img.ravel(),bins=100)
plt.show()
plt.close()

noisy_img=noisy_img.astype('uint8')

img_gauss=cv.add(img,noisy_img)

plt.imshow(img_gauss,cmap="gray")
plt.show()
plt.close()
 
    
r,c=img.shape
r2,c2=conservativeKernal.shape

blur_img=np.zeros(img.shape,dtype='uint8')
tempArr=np.arange(8)
count=0

# APPLYING CONSERVATIVE FILTER ON GAUSS NOISE
for i in range (1,r-1):
    for j in range (1,c-1):
        i1=i-1
        for k in range (r2):
            j1=j-1
            for l in range (c2):
                if not(k==1 and l==1):
                    tempArr[count]=img_gauss[i1,j1]
                    count=count+1
                j1=j1+1
            i1=i1+1     
        count=0    
        minimum=tempArr[0]
        maximum=tempArr[0]
        for m in range (8):
            if(tempArr[m]<=minimum):
                minimum=tempArr[m]
            if(tempArr[m]>=maximum):
                maximum=tempArr[m]
        if(img_gauss[i,j]<minimum):
            blur_img[i,j]=minimum
        elif(img_gauss[i,j]>maximum):
            blur_img[i,j]=maximum
        elif(img_gauss[i,j]>=minimum and img[i,j]<=maximum):
            blur_img[i,j]=img_gauss[i,j]    
        

plt.imshow(blur_img,cmap="gray")
plt.title("BLUR")
plt.show()
plt.close()  



plt.imshow(img,cmap="gray")
plt.show()
plt.close()

# APPLYING SALT AND PEPPER
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

count=0
blur_img2=np.zeros(img.shape,dtype='uint8')
# APPLYING CONSERVATIVE FILTER ON SALT AND PEPPER NOISE
for i in range (1,r-1):
    for j in range (1,c-1):
        i1=i-1
        for k in range (r2):
            j1=j-1
            for l in range (c2):
                if not(k==1 and l==1):
                    tempArr[count]=impulse_noise[i1,j1]
                    count=count+1
                j1=j1+1
            i1=i1+1     
        count=0    
        minimum=tempArr[0]
        maximum=tempArr[0]
        for m in range (8):
            if(tempArr[m]<=minimum):
                minimum=tempArr[m]
            if(tempArr[m]>=maximum):
                maximum=tempArr[m]
        if(impulse_noise[i,j]<minimum):
            blur_img2[i,j]=minimum
        elif(impulse_noise[i,j]>maximum):
            blur_img2[i,j]=maximum
        else:
            blur_img2[i,j]=impulse_noise[i,j]    
        

plt.imshow(blur_img2,cmap="gray")
plt.title("BLUR2")
plt.show()
plt.close()  