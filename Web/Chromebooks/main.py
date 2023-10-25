from flask import Flask

app = Flask(__name__)

def makeButton(buttonLabel, buttonXPos, buttonYPos, onclick):
    html_code = f"""
    <button style="position: absolute; left: {buttonXPos}px; top: {buttonYPos}px;" onclick="window.location.href='{onclick}'">{buttonLabel}</button>
    """
    return html_code

@app.route('/')
def index():
    html_content = ''
    
    # Call the render_template_as_string method with arguments
    html_content += makeButton("Hello", buttonXPos=100, buttonYPos=100, onclick="/Hello")
    html_content += makeButton("Bye", buttonXPos=100, buttonYPos=150, onclick="/Bye")
    return html_content

@app.route('/Hello')
def func1():
    html_content = ''
    print("Hello")
    html_content += makeButton("Bye", buttonXPos=100, buttonYPos=100, onclick="/Bye")
    html_content += makeButton("Return", buttonXPos=100, buttonYPos=150, onclick="/")
    return html_content

@app.route('/Bye')
def func2():
    html_content = ''
    print("Bye")
    html_content += makeButton("Hello", buttonXPos=100, buttonYPos=100, onclick="/Hello")
    html_content += makeButton("Return", buttonXPos=100, buttonYPos=150, onclick="/")
    return html_content

if __name__ == '__main__':
    app.run()
