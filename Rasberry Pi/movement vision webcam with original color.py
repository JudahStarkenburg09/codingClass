import cv2
import numpy as np

cap = cv2.VideoCapture(0)
_, frame = cap.read()
height, width, _ = frame.shape
last_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

while True:
    _, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Calculate the difference between the current and previous frame
    frame_diff = cv2.absdiff(last_gray, gray)

    # Apply a threshold to the difference frame to identify movement
    threshold = 20
    _, frame_diff_thresh = cv2.threshold(frame_diff, threshold, 255, cv2.THRESH_BINARY)

    # Blur the thresholded frame to reduce noise
    kernel = np.ones((3,3), np.uint8)
    frame_diff_thresh = cv2.erode(frame_diff_thresh, kernel, iterations=1)
    frame_diff_thresh = cv2.dilate(frame_diff_thresh, kernel, iterations=1)
    frame_diff_thresh = cv2.GaussianBlur(frame_diff_thresh, (5,5), 0)

    # Find contours in the thresholded frame to identify regions of movement
    contours, _ = cv2.findContours(frame_diff_thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Create an empty image for the color overlay
    overlay = np.zeros((height, width, 3), np.uint8)

    # Loop over the contours and draw rectangles around areas of movement
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)

        # Calculate the color based on the amount of movement
        color = (0, 0, 0)
        movement = cv2.countNonZero(frame_diff_thresh[y:y+h, x:x+w])
        if movement > 100:
            if movement < 1000:
                color = (0, 255 - movement // 4, movement // 4)
            else:
                color = (0, 0, 255)

        # Draw the rectangle on the overlay image
        cv2.rectangle(overlay, (x, y), (x + w, y + h), color, -1)

    # Apply the color overlay to the original frame
    alpha = 0.5
    frame = cv2.addWeighted(overlay, alpha, frame, 1 - alpha, 0)

    # Mirror the frame horizontally
    frame = cv2.flip(frame, 1)

    # Show the resulting frame
    cv2.imshow('frame', frame)

    # Update the previous frame
    last_gray = gray

    # Exit on ESC key press
    if cv2.waitKey(1) == 27:
        break

# Clean up
cap.release()
cv2.destroyAllWindows()
