import cv2

image = cv2.imread(r"H:\OpenCV - github\opencv-master\samples\data\lena.jpg")

cv2.imshow("Image", image)
## Define k as waitKey ##
k = cv2.waitKey(0) & 0xFF
## if k = esc,then destroyallwindows ##
if k == 27:
    cv2.destroyAllWindows()
## or if the s key is pressed, then the file is saved ##
elif k == ord("s"):
    cv2.imwrite("Lena_Image.jpg", image)
    cv2.destroyAllWindows()