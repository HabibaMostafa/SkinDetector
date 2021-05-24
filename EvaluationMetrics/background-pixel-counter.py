# ############################  Background Pixel Counter Program  #############################
# 
# Habiba Mostafa, 1070307
# Daniela Aldave-Garza, 1069571
# 
###############################################################################################

import cv2
import numpy as np
import sys

imageName = sys.argv[1]
  
# reading the image data from desired directory 
img = cv2.imread(imageName) 

cv2.imshow('Image',img) 
  
# counting the number of pixels 
number_of_white_pix = np.sum(img == 255) 
number_of_black_pix = np.sum(img == 0) 
  
print('Number of white pixels:', number_of_white_pix) 
print('Number of black pixels:', number_of_black_pix)
