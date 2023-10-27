from flask import Flask, request
import pyWebDev as PWD

app = Flask(__name__)

# https://getbootstrap.com/docs/5.3/getting-started/introduction/

html_content = []

@app.route('/')
def onOpen():
    global html_content
    blank = app.redirect('/home')
    return blank


@app.route('/home')
def index():
    global html_content
    removeContent = ["return"]
    html_content = [i for i in html_content if i["name"] not in removeContent]
    
    boostrap = {
        "name": "bootstrap",
        "code": """<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">""",
    }

    html_content.append(boostrap)
    html_content.append(PWD.createCheckbox(label="Posession", id="posessionCheckbox", checked=False, name="posessionCheckbox", posx=50, posy=70))
    html_content.append(PWD.createCheckbox(label="Timer", id="timerCheckbox", checked=False, name="timerCheckbox", posx=50, posy=50))
    html_content.append(PWD.makeButton(buttonLabel="Start", buttonName="start" ,buttonXPos=50, buttonYPos=100, onclick='/load', classType="btn btn-primary"))

    index = """"""
    for i in html_content:
        index += str(i["code"])
    # print(index)
    return index

@app.route('/load')
def load():
    global html_content
    removeContent = ["posessionCheckbox", "timerCheckbox", "start"]
    html_content = [i for i in html_content if i["name"] not in removeContent]

    html_content.append(PWD.makeButton(buttonLabel="Return", buttonName="return" ,buttonXPos=50, buttonYPos=100, onclick='/home', classType="btn btn-primary"))
    
    print(html_content)
    index = """"""
    for i in html_content:
        index += str(i["code"])
    return index




if __name__ == '__main__':
    app.run()
