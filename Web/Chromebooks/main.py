from flask import Flask, request
import pyWebDev as PWD

app = Flask(__name__)

# https://getbootstrap.com/docs/5.3/getting-started/introduction/

@app.route('/')
def index():
    global dropArray
    html_content = """<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">"""
    html_content += """"""
    # Call the render_template_as_string method with arguments
    html_content += PWD.createDropdown('btn btn-secondary dropdown-toggle', dropArray)
    html_content += PWD.makeButton("Hello", buttonXPos=100, buttonYPos=100, onclick="/Hello", classType="btn btn-outline-primary")
    html_content += PWD.makeText("Click me", posx=50, posy=50, link="/Hello", underlined=True, color="#FF0000", fontSize=20)
    html_content += PWD.makeEntryBox("entryBox1", "Type here", posx=50, posy=200, actionFunction="/Hello", buttonPosX=400, buttonPosY=100, buttonText="Submit123")
    html_content += PWD.createImage("NCASymbol.png", posX=500, posY=300)
    return html_content

@app.route('/Hello', methods=['GET', 'POST'])
def changePage():
    html_content = ''

    if request.method == 'POST':
        print("Got In")
        entry_content = request.form.get('entryBox1')
        print(f"Entry Box Content: {entry_content}")

    html_content += PWD.makeButton("Hello", buttonXPos=100, buttonYPos=100, onclick="/Hello")
    html_content += PWD.makeText("Back to Home", posx=50, posy=150, link="/", underlined=True, color="#0000FF", fontSize=20)
    html_content += PWD.makeEntryBox("entryBox1", "Type here", posx=50, posy=200, actionFunction="/Hello", buttonPosX=400, buttonPosY=100, buttonText="Submit123")
    html_content += PWD.createImage("NCASymbol.png", posX=500, posY=300)
    return html_content

dropArray = [
    {
        "item": "item1",
        "action": "\Hello",
    }
]


if __name__ == '__main__':
    app.run()
