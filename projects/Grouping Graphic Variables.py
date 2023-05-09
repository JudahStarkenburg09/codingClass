import tkinter as tk
clicks = 0
# Define the function to be executed when the button is clicked
def clicked(event):
    global clicks
    clicks += 1
    print(f"Button clicked! Click #{clicks}")

# Create a Tkinter window
root = tk.Tk()
root.geometry("700x500")

# Create a canvas to draw on
canvas = tk.Canvas(root, width=700, height=500)
canvas.pack()


# region button
# Create the button symbol using create methods
canvas_bg_color = canvas.cget('background')

leftCircleSubmitBind = canvas.create_arc(150, 100, 230, 150, start=90, extent=180, width=0, outline=canvas_bg_color, tags=('submit'), fill=canvas_bg_color) #set fill to bg color
rightCircleSubmitBind = canvas.create_arc(460, 100, 540, 150, start=90, extent=-180, width=0, outline=canvas_bg_color, tags=('submit'), fill=canvas_bg_color) #set fill to bg color

rectBaseSubmit = canvas.create_rectangle(190, 100, 500, 150, fill=None, outline=None, width=0, tags=('submit'))
rectBaseTop = canvas.create_line(190, 100, 500, 100, width=1.5, fill='#E73E8F', tags=('submit'))
rectBaseBottom = canvas.create_line(190, 150, 500, 150, width=1.5, fill='#E73E8F', tags=('submit'))
leftCircleSubmit = canvas.create_arc(150, 100, 230, 150, start=90, extent=180, style="arc", width=1.5, outline='#E73E8F', tags=('submit'))
rightCircleSubmit = canvas.create_arc(460, 100, 540, 150, start=90, extent=-180, style="arc", width=1.5, outline='#E73E8F', tags=('submit'))

# endregion button

# Bind the clicked function to the left mouse button click event on the button symbol
canvas.tag_bind('submit', '<Button-1>', clicked)

canvas.scale('submit', 0, 0, .5, .5)
canvas.move()

# Start the Tkinter main loop
root.mainloop()
