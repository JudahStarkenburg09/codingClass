import cv2

cap = cv2.VideoCapture(0)

while True:
    # Read frame from webcam
    ret, frame = cap.read()

    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Mirror the frame horizontally
    gray = cv2.flip(gray, 1)

    # Create a green overlay rectangle with 20% transparency
    overlay = frame.copy()
    h, w = overlay.shape[:2]
    cv2.rectangle(overlay, (0, 0), (w, h), (0, 255, 0), -1)
    alpha = 0.2

    # Merge the grayscale frame and the overlay with transparency
    gray = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
    result = cv2.addWeighted(overlay, alpha, gray, 1 - alpha, 0)

    # Display the final frame
    cv2.imshow('frame', result)

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
