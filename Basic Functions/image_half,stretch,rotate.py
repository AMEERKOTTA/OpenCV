import cv2

image = cv2.imread("H:\Files For Projects\Pictures\car2.jpg", 1)
print(image.shape)

image_half = cv2.resize(image,(0,0),fx=0.5, fy= 0.5)
image_stretch = cv2.resize(image,(750,600))
M = cv2.getRotationMatrix2D((0,0),-30,1)
rotated = cv2.warpAffine(image,M,(image.shape[1],image.shape[0]))


cv2.imshow("Image", image)
cv2.imshow("Half Image", image_half)
cv2.imshow("Stretch Image", image_stretch)
cv2.imshow("Rotated Image", rotated)

cv2.waitKey(0)
cv2.destroyAllWindows()