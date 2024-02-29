from flask import Flask, render_template_string, request
from flask_socketio import SocketIO, emit

from flask import Flask, render_template_string, request
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, async_mode='threading')  # Specify a valid async mode here


# HTML content for the form page
form_page = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Enter Your Name</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
</head>
<body>
    <div class="container">
        <h1>Enter Your Name</h1>
        <form method="GET" action="/welcome">
            <div class="mb-3">
                <label for="name" class="form-label">Name:</label>
                <input type="text" class="form-control" id="name" name="name" value="{{ name }}" required>
            </div>
            <div class="mb-3">
                <label for="profile" class="form-label">Select Profile:</label>
                <select class="form-select" name="profile" id="profile">
                    {% for profile in profiles %}
                        <option value="{{ profile['name'] }}" {% if profile['name'] == selected_profile %}selected{% endif %}>{{ profile['emoji'] }} {{ profile['name'] }}</option>
                    {% endfor %}
                </select>
            </div>
            <button type="submit" class="btn btn-primary">Submit</button>
        </form>
    </div>
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
    <style>
        .chat-message {
            margin-bottom: 10px;
        }
        .user-message {
            color: blue;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Welcome, {{ name }}!</h1>
        <div id="chat-messages" style="overflow-y: scroll; height: 300px;"></div>
        {% if name not in bad_list %}
        <form onsubmit="sendMessage(event)">
            <div class="mb-3">
                <label for="message-input" class="form-label">Message:</label>
                <input type="text" class="form-control" id="message-input" required>
            </div>
            <button type="submit" class="btn btn-primary">Send</button>
        </form>
        {% else %}
        <p>You are not allowed to send messages.</p>
        {% endif %}
    </div>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/socket.io/4.3.2/socket.io.js"></script>
    <script type="text/javascript" charset="utf-8">
        var socket = io.connect('http://' + document.domain + ':' + location.port);
        
        // Pass bad_list and name to JavaScript variables
        var badList = {{ bad_list|tojson }};
        var name = "{{ name }}";

        socket.on('connect', function() {
            socket.emit('new_user', { name: name, profile: "{{ profile }}" });
        });

        socket.on('user_joined', function(data) {
            var joinMessage = document.createElement('div');
            joinMessage.classList.add('chat-message');
            joinMessage.innerHTML = '<em>' + data.name + ' joined the chat!</em>';
            document.getElementById('chat-messages').appendChild(joinMessage);
            // Scroll to bottom
            document.getElementById('chat-messages').scrollTop = document.getElementById('chat-messages').scrollHeight;
        });

        socket.on('new_message', function(data) {
            var chatMessage = document.createElement('div');
            chatMessage.classList.add('chat-message');
            if (data.name === name) {
                chatMessage.classList.add('user-message');
            }
            chatMessage.innerHTML = '<strong>' + data.name + '</strong>: ' + data.message;
            document.getElementById('chat-messages').appendChild(chatMessage);
            // Scroll to bottom
            document.getElementById('chat-messages').scrollTop = document.getElementById('chat-messages').scrollHeight;
        });

        function sendMessage(event) {
            event.preventDefault();
            var message = document.getElementById('message-input').value;
            document.getElementById('message-input').value = '';
            socket.emit('new_message', { name: name, message: message, profile: "{{ profile }}" });
        }
    </script>
</body>
</html>

"""


# Emoji array for profiles
# profiles = [
#     {"name": "smile", "emoji": "😀"},
#     {"name": "sunglasses", "emoji": "😎"},
#     {"name": "starry", "emoji": "🤩"},
#     {"name": "sad", "emoji": "😟"},
#     {"name": "angry", "emoji": "😡"}
# ]

import json

# Initialize the profiles variable
profiles = None

# File path of the JSON file
file_path = 'profiles.json'

# Read the JSON file and store its content in the profiles variable
with open(file_path, 'r', encoding='utf-8') as json_file:
    profiles = json.load(json_file)

# Now the profiles variable holds the content of the JSON file
print(profiles)




@app.route('/')
def show_form():
    name = request.args.get('name', '')
    selected_profile = request.args.get('profile', profiles[0]['name'])
    return render_template_string(form_page, profiles=profiles, selected_profile=selected_profile, name=name)


@app.route('/welcome')
def welcome():
    global bad_list
    name = request.args.get('name', '')
    profile = request.args.get('profile', '')
    print(profiles)
    equals = True
    for i in profiles:
        if i["name"] != profile and equals:
            equals = False
    if equals:
        profile = "smile"
    return render_template_string(welcome_page, name=name, profile=profile, bad_list=bad_list)



@socketio.on('new_user')
def handle_new_user(user_data):
    name = user_data['name']
    emit('user_joined', {'name': name}, broadcast=True)

import termcolor

@socketio.on('new_message')
def handle_message(message_data):
    profilePic = message_data.get('profile', '')
    name = message_data.get('name', '')
    message = message_data['message']
    profile_emoji = next((profile["emoji"] for profile in profiles if profile["name"] == profilePic), '')

    if name not in bad_list:  # Check if the user is not in the bad list
        emit('new_message', {'name': f"{profile_emoji} {name}", 'message': message}, broadcast=True)
        print(f"{termcolor.colored(name, 'blue')}: {termcolor.colored(message, 'green')}")

    else:
        emit('new_message', {'name': 'Admin', 'message': f"You are not allowed to send messages! Please talk to your admin if you think this is a mistake. (Only you can see this text)"})  # Inform the user
        print(f"{termcolor.colored(name, 'blue')}: {termcolor.colored(message, 'yellow')} - {termcolor.colored('[Blocked!]', 'red', attrs=['dark', 'bold'])}")




import random
import string
from termcolor import cprint

# Function to generate a random access code
def generate_access_code():
    # Generate 2 random digits
    digits = ''.join(random.choices(string.digits, k=2))
    # Generate a random letter (uppercase or lowercase)
    letter = random.choice(string.ascii_letters)
    # Concatenate digits and letter to form the access code
    access_code = digits + letter
    return access_code

# Generate a new access code
access_code = generate_access_code()
cprint("-----------------------------------", 'red')
cprint(f"Access Code: {access_code}", "red")  # Print the access code
cprint("-----------------------------------", 'red')


# HTML content for the admin page
admin_page = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Admin Page</title>
</head>
<body>
    <h1>Welcome to the Admin Page</h1>
    <form method="POST" action="/admin">
        <label for="access-code">Enter Access Code:</label><br>
        <input type="text" id="access-code" name="access_code"><br>
        <input type="submit" value="Submit">
    </form>
</body>
</html>
"""

adminSuccessPage = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Welcome</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
    <style>
        .chat-message {
            margin-bottom: 10px;
        }
        .user-message {
            color: blue;
        }
        a.clickable {
            color: blue;
            text-decoration: underline;
            cursor: pointer;
            position: relative; /* Ensures the hover text is positioned relative to the clickable element */
        }

        a.clickable::after {
            content: "Permenant Ban"; /* Replace "Hover text" with the text you want to display */
            position: absolute;
            top: 100%; /* Position the hover text just below the clickable element */
            left: 0;
            background-color: #f9f9f9; /* Background color of the hover text */
            border: 1px solid #ccc; /* Border of the hover text */
            padding: 5px; /* Padding around the hover text */
            border-radius: 5px; /* Border radius for rounded corners */
            display: none; /* Hide the hover text by default */
        }

        a.clickable:hover::after {
            display: block; /* Display the hover text when the user hovers over the clickable element */
        }

    </style>
</head>
<body>
    <div class="container">
        <h1>Welcome, Admin!</h1>
        <div id="chat-messages" style="overflow-y: scroll; height: 300px;"></div>
        <form onsubmit="sendMessage(event)">
            <div class="mb-3">
                <label for="message-input" class="form-label">Message:</label>
                <input type="text" class="form-control" id="message-input" required>
            </div>
            <button type="submit" class="btn btn-primary">Send</button>
        </form>
    </div>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/socket.io/4.3.2/socket.io.js"></script>
    <script type="text/javascript" charset="utf-8">
        var socket = io.connect('http://' + document.domain + ':' + location.port);

        socket.on('user_joined', function(data) {
            var joinMessage = document.createElement('div');
            joinMessage.classList.add('chat-message');
            joinMessage.innerHTML = '<em>' + data.name + ' joined the chat!</em>';
            document.getElementById('chat-messages').appendChild(joinMessage);
            // Scroll to bottom
            document.getElementById('chat-messages').scrollTop = document.getElementById('chat-messages').scrollHeight;
        });

        socket.on('new_message', function(data) {
            var chatMessage = document.createElement('div');
            chatMessage.classList.add('chat-message');
            if (data.name === "Admin") {
                chatMessage.classList.add('user-message');
            }
            chatMessage.innerHTML = `<a class="clickable" onClick="sayHi('${data.name}')"><strong>` + data.name + '</strong></a>: ' + data.message;
            document.getElementById('chat-messages').appendChild(chatMessage);
            // Scroll to bottom
            document.getElementById('chat-messages').scrollTop = document.getElementById('chat-messages').scrollHeight;
        });

        function sayHi(n) {
            socket.emit('add_to_bad_list', { name: n });
        }

        function sendMessage(event) {
            event.preventDefault();
            var message = document.getElementById('message-input').value;
            document.getElementById('message-input').value = '';
            socket.emit('new_message', { name: "Admin", message: message, profile: "👤" });
        }
    </script>
</body>
</html>
"""


# Route for the admin page
@app.route('/admin', methods=['GET', 'POST'])
def admin():
    global access_code  # Use the global access code variable

    # Check if the form is submitted
    if request.method == 'POST':
        # Get the access code entered by the user
        entered_code = request.form.get('access_code', '')
        # Check if the entered code matches the generated access code
        if entered_code == access_code:
            return adminSuccessPage
        else:
            return "<h1>Incorrect access code.</h1>"

    return render_template_string(admin_page)
 
bad_list = []
@socketio.on('add_to_bad_list')
def add_to_bad_list(data):
    global bad_list
    name = data.get('name', '')
    if name:
        bad_list.append(str(name[2:]))
        print("Bad list:", bad_list)  # Print or log the bad list
        # You can perform other actions here, such as sending the bad list to the client

if __name__ == '__main__':
    socketio.run(app, host="0.0.0.0", port=2447, debug=True)