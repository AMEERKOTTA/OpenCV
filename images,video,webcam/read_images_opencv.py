## Import Opencv Library and sys Function ##
import cv2 as cv
import sys

## Fetch image from the Directory ##
img = cv.imread(cv.samples.findFile("H:\Projects\Files For Projects\Pictures\cat.69.jpg"))
## Resize the Image for Convenience ##
img = cv.resize(img,(300,300))
if img is None:
    sys.exit("Could not read the image.")
cv.imshow("Display window", img)
k = cv.waitKey(0)
if k == ord("s"):
    cv.imwrite("H:\Projects\Files For Projects\Pictures\cat.69.jpg", img)