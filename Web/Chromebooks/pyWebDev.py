def text(content, underlined=False, highlighted=None, bold=False, italic=False, color=None, position=None):
    style = "style='"
    
    if underlined:
        style += "text-decoration: underline; "
    
    if highlighted:
        style += f"background-color: {highlighted}; "
    
    if bold:
        style += "font-weight: bold; "
    
    if italic:
        style += "font-style: italic; "
    
    if color:
        style += f"color: {color}; "

    if position:
        style += f"position: absolute; top: {position[1]}px; left: {position[0]}px; "
    
    style += "'"
    
    return f"<div {style}>{content}</div>"

def entryBox(id, position=None):
    if position:
        style = f"style='position: absolute; top: {position[1]}px; left: {position[0]}px;'"
    else:
        style = ""
    return f"<input type='text' id='{id}' {style}>"

def button(label, onclick=None, position=None):
    if position:
        style = f"style='position: absolute; top: {position[1]}px; left: {position[0]}px;'"
    else:
        style = ""
    
    if onclick:
        return f"<button {style} onclick='{onclick}'>{label}</button>"
    else:
        return f"<button {style}>{label}</button>"

def app():
    "Welcome to Judah's web development module!"


app()
