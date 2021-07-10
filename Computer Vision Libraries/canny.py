import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
import math


def convolve(r,c,r2,c2,kernal,img,result):
    for i in range (round(r2/2),r-round(r2/2)):
        for j in range (round(r2/2),c-round(r2/2)):
            i1=round(i-(r2/2))            
            for k in range (r2):
                j1=round(j-(r2/2))
                for l in range (c2):
                    result[i,j]+=kernal[k,l]*img[i1,j1]
                    j1=j1+1
                i1=i1+1
    return result

def normalize(tempArray):
    result=np.zeros(tempArray.shape,dtype='uint8')
    minimum=tempArray.min()
    maximum=tempArray.max()
    r,c=tempArray.shape
    for i in range (1,r-1):
        for j in range(1,c-1):
            result[i,j]=((tempArray[i,j]-minimum)*255)/(maximum-minimum)  
    return result   

def normalizeDirection(directionMatrix):
    r,c=directionMatrix.shape
    for i in range (r):
        for j in range (c):
            if(directionMatrix[i,j]>=-22.5 and directionMatrix[i,j]<22.5):
                directionMatrix[i,j]=0
            elif(directionMatrix[i,j]>=22.5 and directionMatrix[i,j]<67.5):
                directionMatrix[i,j]=45
            elif(directionMatrix[i,j]>=-67.5 and directionMatrix[i,j]<-22.5):
                directionMatrix[i,j]=135
            else: 
                # i.e directionMatrix[i,j]>=-90 and directionMatrix[i,j]<-67.5
                # or directionMatrix[i,j]>=67.5 and directionMatrix[i,j]<=90
                directionMatrix[i,j]=90
    return directionMatrix            
       
    
def hysterisis(r,c,img,copy,highThreshold,lowThreshold): 
    for i in range(1,r-1):
        for j in range(1,c-1):
            
            if(copy[i,j]<=lowThreshold):
                img[i,j]=0
            
            elif(copy[i,j]>=highThreshold):
                img[i,j]=255
            
            elif(copy[i,j]>lowThreshold and copy[i,j]<highThreshold):
                
                if(   copy[i-1,j]>highThreshold 
                   or copy[i+1,j]>highThreshold
                   or copy[i,j+1]>highThreshold
                   or copy[i,j-1]>highThreshold
                   or copy[i-1,j-1]>highThreshold
                   or copy[i+1,j+1]>highThreshold
                   or copy[i-1,j+1]>highThreshold
                   or copy[i+1,j-1]>highThreshold):
                    
                    img[i,j]=255
                
                else:
                    img[i,j]=0
                    
    return img           

img=cv.imread('building.jpeg',0)
img = np.pad(img, 1, mode='constant', constant_values=0)
r,c=img.shape

plt.imshow(img,cmap="gray")
plt.title("Original")
plt.show()
plt.close()

gaussImg=cv.GaussianBlur(img,(5,5),0,1)


plt.imshow(gaussImg,cmap="gray")
plt.title("BLUR")
plt.show()
plt.close()

Mx=np.array([[1,0,-1],
             [2,0,-2],
             [1,0,-1]])


My=np.array([[ 1, 2, 1],
             [ 0, 0, 0],
             [-1,-2,-1]])

img_copy2=np.zeros(img.shape,dtype='float64')
sobelX=convolve(r,c,3,3,Mx,gaussImg,img_copy2)

img_copy3=np.zeros(img.shape,dtype='float64')
sobelY=convolve(r,c,3,3,My,gaussImg,img_copy3)

sobel=np.zeros(img.shape,dtype='uint8')
  

tempArray=np.zeros(img.shape,dtype='float64')

for i in range (r):
    for j in range (c):
        tempArray[i,j]=((sobelX[i,j]**2)+(sobelY[i,j]**2))**(1/2.0)
        
sobel=normalize(tempArray)  

plt.imshow(sobel,cmap="gray")
plt.title("SOBEL")
plt.show()
plt.close()

directionMatrix=np.zeros(img.shape,dtype='float64')

for i in range (r):
    for j in range (c):
        if(sobelX[i,j]!=0):
            directionMatrix[i,j]=math.degrees(math.atan(sobelY[i,j]/sobelX[i,j]))
        else:
            directionMatrix[i,j]=90

directionMatrix=normalizeDirection(directionMatrix)

# NON MAXIMA SUPPREWSSION
canny=np.zeros(img.shape,dtype='float64')
canny[:][:]=sobel[:][:]

for i in range (1,r-1):
    for j in range (1,c-1):
        if(directionMatrix[i,j]==0):
            if(not(canny[i,j]>canny[i,j-1] and canny[i,j]>canny[i,j+1])):
                canny[i,j]=0
        elif(directionMatrix[i,j]==90):
            if(not(canny[i,j]>canny[i-1,j] and canny[i,j]>canny[i+1,j])):
                canny[i,j]=0
        elif(directionMatrix[i,j]==45):
            if(not(canny[i,j]>canny[i-1,j+1] and canny[i,j]>canny[i+1,j-1])):
                canny[i,j]=0
        elif(directionMatrix[i,j]==135):
            if(not(canny[i,j]>canny[i-1,j-1] and canny[i,j]>canny[i+1,j+1])):
                canny[i,j]=0
                
plt.imshow(canny,cmap="gray")
plt.title("NON MAXIMA SUPPRESSION")
plt.show()
plt.close()

# Double Thresholding

highThresholdRatio=0.2
highThreshold=canny.max()*highThresholdRatio

lowThresholdRatio=0.12
lowThreshold=highThreshold*lowThresholdRatio

# Edge detection using hysteris


copy=np.zeros(img.shape,dtype='float64')
copy[:][:]=canny[:][:]

canny2=np.zeros(img.shape,dtype='float64')
canny2[:][:]=canny[:][:]


canny2=hysterisis(r,c,canny2,copy,highThreshold,lowThreshold)

plt.imshow(canny2,cmap="gray")
plt.title("CANNY EDGE DETECTION")
plt.show()
plt.close()


cv.imwrite("cannypic.jpeg",canny2)
