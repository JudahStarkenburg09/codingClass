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

def button(label, script=None, position=None):
    if position:
        style = f"style='position: absolute; top: {position[1]}px; left: {position[0]}px;'"
    else:
        style = ""
    
    if script:
        js_function = f"""
        <script>
            function executePythonFile() {{
                var xhr = new XMLHttpRequest();
                xhr.open("POST", "/run_python_file", true);
                xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
                xhr.onreadystatechange = function () {{
                    if (xhr.readyState == 4 && xhr.status == 200) {{
                        console.log(xhr.responseText);
                    }}
                }};
                var data = JSON.stringify({{ "file": "{script}" }});
                xhr.send(data);
            }}
        </script>
        """
        return f"{js_function}<button {style} onclick='executePythonFile()'>{label}</button>"
    else:
        return f"<button {style}>{label}</button>"




def app():
    "Welcome to Judah's web development module!"


app()
