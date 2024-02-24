import cv2

def play_video(video_path):
    # Open the video file
    cap = cv2.VideoCapture(video_path)

    # Check if the video file was successfully opened
    if not cap.isOpened():
        print("Error: Could not open video file")
        return

    # Create a background subtractor object
    bg_subtractor = cv2.createBackgroundSubtractorMOG2()

    # Read and display the video frame by frame
    while True:
        # Read the current frame
        ret, frame = cap.read()
        if not ret:
            break

        # Apply background subtraction to detect moving objects
        fg_mask = bg_subtractor.apply(frame)

        # Find contours of moving objects
        contours, _ = cv2.findContours(fg_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Check if contours were found
        if contours:
            # Find the contour with the largest area (presumably the Minecraft zombie)
            max_contour = max(contours, key=cv2.contourArea)

            # Create a bounding box around the largest contour
            x, y, w, h = cv2.boundingRect(max_contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), thickness=2)

            # Print the height of the rectangle
            print("Height of the rectangle:", h)

        # Display the frame with the bounding box around the moving object
        cv2.imshow('Video', frame)

        # Wait for a short duration and check for key press to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):  # Change delay to 1 millisecond
            break

    # Release the video capture object and close all windows
    cap.release()
    cv2.destroyAllWindows()

# Example usage
video_path = 'video.mp4'  # Replace 'video.mp4' with your video file name
play_video(video_path)
