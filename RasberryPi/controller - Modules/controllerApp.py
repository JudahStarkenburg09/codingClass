import controllerModule
import threading
import tkinter as tk
import pygame

pygame.init()
pygame.joystick.init()

root = tk.Tk()
root.title("Joystick Graphics")
root.geometry(f"700x500+200+100")

def create_text(root, x, y, font_size, text_content, color, bgColor):
    # Create a transparent label
    text_label = tk.Label(root, text=text_content, font=("Arial", font_size), fg=color, bg=bgColor)
    text_label.place(x=x, y=y)  # Set the position of the label
    return text_label

triangle = create_text(root, 10, 460, 16, "▲", "green", "gray")
square = create_text(root, 40, 460, 16, "⬜", "pink", "gray")
circle = create_text(root, 78, 460, 16, "🔴", "red", "gray")
ex = create_text(root, 110, 460, 16, "❌", "blue", "gray")
L1 = create_text(root, 150, 460, 16, "L1", "white", "gray")
R1 = create_text(root, 185, 460, 16, "R1", "white", "gray")

# Create a canvas widget for the left joystick (joystickBaseLeft)
canvas_left = tk.Canvas(root, width=300, height=300)
canvas_left.pack(side=tk.LEFT)  # Place it on the left side of the window
# Create the light gray oval for the left joystick base (joystickBaseLeft)
joystickBaseLeft = canvas_left.create_oval(150, 200, 250, 300, fill="light gray")
# Create the smaller dark gray oval for the left joystick (JoystickLeft)
JoystickLeft = canvas_left.create_oval(75, 125, 125, 175, fill="dark gray")
# Create a canvas widget for the right joystick (joystickBaseRight)
canvas_right = tk.Canvas(root, width=300, height=300)
canvas_right.pack(side=tk.LEFT)  # Place it on the right side of the window
# Create the light gray oval for the right joystick base (joystickBaseRight)
joystickBaseRight = canvas_right.create_oval(150, 200, 250, 300, fill="light gray")
# Create the smaller dark gray oval for the right joystick (JoystickRight)
JoystickRight = canvas_right.create_oval(75, 125, 125, 175, fill="dark gray")


joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]

def moveJoysticks(joysticks):
    pygame.event.get()
    leftJoystickPos = controllerModule.leftJSAxis(joysticks)
    rightJoystickPos = controllerModule.rightJSAxis(joysticks)


    centerXleft, centerYleft = controllerModule.convertJSAxisToCoords(200, 250, 25, leftJoystickPos[0], leftJoystickPos[1])
    canvas_left.coords(JoystickLeft, centerXleft - 25, centerYleft - 25, centerXleft + 25, centerYleft + 25)
    
    centerXright, centerYright = controllerModule.convertJSAxisToCoords(200, 250, 25, rightJoystickPos[0], rightJoystickPos[1])
    canvas_right.coords(JoystickRight, centerXright - 25, centerYright - 25, centerXright + 25, centerYright + 25)

def getButtons():
    global ex, triangle, square, circle, L1, R1
    buttonsPressed = controllerModule.getPressedButtons(pygame.event.get())
    print(f"'{buttonsPressed}'")
    for i in buttonsPressed:
        buttonPressed  = i
        if buttonPressed == 'X':
            ex.config(bg='black')
        elif buttonPressed == 'O':
            circle.config(bg='black')
        elif buttonPressed == 'Square':
            square.config(bg='black')
        elif buttonPressed == "Triangle":
            triangle.config(bg='black')
        elif buttonPressed == 'L1':
            L1.config(bg='black')
        elif buttonPressed == 'R1':
            R1.config(bg='black')
        elif buttonPressed == 'Right Joystick PRESS':
            canvas_right.itemconfig(JoystickRight, fill='black')
        elif buttonPressed == 'Left Joystick PRESS':
            canvas_left.itemconfig(JoystickLeft, fill='black')




def whileLoop(joysticks):
    moveJoysticks(joysticks)
    getButtons()
    root.after(20, lambda: whileLoop(joysticks))

root.after(0, lambda: whileLoop(joysticks))

root.mainloop()



