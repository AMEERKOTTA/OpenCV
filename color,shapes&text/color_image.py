import cv2
import numpy as np
## Define Image using numpy np.zeros method ##
image = np.zeros((512,512,3), np.uint8)
print(image)
## Colour the Image with green ##
## 0,0,255  = red ##
## 255,0,0  = Blue ##
## image[100:400,200:400] = 0,255,0 ##
## image[400:600,400:700] = 255,255,0 ##
# Display the Image ##
image[:] = 0,0,255
cv2.imshow("Image", image)

cv2.waitKey(0)