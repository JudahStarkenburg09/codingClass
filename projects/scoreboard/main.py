import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.geometry('500x400')
root.title(" ")

def toggle_fullscreen(event=None):
    global colorLeft, colorRight
    state = not root.attributes('-fullscreen')
    root.attributes('-fullscreen', state)
    if root.attributes('-fullscreen'):
        toast = tk.Label(root, text='Press f11 to toggle fullscreen', background='gray', foreground='white')
        toast.place(x=root.winfo_screenwidth() / 2, y=15, anchor='center')
        root.after(2000, lambda: toast.destroy())
    else: 
        toast = tk.Label(root, text='Press f11 to toggle fullscreen', background='gray', foreground='white')
        toast.place(x=250, y=15, anchor='center')
        root.after(2000, lambda: toast.destroy())
    


screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

print(f"Screen Width: {screen_width}")
print(f"Screen Height: {screen_height}")

# Bind F11 key to toggle fullscreen
root.bind("<F11>", toggle_fullscreen)

canvas = tk.Canvas(width=10000, height=10000, bg='black')
canvas.pack()

def graphics():
    global colorLeft, colorRight, left, right, score_labelR, score_labelL
    if root.attributes('-fullscreen'):
        posxl = root.winfo_screenwidth() / 2 - 7.5
        posxr2 = root.winfo_screenwidth() - 15
        posxr1 = root.winfo_screenwidth() / 2 + 7.5
        posyb = root.winfo_screenheight() - 15
        posyt = 250
        posxScoreL = (10 + posxl) / 2
        posyScoreL = (posyt + posyb) / 2
        posxScoreR = (posxr1 + posxr2) / 2
        posyScoreR = (posyt + posyb) / 2
        fontSize = 300
    else:
        posxl = 245
        posxr2 = 490
        posxr1 = 255
        posyb = 390
        posyt = 100
        posxScoreL = (10 + posxl) / 2
        posyScoreL = (posyt + posyb) / 2
        posxScoreR = (posxr1 + posxr2) / 2
        posyScoreR = (posyt + posyb) / 2
        fontSize = 125

    if left and right:
        canvas.delete(left)
        canvas.delete(right)
        canvas.delete(score_labelL)
        canvas.delete(score_labelR)
    left = canvas.create_rectangle(10, posyt, posxl, posyb, fill=colorLeft)
    right = canvas.create_rectangle(posxr1, posyt, posxr2, posyb, fill=colorRight)
    score_labelL = canvas.create_text(posxScoreL, posyScoreL, text=str(scoreL), fill="white", font=("Helvetica", fontSize), anchor="center")
    score_labelR = canvas.create_text(posxScoreR, posyScoreR, text=str(scoreR), fill="white", font=("Helvetica", fontSize), anchor="center")
    root.after(100, graphics)

scoreL = 10
scoreR = 26

left = None
right = None
score_labelL = None
score_labelR = None

root.after(0, graphics)

colorLeft = "#ff0000"
colorRight = "#0000ff"

root.mainloop()
