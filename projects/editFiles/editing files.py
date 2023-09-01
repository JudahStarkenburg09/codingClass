import fileinput
import os

processing_foo1s = False

responses = [
    {
        "input": ["hello"],
        "response": ["Hi there!"]
    },
]

current_directory = os.getcwd()
folder1 = 'editFiles'
os.chdir(os.path.join(current_directory, folder1))

# Define the new dictionary to add
new_response = """    {
        "input": ["hi"],
        "response": ["Hi there!"]
    },"""

# Loop through the lines in the input file and modify as needed
for line in fileinput.input('fileToEdit.py', inplace=1):
    if line.startswith("    },") and line.endswith("\n]"):
        print("found = True")
        processing_foo1s = True
    else:
        if processing_foo1s:
            # Add the new dictionary to the 'responses' list
            line = new_response + line
            processing_foo1s = False
    print(line, end="")