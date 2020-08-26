## Import opencv Library ##
import cv2

## Fetch The Image ##
img = cv2.imread(r"H:\Projects\OpenCV\Basic Functions\Faceless.jpg")

## Define Canny Image Using "Canny" Function ##
## Canny Function is used to Detect the Edges of an Image ##
canny_img = cv2.Canny(img, 100, 100)

## Display the Image ##
cv2.imshow("Canny Image", canny_img)

cv2.waitKey(0)