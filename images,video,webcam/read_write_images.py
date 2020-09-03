import cv2

## "0" argument is used for gray scale image ##
## "1" argument is used for colored image ##
## "-1" argument is used for alpha channels ##

img = cv2.imread("H:\Files For Projects\Pictures\car2.jpg",-1)


cv2.imshow("Image", img)
cv2.waitKey(0)