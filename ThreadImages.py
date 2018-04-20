import cv2
import threading

body_classifier = cv2.CascadeClassifier('haarcascade_fullbody.xml')


class camThread(threading.Thread):
    def __init__(self, previewName, camID):
        threading.Thread.__init__(self)
        self.previewName = previewName
        self.camID = camID
    def run(self):
        print "Starting " + self.previewName
        camPreview(self.previewName, self.camID)

def camPreview(previewName, camID):
    # cv2.namedWindow(previewName)
    cam = cv2.VideoCapture(camID)
    if cam.isOpened():  # try to get the first frame
        print ("success")
        rval, frame = cam.read()
    else:
        rval = False
    # frame = cv2.imread(camID)
    try:
        while rval:
            frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            # Pass frame to our body classifier
            bodies = body_classifier.detectMultiScale(gray, 1.2, 3)
            print len(bodies)

            for (x, y, w, h) in bodies:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.imshow(previewName, frame)
            rval, frame = cam.read()
            key = cv2.waitKey(20)
            if key == 27:  # exit on ESC
                break
        cv2.destroyWindow(previewName)
    except Exception  as e:
        print (str(e))



# Create two threads as follows
thread1 = camThread("Camera 1", "walking.avi")
thread2 = camThread("Camera 2", "walking.avi")
thread3 = camThread("Camera 3", "c3.jpg")
thread1.start()
# thread2.start()
# thread3.start()
# cv2.destroyAllWindows()