################################## Skin Detection Algo 3 ###################################

# resources - https://www.codespeedy.com/skin-detection-using-opencv-in-python/

# import all essential libraries
import cv2
import numpy as np
import sys

imageName = sys.argv[1]

# minRange for min skin color Rnage
minRange = np.array([0,133,77],np.uint8)

# maxRange for maximum skin color Range
maxRange = np.array([235,173,127],np.uint8)

image = cv2.imread(imageName)

# change image bgr to ycr using cvtcolor() method 
YCRimage = cv2.cvtColor(image,cv2.COLOR_BGR2YCR_CB)

# apply min or max range on skin area in  image
skinArea = cv2.inRange(YCRimage,minRange,maxRange)
detectedSkin = cv2.bitwise_and(image, image, mask = skinArea)

cv2.imwrite("skinDetection.jpg", detectedSkin)
