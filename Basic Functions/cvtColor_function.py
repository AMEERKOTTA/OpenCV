## Import OpenCV Package ##
import cv2

## Fetch Image from the Directory ##
img = cv2.imread(r"H:\Projects\OpenCV\Basic Functions\Faceless.jpg")

## Convert image to gray scale image using "cvtColor" Function ##
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

## Show the Image using "imshow" ##
cv2.imshow("Gray Image", img_gray)

## give wait key ##
cv2.waitKey(0)