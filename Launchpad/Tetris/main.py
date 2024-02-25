import sys
import launchpad_py as launchpad
import time
import random
import copy

lp = launchpad.Launchpad()
if lp.Open():
    print("Launchpad Mk1/S/Mini")
    mode = "Mk1"

lp.ButtonFlush()
lp.Reset()

LaunchpadBoard = [
    [{"Number": 0, "Red": 0, "Green": 0, "Frozen": False}, {"Number": 1, "Red": 0, "Green": 0, "Frozen": False}, {"Number": 2, "Red": 0, "Green": 0, "Frozen": False}, {"Number": 3, "Red": 0, "Green": 0, "Frozen": False}, {"Number": 4, "Red": 0, "Green": 0, "Frozen": False}, {"Number": 5, "Red": 0, "Green": 0, "Frozen": False}, {"Number": 6, "Red": 0, "Green": 0, "Frozen": False}, {"Number": 7, "Red": 0, "Green": 0, "Frozen": False}],
    [{"Number": 16, "Red": 0, "Green": 0, "Frozen": False}, {"Number": 17, "Red": 0, "Green": 0, "Frozen": False}, {"Number": 18, "Red": 0, "Green": 0, "Frozen": False}, {"Number": 19, "Red": 0, "Green": 0, "Frozen": False}, {"Number": 20, "Red": 0, "Green": 0, "Frozen": False}, {"Number": 21, "Red": 0, "Green": 0, "Frozen": False}, {"Number": 22, "Red": 0, "Green": 0, "Frozen": False}, {"Number": 23, "Red": 0, "Green": 0, "Frozen": False}],
    [{"Number": 32, "Red": 0, "Green": 0, "Frozen": False}, {"Number": 33, "Red": 0, "Green": 0, "Frozen": False}, {"Number": 34, "Red": 0, "Green": 0, "Frozen": False}, {"Number": 35, "Red": 0, "Green": 0, "Frozen": False}, {"Number": 36, "Red": 0, "Green": 0, "Frozen": False}, {"Number": 37, "Red": 0, "Green": 0, "Frozen": False}, {"Number": 38, "Red": 0, "Green": 0, "Frozen": False}, {"Number": 39, "Red": 0, "Green": 0, "Frozen": False}],
    [{"Number": 48, "Red": 0, "Green": 0, "Frozen": False}, {"Number": 49, "Red": 0, "Green": 0, "Frozen": False}, {"Number": 50, "Red": 0, "Green": 0, "Frozen": False}, {"Number": 51, "Red": 0, "Green": 0, "Frozen": False}, {"Number": 52, "Red": 0, "Green": 0, "Frozen": False}, {"Number": 53, "Red": 0, "Green": 0, "Frozen": False}, {"Number": 54, "Red": 0, "Green": 0, "Frozen": False}, {"Number": 55, "Red": 0, "Green": 0, "Frozen": False}],
    [{"Number": 64, "Red": 0, "Green": 0, "Frozen": False}, {"Number": 65, "Red": 0, "Green": 0, "Frozen": False}, {"Number": 66, "Red": 0, "Green": 0, "Frozen": False}, {"Number": 67, "Red": 0, "Green": 0, "Frozen": False}, {"Number": 68, "Red": 0, "Green": 0, "Frozen": False}, {"Number": 69, "Red": 0, "Green": 0, "Frozen": False}, {"Number": 70, "Red": 0, "Green": 0, "Frozen": False}, {"Number": 71, "Red": 0, "Green": 0, "Frozen": False}],
    [{"Number": 80, "Red": 0, "Green": 0, "Frozen": False}, {"Number": 81, "Red": 0, "Green": 0, "Frozen": False}, {"Number": 82, "Red": 0, "Green": 0, "Frozen": False}, {"Number": 83, "Red": 0, "Green": 0, "Frozen": False}, {"Number": 84, "Red": 0, "Green": 0, "Frozen": False}, {"Number": 85, "Red": 0, "Green": 0, "Frozen": False}, {"Number": 86, "Red": 0, "Green": 0, "Frozen": False}, {"Number": 87, "Red": 0, "Green": 0, "Frozen": False}],
    [{"Number": 96, "Red": 0, "Green": 0, "Frozen": False}, {"Number": 97, "Red": 0, "Green": 0, "Frozen": False}, {"Number": 98, "Red": 0, "Green": 0, "Frozen": False}, {"Number": 99, "Red": 0, "Green": 0, "Frozen": False}, {"Number": 100, "Red": 0, "Green": 0, "Frozen": False}, {"Number": 101, "Red": 0, "Green": 0, "Frozen": False}, {"Number": 102, "Red": 0, "Green": 0, "Frozen": False}, {"Number": 103, "Red": 0, "Green": 0, "Frozen": False}],
    [{"Number": 112, "Red": 0, "Green": 0, "Frozen": False}, {"Number": 113, "Red": 0, "Green": 0, "Frozen": False}, {"Number": 114, "Red": 0, "Green": 0, "Frozen": False}, {"Number": 115, "Red": 0, "Green": 0, "Frozen": False}, {"Number": 116, "Red": 0, "Green": 0, "Frozen": False}, {"Number": 117, "Red": 0, "Green": 0, "Frozen": False}, {"Number": 118, "Red": 0, "Green": 0, "Frozen": False}, {"Number": 119, "Red": 0, "Green": 0, "Frozen": False}]
]

