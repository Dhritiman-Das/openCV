#  Contour detection

import cv2 as cv
import numpy as np

img = cv.imread('photos/cat3.jpg')
cv.imshow('Cats', img)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Cat_Gray', gray)

blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
cv.imshow('cat_blur', blur)

canny = cv.Canny(img, 125, 175)
cv.imshow('Cat_CannyEdges', canny)

# ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
# #pixel values below 125 becomes 0 and above 125 becomes 255
# cv.imshow('Cats_thresh', thresh)

contours, hierarchies = cv.findContours(blur, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contours(s) found')

cv.drawContours(blank, contours, -1, (0,0,255), 1)
cv.imshow('Contours_drawn', blank)


cv.waitKey(0)
