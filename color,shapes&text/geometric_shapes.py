import cv2
import numpy as np


image = cv2.imread("H:\OpenCV - github\opencv-master\samples\data\lena.jpg")
## image = np.zeros([512,512,3],np.uint8) ##
## image = np.ones([512,512,3],np.uint8) ##


image = cv2.line(image,(0,0),(255,255),(0,255,255),3)
image = cv2.arrowedLine(image,(0,0),(400,298),(255,255,255),5)
image = cv2.rectangle(image,(25,25),(355,355),(0,0,255),2) ## thickness = -1 will give filled shape ##
image = cv2.circle(image,(155,155),150,(255,0,0),4)
image = cv2.putText(image,"I'm Not Done",(155,167),cv2.FONT_HERSHEY_COMPLEX_SMALL,2,(0,0,0),5)




cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()