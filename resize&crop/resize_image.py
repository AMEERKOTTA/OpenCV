import cv2

W = 1000
image = cv2.imread("H:\Files For Projects\Pictures\Bill Gates.jpg",1)
height,width,depth = image.shape
imagescale = W/width

newX, newY = image.shape[1]*imagescale, image.shape[0]*imagescale

newimage = cv2.resize(image, (int(newX), int(newY)))

cv2.imshow("Old Image", image)
cv2.imshow("New Image", newimage)

cv2.waitKey(0)
cv2.destroyAllWindows()