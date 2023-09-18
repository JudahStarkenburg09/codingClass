def upsText(input_text_ups):
    upside_down_chars = {
        'a': 'ɐ', 'b': 'q', 'c': 'ɔ', 'd': 'p', 'e': 'ǝ', 'f': 'ɟ', 'g': 'ƃ',
        'h': 'ɥ', 'i': 'ᴉ', 'j': 'ɾ', 'k': 'ʞ', 'l': 'l', 'm': 'ɯ', 'n': 'u',
        'o': 'o', 'p': 'd', 'q': 'b', 'r': 'ɹ', 's': 's', 't': 'ʇ', 'u': 'n',
        'v': 'ʌ', 'w': 'ʍ', 'x': 'x', 'y': 'ʎ', 'z': 'z',
        'A': '∀', 'B': '𐐒', 'C': 'Ↄ', 'D': '𐐓', 'E': 'Ǝ', 'F': 'Ⅎ', 'G': '⅁',
        'H': 'H', 'I': 'I', 'J': 'ſ', 'K': 'ʞ', 'L': '⅂', 'M': 'W', 'N': 'N',
        'O': 'O', 'P': 'Ԁ', 'Q': 'Ό', 'R': 'ᴚ', 'S': 'S', 'T': '⊥', 'U': '∩',
        'V': 'Λ', 'W': 'M', 'X': 'X', 'Y': '⅄', 'Z': 'Z',
        '0': '0', '1': 'Ɩ', '2': 'ᄅ', '3': 'Ɛ', '4': 'ㄣ', '5': 'ϛ',
        '6': '9', '7': 'ㄥ', '8': '8', '9': '6',
        ',': "'", '.': '˙', '!': '¡', '?': '¿', "'": ',', '`': ',',
        '"': ',,', '(': ')', ')': '(', '[': ']', ']': '[', '{': '}', '}': '{',
        '<': '>', '>': '<', '_': '‾', '&': '⅋', ' ': ' ',
    }

    upside_down_text = [upside_down_chars.get(char, char) for char in input_text_ups]
    return ''.join(upside_down_text)

def upsRvsText(input_textUpsRvs):
    upside_down_chars = {
        'a': 'ɐ', 'b': 'q', 'c': 'ɔ', 'd': 'p', 'e': 'ǝ', 'f': 'ɟ', 'g': 'ƃ',
        'h': 'ɥ', 'i': 'ᴉ', 'j': 'ɾ', 'k': 'ʞ', 'l': 'l', 'm': 'ɯ', 'n': 'u',
        'o': 'o', 'p': 'd', 'q': 'b', 'r': 'ɹ', 's': 's', 't': 'ʇ', 'u': 'n',
        'v': 'ʌ', 'w': 'ʍ', 'x': 'x', 'y': 'ʎ', 'z': 'z',
        'A': '∀', 'B': '𐐒', 'C': 'Ↄ', 'D': '𐐓', 'E': 'Ǝ', 'F': 'Ⅎ', 'G': '⅁',
        'H': 'H', 'I': 'I', 'J': 'ſ', 'K': 'ʞ', 'L': '⅂', 'M': 'W', 'N': 'N',
        'O': 'O', 'P': 'Ԁ', 'Q': 'Ό', 'R': 'ᴚ', 'S': 'S', 'T': '⊥', 'U': '∩',
        'V': 'Λ', 'W': 'M', 'X': 'X', 'Y': '⅄', 'Z': 'Z',
        '0': '0', '1': 'Ɩ', '2': 'ᄅ', '3': 'Ɛ', '4': 'ㄣ', '5': 'ϛ',
        '6': '9', '7': 'ㄥ', '8': '8', '9': '6',
        ',': "'", '.': '˙', '!': '¡', '?': '¿', "'": ',', '`': ',',
        '"': ',,', '(': ')', ')': '(', '[': ']', ']': '[', '{': '}', '}': '{',
        '<': '>', '>': '<', '_': '‾', '&': '⅋', ' ': ' ',
    }

    reversed_text = input_textUpsRvs[::-1]  # Reverse the text
    upside_down_text = [upside_down_chars.get(char, char) for char in reversed_text]
    return ''.join(upside_down_text)

def rvsText(input_textRvs):
    reversedText = input_textRvs[::-1]
    return reversedText

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








# while True:
#     print(upsText(input(": ")))
#     print(upsRvsText(input(": ")))
#     print(rvsText(input(": ")))
#     print(cText(input(": "), (255, 0, 0), True, True, True))
#     print(cText(input(": "), 'bg_blue', True, True, True))