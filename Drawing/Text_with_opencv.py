import cv2
import numpy as np
img=np.zeros((500,500))

'''to write text in any image we will use cv2.putText() inside this function
first the variable where image is stored,what u want ot write,origin,font,scale,color,thickness'''
cv2.putText(img,"Gourav",(100,250),cv2.FONT_HERSHEY_SIMPLEX,3,(255,255,255),3)

cv2.imshow("Text",img)
cv2.waitKey(0)
