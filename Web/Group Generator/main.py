from flask import Flask, request
import pyWebDev as PWD
import classLayout
import os

app = Flask(__name__)

# https://getbootstrap.com/docs/5.3/getting-started/introduction/

html_content = []
boostrap = {
    "name": "bootstrap",
    "code": """<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">""",
}
html_content.append(boostrap)

@app.route('/')
def onOpen():
    global html_content
    blank = app.redirect('/group-generator/home')
    return blank


@app.route('/group-generator/home')
def index():
    global html_content
    removeContent = ["setEditLayouts", "background", "logo", "setEditClasses", "return"]
    html_content = [i for i in html_content if i["name"] not in removeContent]
    


    bg = {
        "name": "background",
        "code": f"""<div class="p-3 mb-2 bg-dark text-white" style="position: fixed; top: 0; right: 0; bottom: -25; left: 0;"></div>""",
    }


    html_content.append(bg)
    html_content.append(PWD.makeButton(buttonLabel="Set/Edit Classroom Layouts", name="setEditLayouts", buttonXPos=125, buttonYPos=25, onclick='/group-generator/classroom/layout', classType="btn btn-primary"))
    html_content.append(PWD.makeButton(buttonLabel="Set/Edit Classes", name="setEditClasses", buttonXPos=375, buttonYPos=25, onclick='/group-generator/classroom/classes', classType="btn btn-primary"))
    html_content.append(PWD.createImage('NCASymbol.png', posX=10, posY=10, name="logo",width=75, height=75))

    index = """"""
    for i in html_content:
        index += str(i["code"])
    return index

@app.route('/group-generator/classroom/layout')
def layout():
    global html_content
    removeContent = ["setEditLayouts", "background", "logo", "setEditClasses", "return"]
    html_content = [i for i in html_content if i["name"] not in removeContent]

    bg = {
        "name": "background",
        "code": f"""<div class="p-3 mb-2 bg-dark text-white" style="position: fixed; top: 0; right: 0; bottom: -25; left: 0;"></div>""",
    }

    html_content = [i for i in html_content if i["name"] not in ["background"]]
    html_content.append(bg)
    html_content.append(PWD.createImage('NCASymbol.png', posX=10, posY=10, name="logo",width=75, height=75))
    html_content.append(PWD.makeButton(buttonLabel="Return", name="return", buttonXPos=125, buttonYPos=25, onclick='/group-generator/home', classType="btn btn-primary"))



    index = """"""
    for i in html_content:
        index += str(i["code"])
    return index

@app.route('/group-generator/classroom/classes')
def classes():
    global html_content
    removeContent = ["setEditLayouts", "background", "logo", "setEditClasses", "return"]
    html_content = [i for i in html_content if i["name"] not in removeContent]

    bg = {
        "name": "background",
        "code": f"""<div class="p-3 mb-2 bg-dark text-white" style="position: fixed; top: 0; right: 0; bottom: -25; left: 0;"></div>""",
    }

    html_content = [i for i in html_content if i["name"] not in ["background"]]
    html_content.append(bg)
    html_content.append(PWD.createImage('NCASymbol.png', posX=10, posY=10, name="logo",width=75, height=75))
    html_content.append(PWD.makeButton(buttonLabel="Return", name="return", buttonXPos=125, buttonYPos=25, onclick='/group-generator/home', classType="btn btn-primary"))
    html_content.append(PWD.makeButton(buttonLabel="Add New", name="addClass", buttonXPos=225, buttonYPos=25, onclick='/group-generator/classroom/classes/add-class', classType="btn btn-primary"))
    html_content.append(PWD.makeText(text="Classes: ", fontSize=25, bold=True, posx=175, posy=100, link=None, color="#FFFFFF", name="classesTitle"))
    
    txt_files =  [f for f in os.listdir(os.getcwd()) if f.endswith('.txt')]
    for num, file in enumerate(txt_files, start=1):  # Start numbering from 1
        html_content.append(PWD.makeText(text=f"> {file.replace('.txt', '')}", posy=125+(30*int(num)), posx=200, name="fileNames", link=None, underlined=False, color="#FFFFFF", fontSize=20))




    index = """"""
    for i in html_content:
        index += str(i["code"])
    return index

@app.route('group-generator/classroom/classes/add-class')
def addClass():
    global html_content
    removeContent = ["setEditLayouts", "background", "logo", "setEditClasses", "return"]
    html_content = [i for i in html_content if i["name"] not in removeContent]

    bg = {
        "name": "background",
        "code": f"""<div class="p-3 mb-2 bg-dark text-white" style="position: fixed; top: 0; right: 0; bottom: -25; left: 0;"></div>""",
    }

    html_content = [i for i in html_content if i["name"] not in ["background"]]
    html_content.append(bg)


    index = """"""
    for i in html_content:
        index += str(i["code"])
    return index

@app.route('/groupGenerator/classroom/layout/class')
def class_page():
    global html_content





    index = """"""
    for i in html_content:
        index += str(i["code"])
    return index




if __name__ == '__main__':
    app.run()