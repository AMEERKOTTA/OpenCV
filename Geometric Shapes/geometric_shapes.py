import cv2
import numpy as np

imagenumpy = np.zeros([512,512,3], np.uint8)
image = cv2.imread("H:\Files For Projects\Pictures\car10.jpg")

image = cv2.line(image,(0,0),(456,654),(0,0,0),10)
imagenumpy = cv2.line(imagenumpy,(0,0),(456,654),(0,0,0),10)
image = cv2.circle(image,(600,600),200,(0,0,255),-1)
imagenumpy = cv2.circle(imagenumpy,(600,600),200,(0,0,255),-1)
image = cv2.rectangle(image,(300,300),(750,550),(255.123,0),4)
imagenumpy = cv2.rectangle(imagenumpy,(300,300),(750,550),(255.123,0),4)
image = cv2.putText(image,"Not Today",(10,500),cv2.FONT_HERSHEY_COMPLEX,5,(255,255,0),10,cv2.LINE_AA)
imagenumpy = cv2.putText(imagenumpy,"Not Today",(10,500),cv2.FONT_HERSHEY_COMPLEX,5,(255,255,0),10,cv2.LINE_AA)


cv2.imshow("Image", image)
cv2.imshow("Numpy Image", imagenumpy)



cv2.waitKey(0)
cv2.destroyAllWindows()