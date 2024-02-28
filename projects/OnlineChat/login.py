from flask import Flask, render_template_string, request, session

app = Flask(__name__)

# Set the secret key to enable session in Flask
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

# HTML content for the form page
form_page = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Enter Your Name</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
    <style>
        .image-container {
            display: flex;
            align-items: center;
        }
        .image-container img {
            margin-right: 10px;
            cursor: pointer; /* Add pointer cursor to indicate clickable */
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Enter Your Name</h1>
        <form method="GET" action="/welcome?name={{ name }}&profile={{ profile_picture }}">
            <div class="mb-3 image-container">
                <img id="profile_pic" src="/static/{{ profile_picture }}" alt="Profile Picture" onclick="changeProfile()"> <!-- Set the ID of the image tag -->
                <label for="name" class="form-label">Name:</label>
                <input type="text" class="form-control" id="name" name="name" value="{{ name }}" required>
                <input type="hidden" class="form-control" id="name" name="profile" value="{{ profile_picture }}">
            </div>
            <button type="submit" class="btn btn-primary">Submit</button>
        </form>
    </div>
    
    <script>
        function changeProfile() {
            window.location.href = '/profile?profile={{ profile_picture }}&name={{ name }}';
        }
    </script>
</body>
</html>
"""

# HTML content for the welcome page
welcome_page = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Welcome</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
</head>
<body>
    <div class="container">
        <h1>Welcome, {{ name }}!</h1>
        <img src="/static/{{ profile_picture }}" alt="Profile Picture">
    </div>
</body>
</html>
"""

# HTML content for the profile page (unchanged)
profile_page = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Profile</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
    <style>
        .image-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(50px, 1fr));
            grid-gap: 10px;
        }
        .image-grid img {
            width: 100%;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Profile Page</h1>
        <p>Select your profile picture:</p>
        <div class="image-grid">
            {% for image in images %}
                <a href="#" onclick="selectProfilePicture('{{ image }}')">
                    <img src="/static/{{ image }}" alt="{{ image }}">
                </a>
            {% endfor %}
        </div>
        <a href="/"> <!-- Add a "Done!" button to return to the enter your name page -->
            <br>
            <button class="btn btn-primary">Done!</button>
        </a>
    </div>
    
    <script>
        function selectProfilePicture(image) {
            // Send an AJAX request to the server to update the user's profile picture
            fetch('/update_profile_picture', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ image: image }),
            }).then(() => {
                // After updating the profile picture, redirect to the enter your name page
                window.location.href = '/?profile=' + image + '&name={{ name }}';
            });
        }
    </script>
</body>
</html>
"""

import os
# Updated list of profile pictures
files = os.listdir('static')

# Filter out only the PNG files
profile_pictures = [file for file in files if file.endswith('.png')]


@app.route('/')
def show_form():
    profile_picture = request.args.get('profile', 'smile.png')
    name = request.args.get('name', '')
    return render_template_string(form_page, profile_picture=profile_picture, name=name)

@app.route('/welcome')
def welcome():
    name = request.args.get('name', '')
    profile_picture = request.args.get('profile', 'smile.png')
    return render_template_string(welcome_page, name=name, profile_picture=profile_picture)

@app.route('/profile')
def show_profile():
    name = request.args.get('name', '')
    return render_template_string(profile_page, images=profile_pictures, name=name)

@app.route('/update_profile_picture', methods=['POST'])
def update_profile_picture():
    data = request.json
    selected_image = data.get('image')

    # Store the selected profile picture in the session
    session['profile_picture'] = selected_image

    return '', 204  # Empty response with status code 204

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=1171, debug=True)
