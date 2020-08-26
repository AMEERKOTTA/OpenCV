import cv2
import numpy as np
# Fetch the Image to be Viewed ##
image = cv2.imread(r"H:\Projects\OpenCV\Warp Perspective\image2.jpg")


width, height = 300,450
## Give the Cordintes to be Selected ##
pts1 = np.float32([[340,268],[556,268],[309,548],[568,548]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
## Define matrix and ImgOtput ##
matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgOutput = cv2.warpPerspective(image, matrix, (width,height))


cv2.imshow("Image", image)
cv2.imshow("Output", imgOutput)


cv2.waitKey(0)