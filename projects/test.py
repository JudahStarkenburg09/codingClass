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

rect1 = canvas.create_rectangle(50, 100, 200, 150, fill=lightish_gray, outline=lighterish_gray, width=.5)
canvas.create_arc(100, 134, 150, 200, start=90, extent=-180, fill=None, outline=light_gray, style="arc", width=1.5)

root.mainloop()