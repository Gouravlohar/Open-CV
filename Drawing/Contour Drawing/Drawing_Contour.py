import cv2
import numpy as np
# Step by Step

# Import Image
image=cv2.imread("shapes.png")

# Converting to Gray Image
img_gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
'''lower: This is the lower threshold for the edge gradient. It determines the minimum intensity gradient required for a 
pixel to be considered as an edge. Pixels with gradients below this threshold are ignored.
upper: This is the upper threshold for the edge gradient. It is used to identify pixels that are likely to be part of an edge. 
If the gradient at a pixel is above this threshold, it is considered a strong edge pixel. Pixels with gradients between the lower 
and upper thresholds are considered weak edge pixels.'''

lower=100
upper=150
canny=cv2.Canny(img_gray,lower,upper)

'''cv2.findContours: This is a function in the OpenCV library used for finding contours in a binary image. 
In this case, it is applied to the result of the Canny edge detection (canny.copy()), which produces a binary image highlighting edges.'''

'''canny.copy(): This creates a copy of the Canny edge detection result. The canny image 
is likely the output of the Canny edge detection algorithm applied to the original image.'''

'''cv2.RETR_EXTERNAL: This is the retrieval mode for contours. It retrieves only the external contours, 
meaning it ignores contours inside other contours.'''

'''cv2.CHAIN_APPROX_NONE: This is the contour approximation method.
 cv2.CHAIN_APPROX_NONE means that all the boundary points of the contours are stored. No approximation is applied.'''
contour,hirar=cv2.findContours(canny.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

'''image.copy(): This creates a copy of the original image. This is done to avoid modifying the original image 
and to draw contours on a separate image (image_copy).

cv2.drawContours: This function is used to draw contours on an image.

image_copy: The image on which contours will be drawn.
contours: The list of contours to be drawn.
-1: This indicates that all contours from the contours list should be drawn.
(0, 255, 0): This is the color of the contours. In this case, it's set to green, specified as (B, G, R).
3: This is the thickness of the contour lines.'''
image_copy=image.copy()
cv2.drawContours(image_copy,contour,-1,(0,255,0),3)

#show everthing
cv2.imshow("Edges",canny)
cv2.imshow("Grayscale",img_gray)
cv2.imshow("Original",image)
cv2.imshow("Contor",image_copy)

'''The cv2.waitKey(0) function is used to wait indefinitely for a key press. When a key is pressed, it returns the ASCII value of that key. 
However, the value returned is a 32-bit integer, and the key information is in the least significant 8 bits.

The & 0xFF operation is a bitwise AND operation with the binary value 0xFF, which is 11111111 in binary. 
This operation helps to keep only the least significant 8 bits of the integer and discard the rest.

In simpler terms, it's used as a mask to ensure that only the lower 8 bits of the key event are considered.
 This is important because sometimes the key value returned by cv2.waitKey() can have additional information in the higher bits, 
 and masking helps to extract only the key information, ensuring compatibility across different platforms.

So, cv2.waitKey(0) & 0xFF essentially extracts the least significant 8 bits of the key event, making it easier 
to compare with ASCII values of specific keys like 'q'.'''

key=cv2.waitKey(0) & 0xFF
if key==ord('q'):
    cv2.destroyAllWindows()
