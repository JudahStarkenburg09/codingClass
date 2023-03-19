import cv2
import numpy as np

cap = cv2.VideoCapture(0)

# Create a background subtractor object
backSub = cv2.createBackgroundSubtractorMOG2()

# Set the threshold value to 90% of the maximum pixel value
threshold_value = int(0.999999 * 255)

while True:
    # Read frame from webcam
    ret, frame = cap.read()

    # Flip the frame horizontally
    frame = cv2.flip(frame, 1)

    # Apply background subtraction
    fgMask = backSub.apply(frame)

    # Apply erosion and dilation to remove noise
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    fgMask = cv2.erode(fgMask, kernel, iterations=1)
    fgMask = cv2.dilate(fgMask, kernel, iterations=1)

    # Apply threshold to convert the gray scale mask to binary
    _, thresh = cv2.threshold(fgMask, threshold_value, 255, cv2.THRESH_BINARY)

    # Create a blank image with the same dimensions as the frame
    blank = np.zeros_like(frame)

    # Use the thresholded mask to copy the moving pixels to the blank image
    movingObjects = cv2.bitwise_and(frame, frame, mask=thresh)

    # Display the final frame
    cv2.imshow('frame', movingObjects)

    # Exit if window is closed
    if not cap.isOpened():
        break

    # Exit on ESC key press or if window is closed
    key = cv2.waitKey(1)
    if key == 27 or cv2.getWindowProperty('frame', cv2.WND_PROP_VISIBLE) < 1:
        break

# Clean up
cap.release()
cv2.destroyAllWindows()
