from flask import Flask, render_template_string, request, session
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

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
        <form onsubmit="handleForm(event)">
            <div class="mb-3">
                <label for="name" class="form-label">Name:</label>
                <input type="text" class="form-control" id="name" name="name" required>
            </div>
            <button type="submit" class="btn btn-primary">Submit</button>
        </form>
    </div>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/socket.io/4.3.2/socket.io.js"></script>
    <script type="text/javascript" charset="utf-8">
        var socket = io.connect('http://' + document.domain + ':' + location.port);

        function handleForm(event) {
            event.preventDefault();
            var name = document.getElementById('name').value;
            socket.emit('new_user', { name: name });
            window.location.href = "/welcome?name=" + encodeURIComponent(name);
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

        socket.on('connect', function() {
            socket.emit('new_user', { name: "{{ name }}" });
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
            if (data.name === "{{ name }}") {
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
            socket.emit('new_message', { name: "{{ name }}", message: message });
        }
    </script>
</body>
</html>
"""

@app.route('/')
def show_form():
    return render_template_string(form_page)

@app.route('/welcome')
def welcome():
    name = request.args.get('name', '')
    return render_template_string(welcome_page, name=name)

@socketio.on('new_user')
def handle_new_user(user_data):
    name = user_data['name']
    emit('user_joined', {'name': name}, broadcast=True)

@socketio.on('new_message')
def handle_message(message_data):
    name = message_data.get('name', '')
    message = message_data['message']
    emit('new_message', {'name': name, 'message': message}, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, host="0.0.0.0", port=1171, debug=True)
