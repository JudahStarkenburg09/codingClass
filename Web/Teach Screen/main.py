from flask import Flask, Response, redirect, jsonify
import pygetwindow as gw
import pyautogui
import cv2
import pyWebDev as PWD
import numpy as np

app = Flask(__name__)

html_content = []
bootstrap = {
    "name": "bootstrap",
    "code": """<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">""",
}
html_content.append(bootstrap)

# Set the screen dimensions
screen = gw.getWindowsWithTitle(gw.getActiveWindowTitle())[0]
screen_width, screen_height = screen.size

def generate():
    while True:
        screenshot = pyautogui.screenshot()
        frame = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

        # Get the current mouse cursor position
        mouse_x, mouse_y = pyautogui.position()

        # Get the color of the pixel above the mouse cursor
        above_color = pyautogui.screenshot(region=(mouse_x, mouse_y - 1, 1, 1)).getpixel((0, 0))

        # Calculate the inverse color
        inverse_color = tuple(255 - component for component in above_color)

        # Draw a circle with the inverse color to represent the mouse cursor
        cv2.circle(frame, (mouse_x, mouse_y), 5, inverse_color, -1)

        _, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/')
def onOpen():
    return redirect('/main')

import os

# Add this function to get a list of files in a specific directory
def get_files_in_directory(directory):
    return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

@app.route('/main')
def mainPage():
    global html_content
    keepContent = ["bootstrap"]
    html_content = [i for i in html_content if i["name"] in keepContent]
    bg = {
        "name": "background",
        "code": f"""<div class="p-3 mb-2 bg-dark text-white" style="position: fixed; top: 0; right: 0; bottom: 0; left: 0; z-index: -1;"></div>""",
    }
    html_content.append(bg)
    # Example: Get the current mouse cursor position
    mouse_x, mouse_y = pyautogui.position()

    # Add a box with items inside
    # box = {
    #     "name": "Box",
    #     "code": f"""
    #     <div style="position: fixed; 
    #                 top: 100px; 
    #                 left: 10px; 
    #                 width: 200px; 
    #                 height: 200px; 
    #                 background-color: rgb(40, 40, 50); 
    #                 padding: 10px;
    #                 text-align: center;
    #                 border: 5px solid black;">
    #         <h3 style="color: rgb(200,200,200);">Files</h3>
    #         <ul>
    #             {generate_file_links()}
    #         </ul>
    #     </div>
    #     """
    # }
    box = {
        "name": "Box",
        "code": f"""
        <div style="position: fixed; 
                    top: 100px; 
                    left: 10px; 
                    width: 200px; 
                    height: 210px; 
                    background-color: rgb(40, 40, 50);  /* Background color */
                    border: 5px solid black;
                    padding: 10px;
                    text-align: center;
                    overflow: hidden; /* Ensure that the box doesn't expand beyond the specified height */
                    ">
            <h3 style="color: rgb(200, 200, 200);">Files</h3>  <!-- Text color -->
            <ul style="list-style: none; padding: 0; overflow-y: auto; max-height: 150px;">  <!-- Enable scrolling -->
                {generate_file_links()}
            </ul>
        </div>
        """
    }



    html_content.append(box)

    videoFeed = {
        "name": "Video",
        "code": f"""
        <body>
            <div style="position: fixed; top: 0; left: 50%; transform: translateX(-50%); border: 5px solid black;">
                <img src="/video_feed?posx={mouse_x}&posy={mouse_y}" width="{screen_width-screen_width/3}" height="{screen_height-screen_height/3}" />
            </div>
        </body>"""
    }
    html_content.append(videoFeed)

    html_content.append(PWD.make_button(label="Enter Fullscreen", name="Fullscreen", x_pos=45, y_pos=35, class_type="btn btn-primary", onclick='/main-fullscreen'))

    index = """"""
    for i in html_content:
        index += str(i["code"])

    return index

def generate_file_links():
    directory = "files"  # Change this to your directory containing the files
    files = get_files_in_directory(directory)
    file_links = ""
    for file in files:
        file_links += f'<li style="color: rgb(100, 100, 100);"><a href="/download/{file}" style="color: rgb(200, 200, 200);" download>{file}</a></li>'
    return file_links



# Add a route for file download
@app.route('/download/<filename>')
def download_file(filename):
    directory = "files"  # Change this to your directory containing the files
    return send_from_directory(directory, filename)

# Import the necessary module for sending files dynamically
from flask import send_from_directory



from flask import render_template_string

@app.route('/main-fullscreen')
def fullscreenMode():
    global html_content
    keepContent = ["bootstrap"]
    html_content = [i for i in html_content if i["name"] in keepContent]
    bg = {
        "name": "background",
        "code": f"""<div class="p-3 mb-2 bg-dark text-white" style="position: fixed; top: 0; right: 0; bottom: 0; left: 0; z-index: -1;"></div>""",
    }
    html_content.append(bg)

    # Example: Get the current mouse cursor position
    mouse_x, mouse_y = pyautogui.position()

    videoFeed = {
        "name": "Video",
        "code": f"""
        <body>
            <div id="fullscreenMessage" style="position: fixed; top: 50%; left: 50%; transform: translate(-50%, -50%); text-align: center;">
                <p style="color: white;">Press F11 to enter fullscreen mode</p>
            </div>
            <div style="position: fixed; top: 0; left: 50%; transform: translateX(-50%); border: 5px solid black;">
                <img src="/video_feed?posx={mouse_x}&posy={mouse_y}" width="{screen_width}" height="{screen_height}" />
            </div>
            <script>
                // Function to hide the fullscreen message
                function hideFullscreenMessage() {{
                    var fullscreenMessage = document.getElementById('fullscreenMessage');
                    fullscreenMessage.style.display = 'none';
                }}

                // Detect fullscreen change event
                document.addEventListener('fullscreenchange', function () {{
                    if (document.fullscreenElement) {{
                        // Entered fullscreen
                        hideFullscreenMessage();
                    }}
                }});
            </script>
        </body>"""
    }
    html_content.append(videoFeed)
    return render_template_string(''.join([i["code"] for i in html_content]))




@app.route('/video_feed')
def video_feed():
    return Response(generate(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
