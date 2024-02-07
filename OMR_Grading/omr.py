import cv2
import numpy as np

image=cv2.imread("Images/my4.PNG")
height=700
weight=700
image=cv2.resize(image,(height,weight))

def preimage(image):
    gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    gaussian_blur=cv2.GaussianBlur(gray,(5,5),1)
    lower=10
    higher=100
    edge=cv2.Canny(gaussian_blur,lower,higher)
    return edge
final=preimage(image)

cv2.imshow("Black&White",final)

cv2.imshow("Output",image)
cv2.waitKey(0)