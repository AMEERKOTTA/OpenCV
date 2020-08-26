## Import opencv library ##
import cv2
## "cv2.VideoCapture(0)" means webcam or First Camera ##
## Setting Parameters of the Image to be taken ##
## "cv2.VideoCapture(1)" means Second Camera or Webcam ##
## "cv2.VideoCapture("video.mp4")" means Video file ##
cap = cv2.VideoCapture(0)
cap.set(4,640)
cap.set(4,480)
cap.set(10,100)
## Define a While loop to go through all the Images in the Video ##
while True:
    ## This will save the image in "img" ##
    ## "success" is a boolean which is True or False ##
    success, img = cap.read()
    ## Display the Video using cv2.imshow ##
    cv2.imshow("Video", img)
    ## To break our the Loop ##
    ## An if statement is defined to go for a plus "q" press to break out the loop ##
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
