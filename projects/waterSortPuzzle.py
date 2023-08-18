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
selected = None
def clear_selection():
    global selected, selectV1_button, selectV2_button, selectV3_button, selected

    selectV1_button.destroy()
    selectV1_button = tk.Button(root, text='Select', bg='gray', command=lambda: select(1, selected))
    selectV1_button.place(x=40, y=20, width=80, height=30)
    selectV2_button.destroy()
    selectV2_button = tk.Button(root, text='Select', bg='gray', command=lambda: select(2, selected))
    selectV2_button.place(x=140, y=20, width=80, height=30)
    selectV3_button.destroy()
    selectV3_button = tk.Button(root, text='Select', bg='gray', command=lambda: select(3, selected))
    selectV3_button.place(x=240, y=20, width=80, height=30)
    selectV4_button.destroy()
    selectV4_button = tk.Button(root, text='Select', bg='gray', command=lambda: select(4, selected))
    selectV4_button.place(x=340, y=20, width=80, height=30)


    selected = None
    print(selected)



def select(selected, previouslySelected):
    global select, selectV1_button, selectV2_button, selectV3_button, selectV4_button
    

    pour()
    
    selectV1_button.destroy()
    selectV1_button = tk.Button(root, text='Select', bg='gray', command=lambda: select(1, selected))
    selectV1_button.place(x=40, y=20, width=80, height=30)
    selectV2_button.destroy()
    selectV2_button = tk.Button(root, text='Select', bg='gray', command=lambda: select(2, selected))
    selectV2_button.place(x=140, y=20, width=80, height=30)
    selectV3_button.destroy()
    selectV3_button = tk.Button(root, text='Select', bg='gray', command=lambda: select(3, selected))
    selectV3_button.place(x=240, y=20, width=80, height=30)
    selectV4_button.destroy()
    selectV4_button = tk.Button(root, text='Select', bg='gray', command=lambda: select(4, selected))
    selectV4_button.place(x=340, y=20, width=80, height=30)
        


    

    if selected == 1:
        selectV1_button.destroy()
        selectV1_button = tk.Button(root, text='Select', bg='green', command=lambda: select(1, selected))
        selectV1_button.place(x=40, y=20, width=80, height=30)
    elif selected == 2:
        selectV2_button.destroy()
        selectV2_button = tk.Button(root, text='Select', bg='green', command=lambda: select(2, selected))
        selectV2_button.place(x=140, y=20, width=80, height=30)
    elif selected == 3:
        selectV3_button.destroy()
        selectV3_button = tk.Button(root, text='Select', bg='green', command=lambda: select(3, selected))
        selectV3_button.place(x=240, y=20, width=80, height=30)
    elif selected == 4:
        selectV4_button.destroy()
        selectV4_button = tk.Button(root, text='Select', bg='green', command=lambda: select(4, selected))
        selectV4_button.place(x=340, y=20, width=80, height=30)


    print(selected)

def pour():
    global select, selectV1_button, selectV2_button, selectV3_button, selected, selectV4_button
    


while True:
    if all(count == color_limit for count in color_counts.values()):
        break
    
    rColor = random.choice(colors)
    if color_counts[rColor] < color_limit:
        result.append(rColor)
        color_counts[rColor] += 1

white = '#FFFFFF'

rColor1, rColor2, rColor3, rColor4, rColor5, rColor6, rColor7, rColor8, rColor9, rColor10, rColor11, rColor12, rColor13, rColor14, rColor15, rColor16 = result
print(result)

root = tk.Tk()
root.geometry('500x400')
root.title('Water Sort Puzzle')
root.config(bg='light gray')   

canvas = tk.Canvas(root, width = 1000, height = 1000, bg=white)
canvas.pack()

# region beaker1

selectV1_button = tk.Button(root, text='Select', bg='gray', command=lambda: select(1, selected))
selectV1_button.place(x=40, y=20, width=80, height=30)

canvas.create_arc(50, 300, 105, 234, start=180, extent=180, fill=rColor1, outline='black', width=1.5, tags=('beaker1')) #bottom
canvas.create_rectangle(50, 227, 105, 267, fill=rColor2, width=1.5, outline='black', tags=('beaker1')) #2nd layer
canvas.create_line(51, 267, 104, 267, fill=rColor1, width=1.5, tags=('beaker1')) #bottom line
canvas.create_rectangle(50, 187, 105, 227, fill=rColor3, width=1.5, outline='black', tags=('beaker1')) #3rd layer
canvas.create_line(51, 227, 104, 227, fill=rColor2, width=1.5, tags=('beaker1')) #2nd line
canvas.create_rectangle(50, 147, 105, 187, fill=rColor4, width=1.5, outline='black', tags=('beaker1')) #4th layer
canvas.create_line(51, 187, 104, 187, fill=rColor3, width=1.5, tags=('beaker1')) #3rd line
canvas.create_rectangle(50, 107, 105, 147, fill=white, width=1.5, outline='black', tags=('beaker1')) #5th layer
canvas.create_line(51, 147, 104, 147, fill=rColor4, width=1.5, tags=('beaker1')) #4th line
canvas.create_rectangle(50, 67, 105, 107, fill=white, width=1.5, outline='black', tags=('beaker1')) #6th layer
canvas.create_line(51, 107, 104, 107, fill=white, width=1.5, tags=('beaker1')) #5th line
canvas.create_line(51, 67, 104, 67, fill=white, width=1.5, tags=('beaker1')) #6th line

canvas.move('beaker1', 0, 0)
# endregion

# region beaker2

