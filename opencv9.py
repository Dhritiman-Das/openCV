# bluring

import cv2 as cv

img = cv.imread('photos/cat1.jpg')
cv.imshow('Cat', img)

# 1. Bluring by Averaging
#taking average of the kernal 
average = cv.blur(img, (3,3))
cv.imshow('Cat_avg', average)

# 2. Gaussian Blur
#we get less blur compared to averaging but the gaussian blur is more natural looking
gaussian = cv.GaussianBlur(img, (3,3), 0)
cv.imshow('Cat_gaussian', gaussian)

# 3. Median Blur
#takes median of the kernal, better removes noises
median = cv.medianBlur(img, 3)
cv.imshow('Cat_median', median)

# 4. Bilateral blurring
#retains the edges
bilateral = cv.bilateralFilter(img, 5, 15, 15)
cv.imshow('Bilateral', bilateral)

cv.waitKey(5000)