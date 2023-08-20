# need to fix overflowing and emptiness. Need Dad, dont do it during coding










import tkinter as tk
import random
colors = ['red', 'orange', 'yellow', 'blue']
color_counts = {color: 0 for color in colors}
color_limit = 4
redcount = 0
orangecount = 0
yellowcount = 0
bluecount = 0
result = []




while True:
    if all(count == color_limit for count in color_counts.values()):
        break
    
    rColor = random.choice(colors)
    if color_counts[rColor] < color_limit:
        result.append(rColor)
        color_counts[rColor] += 1

white = '#FFFFFF'
# rColor1, rColor2, rColor3, rColor4, rColor5, rColor6, rColor7, rColor8, rColor9, rColor10, rColor11, rColor12, rColor13, rColor14, rColor15, rColor16 = result
print(result)

def checkWin():
    ''

class Vial:
    def __init__(self, canvas, vialx, color):
        self.canvas = canvas
        self.vialx = vialx
        self.color = color
        self.draw_vial()

    def draw_vial(self):
        # make a temporary color list and fill empty with white
        colorFill = []
        for n in range(0, 6):
            colorFill.append(self.color[n] if len(self.color) > n else 'white')
        # draw the bottom art
        self.canvas.create_arc(self.vialx + 50, 300, self.vialx + 105, 234, start=180, extent=180, fill=colorFill[0], outline='black', width=1.5, tags=('beaker1'))  # bottom
        # draw each rectangle of color
        for n in range(1, 6):
            self.canvas.create_rectangle(self.vialx + 50, 267 - 40 * n, self.vialx + 105, 307 - 40 * n, fill=colorFill[n], width=1.5, outline='black', tags=('beaker1'))
        # draw a line to cover up the borders
        for n in range(0, 5):
            self.canvas.create_line(self.vialx + 51, 267 - 40 * n, self.vialx + 104, 267 - 40 * n, fill=colorFill[n], width=1.5, tags=('beaker1'))  # bottom line
            
    def add_color(self, newColor):
        if (len(self.color) > 5):
            print("No!  This vial is full!")
            return
        self.color.append(newColor)
        self.draw_vial()

    def pour(self):
        print("My colors are: ", self.color)
        if (len(self.color) == 0):
            print("No!  This vial is empty!")
            return
        topColor = self.color.pop()
        self.draw_vial()
        return topColor
        

class Button:
    def __init__(self, canvas, buttonx, i, button_click):
        self.canvas = canvas
        self.buttonx = buttonx
        self.i = i
        self.button_click = button_click
        self.is_green = False
        self.draw_buttons()
        
    def draw_buttons(self):
        self.button = tk.Button(self.canvas, bg='gray', text="Select", command=lambda: self.button_click(self.i + 1, self))
        x_position = self.buttonx + 75
        self.canvas.create_window(x_position, 45, window=self.button)



def button_click(buttonNumber, button_instance):
    global vials, poured, clickNumber
    print(f"You clicked on button #{buttonNumber}, poured = {poured}")
    if (clickNumber > 0):
        clickNumber = 0
        vials[buttonNumber - 1].add_color(poured)
        checkWin()
    else:
        clickNumber = 1
        poured = vials[buttonNumber - 1].pour()
        

def update_button_colors():
    green_count = sum(button.is_green for button in buttons)
    for button in buttons:
        button.button.config(bg="green" if button.is_green else "gray")
    if green_count >= 2:
        reset_buttons()

def reset_buttons():
    for button in buttons:
        button.is_green = False
    update_button_colors()
    if hasattr(button_click, 'selected_button'):
        del button_click.selected_button
    if hasattr(button_click, 'second_selected_button'):
        del button_click.second_selected_button

root = tk.Tk()
canvas = tk.Canvas(root, width=600, height=400, bg='white')
canvas.pack()

vials = []
poured = ''
clickNumber = 0

split_size = 4
split_lists = [result[i:i+split_size] for i in range(0, len(result), split_size)]
c1, c2, c3, c4 = split_lists


for i in range(4):
    colorToUse = f'c{i+1}'
    color = globals()[colorToUse]
    

    vials.append(Vial(canvas, i * 150, color))

buttons = []
for i in range(4):
    button = Button(canvas, i * 150, i, button_click)
    buttons.append(button)


root.mainloop()
