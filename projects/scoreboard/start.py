import tkinter as tk
from tkinter import messagebox
from tkinter import font

def handelGraphics(timer, timerValue, possession, switch, team1, team2, coloredSides, icon1, icon2):
    global root, colorLeft, colorRight, left, right, score_labelL, score_labelR, scoreL, scoreR, side
    scoreL = 0
    scoreR = 0
    side = "left"
    messagebox.showinfo("Info", """Press (Q, W) to change left score
Press (O, P) to change right score
Press space to switch sides
Press T to start/pause the timer
Press F11 To Toggle Fullscreen
Press arrow keys (< >) to change possession
Press Enter to Reset Score, Possession, and Timer
                """)

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

    def update_scores(event):
        global scoreL, scoreR, side, colorLeft, colorRight, side

        if event.keysym == 'q':
            scoreL += 1
        elif event.keysym == 'w':
            scoreL -= 1
        elif event.keysym == 'o':
            scoreR -= 1
        elif event.keysym == 'p':
            scoreR += 1
        elif event.keysym == 'space':
            if side == "left":
                side = "right"
            else:
                side = "left"


    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    root.bind("<F11>", toggle_fullscreen)
    root.bind("<Key>", update_scores)

    canvas = tk.Canvas(width=10000, height=10000, bg='black')
    canvas.pack()

    def graphics():
        global colorLeft, colorRight, left, right, score_labelR, score_labelL, side, colorRight, colorLeft
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

        if (left and right) or (coloredSides == False):
            canvas.delete(score_labelL)
            canvas.delete(score_labelR)

        if side == "left":
            colorLeft = "#ff0000"
            colorRight = "#0000ff"
            if coloredSides:
                left = canvas.create_rectangle(10, posyt, posxl, posyb, fill=colorLeft)
                right = canvas.create_rectangle(posxr1, posyt, posxr2, posyb, fill=colorRight)
            score_labelL = canvas.create_text(posxScoreL, posyScoreL, text=str(scoreL), fill="white", font=font.Font(family='ds-digital', size=fontSize), anchor="center")
            score_labelR = canvas.create_text(posxScoreR, posyScoreR, text=str(scoreR), fill="white", font=font.Font(family='ds-digital', size=fontSize), anchor="center")
        else:
            colorLeft = "#0000ff"
            colorRight = "#ff0000"
            if coloredSides:
                left = canvas.create_rectangle(10, posyt, posxl, posyb, fill=colorLeft)
                right = canvas.create_rectangle(posxr1, posyt, posxr2, posyb, fill=colorRight)
            score_labelL = canvas.create_text(posxScoreL, posyScoreL, text=str(scoreR), fill="white", font=font.Font(family='ds-digital', size=fontSize), anchor="center")
            score_labelR = canvas.create_text(posxScoreR, posyScoreR, text=str(scoreL), fill="white", font=font.Font(family='ds-digital', size=fontSize), anchor="center")


        root.after(100, graphics)

    def timerFunction():
        global timerValue, minutes, seconds
        # print(timerValue)
        minutes, seconds = str(timerValue).split(":")
        minutes = int(minutes)
        seconds = int(seconds)
        seconds -= 1
        if seconds > 0:
            seconds = seconds
        elif seconds < 0:
            seconds = 59
            minutes -= 1
        else:
            print("Failed")
        minutes = str(minutes)
        seconds = str(seconds)
        if len(seconds) == 1:
            seconds = (f"0{seconds}")
        if len(minutes) == 1:
            minutes = (f"0{minutes}")
        timerValue = (f"{minutes}:{seconds}")
        print(timerValue)
        root.after(1000, timerFunction)

    left = None
    right = None
    score_labelL = None
    score_labelR = None

    root.after(0, graphics)
    if timer:
        root.after(0, timerFunction)
    colorLeft = "#ff0000"
    colorRight = "#0000ff"




    root.mainloop()

if __name__ == "__main__":
    handelGraphics(10, 15, 'possession', 'switch', 'team1', 'team2', True)
