import numpy as np
import cv2

path = r"H:\Projects\OpenCV\contours,shapes\shapes2.png"
img = cv2.imread(path)
print(img.shape)
image = cv2.resize(img, (400,400))
imageContour = image.copy() 

def getContours(image):                                                 ## Define a function to look at all shapes in the Image ##
    contours,hierarchy = cv2.findContours(image,
                            cv2.RETR_EXTERNAL,
                            cv2.CHAIN_APPROX_NONE)
    for cnt in contours:                                                ## For every shape in Contour Image ##
        area = cv2.contourArea(cnt)
        print(area)
        
        if area>500:
            cv2.drawContours(imageContour, cnt, -1, (255,0,0),5)        
            perimeter = cv2.arcLength(cnt, True)
            print(perimeter)
            approx = cv2.approxPolyDP(cnt, 0.03*perimeter, True)
            print("corner points",len(approx))
            objectcorner = len(approx)
            x,y,w,h = cv2.boundingRect(approx)

            if objectcorner == 3: Objecttype = "Triangle"
            elif objectcorner == 4:
                aspectratio = w/float(h)
                if aspectratio>0.95 and aspectratio<1.05:
                    Objecttype = "Square"
                else:
                    Objecttype = "Rectangle"
            elif objectcorner>4: Objecttype = "Circle"
            else: Objecttype = "None"

            cv2.rectangle(imageContour,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.putText(imageContour, Objecttype,                       ## ImageContour and Objecttype ##
                        (x+(w//2)-10,y+(h//2)-10),                      ## Location where text to be put ##
                        cv2.FONT_HERSHEY_COMPLEX,                       ## Font Style ##
                        0.5, 
                        (0,0,0),                                        ## Font Color ##
                        2)                                              ## Thickness ##

## Define Respective Images ##
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image_blur = cv2.GaussianBlur(image_gray,(7,7),2)
image_canny = cv2.Canny(image_blur, 50,50)
getContours(image_canny)

## Display respective images ##
cv2.imshow("Original", image)
cv2.imshow("Gray Image", image_gray)
cv2.imshow("Blur Image", image_blur)
cv2.imshow("Canny Image", image_canny)
cv2.imshow("Image Contour", imageContour)


cv2.waitKey(0)