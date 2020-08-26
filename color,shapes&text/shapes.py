import cv2
import numpy as np

image = np.ones((512,512,3), np.uint8)
print(image)

image[:] = 255,0,255
################   RECTANGLE   #####################
## Deifne Rectangle with points ##
cv2.rectangle(image,(0,0),(255,255),(255,255,0),3)
## Cv2.FILLED is used to fill the space of the shape ##
cv2.rectangle(image,(155,155),(512,412),(255,0,0),cv2.FILLED) 
###############   CIRCLES     ######################
## Define Circles with origin, radius, color, thickness ##
cv2.circle(image,(345,456),100,(0,0,255),5)
cv2.circle(image,(112,321),250,(0,255,255),cv2.FILLED)


cv2.imshow("Image", image)

cv2.waitKey(0)