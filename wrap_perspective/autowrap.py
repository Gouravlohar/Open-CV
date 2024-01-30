import cv2
import numpy as np

# Define the image path
img_path = "../resource/Images/cards.jpg"

# Read the image
img = cv2.imread(img_path)

# Set the desired width and height for the output image
width, height = 500, 500

# Create an empty list to store the measured points
pts1 = []

# Callback function for mouse events
def mouse_callback(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        
        pts1.append([x, y])
        
        cv2.circle(img, (x, y), 5, (0, 255, 0), -1)
        
        cv2.imshow("Image", img)

# Set the window name
cv2.namedWindow("Image")


cv2.setMouseCallback("Image", mouse_callback)


cv2.imshow("Image", img)
cv2.waitKey(0)

pts1 = np.float32(pts1)

# Define the destination points for perspective transformation
pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])

# Calculate the perspective transformation matrix
matrix = cv2.getPerspectiveTransform(pts1, pts2)

# Apply the perspective transformation to the image
image = cv2.warpPerspective(img, matrix, (width, height))

# Display the transformed image
cv2.imshow("Transformed Image", image)
cv2.waitKey(0)

# Close all OpenCV windows
cv2.destroyAllWindows()
