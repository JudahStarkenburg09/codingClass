import cv2

cap = cv2.VideoCapture(0)

while True:
    # Read frame from webcam
    ret, frame = cap.read()

    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Mirror the frame horizontally
    gray = cv2.flip(gray, 1)

    # Display mirrored grayscale frame
    cv2.imshow('frame', gray)

    # Exit on ESC key press
    if cv2.waitKey(1) == 27:
        break

# Clean up
cap.release()
cv2.destroyAllWindows()
