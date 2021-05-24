# ################################## Median Filtering Algorithm ##############################
# 
# Habiba Mostafa, 1070307
# Daniela Aldave-Garza, 1069571
# 
##############################################################################################

from PIL import Image
import statistics
import sys

# open image and load it as a pixel map
img = Image.open(sys.argv[1]).convert('YCbCr')
pixelMap = img.load()

# convert image to RGB
segmentedImg = Image.open(sys.argv[1]).convert('RGB')
newPixelMap = segmentedImg.load()

# iterate through all pixels in image
for i in range(0, img.size[0]):
    for j in range(0, img.size[1]):
        cb = pixelMap[i,j][1]
        cr = pixelMap[i,j][2]
        if not ((77 < cb and cb < 127) and (133 < cr and cr < 173)):
            newPixelMap[i,j] = (0,0,0)

# show processed image 
segmentedImg.show()

# close image view 
img.close()
segmentedImg.close()
