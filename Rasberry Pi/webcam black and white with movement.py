import cv2

cap = cv2.VideoCapture(0)

# Initialize variables
alpha = 0.2
last_gray = None

while True:
    # Read frame from webcam
    ret, frame = cap.read()

    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Mirror the frame horizontally
    gray = cv2.flip(gray, 1)

    # Calculate the difference between the current frame and the last frame
    if last_gray is not None:
        frame_diff = cv2.absdiff(last_gray, gray)
        thresh = cv2.threshold(frame_diff, 30, 255, cv2.THRESH_BINARY)[1]
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Draw colored rectangles on the addedColor frame
        addedColor = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
        for contour in contours:
            (x, y, w, h) = cv2.boundingRect(contour)
            color = (0, 0, 255)
            cv2.rectangle(addedColor, (x, y), (x + w, y + h), color, 2)

        # Resize the addedColor to match the size of overlay
        overlay = cv2.resize(addedColor, (frame.shape[1], frame.shape[0]))

        # Merge the grayscale frame and the overlay with transparency
        result = cv2.addWeighted(overlay, alpha, frame, 1 - alpha, 0)

        # Display the final frame
        cv2.imshow('frame', result)

    # Update the last_gray variable
    last_gray = gray.copy()

    # Exit if window is closed
    if not cap.isOpened():
        break

    # # Exit on ESC key press or if window is closed
    # key = cv2.waitKey(1)
    # if key == 27 or cv2.getWindowProperty('frame', cv2.WND_PROP_VISIBLE) < 1:
    #     break

# Clean up
cap.release()
cv2.destroyAllWindows()
