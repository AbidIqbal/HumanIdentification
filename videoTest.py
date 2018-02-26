from google.cloud import storage
from firebase import firebase
import cv2
import numpy as np
import datetime
import time



# Create our body classifier
body_classifier = cv2.CascadeClassifier('humandetector.xml')

firebase=firebase.FirebaseApplication('https://fypapplication-22974.firebaseio.com/')


# Initiate video capture for video file
cap = cv2.VideoCapture('videos/3.mp4')

# Loop once video is successfully loaded
count=0
while cap.isOpened():

    # Read first frame
    ret, frame = cap.read()
    frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Pass frame to our body classifier
    bodies = body_classifier.detectMultiScale(gray, 1.2, 3)

    # Extract bounding boxes for any bodies identified

    for (x, y, w, h) in bodies:
        if len(bodies)==0:
            print "No body"
            break
        else:
            print "Bodies found"
            timestamp = int(time.time())

            posted = firebase.post('Human', {'object': 'Human','time':timestamp})
            # posted = firebase.put('cats','', {'object': 'Cat','time':timestamp})
            count=count+1
            print (count)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)
            cv2.imshow('Persons', frame)

    if cv2.waitKey(1) == 13:  # 13 is the Enter Key
        break

cap.release()
cv2.destroyAllWindows()