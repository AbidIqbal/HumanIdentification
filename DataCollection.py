import urllib
import cv2
import numpy as np
import os

def store_raw_images():
    positive_imgages_link='http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n04547592'
    positive_image_url=urllib.urlopen(positive_imgages_link).read().decode()

    if not os.path.exists('wall'):
        os.makedirs('wall')

    pic_num=1

    for i in positive_image_url.split('\n'):
        try:
            print (i)
            urllib.urlretrieve(i,"wall/"+str(pic_num)+'.jpg')
            # img=cv2.imread("positive/"+str(pic_num)+'.jpg',cv2.IMREAD_GRAYSCALE)
            # resized_image=cv2.resize(img,(100,100))
            # cv2.imwrite("positive/"+str(pic_num)+'.jpg',resized_image)
            print pic_num
            pic_num+=1
        except Exception as e:
            print (str(e))


def resize_grayscale_image():
    image_path='newData/1'
    storage_path='latestTraining/positive/rawdata'
    pic_num = 1
    for img in os.listdir(image_path):
        try:

            current_image_path = str(image_path) + '/' + str(img)
            print current_image_path
            checkImage = cv2.imread(current_image_path,cv2.IMREAD_GRAYSCALE)
            # checkImage = cv2.imread(current_image_path)
            resized_image=cv2.resize(checkImage,(700,700))
            cv2.imwrite(str(storage_path)+'/'+str(pic_num)+'.bmp',resized_image)


            print pic_num
            pic_num+=1

        except Exception  as e:
            print (str(e))



def remove_uglies():
    for file_type in ['New/cat_resized']:
        for img in os.listdir(file_type):
            for ugly in os.listdir('New/ugly'):
                try:
                    current_image_path=str(file_type)+'/'+str(img)
                    ugly=cv2.imread('New/ugly/'+str(ugly))

                    checkImage=cv2.imread(current_image_path)
                    if ugly.shape==checkImage.shape and not (np.bitwise_xor(ugly,checkImage).any()):
                        print "Yeah it's ugly"
                        print (current_image_path)
                        os.remove(current_image_path)
                except Exception  as e:
                    print (str(e))


def change_image_extension():
    pic_num=1
    for file_type in ['myVideo1']:
        for img in os.listdir(file_type):
            try:
                current_image_path=str(file_type)+'/'+str(img)
                jpg_image=cv2.imread(current_image_path,)
                cv2.imwrite("training/positive/rawdata/" + str(pic_num) + '.bmp', jpg_image)
                print (current_image_path)
                pic_num+=1

            except Exception  as e:
                print (str(e))

resize_grayscale_image()
# change_image_extension()
# remove_uglies()
# store_raw_images()