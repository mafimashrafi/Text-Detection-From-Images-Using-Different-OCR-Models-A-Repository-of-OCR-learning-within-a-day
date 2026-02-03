import numpy as np 
import cv2 
import os 
import matplotlib.pyplot as plt 

script_dir = os.path.dirname(os.path.abspath(__file__))
opencv_dir = os.path.join(script_dir, 'OpenCV')
images_dir = os.path.join(opencv_dir, 'images')

img_path = os.path.join(images_dir, 'sample.jpg')