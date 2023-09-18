def cText(text, color='reset', italic=False, bold=False, underlined=False):
    colors = {
        'reset': '\033[0m',
        'black': '\033[30m',
        'red': '\033[31m',
        'green': '\033[32m',
        'yellow': '\033[33m',
        'blue': '\033[34m',
        'purple': '\033[35m',
        'cyan': '\033[36m',
        'white': '\033[37m',
        'bg_black': '\033[40m',
        'bg_red': '\033[41m',
        'bg_green': '\033[42m',
        'bg_yellow': '\033[43m',
        'bg_blue': '\033[44m',
        'bg_purple': '\033[45m',
        'bg_cyan': '\033[46m',
        'bg_white': '\033[47m',
    }

    text_attributes = {
        'reset': '\033[0m',
        'italic': '\033[3m',
        'bold': '\033[1m',
        'underlined': '\033[4m',
    }

    if isinstance(color, tuple) and len(color) == 3:
        r, g, b = color
        color_code = f'\033[38;2;{r};{g};{b}m'
    elif color.startswith('#') and len(color) == 7:
        color_code = f'\033[38;2;{int(color[1:3], 16)};{int(color[3:5], 16)};{int(color[5:7], 16)}m'
    else:
        color_code = colors.get(color, colors['reset'])

    attributes = ''
    if italic:
        attributes += text_attributes['italic']
    if bold:
        attributes += text_attributes['bold']
    if underlined:
        attributes += text_attributes['underlined']

    formatted_text = color_code + attributes + text + text_attributes['reset']

    return formatted_text

# Example usage:
cText("This is green text.", color='green', italic=True, bold=True, underlined=True)
cText("This is red text.", color='#FF0000', italic=True)  # Hex code for red
cText("This is blue text.", color=(0, 0, 255), underlined=True)  # RGB tuple for blue
cText("This is normal text.", color='reset')  # Use 'reset' for normal text
print(cText("Red Text", (255, 0, 0), True))
