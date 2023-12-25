import cv2
img=cv2.imread("../resource/Images/lambo.png")
blur=cv2.GaussianBlur(img,(87,87),0)
cv2.imshow("Output",blur)
cv2.waitKey(0)