# ################################ Skin Pixel Counter Program  ################################
# 
# Habiba Mostafa, 1070307
# Daniela Aldave-Garza, 1069571
# 
###############################################################################################

from PIL import Image
import sys

#read in image from command line
imageName = sys.argv[1]
  
# reading the image data from desired directory 
img = Image.open(sys.argv[1]).convert('RGB')
pixelMap = img.load()

counter = 0

#loop through all pixels
for i in range(0, img.size[0]):
    for j in range(0, img.size[1]):
        #check if pixel is skin
        if not pixelMap[i,j] == (0,0,0):
           counter = counter + 1
  
# print number of skin pixels 
print(counter)
