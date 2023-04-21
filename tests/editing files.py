import fileinput

processing_foo1s = False

responses = [
    {
        "input": ["hello"],
        "response": ["Hi there!"]
    },
]


'pointHere#51'


for line in fileinput.input('test2.py', inplace=1):
    if line.startswith("'pointHere#51'"):
        processing_foo1s = True
    else:
        if processing_foo1s:
            line = ("""print('Adding line')     \n""") + line
            processing_foo1s = False
    print(line, end="")
