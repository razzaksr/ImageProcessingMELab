# import the necessary packages 
import cv2 
import numpy as np 
import matplotlib.pyplot as plt 

# erosion
# read the image 
img = cv2.imread(r"input7-1.jpg", 0) 
# binarize the image 
binr = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)[1] 
# define the kernel 
kernel = np.ones((5, 5), np.uint8) 
# invert the image 
invert = cv2.bitwise_not(binr) 
# erode the image 
erosion = cv2.erode(invert, kernel,iterations=1) 
# print the output 
plt.imshow(erosion, cmap='gray') 


# dilation
img = cv2.imread("input7-1.jpg", 0) 
# binarize the image 
binr = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)[1] 
# define the kernel 
kernel = np.ones((3, 3), np.uint8) 
# invert the image 
invert = cv2.bitwise_not(binr) 
# dilate the image 
dilation = cv2.dilate(invert, kernel, iterations=1)   
# print the output 
plt.imshow(dilation, cmap='gray') 


# opening
img = cv2.imread("input7-2.png", 0) 
# binarize the image 
binr = cv2.threshold(img, 0, 255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)[1] 
# define the kernel 
kernel = np.ones((3, 3), np.uint8) 
# opening the image 
opening = cv2.morphologyEx(binr, cv2.MORPH_OPEN, kernel, iterations=1) 
# print the output 
plt.imshow(opening, cmap='gray') 


# closing
img = cv2.imread("input7-2.png", 0) 
# binarize the image 
binr = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)[1] 
# define the kernel 
kernel = np.ones((3, 3), np.uint8) 
# opening the image 
closing = cv2.morphologyEx(binr, cv2.MORPH_CLOSE, kernel, iterations=1) 
# print the output 
plt.imshow(closing, cmap='gray') 