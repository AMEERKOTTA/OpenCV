import numpy as np
import cv2

image = cv2.imread("H:\Files For Projects\Pictures\Bill Gates.jpg",1)
image = cv2.resize(image,(500,500))
print(image.shape)

kernel = np.ones((5,5), "uint8")

blurImage = cv2.GaussianBlur(image,(5,55),0)
dilateImage = cv2.dilate(image,kernel,iterations=1)
erodeImage = cv2.erode(image, kernel, iterations=1)

img = np.concatenate((blurImage,dilateImage,erodeImage), axis=1)

cv2.imshow("IMAGE", img)
cv2.waitKey(0)
cv2.destroyAllWindows()