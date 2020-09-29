import cv2

image = cv2.imread("H:\Files For Projects\Pictures\Bill Gates.jpg",1)
grayimage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imwrite("H:\Files For Projects\Pictures\BillGateGray.jpg", grayimage)

b = image[:,:,0]
g = image[:,:,1]
r = image[:,:,2]

rgba = cv2.merge((b,g,r,g))
cv2.imwrite("H:\Files For Projects\Pictures\rgba.png", rgba)

cv2.imshow("Original Image", image)
cv2.imshow("Gray Image",grayimage)
cv2.imshow("RGBA Image", rgba)


cv2.waitKey(0)