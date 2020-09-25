import numpy as np
import cv2

## Black Image and displaying it ##
black = np.zeros([200,200,1], "uint8")
cv2.imshow("Black Image", black)
print("pixel value in black image is", black[0,0])

## Black Image with three channels and displaying it ##
ones = np.ones([200,200,3], "uint8")
cv2.imshow("Ones", ones)
print("pixel value in ones image is", ones[0,0])

## White Image and displaying it ##
white = np.ones([200,200,3],"uint8")
white *= (2**16-1)
cv2.imshow("White", white)
print("Pixel value in white image is", white[0,0])

## Blue Image and displaying it ##
blue = np.ones([200,200,3], "uint8")
blue[:,:] = (255,0,0)
cv2.imshow("Blue", blue)
print("Pixel value in Blue Image is", blue[0,0])


cv2.waitKey(0)
cv2.destroyAllWindows()