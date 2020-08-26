import cv2
import numpy as np

## Import Image and Find its Size ##
image = cv2.imread(r"H:\Projects\OpenCV\Basic Functions\Faceless.jpg")
print(image.shape)

## Crop the Image to required size ##
crop_image = image[200:700, 500:700]

## Show both images and compare ##
cv2.imshow("Real Image", image)
cv2.imshow("Cropped Image", crop_image)


cv2.waitKey(0)
