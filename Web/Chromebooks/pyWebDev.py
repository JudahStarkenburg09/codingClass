# https://getbootstrap.com/docs/5.3/getting-started/introduction/

def makeButton(buttonLabel, buttonXPos, buttonYPos, onclick, classType=None):
    html_code = f"""
    <button class="{classType}" style="position: absolute; left: {buttonXPos}px; top: {buttonYPos}px;" onclick="window.location.href='{onclick}'">{buttonLabel}</button>
    """
    return html_code

def makeText(text=None, posy=None, posx=None, link=None, underlined=False, bold=False, color=None, highlightColor=None, fontSize=None, font=None):
    style = ""
    if underlined:
        style += "text-decoration: underline;"
    if bold:
        style += "font-weight: bold;"
    if color:
        style += f"color: {color};"
    if highlightColor:
        style += f"background-color: {highlightColor};"
    if fontSize:
        style += f"font-size: {fontSize}px;"
    if font:
        style += f"font-family: {font};"

    html_code = f"""
    <a href="{link}" style="position: absolute; left: {posx}px; top: {posy}px; {style}">{text}</a>
    """
    return html_code

def makeEntryBox(id, placeholder, actionFunction, posx, posy, buttonPosX, buttonPosY, buttonText):
    html_code = f"""
    <form method="POST" action="{actionFunction}">
        <input type="text" id="{id}" name="{id}" placeholder="{placeholder}" style="position: absolute; left: {posx}px; top: {posy}px;">
        <input type="submit" value="{buttonText}" style="position: absolute; left: {buttonPosX}px; top: {buttonPosY}px;">
    </form>
    """
    return html_code

def createImage(fileName, posX, posY):
    html_code = f"""
    <img src="/static/{fileName}" style="position: absolute; left: {posX}px; top: {posY}px;">
    """
    return html_code

def createTable():
    ''

def createDropdown(classType, dropArray):
    ''

def createScrollspy():
    ''

def createProgressBar():
    ''

def createSpinner():
    ''

def createToast():
    ''
    
def createBadge():
    ''

def createModal():
    ''