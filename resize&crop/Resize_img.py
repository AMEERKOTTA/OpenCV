import cv2
import numpy as np

image = cv2.imread(r"H:\Projects\OpenCV\Basic Functions\Faceless.jpg")
print(image.shape)

resize_image = cv2.resize(image, (500,500))

cv2.imshow("Image", image)
cv2.imshow("Resized Image", resize_image)

cv2.waitKey(0)
