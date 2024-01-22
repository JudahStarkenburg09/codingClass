from flask import Flask, render_template, Response
import cv2
from email.message import EmailMessage
import ssl
import smtplib
import socket
from datetime import datetime



def sendEmail(link, emails):
    email_sender = 'linuschatbot@gmail.com'
    #code, do not share
    email_password = 'uhnt nlct ujvh cdxu'

    for email in emails:
        email_reciever = email
        now = datetime.now()
        subject = "Your Local Website"
        body = f"""Your local website ip/link address is {link}.
Server was made active at {now.strftime("%d/%m/%Y %H:%M:%S")}
Reply to this email: 'Unsubscribe' and you will be unsubscribe within 5 days
        """

        em = EmailMessage()
        em['From'] = email_sender
        em['To'] = email_reciever
        em['Subject'] = subject
        em.set_content(body)

        thecontext = ssl.create_default_context()

        try:
            with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=thecontext) as smtp:
                smtp.login(email_sender, email_password)
                smtp.sendmail(email_sender, email_reciever, em.as_string())
                print("Email sent successfully!")
        except Exception as e:
            print(f"An error occurred: {e}")


app = Flask(__name__)

# # Try to initialize a webcam. If not available, use the default camera (built-in camera).
# try:
#     cap = cv2.VideoCapture(1)  # Try using the second camera (change if needed)
#     if not cap.isOpened():
#         raise Exception("Webcam not available")
# except Exception as e:
#     print(f"Error: {e}")
#     cap = cv2.VideoCapture(0)  # Fall back to the default camera
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
    private_ip = socket.gethostbyname(socket.gethostname())

    file_name = "email.txt"

    with open(file_name, 'r') as file:
        emailList = file.readlines()

    sendEmail(link=f"{private_ip}:1171", emails=emailList)


    app.run(host='0.0.0.0', port=1171, debug=True)

