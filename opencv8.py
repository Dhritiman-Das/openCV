# splitting and merging color channels

import cv2 as cv
import numpy as np

img = cv.imread('photos/cat1.jpg')
cv.imshow('Cat', img)

#spliting
b,g,r = cv.split(img)
blank = np.zeros(img.shape[:2], dtype = 'uint8')
blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

cv.imshow('Blue',b)
cv.imshow('blue_visualized', blue)

cv.imshow('Green',g)
cv.imshow('green_visualized', green)

cv.imshow('Red',r) 
cv.imshow('red_visualized', red)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

#merging
merged = cv.merge([b,g,r])
cv.imshow('Merged', merged)

cv.waitKey(4000)