import cv2

def take_picture():
    # Open the camera
    cap = cv2.VideoCapture(0)

    # Check if the camera is opened successfully
    if not cap.isOpened():
        print("Failed to open the camera")
        return

    # Capture a frame from the camera
    ret, frame = cap.read()

    # Release the camera
    cap.release()

    # Check if the frame was captured successfully
    if not ret:
        print("Failed to capture frame")
        return

    # Save the captured frame as an image file
    cv2.imwrite("profile.jpg", frame)

# Call the function to take a picture
take_picture()
