from flask import Flask, request
import pyWebDev as PWD

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
    keepContent = ["bootstrap", "background", "logo"]
    html_content = [i for i in html_content if i["name"] in keepContent]
    


    bg = {
        "name": "background",
        "code": f"""<div class="p-3 mb-2 bg-dark text-white" style="position: fixed; top: 0; right: 0; bottom: -25; left: 0;"></div>""",
    }


    html_content.append(bg)
    # html_content.append(PWD.makeButton(buttonLabel="Set/Edit Classroom Layouts", name="setEditLayouts", buttonXPos=125, buttonYPos=25, onclick='/group-generator/classroom/layout', classType="btn btn-primary"))
    html_content.append(PWD.makeButton(buttonLabel="Set/Edit Classes", name="setEditClasses", buttonXPos=125, buttonYPos=25, onclick='/group-generator/classroom/classes', classType="btn btn-primary"))
    html_content.append(PWD.makeButton(buttonLabel="Generate Random Group", name="makeGroups", buttonXPos=275, buttonYPos=25, onclick='/group-generator/group/select', classType="btn btn-primary"))
    html_content.append(PWD.createImage('NCASymbol.png', posX=10, posY=10, name="logo",width=75, height=75))

    index = """"""
    for i in html_content:
        index += str(i["code"])
    return index

@app.route('/group-generator/group/select')
def selectGroups():
    global html_content
    keepContent = ["bootstrap", "background", "logo"]
    html_content = [i for i in html_content if i["name"] in keepContent]


    bg = {
        "name": "background",
        "code": f"""<div class="p-3 mb-2 bg-dark text-white" style="position: fixed; top: 0; right: 0; bottom: -25; left: 0;"></div>""",
    }

    html_content = [i for i in html_content if i["name"] not in ["background"]]
    html_content.append(bg)
    html_content.append(PWD.makeButton(buttonLabel="Return", name="return", buttonXPos=125, buttonYPos=25, onclick='/group-generator/home', classType="btn btn-primary"))
    html_content.append(PWD.createImage('NCASymbol.png', posX=10, posY=10, name="logo",width=75, height=75))

    index = """"""
    for i in html_content:
        index += str(i["code"])
    return index


@app.route('/group-generator/group/generate')
def generateGroups():
    global html_content
    keepContent = ["bootstrap", "background", "logo"]
    html_content = [i for i in html_content if i["name"] in keepContent]



    index = """"""
    for i in html_content:
        index += str(i["code"])
    return index

@app.route('/group-generator/classroom/classes')
def classes():
    global html_content, studentList
    studentList = []
    keepContent = ["bootstrap", "background", "logo"]
    html_content = [i for i in html_content if i["name"] in keepContent]

    bg = {
        "name": "background",
        "code": f"""<div class="p-3 mb-2 bg-dark text-white" style="position: fixed; top: 0; right: 0; bottom: -25; left: 0;"></div>""",
    }

    html_content = [i for i in html_content if i["name"] not in ["background"]]
    html_content.append(bg)
    html_content.append(PWD.createImage('NCASymbol.png', posX=10, posY=10, name="logo",width=75, height=75))
    html_content.append(PWD.makeButton(buttonLabel="Return", name="return", buttonXPos=125, buttonYPos=25, onclick='/group-generator/home', classType="btn btn-primary"))
    html_content.append(PWD.makeButton(buttonLabel="Add New", name="addClass", buttonXPos=225, buttonYPos=25, onclick='/group-generator/classroom/classes/add-class', classType="btn btn-primary"))
    html_content.append(PWD.makeText(text="Classes: ", fontSize=25, bold=True, posx=175, posy=100, link=None, color="#FFFFFF", name="classesTitle", hoverText=None))

    txt_files =  [f for f in os.listdir(os.getcwd()) if f.endswith('.txt')]
    for num, file in enumerate(txt_files, start=0):
        html_content.append(PWD.makeText(
            text=f"> {file.replace('.txt', '')}",
            posy=150 + (30 * int(num)),
            posx=200,
            name="fileNames",
            link='/group-generator/classroom/classes/edit-class?file_name=' + file.replace('.txt', ''),
            hoverText=f"Click To Edit {file.replace('.txt', '')}",
            underlined=False,
            color="#FFFFFF",
            fontSize=20
        ))





    index = """"""
    for i in html_content:
        index += str(i["code"])
    return index

