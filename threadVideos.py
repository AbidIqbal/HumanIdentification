# Install Opencv,imutils and numpy packages on your platform.

import cv2
import numpy as np
import imutils

cap1 = cv2.VideoCapture('walking.avi')
# cap1 refers to capture 1 from camera 1
# (0) refers to index 0 of camera 1 on your system.
cap2 = cv2.VideoCapture('walking.avi')
# cap2 refers to capture 2 from camera 2
# (1) refers to index 1 of camera 2 on your system

while cap1.isOpened() and cap2.isOpened():
    ret, frame1 = cap1.read()
    ret, frame2 = cap2.read()

    cv2.imshow('cam1', cap1)
    cv2.waitKey(1)
    cv2.imshow('cam2', cap2)
    cv2.waitKey(1)
# Enter z = 0 for still images or z = 1 for video stream.