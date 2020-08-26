## Import Required opencv Library ##
import cv2

## Import Video from the Directory ##
cap = cv2.VideoCapture(r"H:\Projects\OpenCV\test_video.mp4")

## Display the Video ##
## Video is the Collection of Sequence of Images ##
## Define a While loop to go through all the Images in the Video ##
while True:
    ## This will save the image in "img" ##
    ## "success" is a boolean which is True or False ##
    success, img = cap.read()
    
    ## Display the Video using cv2.imshow ##
    cv2.imshow("Video",img)

    ## To break our the Loop ##
    ## An if statement is defined to go for a plus "q" press to break out the loop ##
    if cv2.waitKey(1) & 0xFF ==ord("q"):
        break
