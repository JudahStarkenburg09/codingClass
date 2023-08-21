import time
import tkinter as tk
import random

# List of available colors
colors = ['red', 'orange', 'yellow', 'blue']

# Dictionary to keep track of color counts
color_counts = {color: 0 for color in colors}

# Maximum limit for each color
color_limit = 4

# Initialize color count variables
redcount = 0
orangecount = 0
yellowcount = 0
bluecount = 0

# List to store the randomly generated colors
result = []

# Counter for the number of turns
turns = 0

# Generate random colors until color limits are reached for all colors
while True:
    if all(count == color_limit for count in color_counts.values()):
        break
    
    rColor = random.choice(colors)
    if color_counts[rColor] < color_limit:
        result.append(rColor)
        color_counts[rColor] += 1

# Hexadecimal code for white color
white = '#FFFFFF'

# Printing the generated colors
print(result)

# Variables for canvas text display
canvasText = None
canvasTurnText = None

# Function to delete canvas text
def deleteText(textToPrint):
    global canvasText
    if textToPrint == 'You Win!':
        exit()
    canvas.delete(canvasText)

# Function to display temporary text on canvas
def printingText(textToPrint):
    global canvasText
    if canvasText is not None:
        canvas.delete(canvasText)
    canvasText = canvas.create_text(300, 5, text=textToPrint, bg=None, font=('Arial', 15), anchor='n')
    canvas.after(5000, lambda: deleteText(textToPrint))
    return

# Function to update the displayed turns count
def turnsTextUpdate():
    global turns, canvasTurnText
    if canvasTurnText is not None:
        canvas.delete(canvasTurnText)
    canvasTurnText = canvas.create_text(15, 5, text=f"Turns: {turns}", font=('Arial', 15), anchor='nw')

# Class to represent a vial
class Vial:
    def __init__(self, canvas, vialx, color):
        self.canvas = canvas
        self.vialx = vialx
        self.color = color
        self.draw_vial()

    # Function to draw the vial graphics
    def draw_vial(self):
        colorFill = []  # Temporary color list for filling the vial
        for n in range(0, 6):
            colorFill.append(self.color[n] if len(self.color) > n else 'white')
        # Draw the bottom art of the vial
        self.canvas.create_arc(self.vialx + 50, 300, self.vialx + 105, 234, start=180, extent=180, fill=colorFill[0], outline='black', width=1.5, tags=('beaker1'))  # bottom
        # Draw each rectangle of color inside the vial
        for n in range(1, 6):
            self.canvas.create_rectangle(self.vialx + 50, 267 - 40 * n, self.vialx + 105, 307 - 40 * n, fill=colorFill[n], width=1.5, outline='black', tags=('beaker1'))
        # Draw lines to cover up the borders
        for n in range(0, 5):
            self.canvas.create_line(self.vialx + 51, 267 - 40 * n, self.vialx + 104, 267 - 40 * n, fill=colorFill[n], width=1.5, tags=('beaker1'))  # bottom line
    
    # Function to add a color to the vial
    def add_color(self, newColor):
        if len(self.color) > 5:
            printingText("No! This vial is full!")
            return False
        self.color.append(newColor)
        self.draw_vial()
        return True
    
    # Function to check if the vial contains a winning combination of colors
    def checkWin(self):
        if len(self.color) != 4:
            return False
        for w in range(1, 3):
            if color[w] != color[0]:
                return False
        return True

    # Function to pour out a color from the vial
    def pour(self):
        print("My colors are: ", self.color)
        if len(self.color) == 0:
            printingText("No! This vial is empty!")
            return False
        topColor = self.color.pop()
        self.draw_vial()
        return topColor

# Function to check if all vials have a winning combination of colors
def checkIfWin():
    for W in range(0, 3):
        if not vials[W].checkWin():
            return False
    return True

# Class to represent a button
class Button:
    def __init__(self, canvas, buttonx, i, button_click):
        self.canvas = canvas
        self.buttonx = buttonx
        self.i = i
        self.button_click = button_click
        self.is_green = False
        self.draw_buttons()

    # Function to draw the buttons on the canvas
    def draw_buttons(self):
        self.button = tk.Button(self.canvas, bg='gray', text="Select", command=lambda: self.button_click(self.i + 1, self))
        x_position = self.buttonx + 75
        self.canvas.create_window(x_position, 45, window=self.button)

# Function to represent the container where poured color is displayed
def container():
    global contain
    if poured == 'white':
        canvas.delete(contain)
    else:
        contain = canvas.create_oval(250, 300, 350, 400, fill=poured)

contain = None

# Function to exit the program
def exitProgram():
    exit()

# Function to handle button clicks
def button_click(buttonNumber, button_instance):
    global vials, poured, clickNumber, turns
    print(f"You clicked on button #{buttonNumber}, poured = {poured}")
    if clickNumber > 0:
        res = vials[buttonNumber - 1].add_color(poured)
        if res == False:
            return
        clickNumber = 0
        poured = 'white'
    else:
        poured = vials[buttonNumber - 1].pour()
        if poured == False:
            return
        
        clickNumber = 1
        turns += 1
        turnsTextUpdate()
    container()
    if checkIfWin():
        printingText('You Win!')

# Function to update button colors
def update_button_colors():
    green_count = sum(button.is_green for button in buttons)
    for button in buttons:
        button.button.config(bg="green" if button.is_green else "gray")
    if green_count >= 2:
        reset_buttons()

# Function to reset button states
def reset_buttons():
    for button in buttons:
        button.is_green = False
    update_button_colors()
    if hasattr(button_click, 'selected_button'):
        del button_click.selected_button
    if hasattr(button_click, 'second_selected_button'):
        del button_click.second_selected_button

# Create the main tkinter window
root = tk.Tk()
canvas = tk.Canvas(root, width=600, height=400, bg='white')
canvas.pack()

# Create vial instances and buttons
vials = []
poured = ''
clickNumber = 0

# Split the generated colors into groups
split_size = 4
split_lists = [result[i:i+split_size] for i in range(0, len(result), split_size)]
c1, c2, c3, c4 = split_lists

# Create vials using split color lists
for i in range(4):
    colorToUse = f'c{i+1}'
    color = globals()[colorToUse]
    vials.append(Vial(canvas, i * 150, color))

# Create buttons for each vial
buttons = []
for i in range(4):
    button = Button(canvas, i * 150, i, button_click)
    buttons.append(button)

# Start the main tkinter event loop
root.mainloop()
