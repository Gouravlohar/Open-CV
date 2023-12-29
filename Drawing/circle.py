import cv2
import numpy as np

img=np.zeros((500,500))

# circle will take origin and radius only
cv2.circle(img,(250,250),120,(255,255,255),5)
cv2.circle(img,(250,250),100,(255,255,255),cv2.FILLED)

cv2.imshow("Circle",img)
cv2.waitKey(0)
