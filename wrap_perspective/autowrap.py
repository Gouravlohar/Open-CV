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
        # Append the clicked point to the list
        pts1.append([x, y])
        # Draw a circle at the clicked point for visualization
        cv2.circle(img, (x, y), 5, (0, 255, 0), -1)
        # Display the image with the clicked point
        cv2.imshow("Image", img)

# Set the window name
cv2.namedWindow("Image")

# Set the mouse callback function
cv2.setMouseCallback("Image", mouse_callback)

# Display the image and wait for the user to click points
cv2.imshow("Image", img)
cv2.waitKey(0)

# Convert the list of points to a NumPy array
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
