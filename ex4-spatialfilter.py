# Low Pass SPatial Domain Filtering 
# to observe the blurring effect 


import cv2 
import numpy as np 

# low average filter	
# Read the image 
img = cv2.imread('ex2-input.png', 0) 

# Obtain number of rows and columns 
# of the image 
m, n = img.shape 

# Develop Averaging filter(3, 3) mask 
mask = np.ones([3, 3], dtype = int) 
mask = mask / 9

# Convolve the 3X3 mask over the image 
img_new = np.zeros([m, n]) 

for i in range(1, m-1): 
	for j in range(1, n-1): 
		temp = img[i-1, j-1]*mask[0, 0]+img[i-1, j]*mask[0, 1]+img[i-1, j + 1]*mask[0, 2]+img[i, j-1]*mask[1, 0]+ img[i, j]*mask[1, 1]+img[i, j + 1]*mask[1, 2]+img[i + 1, j-1]*mask[2, 0]+img[i + 1, j]*mask[2, 1]+img[i + 1, j + 1]*mask[2, 2] 
		
		img_new[i, j]= temp 
		
img_new = img_new.astype(np.uint8) 
cv2.imwrite('exp4-lowpass.tif', img_new) 

# median filter
# Read the image 
img_noisy1 = cv2.imread('ex2-input.png', 0) 
  
# Obtain the number of rows and columns  
# of the image 
m, n = img_noisy1.shape 

img_new1 = np.zeros([m, n]) 
  
for i in range(1, m-1): 
    for j in range(1, n-1): 
        temp = [img_noisy1[i-1, j-1], 
               img_noisy1[i-1, j], 
               img_noisy1[i-1, j + 1], 
               img_noisy1[i, j-1], 
               img_noisy1[i, j], 
               img_noisy1[i, j + 1], 
               img_noisy1[i + 1, j-1], 
               img_noisy1[i + 1, j], 
               img_noisy1[i + 1, j + 1]] 
          
        temp = sorted(temp) 
        img_new1[i, j]= temp[4] 
  
img_new1 = img_new1.astype(np.uint8) 
cv2.imwrite('exp4-median.png', img_new1) 