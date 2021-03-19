# Color spaces

# By default, openCV reads images as BGR images
# By default, matplotlib reads images as RGB images

import cv2 as cv

img = cv.imread('photos/cat1.jpg')
cv.imshow('Cat', img)

# 1. convert BGR --> grayscale image
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# 2. convert BGR --> HSV image
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

# 3. convert BGR --> LAB image
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB', lab)

# 4. convert BGR --> RGB imgae
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)

cv.waitKey(2000)