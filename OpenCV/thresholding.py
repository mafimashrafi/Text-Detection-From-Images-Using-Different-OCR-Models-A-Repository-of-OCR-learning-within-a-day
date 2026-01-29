import cv2
import numpy as np 

img = cv2.imread('images/bookpage.jpg')
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
retval, threshold = cv2.threshold(img, 12, 255, cv2.THRESH_BINARY_INV)
retval, threshold_bw = cv2.threshold(gray_img, 12, 255, cv2.THRESH_BINARY_INV)

gaus = cv2.adaptiveThreshold(gray_img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)

cv2.imshow('Original', img)
cv2.imshow('Black & White', gray_img)
cv2.imshow('Threshold', threshold)
cv2.imshow('B&W Threshold', threshold_bw)
cv2.imshow('Gausian Threshold', gaus) 
cv2.waitKey(0)
cv2.destroyAllWindows()