from firebase import firebase
import base64
import time
strarr=[]
i=0;
timestamp = int(time.time())
firebase=firebase.FirebaseApplication('https://securitysystem-9f723.firebaseio.com/')


with open('output\\10.bmp', "rb") as imageFile:
    str = base64.b64encode(imageFile.read())
    strarr.append(str)
    img1 = strarr[0]
    firstPart = img1[:len(img1) / 2]
    secondPart = img1[len(img1) / 2:]
    posted = firebase.post('Human', {'time': timestamp})

    print i
    i+=1

    posted = firebase.post('Images', {'img_url1':firstPart})
    posted = firebase.post('Images', {'img_url2': secondPart})

    posted = firebase.post('Notification', {'id': "1"})
    posted = firebase.post('NotificationImages', {'img_url1':firstPart})
    posted = firebase.post('NotificationImages', {'img_url2': secondPart})

