import cv2
import numpy as np 
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
video_path = os.path.join(script_dir, 'sample_video.mp4')

cap = cv2.VideoCapture(0) #to read webcame
cap_1 = cv2.VideoCapture(video_path) #to read saved videos not webcame
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('Webcam.avi', fourcc, 20.0, (640, 480))

while True: 
    ret, frame = cap_1.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # out.write(gray)
    cv2.imshow('frame', frame)
    cv2.imshow('gray', gray)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cv2.release()
# out.release()
cv2.destroyAllWindows()