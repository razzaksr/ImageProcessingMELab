# Python program to illustrate 
# arithmetic operation of 
# addition of two images 
	
# organizing imports 
import cv2 
import numpy as np 
	
# path to input images are specified and 
# images are loaded with imread command 
image1 = cv2.imread('ex1-input1.jpg') 
image2 = cv2.imread('ex1-input2.jpg') 

# cv2.addWeighted is applied over the 
# image inputs with applied parameters of addition
weightedSum = cv2.addWeighted(image1, 0.5, image2, 0.4, 0) 

# image inputs with applied parameters of subtraction
#weightedSum = cv2.subtract(image1, image2)

# the window showing output image 
# with the weighted sum 
cv2.imshow('Weighted Image', weightedSum) 

# De-allocate any associated memory usage 
if cv2.waitKey(0) & 0xff == 27: 
	cv2.destroyAllWindows() 
