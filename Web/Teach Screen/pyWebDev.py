import html

COMMON_STYLE = "position: absolute;"

def make_button(label, name, x_pos=None, y_pos=None, onclick=None, class_type=None):
    html_code = f"""
    <button class="{class_type}" style="{COMMON_STYLE} left: {x_pos}px; top: {y_pos}px;" onclick="window.location.href='{onclick}'">{label}</button>
    """
    return {"name": name, "code": html_code}

def create_checkbox(id, name, label,  x_pos, y_pos, checked=False):
    html_code = f"""
    <div class="form-check" style="{COMMON_STYLE} left: {x_pos}px; top: {y_pos}px;">
        <input class="form-check-input" type="checkbox" value="" id="{id}">
        <label class="form-check-label" for="{id}">{label}</label>
    </div>
    """
    return {"name": name, "code": html_code}

def make_text(name, text=None, posy=None, posx=None, link=None, underlined=False, bold=False, color=None, highlight_color=None, font_size=None, font=None, hover_text=None):
    style = f"{COMMON_STYLE} left: {posx}px; top: {posy}px;"
    if underlined:
        style += "text-decoration: underline;"
    if bold:
        style += "font-weight: bold;"
    if color:
        style += f"color: {color};"
    if highlight_color:
        style += f"background-color: {highlight_color};"
    if font_size:
        style += f"font-size: {font_size}px;"
    if font:
        style += f"font-family: {font};"

    has_link = f' href="{link}"' if link else ''
    hover_attribute = f' title="{hover_text}"' if hover_text else ''

    html_code = f"""
    <a{has_link} style="{style}"{hover_attribute}>{html.escape(text)}</a>
    """

    return {"name": name, "code": html_code}

def make_entry_box(id, placeholder, bar_text, name, x_pos, y_pos, bg_color, width, height):
    html_code = f"""
    <form method="POST">
        <div style="{COMMON_STYLE} left: {x_pos}px; top: {y_pos}px; background-color: {bg_color}; width: {width}px; height: {height}px;" class="input-group flex-nowrap">
            <span class="input-group-text" id="{id}">{bar_text}</span>
            <input type="text" class="form-control" id="{id}" placeholder="{placeholder}" aria-label="{placeholder}" aria-describedby="addon-wrapping" name="{name}">
        </div>
    </form>
    """
    return {"name": name, "code": html_code}

def create_image(file_name, x_pos, y_pos, name, width=None, height=None):
    html_code = f"""
    <img src="/static/{file_name}" style="{COMMON_STYLE} left: {x_pos}px; top: {y_pos}px; width: {width}px; height: {height}px;">
    """
    return {"name": name, "code": html_code}
