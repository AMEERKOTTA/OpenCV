import numpy as np
import cv2

## Define Image ##
image = np.zeros([200,200,1],"uint8")
## Display Image ##
cv2.imshow("Image",image)
## Giving Delay ##
cv2.waitKey(0)
cv2.destroyAllWindows()