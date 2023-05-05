import tkinter as tk
whitish = '#B6B6B6' #Order from lightest to darkest
light_gray = '#8A8A8A'
lighterish_gray = '#4D4D4D'
lightish_gray = '#3F3F3F'
darkGray = '#343434'
hotPinkRed = '#FF69B4'
font = ("Arial", 15)

# Create a Tkinter window
root = tk.Tk()
root.geometry("500x400")
root.config(bg=darkGray)

# Create a canvas to draw on
canvas = tk.Canvas(root, width=2000, height=2000)
canvas.config(bg=darkGray)
canvas.pack()

rect1 = canvas.create_rectangle(0, 100, 500, 150, fill=lightish_gray, outline=lighterish_gray, width=.5)
rect2 = canvas.create_rectangle(0, 150, 500, 200, fill=lightish_gray, outline=lighterish_gray, width=.5)

# region User Symbol


# Create a cicle
circle = canvas.create_oval(66.7, 66.7, 133.3, 133.3, fill=None, outline=light_gray, width=1.5, tags=('userSymbol'))

# Create a half circle, Create a line to close off the bottom
half_circle = canvas.create_arc(50, 134, 150, 234, start=0, extent=180, fill=None, outline=light_gray, style="arc", width=1.5, tags=('userSymbol'))
#                                X   Y   X    Y                        
line1 = canvas.create_line(48, 184, 152, 184, width=1.5, fill=light_gray, tags=('userSymbol'))
#                           X   Y    X    Y



# endregion

canvas.scale('userSymbol', 0, 0, .18, .18)  # shrink the size of the symbol
canvas.move('userSymbol', 33, 101)



# region Lock Symbol


# Create the base
base = canvas.create_arc(50, 50, 150, 150, start=20, extent=-220, style="chord",fill=None, outline=light_gray, width=2, tags=('lockSymbol',))

# Create the loop
loop = canvas.create_arc(60, 30, 140, 140, start=0, extent=180, style="arc",fill=None, outline=light_gray, width=2, tags=('lockSymbol',))

# Create the keyhole
keyhole = canvas.create_oval(90, 100, 110, 120, fill=None, outline=light_gray, tags=('lockSymbol',))


# endregion


# Scale and move the symbol
canvas.scale('lockSymbol', 0, 0, 0.2, 0.2)
canvas.move('lockSymbol', 30, 155)




# Create entry box with initial text and color
username_entry = tk.Entry(canvas, width=37, fg=light_gray, font=font, bd=0, insertbackground=lighterish_gray) #border=.5,)
username_entry.insert(0, 'Username')
username_entry.configure({"background": lightish_gray})

# Define functions to handle focus and unfocus events
def on_entry_click1(event):
    if username_entry.get() == 'Username':
        username_entry.delete(0, "end") # Delete all the text in the entry
        username_entry.configure(fg=whitish)

def on_entry_unfocus1(event):
    if len(username_entry.get()) == 0:
        username_entry.configure(fg=light_gray)
        username_entry.insert(0, 'Username')


# Bind focus and unfocus events to entry box
username_entry.bind('<FocusIn>', on_entry_click1)
username_entry.bind('<FocusOut>', on_entry_unfocus1)

# Place entry box on canvas
canvas.create_window(280, 125, window=username_entry)

# Create entry box with initial text and color
password_entry = tk.Entry(canvas, width=37, fg=light_gray, font=font, bd=0, insertbackground=lighterish_gray) #border=.5,)
password_entry.insert(0, 'Password')
password_entry.configure({"background": lightish_gray})

def toggle_password_visibility():
    
    global hide_password
    if hide_password:
        # Show the password
        password_entry.config(show='*')
        hide_password = False
    else:
        # Hide the password
        password_entry.config(show='')
        hide_password = True

# Define functions to handle focus and unfocus events
def on_entry_click2(event):
    global hide_password
    if password_entry.get() == 'Password':
        password_entry.delete(0, "end") # Delete all the text in the entry
        password_entry.configure(fg=whitish)
        hide_password = True

        toggle_password_visibility()
def on_entry_unfocus2(event):
    global hide_password
    if len(password_entry.get()) == 0:
        password_entry.configure(fg=light_gray)
        password_entry.insert(0, 'Password')
        hide_password = False

        toggle_password_visibility()



# Bind focus and unfocus events to entry box
password_entry.bind('<FocusIn>', on_entry_click2)
password_entry.bind('<FocusOut>', on_entry_unfocus2)

# Place entry box on canvas
canvas.create_window(280, 175, window=password_entry)

# Define function to remove focus from canvas
def remove_focus(event):
    root.focus()

# Bind the function to the '<Button-1>' event of the canvas
canvas.bind('<Button-1>', remove_focus)

# button = tk.Button(text='Login', command=lambda: print("clicked"), bg=lightish_gray, fg=whitish, activebackground=lighterish_gray, activeforeground=whitish, padx=10, pady=5, highlightthickness=0, font=('Arial', 10, 'bold'), relief='solid', bd=1, borderwidth=1, highlightbackground='black')

# canvas.create_window(250, 200, window=button)



hide_password = False

# region eye Symbol

# Create a circle
circle = canvas.create_oval(27.2, 17.2, 42.8, 32.8, fill="black", outline="black", tags=('eyeShowPassword'))
# Create a half circle, Create a line to close off the bottom
half_circle = canvas.create_arc(0, 0, 70, 60, start=0, extent=180, fill="black", outline="black", style="arc", width=4, tags=('eyeShowPassword'))
rectToBindEye = canvas.create_rectangle(-5, -5, 75, 40, fill=None, outline=None, width=0,tags=('eyeShowPassword'))
# endregion

canvas.scale('eyeShowPassword', 0, 0, 0.3, 0.3)  # shrink the size of the symbol
canvas.move('eyeShowPassword', 450, 180)  # move the symbol with x, y directional pixel





canvas.tag_bind(rectToBindEye, "<Button-1>", lambda event: toggle_password_visibility())



root.mainloop()