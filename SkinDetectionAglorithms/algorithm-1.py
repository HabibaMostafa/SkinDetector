# ################################## Skin Detection Algorithm 1 ##############################
# 
# Habiba Mostafa, 1070307
# Daniela Aldave-Garza, 1069571
# 
##############################################################################################

from PIL import Image
import statistics
import sys

# open image and load it as a pixel map
img = Image.open(sys.argv[1]).convert('RGB')
pixelMap = img.load()

segmentedImg = img.copy()
newPixelMap = segmentedImg.load()

# iterate through all pixels in image
for i in range(0, img.size[0]):
    for j in range(0, img.size[1]):
        r = pixelMap[i,j][0]
        g = pixelMap[i,j][1]
        b = pixelMap[i,j][2]

        # check if current pixel satisfies the the 3 rgb range values and hence is a skin pixel
        if not ((r > 95 and g > 40 and b > 20) 
            and (max(r,g,b) - min(r,g,b) > 15) 
            and (abs(r-g) > 15) 
            and (r > g and r > b)):
                newPixelMap[i,j] = (0,0,0)

# show processed image 
segmentedImg.show()

# close image view 
img.close()
segmentedImg.close()
