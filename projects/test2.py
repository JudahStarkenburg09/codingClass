text = '          *'
for i in range(0, 10):
    print(text + text[::-1])
    text = text[1:]
    text += '*'
for i in range(0,5):
    print((" "*9) + ("*"*5))
