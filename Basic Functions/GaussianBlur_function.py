## Import opencv library ##
import cv2

## Fetch Image ##
img = cv2.imread(r"H:\Projects\OpenCV\Basic Functions\Faceless.jpg")

## Blur the Image wrt original image ##
## If we want  to Blur the Image wrt Gray Image, then first define it ##
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur_img = cv2.GaussianBlur(gray_img, (7,7), 0)

## Show the Images ##
cv2.imshow("Gray Image", gray_img)
cv2.imshow("Blur Image", blur_img)

cv2.waitKey(0)