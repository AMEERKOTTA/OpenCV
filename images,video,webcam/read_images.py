## Import opencv Library ##
import cv2

## Give the Image File Path ##
## Image is readed by "cv2.imread" and given the path ##
img = cv2.imread("H:\Projects\OpenCV\Faceless.jpg")

## Show the Image in a Window ##
## Specify the Window Name and image to be Displayed and which is given in imread function ##
cv2.imshow("Read Image", img)

## Giving a time to show the Image in the window ##
## for that using ""waitKey"" function ##
cv2.waitKey(0)
