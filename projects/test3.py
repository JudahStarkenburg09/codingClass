import tkinter as tk

class Button:
    def __init__(self, canvas, buttonx, i, button_click):
        self.canvas = canvas
        self.buttonx = buttonx
        self.i = i
        self.button_click = button_click
        self.draw_buttons()
        
    def draw_buttons(self):
        self.button = tk.Button(self.canvas, text="Select", command=lambda: self.button_click(self.i + 1))
        x_position = self.buttonx + 75  # Adjust the x-coordinate for each button
        self.canvas.create_window(x_position, 45, window=self.button)

def button_click(index):
    print(f"Button {index} clicked!")

root = tk.Tk()
root.title("Button Example")

canvas = tk.Canvas(root, width=600, height=150)
canvas.pack()

buttons = []
for i in range(4):
    button = Button(canvas, i * 150, i, button_click)
    buttons.append(button)

root.mainloop()
