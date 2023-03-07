from tkinter import *
import random

window = Tk()
window.geometry('300x300')

canvas = Canvas(window, width=250, height=250, bg="white")
canvas.pack()

# create the square shape
square = canvas.create_rectangle(60, 60, 100, 100, fill="white")

# define the checkmark line coordinates
checkmark_coords = [(70, 80), (80, 90), (95, 70)]

# create a boolean variable to keep track of whether the checkbox is checked
checked = False

# create a function to handle checkbox clicks
def on_checkbox_click(event):
    global checked
    if not checked:
        # draw the checkmark line on top of the square
        canvas.create_line(*checkmark_coords, width=3, fill="black")
        checked = True
    else:
        # delete the checkmark line
        canvas.delete("all")
        canvas.create_rectangle(60, 60, 100, 100, fill="white", width=2)
        checked = False

# bind the click event to the square
canvas.tag_bind(square, "<Button-1>", on_checkbox_click)

window.mainloop()




def captcha():
    window.destroy()
    root = Tk()
    root.geometry('400x400')

    canvas = Canvas(root, width=300, height=300)
    canvas.pack()

    shapes = ["square", "triangle", "circle"]
    colors = ["red", "green", "blue", "yellow", "orange", "cyan", "pink", "purple", "gray"]
    listOfCombos = []




    positions = []
    for i in range(3):
        for j in range(3):
            x1 = i * 100 + 10
            y1 = j * 100 + 10
            x2 = x1 + 80
            y2 = y1 + 80
            positions.append([x1, y1, x2, y2])

    for i in range(9):
        shape_choice = random.choice(shapes)
        square_choice = random.choice(positions)
        positions.remove(square_choice)
        color_choice = random.choice(colors)
        colors.remove(color_choice)
        if shape_choice == "square":
            shape = canvas.create_rectangle(square_choice[0], square_choice[1], square_choice[2], square_choice[3], fill=color_choice)
        elif shape_choice == "triangle":
            x1, y1 = square_choice[0] + 40, square_choice[1] + 10
            x2, y2 = square_choice[2] - 10, square_choice[3] - 10
            x3, y3 = square_choice[0] + 10, square_choice[3] - 10
            shape = canvas.create_polygon(x1, y1, x2, y2, x3, y3, fill=color_choice)
        elif shape_choice == "circle":
            shape = canvas.create_oval(square_choice[0], square_choice[1], square_choice[2], square_choice[3], fill=color_choice, outline="")
        canvas.tag_bind(shape, "<Button-1>", lambda event, shape=shape_choice, color=color_choice: on_click(event, shape, color))
        listOfCombos.append(f"{color_choice} {shape_choice}")


    clickOn = random.choice(listOfCombos)
    text_label = Label(root, text=f"To Verify You Are Human, Click a {clickOn}")
    text_label.pack(side=BOTTOM)

    def on_click(event, shape, color):
        print(f"You clicked on a {color} {shape}.")
        clicked = f"{color} {shape}"
        if clickOn == clicked:
            print("Human Verified")
        else:
            print("FALSE")

    root.mainloop()



window.mainloop()
