import cv2
import numpy as np

image = cv2.imread(r"H:\Projects\OpenCV\Joining Images\image.jpg")

image_Hor = np.hstack((image,image))
image_Ver = np.vstack((image,image))

cv2.imshow("Horizontal Output", image_Hor)
cv2.imshow("Vertical Outout", image_Ver)

cv2.waitKey(0)