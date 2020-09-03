import cv2

## 0 for index 0 camera ##
## 1 for index 1 camera ##
## or give the video path ##

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter("output3.mp4", fourcc, 20.0, (640,480))


print(cap.isOpened())

while(cap.isOpened()):
    ret,frame = cap.read() ## ret is the boolean whether true or false ##
                           ## frame will be the video captured by the script ##

    print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  ## width of the frame ##
    print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) ## height of the frame ##
    out.write(frame)  ## Save the output value ##


    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) ## Convert the frame to gray ##
    cv2.imshow("frame", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()