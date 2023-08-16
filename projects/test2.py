import tkinter as tk
import random
from tkinter import messagebox

colors = ['red', 'orange', 'yellow', 'blue']
color_counts = {color: 0 for color in colors}
color_limit = 6

result = []

while True:
    if all(count == color_limit for count in color_counts.values()):
        break
    
    rColor = random.choice(colors)
    if color_counts[rColor] < color_limit:
        result.append(rColor)
        color_counts[rColor] += 1

def pour_color(vial_index):
    selected_vial = vial_buttons[vial_index]
    if selected_vial['color_count'] < color_limit:
        selected_color = selected_vial['color']
        if selected_color:
            result_color = result.pop(0)
            selected_vial['color_count'] += 1
            selected_vial['color'] = result_color
            update_vial(selected_vial)
            check_win_condition()

def clear_selection():
    for vial in vial_buttons:
        vial['selected'] = False
        update_vial(vial)

def update_vial(vial):
    canvas.itemconfig(vial['color_rectangle'], fill=vial['color'])
    if vial['color_count'] >= color_limit:
        canvas.itemconfig(vial['button'], state=tk.DISABLED)
    else:
        canvas.itemconfig(vial['button'], state=tk.NORMAL)
    if vial['selected']:
        canvas.itemconfig(vial['button'], bg='green')
    else:
        canvas.itemconfig(vial['button'], bg='SystemButtonFace')

def check_win_condition():
    win = all(vial['color'] == vial['color'] * color_limit for vial in vial_buttons)
    if win:
        messagebox.showinfo("Congratulations!", "You've won the game!")

def vial_button_click(vial_index):
    clear_selection()
    vial_buttons[vial_index]['selected'] = True
    update_vial(vial_buttons[vial_index])

root = tk.Tk()
root.geometry('500x400')
root.title('Water Sort Puzzle')
root.config(bg='light gray')

canvas = tk.Canvas(root, width=500, height=400, bg='white')
canvas.pack()

vial_buttons = []

for i in range(4):
    vial_color = result.pop(0)
    vial = {
        'color': vial_color,
        'color_count': 1,
        'selected': False,
    }
    
    vial['color_rectangle'] = canvas.create_rectangle(
        50 + i * 115, 150, 150 + i * 115, 350,
        fill='white', outline='black', width=1.5
    )
    
    vial['button'] = tk.Button(
        root, text='Vial {}'.format(i + 1),
        command=lambda index=i: vial_button_click(index)
    )
    vial['button'].place(x=50 + i * 115, y=110, width=100, height=30)
    
    vial_buttons.append(vial)

clear_button = tk.Button(root, text='Clear', command=clear_selection)
clear_button.place(x=10, y=350, width=80, height=30)

root.mainloop()
