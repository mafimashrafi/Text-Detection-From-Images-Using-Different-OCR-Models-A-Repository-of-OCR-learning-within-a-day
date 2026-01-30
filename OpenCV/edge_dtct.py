import cv2
import numpy as np 

cap = cv2.VideoCapture('sample_video.mp4')
while True:
    _, frame = cap.read()
    
    laplacian = cv2.Laplacian(frame, cv2.CV_64F)
    sobelx = cv2.Sobel(frame, cv2.CV_64F, 1, 0, ksize=5)
    edges = cv2.Canny(frame, 100, 100)
    
    # cv2.imshow('video', frame)
    # cv2.imshow('Laplacian', laplacian)
    # cv2.imshow('Sobel X', sobelx)
    cv2.imshow("Edges", edges)
    
    k = cv2.waitKey(5) & 0xFF 
    if k == 27:
        break
    
cv2.release()
cv2.destroyAllWindows()