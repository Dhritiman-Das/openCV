# Face recognition

import os
import cv2 as cv
import numpy as np

people = ['Leo', 'sushant']
DIR = r'C:\Users\Dhritiman Das\Desktop\opencv\photos\train'

haar_cascade = cv.CascadeClassifier('haar_face.xml')

features = []
labels = []

def create_train():
    for person in people:
        path = os.path.join(DIR, person)
        # print(path)
        label = people.index(person)
        # print(label)

        for img in os.listdir(path):
            img_path = os.path.join(path,img)

            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors = 4) # returns an array[x,y,w,h]
            # print(faces_rect)
            # print('------------')
            for(x,y,w,h) in faces_rect:
                faces_roi = gray[y:y+h, x:x+w] #crops the image
                # cv.imshow('y', faces_roi)
                # cv.waitKey(1000)
                features.append(faces_roi) 
                labels.append(label)

create_train()
print('Training done----------------------------')

#training our recognizer

features = np.array(features, dtype = 'object')
labels = np.array(labels)

# print(labels)
# print(features)

face_recognizer = cv.face.LBPHFaceRecognizer_create()

#training our data
face_recognizer.train(features, labels)
face_recognizer.save('face_trained.yml')

np.save('features.npy', features)
np.save('labels.npy', labels)