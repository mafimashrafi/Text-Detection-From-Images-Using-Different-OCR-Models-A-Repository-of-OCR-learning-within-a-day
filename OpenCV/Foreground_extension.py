import numpy as np 
import cv2 
import matplotlib.pyplot as plt 
import os

# Get the absolute path to the OpenCV directory
script_dir = os.path.dirname(os.path.abspath(__file__))
opencv_dir = os.path.join(script_dir, 'OpenCV')
images_dir = os.path.join(opencv_dir, 'images')

img_path = os.path.join(images_dir, 'sample.jpg')

img = cv2.imread(img_path)
mask = np.zeros(img.shape[:2], np.uint8)

bgdModel = np.zeros((1, 65), np.float64)
fgdModel = np.zeros((1, 65), np.float64)

rect = (161, 79, 150, 150)

cv2.grabCut(img, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)
mask2 = np.where((mask==2) | (mask==0), 0, 1) .astype('uint8')
img = img*mask2[:,:,np.newaxis]

plt.imshow(img)
plt.colorbar()
plt.show()

#wroks like messengers stiker cut