selectV2_button = tk.Button(root, text='Select', bg='gray', command=lambda: select(2, selected))
selectV2_button.place(x=140, y=20, width=80, height=30)

canvas.create_arc(50, 300, 105, 234, start=180, extent=180, fill=rColor5, outline='black', width=1.5, tags=('beaker2')) #bottom
canvas.create_rectangle(50, 227, 105, 267, fill=rColor6, width=1.5, outline='black', tags=('beaker2')) #2nd layer
canvas.create_line(51, 267, 104, 267, fill=rColor5, width=1.5, tags=('beaker2')) #bottom line
canvas.create_rectangle(50, 187, 105, 227, fill=rColor7, width=1.5, outline='black', tags=('beaker2')) #3rd layer
canvas.create_line(51, 227, 104, 227, fill=rColor6, width=1.5, tags=('beaker2')) #2nd line
canvas.create_rectangle(50, 147, 105, 187, fill=rColor8, width=1.5, outline='black', tags=('beaker2')) #4th layer
canvas.create_line(51, 187, 104, 187, fill=rColor7, width=1.5, tags=('beaker2')) #3rd line
canvas.create_rectangle(50, 107, 105, 147, fill=white, width=1.5, outline='black', tags=('beaker2')) #5th layer
canvas.create_line(51, 147, 104, 147, fill=rColor8, width=1.5, tags=('beaker2')) #4th line
canvas.create_rectangle(50, 67, 105, 107, fill=white, width=1.5, outline='black', tags=('beaker2')) #6th layer
canvas.create_line(51, 107, 104, 107, fill=white, width=1.5, tags=('beaker2')) #5th line
canvas.create_line(51, 67, 104, 67, fill=white, width=1.5, tags=('beaker2')) #6th line



canvas.move('beaker2', 100, 0)
# endregion

# region beaker3

selectV3_button = tk.Button(root, text='Select', bg='gray', command=lambda: select(3, selected))
selectV3_button.place(x=240, y=20, width=80, height=30)

canvas.create_arc(50, 300, 105, 234, start=180, extent=180, fill=rColor9, outline='black', width=1.5, tags=('beaker3')) #bottom
canvas.create_rectangle(50, 227, 105, 267, fill=rColor10, width=1.5, outline='black', tags=('beaker3')) #2nd layer
canvas.create_line(51, 267, 104, 267, fill=rColor9, width=1.5, tags=('beaker3')) #bottom line
canvas.create_rectangle(50, 187, 105, 227, fill=rColor11, width=1.5, outline='black', tags=('beaker3')) #3rd layer
canvas.create_line(51, 227, 104, 227, fill=rColor10, width=1.5, tags=('beaker3')) #2nd line
canvas.create_rectangle(50, 147, 105, 187, fill=rColor12, width=1.5, outline='black', tags=('beaker3')) #4th layer
canvas.create_line(51, 187, 104, 187, fill=rColor11, width=1.5, tags=('beaker3')) #3rd line
canvas.create_rectangle(50, 107, 105, 147, fill=white, width=1.5, outline='black', tags=('beaker3')) #5th layer
canvas.create_line(51, 147, 104, 147, fill=rColor12, width=1.5, tags=('beaker3')) #4th line
canvas.create_rectangle(50, 67, 105, 107, fill=white, width=1.5, outline='black', tags=('beaker3')) #6th layer
canvas.create_line(51, 107, 104, 107, fill=white, width=1.5, tags=('beaker3')) #5th line
canvas.create_line(51, 67, 104, 67, fill=white, width=1.5, tags=('beaker3')) #6th line

canvas.move('beaker3', 200, 0)

# endregion

# region beaker4

selectV4_button = tk.Button(root, text='Select', bg='green', command=lambda: select(4, selected))
selectV4_button.place(x=340, y=20, width=80, height=30)

canvas.create_arc(50, 300, 105, 234, start=180, extent=180, fill=rColor13, outline='black', width=1.5, tags=('beaker4')) #bottom
canvas.create_rectangle(50, 227, 105, 267, fill=rColor14, width=1.5, outline='black', tags=('beaker4')) #2nd layer
canvas.create_line(51, 267, 104, 267, fill=rColor13, width=1.5, tags=('beaker4')) #bottom line
canvas.create_rectangle(50, 187, 105, 227, fill=rColor15, width=1.5, outline='black', tags=('beaker4')) #3rd layer
canvas.create_line(51, 227, 104, 227, fill=rColor14, width=1.5, tags=('beaker4')) #2nd line
canvas.create_rectangle(50, 147, 105, 187, fill=rColor16, width=1.5, outline='black', tags=('beaker4')) #4th layer
canvas.create_line(51, 187, 104, 187, fill=rColor15, width=1.5, tags=('beaker4')) #3rd line
canvas.create_rectangle(50, 107, 105, 147, fill=white, width=1.5, outline='black', tags=('beaker4')) #5th layer
canvas.create_line(51, 147, 104, 147, fill=rColor16, width=1.5, tags=('beaker4')) #4th line
canvas.create_rectangle(50, 67, 105, 107, fill=white, width=1.5, outline='black', tags=('beaker4')) #6th layer
canvas.create_line(51, 107, 104, 107, fill=white, width=1.5, tags=('beaker4')) #5th line
canvas.create_line(51, 67, 104, 67, fill=white, width=1.5, tags=('beaker4')) #6th line

canvas.move('beaker4', 300, 0)

# endregion


clear_button = tk.Button(root, text='Clear', command=clear_selection)
clear_button.place(x=10, y=350, width=80, height=30)

root.mainloop()