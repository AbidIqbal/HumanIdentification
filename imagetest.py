import cv2
from firebase import firebase
import numpy as np
import os
import time


# Create our body classifier

body_classifier = cv2.CascadeClassifier('mycatdetector.xml')

firebase=firebase.FirebaseApplication('https://fypapplication-22974.firebaseio.com/')


# pic=1
# for file_type in ['videos/cat']:
#     for img in os.listdir(file_type):
#         try:
#             current_image_path = str(file_type) + '/' + str(img)
#             frame = cv2.imread(current_image_path)
#             print current_image_path
#             frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)
#             gray = frame
#             gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#             # Pass frame to our body classifier
#             bodies = body_classifier.detectMultiScale(gray, 1.2, 3)
#             print pic
#             pic+=1
#             print len(bodies)
#
#             cv2.imshow('Imag', frame)
#
#             print "Bodies found"
#             for (x, y, w, h) in bodies:
#                 cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
#                 cv2.imshow('Objects', frame)
#                 cv2.waitKey(0)
#
#
#         except Exception  as e:
#             print (str(e))

frame=cv2.imread('videos/c4.jpg')
#
frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)

gray=frame
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
# Pass frame to our body classifier
bodies = body_classifier.detectMultiScale(gray, 1.2, 3)

print len(bodies)

cv2.imshow('Imag',frame)

print "Bodies found"
for (x,y,w,h) in bodies:
    timestamp = int(time.time())
    posted = firebase.post('cats', {'object': 'cats', 'time': timestamp})
    cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.imshow('Objects',frame)
    cv2.waitKey(0)
cv2.destroyAllWindows()