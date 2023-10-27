from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('your_template.html')

@app.route('/process_data', methods=['POST'])
def process_data():
    user_input = request.form['user_input']
    # Now you can access the user's input in the 'user_input' variable
    return f'User input: {user_input}'

if __name__ == '__main__':
    app.run()
