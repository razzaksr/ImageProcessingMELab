# We need cv2 module for image 
# reading and matplotlib module 
# for plotting 
import cv2 
import matplotlib.pyplot as plt 

img_bgr = cv2.imread('ex2-input.png', 1) 

color = ('b', 'g', 'r') 

for i, col in enumerate(color): 
	histr = cv2.calcHist([img_bgr], [i], None, [256], [0, 256]) 
	plt.plot(histr, color = col) 
	plt.xlim([0, 256]) 
	
plt.show() 

img_neg = 1 - img_bgr 

plt.imshow(img_neg) 
plt.show() 