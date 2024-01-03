import cv2
import numpy as np

image=np.zeros((500,500))

# This will draw  a rectangle
cv2.rectangle(image,(0,0),(250,250),(255,255,255),5)

'''image: The image on which the rectangle will be drawn.
(500, 0): The coordinates of the top-left corner of the rectangle.
(350, 150): The coordinates of the bottom-right corner of the rectangle.
(255, 255, 255): The color of the rectangle in BGR format. Here, it's white because all three channels (blue, green, and red) have the maximum intensity of 255.
-1: The thickness of the rectangle border. In this case, -1 indicates that the rectangle should be filled.'''

# If u want a filled rectangle u can use -1 or cv2.FILLED function
cv2.rectangle(image,(500,0),(350,150),(255,255,255),-1)

cv2.imshow("rectangle",image)
cv2.waitKey(0)


