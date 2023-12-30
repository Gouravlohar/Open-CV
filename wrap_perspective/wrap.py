import cv2
import numpy as np
img=cv2.imread("../resource/Images/cards2.jpg")

width,height=500,500

pts1=np.float32([[705,150],[1124,418],[288,694],[718,994]])

pts2=np.float32([[0,0],[width,0],[0,height],[width,height]])

matrix=cv2.getPerspectiveTransform(pts1,pts2)

image=cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow("wrap",image)
cv2.imshow("card",img)
cv2.waitKey(0)
