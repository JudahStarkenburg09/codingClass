import pygame
import tkinter as tk
import threading
import time

buttonsCorrespondings = [
    {
        "button": 0,
        "correspond": "X",
    },
    {
        "button": 1,
        "correspond": "O",
    },
    {
        "button": 2,
        "correspond": "Square",
    },
    {
        "button": 3,
        "correspond": "Triangle",
    },
    {
        "button": 4,
        "correspond": "Share",
    },
    {
        "button": 6,
        "correspond": "Options",
    },
    {
        "button": 7,
        "correspond": "Left Joystick PRESS",
    },
    {
        "button": 8,
        "correspond": "Right Joystick PRESS",
    },
    {
        "button": 9,
        "correspond": "L1",
    },
    {
        "button": 10,
        "correspond": "R1",
    },
    {
        "button": 11,
        "correspond": "Directional Button Up",
    },
    {
        "button": 12,
        "correspond": "Directional Button Down",
    },
    {
        "button": 13,
        "correspond": "Directional Button Left",
    },
    {
        "button": 14,
        "correspond": "Directional Button Right",
    },
    {
        "button": 15,
        "correspond": "Touchpad Click",
    },
]



pygame.init()
pygame.joystick.init()

# List the available joystick devices
joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]

# Initialize all detected joysticks
for joystick in joysticks:
    joystick.init()
    print(f"Joystick {joystick.get_id()}: {joystick.get_name()}")


root = tk.Tk()
ws = root.winfo_screenwidth() # width of the screen
hs = root.winfo_screenheight() # height of the screen
# Create the main window
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



# Function to update the position of the left joystick (JoystickLeft)
def move_joystick_left():
    while True:
        pygame.event.get()
        left_x_axis = 0
        left_y_axis = 0

        for joystick in joysticks:
            left_x_axis = joystick.get_axis(0)
            left_y_axis = joystick.get_axis(1)
            right_x_axis = joystick.get_axis(2)
            right_y_axis = joystick.get_axis(3)
        # print("Threaded Left")

        # Calculate the position based on left joystick input
        max_displacement_left = 25  # Maximum displacement for the left joystick
        new_x_left = 150 + int(max_displacement_left * left_x_axis)
        new_y_left = 250 + int(max_displacement_left * left_y_axis)

        # Ensure the left joystick (Joystickleft) stays within the left joystick base (joystickBaseleft)
        if new_x_left < 125:
            new_x_left = 125
        elif new_x_left > 175:
            new_x_left = 175
        if new_y_left < 225:
            new_y_left = 225
        elif new_y_left > 275:
            new_y_left = 275

        new_x_left += 50

        canvas_left.coords(JoystickLeft, new_x_left - 25, new_y_left - 25, new_x_left + 25, new_y_left + 25)
        root.update_idletasks()  # Update the tkinter window

def move_joystick_right():
    while True:
        pygame.event.get()  # Get joystick events

        # Initialize variables for the right joystick axes
        right_x_axis = 0
        right_y_axis = 0

        for joystick in joysticks:
            left_x_axis = joystick.get_axis(0)
            left_y_axis = joystick.get_axis(1)
            right_x_axis += joystick.get_axis(2)
            right_y_axis += joystick.get_axis(3)


        # Calculate the position based on right joystick input
        max_displacement_right = 25  # Maximum displacement for the right joystick
        new_x_right = 150 + int(max_displacement_right * right_x_axis)
        new_y_right = 250 + int(max_displacement_right * right_y_axis)

        # Ensure the right joystick (JoystickRight) stays within the right joystick base (joystickBaseRight)
        if new_x_right < 125:
            new_x_right = 125
        elif new_x_right > 175:
            new_x_right = 175
        if new_y_right < 225:
            new_y_right = 225
        elif new_y_right > 275:
            new_y_right = 275
        
        new_x_right += 50

        # Update the position of the right joystick (JoystickRight)
        canvas_right.coords(JoystickRight, new_x_right - 25, new_y_right - 25, new_x_right + 25, new_y_right + 25)
        # print(new_x_right, new_y_right)
        root.update_idletasks()  # Update the tkinter window

def onPress(corresponded):
    global ex, triangle, square, circle, L1, R1
    if corresponded == 'X':
        ex.config(bg='black')
    elif corresponded == 'O':
        circle.config(bg='black')
    elif corresponded == 'Square':
        square.config(bg='black')
    elif corresponded == "Triangle":
        triangle.config(bg='black')
    elif corresponded == 'L1':
        L1.config(bg='black')
    elif corresponded == 'R1':
        R1.config(bg='black')
    elif corresponded == 'Right Joystick PRESS':
        canvas_right.itemconfig(JoystickRight, fill='black')
    elif corresponded == 'Left Joystick PRESS':
        canvas_left.itemconfig(JoystickLeft, fill='black')


def onRelease(corresponded):
    global ex, triangle, square, circle, L1, Ri
    if corresponded == 'X':
        ex.config(bg='gray')
    elif corresponded == 'O':
        circle.config(bg='gray')
    elif corresponded == 'Square':
        square.config(bg='gray')
    elif corresponded == "Triangle":
        triangle.config(bg='gray')
    elif corresponded == 'L1':
        L1.config(bg='gray')
    elif corresponded == 'R1':
        R1.config(bg='gray')
    elif corresponded == 'Right Joystick PRESS':
        canvas_right.itemconfig(JoystickRight, fill='gray')
    elif corresponded == 'Left Joystick PRESS':
        canvas_left.itemconfig(JoystickLeft, fill='gray')


def buttonsClicks():
    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.JOYBUTTONDOWN:
                button_pressed = event.button
                for correspond in buttonsCorrespondings:
                    if correspond["button"] == button_pressed:
                        corresponded = correspond['correspond']
                        onPress(corresponded)
            elif event.type == pygame.JOYBUTTONUP:
                button_released = event.button
                for correspond in buttonsCorrespondings:
                    if correspond["button"] == button_released:
                        corresponded = correspond['correspond']
                        onRelease(corresponded)



# Create threads for joystick movement simulation
thread_left = threading.Thread(target=move_joystick_left)
thread_left.daemon = True
thread_left.start()

thread_right = threading.Thread(target=move_joystick_right)
thread_right.daemon = True
thread_right.start()

thread_click = threading.Thread(target=buttonsClicks)
thread_click.daemon = True
thread_click.start()

# Start the main tkinter loop
root.mainloop()
# print(f"Left Joystick: X={left_x_axis}, Y={left_y_axis}, Right Joystick: X={right_x_axis}, Y={right_y_axis}")

