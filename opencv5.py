# image transformations

import cv2 as cv
import numpy as np

img = cv.imread('photos/cat1.jpg')
cv.imshow('Cat', img)

# 1. Translation(shifting an image along X and/or Y axis)
def translate(img, x, y):
    transMat = np.float32([[1,0,x], [0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

# -x --> left
# -y --> up
# x --> right
# y --> down

translated = translate(img, -100, 100)
cv.imshow('Cat_Translated', translated)

# 2. Rotation
def rotate(img, angle, rotPoint = None):
    (height, width) = img.shape[:2]
    
    if rotPoint is None:
        rotPoint = (width//2, height//2)
    
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)
    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, 45)
cv.imshow('Cat_rotated', rotated)

# 3. Flipping
flipped = cv.flip(img, -1)
# 0 --> vertically
# 1 --> horizontally
# -1 --> vetically and horizontally both
cv.imshow('Cat_flipped', flipped)

# 4. Resizing
#Discussed in previous file (opencv4.py)

# 5. Cropping
#Discussed in previous file (opencv4.py)

cv.waitKey(2000)