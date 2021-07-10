# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import imageio as io
import matplotlib.pyplot as plt

img = io.imread('pic1.png')

r,c,t=img.shape
for i in range(r):
    for j in range(c):
        print(img[i,j])
        
plt.imshow(img,cmap="gray")
plt.show()
plt.close()
        