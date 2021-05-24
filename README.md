The following algorithms have been developed in python3 and should be run in python3 accordingly.

-- In collaboration with Daniela -- 

## Prerequisite package installations 

pillow - pip install Pillow

numpy - pip install numpy

opencv-python - pip install opencv-python

---------------------------------------------------------------------------------------------------------------------------

## Skin Detection Algorithms

### Algorithm 1 - Proposed by Peter Peer 

This skin detection algorithm operates in the RGB color space.
A pixel in the image is classified as skin if it passes the following three conditions:

R1: R > 95 and G > 40 and B > 20
R2: max(R,G,B) - min(R,G,B) > 15
R3: |R-G| > 15 and R > G and R > B

where R,G,B are the red, green and blue values of the pixels respectively.

program: algorithm-1.py

To run:
$ python3 algorithm-2.py pathToImage

### Algorithm 2 - Proposed by Douglas Chai 

This skin detection algorithm operates in the YCbCr color space. 
A pixel in the image is classified as skin if it passes the following conditions:

R1: 77 ≤ Cb ≤ 127
R2: 133 ≤ Cr ≤ 173

where Cb and Cr are the Cb and Cr values of the pixel.

program: algorithm-2.py

To run:
$ python3 algorithm-2.py pathToImage

### Algorithm 3 - Skin Colour Thresholding 

This skin detection algorithm references OpenCV’s cv2 library to identify skin pixels within a provided image. 
It defines maximum and minimum boundaries for pixel intensities to be classified as skin pixels upon image processing.

program: algorithm-3.py

To run:
$ python3 algorithm-3.py pathToImage

### Algorithm 4 - RGB-H-CbCr Skin Colour Segmentation

The RGB-H-CbCr Skin Colour Segmentation skin detection algorithm is based on skin tone thresholds (RGB-YCrCb). 
It converts the BGR image to YCbCr and HSV colour spaces then runs the RGB_H_CbCr bounding rule on all three frames and
outputs the segmented image presenting all identified skin pixels.

program: algorithm-4.py

To run:
$ python3 algorithm-4.py pathToImage

---------------------------------------------------------------------------------------------------------------------------

## Skin Detection Algorithms Evaluation Metric 

An evaluation metric python script that computes the total number of skin pixels found in input image.

program: skin-pixel-counter.py

To run:
$ python3 skin-pixel-counter.py pathToImage

## Skin Detection Algorithms Evaluation Metric 

An evaluation metric python script that computes the total number of black and white pixels found in the background 
of processed images.

program: background-pixel-counter.py

To run:
$ python3 background-pixel-counter.py pathToImage
