from flask import Flask, request
import pyWebDev as PWD

app = Flask(__name__)

# https://getbootstrap.com/docs/5.3/getting-started/introduction/


@app.route('/')
def onOpen():
    blank = app.redirect('/home')
    return blank

@app.route('/home')
def index():
    global dropArray, html_content
    boostrap = {
        "name": "bootstrap",
        "code": """<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">""",
    }

    html_content = [boostrap]
    html_content.append(PWD.makeButton(buttonLabel="Sign In", buttonName="button" ,buttonXPos=50, buttonYPos=50, onclick='/sign-in', classType="btn btn-primary"))


    index = """"""
    for i in html_content:
        index += str(i["code"])
    return index

# if request.method == 'POST':
#     print("Got In")
#     entry_content = request.form.get('entryBox1')
#     print(f"Entry Box Content: {entry_content}")
@app.route('/sign-in', methods=['GET', 'POST'])
def changePage():
    global html_content
    for i in html_content:
        if i["name"] == "button":
            html_content.remove(i)



    
    index = ''
    for i in html_content:
        index += str(i["code"])
    return index

dropArray = [
    {
        "item": "item1",
        "action": "\Hello",
    }
]


if __name__ == '__main__':
    app.run()
