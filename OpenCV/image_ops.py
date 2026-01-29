import cv2
import numpy as np 
import matplotlib as plt 
import os 

script_dir = os.path.dirname(os.path.abspath(__file__))
img_path = os.path.join(script_dir, 'sample.jpg')

img = cv2.imread(img_path, cv2.IMREAD_COLOR)

img[100:250, 100:350] = [255, 255, 255]

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()