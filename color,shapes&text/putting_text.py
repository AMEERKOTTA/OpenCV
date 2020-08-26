import cv2
import numpy as np

image = np.zeros((512,512,3), np.uint8)
print(image)

image[:] = 255,34,170

## Define text using putText function and specify the arguments ##
## There are many more font models in the putText Function ##
cv2.putText(image,                     ## image on to write the Text ##
            "TRY AGAIN",               ## Text to be Displayed ##
            (170,100),                 ## Cordinates of text ##
            cv2.FONT_HERSHEY_TRIPLEX,  ## Font Style ##
            2,                         ## Text Size ##
            (0,150,0),                 ## Color ##
            5)                         ## Thickness ##

cv2.imshow("Image",image)

cv2.waitKey(0)