# reading photos and videos

import cv2 as cv

# Reading photos
# img = cv.imread('photos/cat1.jpg')
# takes a path to an image and return a matrix of pixels

# cv.imshow('Cat', img)

# cv.waitKey(0)
# 0 means the image window will be open for infinite amount of time
# any other number will means that number of miliseconds

# Reading videos
capture = cv.VideoCapture('videos/catvideo1.mp4')

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)
    if cv.waitKey(20) & 0xFF == ord('d'):
        # this line means that frame rate will be 1 frame/20ms
        # and the window wont exit until we press 'd'
        break
capture.release()
cv.destroyAllWindows()
