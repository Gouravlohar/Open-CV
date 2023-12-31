import cv2
import numpy as np

'''Joining of Images will only work if it have same 
1) Shape
2) Color'''
# import first image
img1=cv2.imread("../resource/Images/cards.jpg")
print("image1",img1.shape)

# Resizing this for full the criteria
# import Second Image
img2=cv2.imread("../resource/Images/car.jpg")
resize_img2=cv2.resize(img2,(477,500))
print("image2",resize_img2)

'''To join images horizontally we will use 
np.hstack
and for vertical we will use
np.vstack'''
horizontal=np.hstack((img1,resize_img2))
vertical=np.vstack((img1,resize_img2))

cv2.imshow("1",horizontal)
cv2.imshow("2",vertical)

cv2.waitKey(0)
