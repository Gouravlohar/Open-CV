import cv2
img=cv2.imread("../resource/Images/lambo.png")
imggray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("output",imggray)
cv2.imshow("d",img)
cv2.waitKey(0)
