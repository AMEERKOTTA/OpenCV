import cv2

image = cv2.imread("H:\Files For Projects\Pictures\car3.jpg",-1)
## cv2.IMREAD_UNCHANGED = -1 ##
## cv2.IMREAD_GRAYSCALE = 0 ##
## cv2.IMREAD_COLOR = 1 ##

print(image)
cv2.imshow("Diplay Image", image)
cv2.waitKey(0)
