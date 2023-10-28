# https://getbootstrap.com/docs/5.3/getting-started/introduction/

def makeButton(buttonLabel, name, buttonXPos=None, buttonYPos=None, onclick=None, classType=None):
    html_code = f"""
    <button class="{classType}" style="position: absolute; left: {buttonXPos}px; top: {buttonYPos}px;" onclick="window.location.href='{onclick}'">{buttonLabel}</button>
    """
    array = {
        "name": f"{name}",
        "code": html_code
    }
    return array

def createCheckbox(id, name, label,  posx, posy, checked=False):
    html_code = f"""
<div class="form-check">
   <input class="form-check-input" type="checkbox" value="" id="{id}" style="position: absolute; left: {posx}px; top: {posy}px;">
   <label class="form-check-label" for="{id}" style="position: absolute; left: {posx}px; top: {posy}px;">
    {label}
   </label>
</div>
"""
    array = {
        "name": name,
        "code": html_code
    }
    return array


def makeText(name, text=None, posy=None, posx=None, link=None, underlined=False, bold=False, color=None, highlightColor=None, fontSize=None, font=None):
    style = ""
    hasLink = ''
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
    if link:
        hasLink = f""" href='{link}'"""

    html_code = f"""
    <a{hasLink} style="position: absolute; left: {posx}px; top: {posy}px; {style}">{text}</a>
    """

    array = {
        "name": name,
        "code": html_code,
    }

    return array

def makeEntryBox(id, placeholder, barText, entryName, posx, posy):
    html_code = f"""
<div style="position: absolute; left: {posx}px; top: {posy}px;" class="input-group flex-nowrap">
  <span class="input-group-text" id="{id}">{barText}</span>
  <input type="text" class="form-control" placeholder="{placeholder}" aria-label="{placeholder}" aria-describedby="addon-wrapping">
</div>
    """
    array = {
        "name": f"{entryName}",
        "code": html_code,
    }

    return array

def createImage(fileName, posX, posY, name, width=None, height=None):
    html_code = f"""
    <img src="/static/{fileName}" style="position: absolute; left: {posX}px; top: {posY}px; width: {width}px; height: {height}px;">
    """

    array = {
        "name": f"{name}",
        "code": html_code
    }
    return array


