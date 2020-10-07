import cv2

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter("output.avi", fourcc, 20.0, (640,480))

while(True):
    ret,frame = cap.read()
    if ret == True:
        out.write(frame)
        cv2.imshow("Frame",frame)
        if cv2.waitKey(1) & 0xFF == ord("s"):
            break
    else:
        break


cap.release()
out.release()
cv2.destroyAllWindows()