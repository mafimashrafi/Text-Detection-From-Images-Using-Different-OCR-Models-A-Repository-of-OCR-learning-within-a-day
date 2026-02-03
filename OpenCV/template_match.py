import numpy as np 
import cv2
import os

# Get the absolute path to the script directory
script_dir = os.path.dirname(os.path.abspath(__file__))
images_dir = os.path.join(script_dir, 'images')

# Read images with absolute paths
img1_path = os.path.join(images_dir, 'opencv-template-matching-python-tutorial.jpg')
template_path = os.path.join(images_dir, 'opencv-template-for-matching.jpg')

img1 = cv2.imread(img1_path)
template = cv2.imread(template_path, 0)

img1_gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

w, h = template.shape[::-1]

res = cv2.matchTemplate(img1_gray, template, cv2.TM_CCOEFF_NORMED)
threshol = 0.8
loc = np.where(res>=threshol)

for pt in zip(*loc[::-1]):
    cv2.rectangle(img1, pt, (pt[0]+w, pt[1]+h), (0, 255, 255), 2)
    
cv2.imshow('detected', img1)

cv2.waitKey(0)
cv2.destroyAllWindows()