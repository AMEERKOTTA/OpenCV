import cv2

image = cv2.imread("H:\Files For Projects\Pictures\Bill Gates.jpg",1)
image = cv2.resize(image,(500,500))

k = cv2.waitKey(0)
if k == ord("s"):
    cv2.imwrite("Saved Image.jpg", image)
    print("New Image is saved Succesfully")
    cv2.destroyAllWindows()

elif k == 27:
    cv2.destroyAllWindows()