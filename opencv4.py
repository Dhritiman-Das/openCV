# Basic functions of openCV

import cv2 as cv

img = cv.imread('photos/cat1.jpg')
cv.imshow('Cat', img)

#1. Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Cat_gray', gray)

#2. Blurring an imgae
blur = cv.GaussianBlur(img, (5,5), cv.BORDER_DEFAULT)
#to increase blur, increase the kernal size((5,5) in our case)
cv.imshow('Cat_blur', blur)

#3. Edge Cascading(getting edges) of an image
canny = cv.Canny(blur, 125, 175)
cv.imshow('Cat_cascasde', canny)

#4. Dilating(making edges thicker) of an image
dilated = cv.dilate(canny, (7,7), iterations = 3)
cv.imshow('Cat_dilated', dilated)

#5. Eroding(making edges thinner) of an image
eroded = cv.erode(dilated, (7,7), iterations = 3)
cv.imshow('cat_eroded', eroded)

#6. Resize
resized = cv.resize(img, (300,300), interpolation = cv.INTER_CUBIC)
#if we are increase size of image then go for cv.INTER_CUBIC. it is slower but image is of better quality
#if we are shrinking the image, then go for cv.INTER_AREA
cv.imshow('cat_resized', resized)

#7. Cropping
cropped = img[50:200, 200:400]
cv.imshow('cat_cropped', cropped)

cv.waitKey(10000)