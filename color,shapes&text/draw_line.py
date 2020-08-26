import cv2
import numpy as np

image = np.zeros((512,512,3), np.uint8)

image[:] = 0,255,0

cv2.line(image,(23,34),(76,300),(255,0,0), 3)
cv2.line(image,(512,200),(412,100),(255,0,255), 3)
cv2.line(image,(0,0),(512,512),(255,255,0), 10)


cv2.imshow("Image", image)

cv2.waitKey(0)

