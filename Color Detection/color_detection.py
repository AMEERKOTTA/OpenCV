import cv2
import numpy as np

def empty(a):
    pass


path = r"H:\Projects\OpenCV\Color Detection\Faceless.jpg"
img = cv2.imread(path)
image = cv2.resize(img,(250,250))

## Trackbars ##
## There will be six TrackBars ##
cv2.namedWindow("TrackBars")                                    ## Trackbars ##
cv2.resizeWindow("TrackBars", 640,240)                          ## Size of the Window ##
cv2.createTrackbar("Hue Min","TrackBars",0,179,empty)           ## Hue Minimum ##
cv2.createTrackbar("Hue Max","TrackBars",179,179,empty)         ## Hue Maximum ##
cv2.createTrackbar("Sat Min","TrackBars",0,255,empty)           ## Saturation Minimum ##
cv2.createTrackbar("Sat Max","TrackBars",255,255,empty)         ## Saturation Maximum ##
cv2.createTrackbar("Val Min","TrackBars",0,255,empty)           ## Value Minimum ##
cv2.createTrackbar("Val Max","TrackBars",255,255,empty)         ## Value Maximum ##

while True:

    ## First Convert Image into HSV space ##
    imageHSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("Hue Min", "TrackBars")
    h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
    s_min = cv2.getTrackbarPos("Sat Min", "TrackBars")
    s_max = cv2.getTrackbarPos("Sat Max", "TrackBars")
    v_min = cv2.getTrackbarPos("Val Min", "TrackBars")
    v_max = cv2.getTrackbarPos("Val Max", "TrackBars")
    print(h_min,h_max,s_min,s_max,v_min,v_max)

    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])

    mask = cv2.inRange(imageHSV, lower,upper)
    imageResult = cv2.bitwise_and(image,image, mask = mask)

    

    cv2.imshow("Original", image)
    cv2.imshow("HSV Image", imageHSV)
    cv2.imshow("Mask", mask)
    cv2.imshow("Result", imageResult)
    cv2.waitKey(0)
