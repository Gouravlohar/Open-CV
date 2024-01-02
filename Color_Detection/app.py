import cv2
import numpy as np
'''
The code def empty(a): pass defines a Python function named empty that takes one parameter a but does nothing 
when called. The pass statement is a no-operation statement in Python;
 it serves as a placeholder where syntactically some code is required but no action is desired or necessary.
'''
def empty(a):
    pass


# the cv2.namedWindow() function. This function is used to create a resizable window to display images or graphical
# interfaces in OpenCV applications.
cv2.namedWindow("Trackbars")

'''
the cv2.resizeWindow('My Image Window', 600, 400) line resizes the window named 
'My Image Window' to have a width of 600 pixels and a height 
of 400 pixels. Adjust the size as needed for your specific requirements.
'''
cv2.resizeWindow("Trackbars",640,240)

"""
In OpenCV, the cv2.createTrackbar() function is used to create a trackbar (slider) that allows you to 
interactively adjust a value. This is often used for parameter tuning or any scenario where you want 
to dynamically adjust a variable using a graphical user interface.
"""
cv2.createTrackbar("Hue Min", "Trackbars", 0, 179, empty)
cv2.createTrackbar("Hue Max", "Trackbars", 179, 179, empty)
cv2.createTrackbar("Sat Min", "Trackbars", 0, 255, empty)
cv2.createTrackbar("Sat Max", "Trackbars", 255, 255, empty)
cv2.createTrackbar("Val Min", "Trackbars", 0, 255, empty)
cv2.createTrackbar("Val Max", "Trackbars", 255, 255, empty)

while True:
    image=cv2.imread("../resource/Images/lambo.png")

    imgHSV=cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    h_min=cv2.getTrackbarPos("Hue Min", "Trackbars")
    h_max=cv2.getTrackbarPos("Hue Max", "Trackbars")
    s_min=cv2.getTrackbarPos("Sat Min", "Trackbars")
    s_max=cv2.getTrackbarPos("Sat Max", "Trackbars")
    v_min=cv2.getTrackbarPos("Val Min", "Trackbars")
    v_max=cv2.getTrackbarPos("Val Max", "Trackbars")

    print(h_min, h_max, s_min, s_max, v_min, v_max)
    lower=np.array([h_min, s_min, v_min])
    upper=np.array([h_max, s_max, v_max])

    mask=cv2.inRange(imgHSV, lower, upper)

    cv2.imshow("Original Image", image)

    cv2.imshow("HSV Image", imgHSV)

    cv2.imshow("Mask Image", mask)
    cv2.waitKey(1)



