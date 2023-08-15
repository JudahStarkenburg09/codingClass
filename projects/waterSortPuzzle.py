import tkinter as tk
import random

colors = ['red', 'orange', 'yellow', 'blue']
redcount = 0
orangecount = 0
yellowcount = 0
bluecount = 0
import random

colors = ['red', 'orange', 'yellow', 'blue']
color_counts = {color: 0 for color in colors}
color_limit = 4

result = []

while True:
    if all(count == color_limit for count in color_counts.values()):
        break
    
    rColor = random.choice(colors)
    if color_counts[rColor] < color_limit:
        result.append(rColor)
        color_counts[rColor] += 1

rColor1, rColor2, rColor3, rColor4, rColor5, rColor6, rColor7, rColor8, rColor9, rColor10, rColor11, rColor12, rColor13, rColor14, rColor15, rColor16 = result
print(result)

root = tk.Tk()
root.geometry('500x300')
root.title('Water Sort Puzzle')
root.config(bg='light gray')

canvas = tk.Canvas(root, width = 1000, height = 1000, bg='light gray')
canvas.pack()


canvas.create_arc(50, 200, 105, 134, start=180, extent=180, fill=rColor1, outline='black', width=1.5, tags=('beaker1'))
canvas.create_line(51, 167, 104, 167, fill=rColor1, width=1.5, tags=('beaker1'))
canvas.create_rectangle()





root.mainloop()