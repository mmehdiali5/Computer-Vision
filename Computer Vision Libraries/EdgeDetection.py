import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv

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

img=cv.imread('moon.png',0)
img = np.pad(img, 1, mode='constant', constant_values=0)

r,c=img.shape

My=np.array([[ 1, 2, 1],
             [ 0, 0, 0],
             [-1,-2,-1]])

# My=np.array([[ 1, 1, 1, 1, 1],
#              [ 1, 1, 2, 1, 1],
#              [ 0, 0, 0, 0, 0],
#              [-1,-1,-2,-1,-1],
#              [-1,-1,-1,-1,-1]])

r2,c2=My.shape

img_copy2=np.zeros(img.shape,dtype='float64')
img_copy2=convolve(r,c,r2,c2,My,img,img_copy2)

Mx=np.array([[1,0,-1],
             [2,0,-2],
             [1,0,-1]])

# Mx=np.array([[ 1, 1, 0,-1,-1],
#              [ 1, 1, 0,-1,-1],
#              [ 1, 2, 0,-2,-1],
#              [ 1, 1, 0,-1,-1],
#              [ 1, 1, 0,-1,-1]])
 

img_copy1=np.zeros(img.shape,dtype='float64')

img_copy1=convolve(r,c,r2,c2,Mx,img,img_copy1)


sobel=np.zeros(img.shape,dtype='uint8')
sobelx=normalize(img_copy1)
sobely=normalize(img_copy2)               
               
tempArray=np.zeros(img_copy1.shape,dtype='float64')

for i in range (r):
    for j in range (c):
        tempArray[i,j]=((img_copy1[i,j]**2)+(img_copy2[i,j]**2))**(1/2.0)
       
sobel=normalize(tempArray)
        
# plt.subplot(221), plt.axis('off'), plt.imshow(img,cmap='gray'), plt.title('Original')
# plt.subplot(222), plt.axis('off'), plt.imshow(sobelx,cmap='gray'), plt.title('SobelX')
# plt.subplot(223), plt.axis('off'), plt.imshow(sobely,cmap='gray'), plt.title('SobelY')
# plt.subplot(224), plt.axis('off'), plt.imshow(sobel,cmap='gray'), plt.title('Sobel')


My=np.array([[1,1,1],
              [0,0,0],
              [-1,-1,-1]])

# My=np.array([[ 1, 1, 1, 1, 1],
#              [ 1, 1, 2, 1, 1],
#              [ 0, 0, 0, 0, 0],
#              [-1,-1,-2,-1,-1],
#              [-1,-1,-1,-1,-1]])

r2,c2=My.shape

img_copy2=np.zeros(img.shape,dtype='float64')
img_copy2=convolve(r,c,r2,c2,My,img,img_copy2)

Mx=np.array([[1,0,-1],
             [2,0,-2],
             [1,0,-1]])

# Mx=np.array([[ 1, 1, 0,-1,-1],
#              [ 1, 1, 0,-1,-1],
#              [ 1, 2, 0,-2,-1],
#              [ 1, 1, 0,-1,-1],
#              [ 1, 1, 0,-1,-1]])
 

img_copy1=np.zeros(img.shape,dtype='float64')

img_copy1=convolve(r,c,r2,c2,Mx,img,img_copy1)


prewitt=np.zeros(img.shape,dtype='uint8')
prewittx=normalize(img_copy1)
prewitty=normalize(img_copy2)               
               
tempArray=np.zeros(img_copy1.shape,dtype='float64')

for i in range (r):
    for j in range (c):
        tempArray[i,j]=((img_copy1[i,j]**2)+(img_copy2[i,j]**2))**(1/2.0)
       
prewitt=normalize(tempArray)
        
# plt.subplot(221), plt.axis('off'), plt.imshow(img,cmap='gray'), plt.title('Original')
# plt.subplot(222), plt.axis('off'), plt.imshow(prewittx,cmap='gray'), plt.title('PrewittX')
# plt.subplot(223), plt.axis('off'), plt.imshow(prewitty,cmap='gray'), plt.title('PrewitY')
# plt.subplot(224), plt.axis('off'), plt.imshow(prewitt,cmap='gray'), plt.title('Prewitt')

laplacian=np.zeros(img.shape,dtype='uint8')

laplaceMask =np.array([[1, 1, 1],
                       [1,-8, 1],
                       [1, 1, 1]])


 
img_copy4=np.zeros(img.shape,dtype='float64')

laplaceImg=convolve(r,c,3,3,laplaceMask,img,img_copy4)

plt.imshow(laplaceImg,cmap="gray")
plt.title("LAPLACIAN")
plt.show()
plt.close()

laplaceImg=normalize(laplaceImg)

plt.imshow(laplaceImg,cmap="gray")
plt.title("LAPLACIAN")
plt.show()
plt.close()

copyImg=np.zeros(img.shape,dtype='float64')
copyImg[:][:]=img[:][:]





laplaceImg=copyImg-laplaceImg

plt.imshow(img,cmap="gray")
plt.title("Original")
plt.show()
plt.close()

plt.imshow(laplaceImg,cmap="gray")
plt.title("LAPLACIAN")
plt.show()
plt.close()