@app.route('/group-generator/classroom/classes/edit-class')
def editClass():
    global html_content, studentList
    keepContent = ["bootstrap", "background", "logo"]
    html_content = [i for i in html_content if i["name"] in keepContent]

    # Get the 'file_name' parameter from the URL query
    file_name = request.args.get('file_name')

    bg = {
        "name": "background",
        "code": f"""<div class="p-3 mb-2 bg-dark text-white" style="position: fixed; top: 0; right: 0; bottom: -25; left: 0;"></div>""",
    }

    html_content = [i for i in html_content if i["name"] not in ["background"]]
    html_content.append(bg)
    html_content.append(PWD.makeButton(buttonLabel="Save And Exit", name="saveAndExit", buttonXPos=125, buttonYPos=25, onclick='/group-generator/classroom/classes/add-class/save', classType="btn btn-primary"))
    html_content.append(PWD.makeButton(buttonLabel="Discard Changes", name="exit", buttonXPos=275, buttonYPos=25, onclick='/group-generator/classroom/classes', classType="btn btn-primary"))
    html_content.append(PWD.createImage('NCASymbol.png', posX=10, posY=10, name="logo",width=75, height=75))

    html_content.append(PWD.makeEntryBox(id="nameOfClass", placeholder="Class Name", barText="📛", posx=125, posy=100, name="nameOfClass", width=300, bgColor="#7F7F7F", height=None))
    html_content.append(PWD.makeEntryBox(id="addNew", placeholder="Student", barText="👤", posx=125, posy=150, name="addNew", width=300, bgColor="#7F7F7F", height=None))
    contents = ''
    html_content.append(PWD.makeButton(buttonLabel="Add", name='add', buttonXPos=440, buttonYPos=150, onclick=f'/get?contents={contents}', classType="btn btn-primary"))


    # Use the file_name as needed in your route handler
    print(f"Editing file: {file_name}")

    index = """"""
    for i in html_content:
        index += str(i["code"])
    return index

studentList = []
@app.route('/get')
def get():
    global html_content


    return app.redirect('/group-generator/classroom/classes/edit-class')



@app.route('/group-generator/classroom/classes/add-class')
def addClass():
    global html_content
    keepContent = ["bootstrap", "background", "logo"]
    html_content = [i for i in html_content if i["name"] in keepContent]

    removeContent = ["setEditLayouts", "background", "logo", "setEditClasses", "return"]
    html_content = [i for i in html_content if i["name"] not in removeContent]

    bg = {
        "name": "background",
        "code": f"""<div class="p-3 mb-2 bg-dark text-white" style="position: fixed; top: 0; right: 0; bottom: -25; left: 0;"></div>""",
    }

    html_content = [i for i in html_content if i["name"] not in ["background"]]
    html_content.append(bg)
    html_content.append(PWD.makeButton(buttonLabel="Save And Exit", name="saveAndExit", buttonXPos=125, buttonYPos=25, onclick='/group-generator/classroom/classes/add-class/save', classType="btn btn-primary"))
    html_content.append(PWD.makeButton(buttonLabel="Discard Changes", name="exit", buttonXPos=275, buttonYPos=25, onclick='/group-generator/classroom/classes', classType="btn btn-primary"))
    html_content.append(PWD.createImage('NCASymbol.png', posX=10, posY=10, name="logo",width=75, height=75))


    index = """"""
    for i in html_content:
        index += str(i["code"])
    return index

@app.route('/group-generator/classroom/classes/add-class/save')
def save():
    global html_content
    keepContent = ["bootstrap", "background", "logo"]
    html_content = [i for i in html_content if i["name"] in keepContent]



    index = """"""
    for i in html_content:
        index += str(i["code"])
    return app.redirect('/group-generator/classroom/classes')


if __name__ == '__main__':
    app.run(port=7824)