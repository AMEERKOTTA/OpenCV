import numpy as np
import cv2
## Import image from directory ##
img = cv2.imread("H:\Projects\OpenCV\Face Detection\image2.jpg")
print(img.shape)
## FaceCascade haar file is fetched from directory ##
faceCascade = cv2.CascadeClassifier("H:\Projects\OpenCV\Face Detection\haarcascade_frontalface_default.xml")
## make the image to gary image ##
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
## Detect faces from the image using haar cacsade method ##
faces = faceCascade.detectMultiScale(gray_img,1.1, 4)
## make bounded rectangle to represent faces ##
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)

cv2.imshow("Result", img)


cv2.waitKey(0)