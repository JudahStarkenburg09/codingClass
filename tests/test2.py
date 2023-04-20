import fileinput

processing_foo1s = False

responses = [
    {
        "input": ["hello"],
        "response": ["Hi there!"]
    },
]






for line in fileinput.input('test2.py', inplace=1):
    if line.startswith('responses = ['):
        processing_foo1s = True
    else:
        if processing_foo1s:
            line = ("""    {
        "input": ["how are you"],
        "response": ["I'm good, thank you!"]
    },\n""") + line
            processing_foo1s = False
    print(line, end="")
