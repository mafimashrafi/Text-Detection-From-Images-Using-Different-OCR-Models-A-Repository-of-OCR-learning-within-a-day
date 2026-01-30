import cv2
import numpy as np 

cap = cv2.VideoCapture(0)
while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    #thus we can select which color to show and which is not by using mask
    lower_color = np.array([160,100,100]) #the cordinate below will only show red
    upper_color = np.array([179,255,255])
    mask = cv2.inRange(hsv, lower_color, upper_color)
    res = cv2.bitwise_and(frame, frame, mask=mask)
    
    kernel = np.ones((15, 15), np.uint8)
    erosion = cv2.erode(mask, kernel, iterations = 1)
    dialation = cv2.dilate(mask, kernel, iterations = 1)
    
    
    cv2.imshow('video', frame)
    cv2.imshow('res', res)
    cv2.imshow('erosion', erosion)
    cv2.imshow('dialation', dialation)
    
    k = cv2.waitKey(5) & 0xFF 
    if k == 27:
        break
    
cv2.release()
cv2.destroyAllWindows()