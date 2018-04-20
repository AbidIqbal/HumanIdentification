import cv2
from firebase import firebase
import numpy as np
import os
import time


# Create our body classifier

body_classifier = cv2.CascadeClassifier('humandetector.xml')

# firebase=firebase.FirebaseApplication('https://fypapp-37b93.firebaseio.com/')



frame=cv2.imread('newData/1/74.jpg')
#
# frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)
frame=cv2.resize(frame,(700,700))
gray=frame
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
# Pass frame to our body classifier
bodies = body_classifier.detectMultiScale(gray, 1.3, 5)

print len(bodies)

# cv2.imshow('Imag',frame)
area=0
maxh=0
maxw=0
startx=0
starty=0
print "Bodies found"
for (x,y,w,h)  in bodies:

    timestamp = int(time.time())
    if((w*h)>area):
        startx=x
        starty=y
        maxw=w
        maxh=h

cv2.rectangle(frame, (startx-5, starty-20), (startx + maxw-20, starty + maxh+100), (0, 0, 255), 2)
# # posted = firebase.post('Notification', {'object': 'Cat','time':timestamp})
# # posted = firebase.post('Human', {'object': 'Human','time':timestamp})
cv2.imshow('Objects', frame)
cv2.waitKey(0)
cv2.destroyAllWindows()