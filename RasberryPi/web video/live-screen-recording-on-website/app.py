from flask import Flask, render_template, Response, request, jsonify
import time

# Import try-except block for notification handling
try:
    from plyer import notification
except ImportError:
    print("Plyer library not installed. Install it using 'pip install plyer'.")

import cv2
import pygetwindow as gw
import pyautogui
import numpy as np

app = Flask(__name__)

# Set the screen dimensions
screen = gw.getWindowsWithTitle(gw.getActiveWindowTitle())[0]
screen_width, screen_height = screen.size

# Set the minimum time between notifications in seconds
MIN_NOTIFICATION_INTERVAL = 10
last_notification_time = 0

def generate():
    while True:
        screenshot = pyautogui.screenshot()
        frame = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

        # Get the current mouse cursor position
        mouse_x, mouse_y = pyautogui.position()

        # Draw a red circle to represent the mouse cursor
        cv2.circle(frame, (mouse_x, mouse_y), 5, (0, 0, 255), -1)

        _, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@app.route('/')
def index():
    return render_template('index.html', screen_width=screen_width, screen_height=screen_height)

@app.route('/video_feed')
def video_feed():
    return Response(generate(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/send_notification', methods=['POST'])
def send_notification():
    global last_notification_time
    current_time = time.time()

    # Check if the time since the last notification is greater than the minimum interval
    if current_time - last_notification_time < MIN_NOTIFICATION_INTERVAL:
        return jsonify({'error': 'Too many requests. Please wait before sending another message.'}), 429

    data = request.get_json()
    message = data.get('message', '')

    # Display the message as a notification
    try:
        notification.notify(
            title='New Message',
            message=message,
            app_icon=None,  # e.g., 'C:\\icon_32x32.ico'
            timeout=4,  # seconds
        )
    except Exception as e:
        print(f"Error displaying notification: {e}")

    last_notification_time = current_time  # Update the last notification time

    return '', 204

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
