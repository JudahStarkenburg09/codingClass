import cv2
import numpy as np

cap = cv2.VideoCapture(0)
_, frame = cap.read()
height, width, _ = frame.shape
last_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# Create a background subtractor object
backSub = cv2.createBackgroundSubtractorMOG2()

# Set the threshold value to 90% of the maximum pixel value
threshold_value = int(0.9 * 255)

while True:
    _, frame = cap.read()

    # Apply background subtraction
    fgMask = backSub.apply(frame)

    # Apply erosion and dilation to remove noise
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    fgMask = cv2.erode(fgMask, kernel, iterations=1)
    fgMask = cv2.dilate(fgMask, kernel, iterations=1)

    # Apply threshold to convert the gray scale mask to binary
    _, thresh = cv2.threshold(fgMask, threshold_value, 255, cv2.THRESH_BINARY)

    # Find contours in the thresholded frame to identify regions of movement
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Create an empty image for the color overlay
    overlay = np.zeros((height, width, 3), np.uint8)

    # Loop over the contours and draw rectangles around areas of movement
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)

        # Calculate the color based on the amount of movement
        movement = cv2.countNonZero(thresh[y:y+h, x:x+w])
        color = (0, 0, 0)
        if movement > 200:
            if movement > 1000:
                movement = 1000
            color = (0, movement/3, movement/4)

        # Draw the rectangle on the overlay image
        cv2.rectangle(overlay, (x, y), (x + w, y + h), color, -1)

    # Apply the color overlay to the original frame
    alpha = 0.5
    frame = cv2.addWeighted(overlay, alpha, frame, 1 - alpha, 0)

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

    # Use the thresholded mask to copy the moving pixels to the blank image
    frame = cv2.bitwise_and(frame, frame, mask=thresh)

    # Show the resulting frame
    cv2.imshow('frame', frame)

    # Exit on ESC key press or if window is closed
    if cv2.waitKey(1) == 27 or cv2.getWindowProperty('frame', cv2.WND_PROP_VISIBLE) < 1:
        break

    # Update the previous frame
    last_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# Clean up
cap.release()
cv2.destroyAllWindows()
