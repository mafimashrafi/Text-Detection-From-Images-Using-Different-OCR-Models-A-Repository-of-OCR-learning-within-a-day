import cv2
import numpy as np 

img1 = cv2.imread('images/3D-Matplotlib.png', cv2.IMREAD_COLOR)
img2 = cv2.imread('images/mainsvmimage.png', cv2.IMREAD_COLOR)
img3 = cv2.imread('images/mainlogo.png')

add = img1+img2 #do both the image has to be of same legnth? 
add_cv = cv2.add(img1, img2) #adds each pixel values and created a new image
weighted = cv2.addWeighted(img1, 0.6, img2, 0.4, 0) #0 at the end is gama

#lets the loo at the top right corner
rows, cols, channels = img3.shape
roi = img1[0:rows, 0:cols]
img3gray = cv2.cvtColor(img3, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img3gray, 220, 255, cv2.THRESH_BINARY_INV)

mask_inv = cv2.bitwise_not(mask) #the black area of the mask
img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
img3_fg = cv2.bitwise_and(img3, img3, mask = mask)
dst = cv2.add(img1_bg, img3_fg)
img1[0:rows, 0:cols] = dst

cv2.imshow('image', img1)
cv2.waitKey(0)
cv2.destroyAllWindows()