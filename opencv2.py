import cv2 as cv


def rescaleFrame(frame, scale=0.75):
    # works for images, videos and live videos(like from a webcam)
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    # frame.shape[1] means width of our frame
    # frame.shape[0] means heoght of our frame

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# def changeres(width, height):
#     #works for live video only(like from a webcam or external camera)
#     capture.set(3,width)
#     capture.set(4, height)

# reading images
# img = cv.imread('photos/cat1.jpg')
# cv.imshow('Cat', img)
# resized_image = rescaleFrame(img)
# cv.imshow('Cat_resized', resized_image)


# Reading videos
capture = cv.VideoCapture('videos/catvideo1.mp4')

while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame)
    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)
    if cv.waitKey(20) & 0xFF == ord('d'):
        # this line means that frame rate will be 1 frame/20ms
        # and the window wont exit until we press 'd'
        break
capture.release()
cv.destroyAllWindows()

cv.waitKey(0)
