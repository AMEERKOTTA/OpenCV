import cv2

cap = cv2.VideoCapture(r"H:\Files For Projects\Videos\video.mp4")

while (True):
    ret, frame = cap.read()
    grayImage = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("GrayImage", grayImage)

    if cv2.waitKey(1) & 0xFF == ord("s"):
        break

cap.release()
cv2.destroyAllWindows()