def resetBoard():
    global LaunchpadBoard
    for row in LaunchpadBoard:
        for cell in row:
            if not cell["Frozen"]:
                cell["Red"] = 0
                cell["Green"] = 0
                # Keep the previous "Frozen" value
                # cell["Frozen"] remains unchanged



def update_value(row, col, newColor=[0,0]):
    global LaunchpadBoard
    row -= 1
    col -= 1
    object = LaunchpadBoard[row][col]
    raw = object["Number"]
    LaunchpadBoard[row][col] = {"Number": int(raw), "Red": newColor[0], "Green": newColor[1], "Frozen": object["Frozen"]}

resetBoard()


def freezeBoard():
    print("Froze")
    global LaunchpadBoard
    for row in LaunchpadBoard:
        for array in row:
            if array["Red"] != 0 or array["Green"] != 0:
                array["Frozen"] = True


def colorBoard():
    global LaunchpadBoard
    for row in LaunchpadBoard:
        for rowCol in row:
            if not rowCol['Frozen']:
                lp.LedCtrlRaw(rowCol['Number'], red=int(rowCol['Red']), green=rowCol['Green'])

posy = -1
square1 = [1,2]
square2 = [2,3]
square3 = [3,4]
square4 = [4,5]
square5 = [5,6]
square6 = [6,7]
square7 = [7,8]
colors = [
    [0, 1],
    [0, 2],
    [0, 3],
    [1, 0],
    [1, 1],
    [1, 2],
    [1, 3],
    [2, 0],
    [2, 1],
    [2, 2],
    [2, 3],
    [3, 0],
    [3, 1],
    [3, 2],
    [3, 3],
]

shapes = [square1, square2, square3, square4, square5, square6, square7]

currentShape = random.choice(shapes)
color = random.choice(colors)


def nextIsAvailable():




    
    return True


while True:
    Column1 = currentShape[0]
    Column2 = currentShape[1]


    if nextIsAvailable():
        if 7 >= posy >= 1:
            update_value(posy, Column1, newColor=color)
            update_value(posy, Column2, newColor=color)
        if 7 >= posy >= 0:
            update_value(posy+1, Column1, newColor=color)
            update_value(posy+1, Column2, newColor=color)

        if posy < 7:
            posy += 1
        else:
            colorBoard()  # Update the display before resetting
            freezeBoard()
            posy = -1
            currentShape = random.choice(shapes)
            color = random.choice(colors)

        colorBoard()  # Update the display each iteration
        time.sleep(0.25)
        resetBoard()
