import cv2
import numpy as np


# Initiate video capture for video file
cap = cv2.VideoCapture('videos/c2.mp4')

# Loop once video is successfully loaded
pic_num=1
storage_path = 'videos/cat'
while cap.isOpened():
    # Read first frame
    print 'Reading'
    ret, frame = cap.read()
    resized_image = cv2.resize(frame, (500, 500))
    cv2.imwrite(str(storage_path) + '/' + str(pic_num) + '.jpg', frame)
    print pic_num
    pic_num+=1
print 'done'
cap.release()
cv2.destroyAllWindows()