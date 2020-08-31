## Import OpenCV as CV2 ##
## Import numpy as np ##
import cv2
import numpy as np

## Fetch the haarcascade files for face and eye detection ##
face_cascade = cv2.CascadeClassifier(r"H:\Projects\Files For Projects\Other Files\haar cascade files\haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier(r"H:\Projects\Files For Projects\Other Files\haar cascade files\haarcascade_eye.xml")

## Fetch the image file to be identified from the Directory ##
img = cv2.imread(r"H:\Projects\OpenCV\Face and Eye Detection\kiera knightly.jpg")
print(img.shape)
## Resize to convenient Size ##
img = cv2.resize(img, (450,400))
## Convert it to gary image ##
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

## Detecting face ##
faces = face_cascade.detectMultiScale(gray_img,1.2,4)
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray_img[y:y+h,x:x+w]
    roi_color = img[y:y+h,x:x+w]

    ## Detecting eye ##
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,255),2)

cv2.imshow("Image", img)

k = cv2.waitKey(0)
if k == 1000:
    cv2.destroyAllWindows()
elif k == ord("s"):
        cv2.imwrite("image.jpg",img)
        cv2.destroyAllWindows()



cv2.imshow("Image",img)
cv2.waitKey(0)