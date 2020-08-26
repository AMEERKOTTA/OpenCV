import cv2
import numpy as np

image = cv2.imread(r"H:\Projects\OpenCV\Basic Functions\Faceless.jpg")
kernel = np.ones((5,5), np.uint8)

canny_image = cv2.Canny(image, 100,100)
dilated_image = cv2.dilate(canny_image, kernel, iterations=1)

cv2.imshow("Dilated Image", dilated_image)

cv2.waitKey(0)
