from google.cloud import storage
from firebase import firebase
# import psycopg2
from PIL import Image
import cv2
import numpy as np
import datetime
import time
import base64


#
strarr=[]
#
#

# with open("1.jpg", "rb") as imageFile:
#     str = base64.b64encode(imageFile.read())
#     strarr.append(str)
#     # print str
# print strarr
# fh = open("imageToSave.png", "wb")
# fh.write(strarr[0].decode('base64'))
# fh.close()
# Create our body classifier
body_classifier = cv2.CascadeClassifier('humandetector.xml')

firebase=firebase.FirebaseApplication('https://securitysystem-9f723.firebaseio.com/')


# img=Image.open('1.jpg')
# numpyimage=np.array(img)
# print (numpyimage)



# blob=open('1.jpg','rb').read();
# newblob=blob.decode("utf-8")
# print blob
# print newblob
# posted = firebase.put('Blob', {'object': 'Cat','time':blob})
# print len(strarr[0])
# posted = firebase.put('user', 'three',strarr)

# Initiate video capture for video file
cap = cv2.VideoCapture('newData/1.mp4')

# Loop once video is successfully loaded
count=0
framecount=0
while cap.isOpened():

    # Read first frame
    ret, frame = cap.read()
    frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)

    # frame = cv2.resize(frame, (700, 700))
    gray = frame
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Pass frame to our body classifier
    bodies = body_classifier.detectMultiScale(gray, 1.3, 5)

    print len(bodies)

    # cv2.imshow('Imag',frame)
    area = 0
    maxh = 0
    maxw = 0
    startx = 0
    starty = 0
    print "Bodies found"
    for (x, y, w, h) in bodies:
        if len(bodies) == 0:
            print "No body"
            break
        else:
            timestamp = int(time.time())
            if ((w * h) > area):
                startx = x
                starty = y
                maxw = w
                maxh = h

        if(framecount==10):
            cv2.rectangle(frame, (startx, starty), (startx + maxw, starty + maxh), (0, 0, 255), 2)
            # cv2.imwrite("output/" + str(count) + '.jpg', frame)
            # data=cv2.imread("output/" + str(count) + '.jpg')
            with open('output\\10.bmp', "rb") as imageFile:
                str = base64.b64encode(imageFile.read())
                strarr.append(str)
                img1=strarr[0]
                firstPart=img1[:len(img1)/4]
                secondPart=img1[len(img1)/4:len(img1)/2]
                thirdPart=img1[len(img1)/2:len(img1)/2+len(img1)/4]
                fourthPart=img1[len(img1)/2+len(img1)/4:]
                posted = firebase.post('Human', {'object': 'Human','time':timestamp,'images':{'firstPart':firstPart,'secondPart':secondPart,'thirdPart':thirdPart,'fourthPart':fourthPart}})
            framecount=0
    # posted = firebase.post('Notification', {'object': 'Cat','time':timestamp})
    #         posted = firebase.post('Human', {'object': 'Human','time':timestamp})
        cv2.imshow('Objects', frame)
        count+=1
        framecount+=1
# cv2.waitKey(0)
# cv2.destroyAllWindows()
    # frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)
    #
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # # Pass frame to our body classifier
    # bodies = body_classifier.detectMultiScale(gray, 2.2, 15)
    #
    # # Extract bounding boxes for any bodies identified
    #
    # for (x, y, w, h) in bodies:
    #     if len(bodies)==0:
    #         print "No body"
    #         break
    #     else:
    #         print "Bodies found"
    #         timestamp = int(time.time())
    #
    #         # storage_client=storage.Client.from_service_account_json()
    #
    #         # posted = firebase.post('Notification', {'object': 'Cat','time':timestamp})
    #         # posted = firebase.post('Human', {'object': 'Human','time':timestamp})
    #         # posted = firebase.post('cats', {'object': 'cats','time':timestamp})
    #
    #
    #
    #
    #         # posted = firebase.put('cats','', {'object': 'Cat','time':timestamp})
    #         count=count+1
    #         cv2.imwrite("output/" + str(count) + '.bmp', frame)
    #         cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)
    #         cv2.imshow('Persons', frame)

    # if cv2.waitKey(1) == 13:  # 13 is the Enter Key
    #     break

cap.release()
cv2.destroyAllWindows()