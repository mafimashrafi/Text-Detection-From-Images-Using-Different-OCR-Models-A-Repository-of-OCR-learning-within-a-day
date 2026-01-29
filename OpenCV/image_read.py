import cv2
import numpy as np 
import matplotlib.pyplot as plt 
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
img_path = os.path.join(script_dir, 'sample.jpg')

img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

# cv2.imshow('sample image', img)
# cv2.waitKey(0)
# cv2.destroyALLWindows()

## to save
#cv2.imwrite('samplegray.jpg', img)

#visualising using matplotlib
plt.imshow(img, cmap='gray', interpolation='bicubic')
plt.plot([50, 100], [80, 100], 'c', linewidth = 5)
plt.show()