import cv2 as cv
import numpy as np

#creating a blank image of 500x500 pixels which has 3 channels(RGB)
blank = np.zeros((500,500,3), dtype = 'uint8')
img = cv.imshow('Blank', blank)

#1. Paint the image a certain colour
blank[:] = 0,255,0
img = cv.imshow('Green', blank)
# blank[:] = 255,0,0
# img = cv.imshow('Blue', blank)
# blank[:] = 0,0,255
# img = cv.imshow('Red', blank)

#2. Draw a box
blank = cv.rectangle(blank, (0,0), (250,250), (255,0,0), thickness = 2)
#rectangle function takes in the image(blank), top-left point(0,0), bottom right point(250,250) and colour of the box(0,255,0)
cv.imshow('Rectangle box', blank)

#3. Draw a circle
blank  = cv.circle(blank, (250,250), 40, (0,0,255), thickness = 2)
cv.imshow('Circle', blank)

#4. Draw a line
blank = cv.line(blank, (0,0), (250,250), (255,255,255), thickness = 2)
cv.imshow('Line', blank)

#5. Write text on an image
cv.putText(blank, 'Hello', (225,225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (100,100,100), 2)
cv.imshow('Text', blank)


cv.waitKey(0)
