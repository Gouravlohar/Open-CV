import cv2
import numpy as np

image=np.zeros((500,500,3))
# to colur the background we can use below line where first is red green and vlue
image[:]=0,255,0
cv2.imshow("Black",image)
cv2.waitKey(0)
