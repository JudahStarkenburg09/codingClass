from flask import Flask, render_template, Response
import cv2

app = Flask(__name__)

# Try to initialize a webcam. If not available, use the default camera (built-in camera).
try:
    cap = cv2.VideoCapture(1)  # Try using the second camera (change if needed)
    if not cap.isOpened():
        raise Exception("Webcam not available")
except Exception as e:
    print(f"Error: {e}")
    cap = cv2.VideoCapture(0)  # Fall back to the default camera

def generate():
    while True:
        ret, frame = cap.read()
        _, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(generate(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
