import cv2
import numpy as np

image=np.zeros((500,500,3))
# to colur the background we can use below line where first is red green and vlue
image[:]=0,255,0

# 250 in x axis and 0 in y axis and 250 in x axis and 500 in y axis
cv2.line(image,(250,0),(250,500),(0,0,255),3)



cv2.imshow("Black",image)
cv2.waitKey(0)
