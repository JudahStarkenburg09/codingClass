from flask import Flask, render_template_string, request

app = Flask(__name__)

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
</head>
<body>
    <div class="container">
        <h1>Welcome, {{ name }}!</h1>
        <p>Profile: {{ profile }}</p>
    </div>
</body>
</html>
"""

# Emoji array for profiles
profiles = [
    {"name": "smile", "emoji": "😀"},
    {"name": "sunglasses", "emoji": "😎"},
    {"name": "starry", "emoji": "🤩"},
    {"name": "sad", "emoji": "😟"},
    {"name": "angry", "emoji": "😡"}
]

@app.route('/')
def show_form():
    name = request.args.get('name', '')
    selected_profile = request.args.get('profile', profiles[0]['name'])
    return render_template_string(form_page, profiles=profiles, selected_profile=selected_profile, name=name)

@app.route('/welcome')
def welcome():
    name = request.args.get('name', '')
    profile_name = request.args.get('profile', '')
    profile_emoji = next((profile["emoji"] for profile in profiles if profile["name"] == profile_name), '')
    return render_template_string(welcome_page, name=name, profile=profile_emoji)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=1171, debug=True)
