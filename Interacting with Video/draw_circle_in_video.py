import cv2

cap = cv2.VideoCapture(0)
color = (255,0,234)
line_width = 3
radius = 100
point = (0,0)

### Initialize the Event Click ###
def click (event, x, y, flags, param):
    global point, pressed
    if event == cv2.EVENT_LBUTTONDOWN:
        print("pressed", x,y)
        point = (x,y)
### Name the Window and Call the Click ##
cv2.namedWindow("frame")
cv2.setMouseCallback("frame", click)

### Read frame by frame ###
while (True):
    ret, frame = cap.read()
    ### Draw the Circle where point is ###
    cv2.circle(frame, point, radius, color, line_width)
    cv2.imshow("frame", frame)
    ### Wait for the key press and "s" for Exit ###
    ch = cv2.waitKey(1)
    if ch & 0xFF == ord("s"):
        break

cap.release()
cv2.destroyAllWindows()