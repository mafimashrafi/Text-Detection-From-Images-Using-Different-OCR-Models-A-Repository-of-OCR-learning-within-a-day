import cv2
import numpy as np 

cap = cv2.VideoCapture('sample_video.mp4')
while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    #thus we can select which color to show and which is not by using mask
    lower_color = np.array([160,100,100]) #the cordinate below will only show red
    upper_color = np.array([179,255,255])
    mask = cv2.inRange(hsv, lower_color, upper_color)
    res = cv2.bitwise_and(frame, frame, mask=mask)
    
    #Smmothing.   cordinate of Dynamic range
    kernel = np.ones((15, 15), np.float32)/255
    smoothed = cv2.filter2D(frame, -1, kernel)
    
    #gaussian blurr
    blur = cv2.GaussianBlur(frame, (15, 15), 0)
    
    #there is also median blur
    median = cv2.medianBlur(frame, 15)
    
    cv2.imshow('video', frame)
    cv2.imshow('hsv', hsv)
    cv2.imshow('video', res)
    cv2.imshow('Smooth', smoothed)
    cv2.imshow('blur', blur)
    cv2.imshow('Median Blur', median)
    
    k = cv2.waitKey(5) & 0xFF 
    if k == 27:
        break
    
cv2.release()
cv2.destroyAllWindows()