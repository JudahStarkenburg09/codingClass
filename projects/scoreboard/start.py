import tkinter as tk
from tkinter import messagebox
from tkinter import font



def handelGraphics(timer, timerValuestr, possession, switch, team1, team2, coloredSides, icon1, icon2, hasPeriod):
    global switchPossible, currentPos, timerBase, keybinds, toggle_fullscreen, update_scores, period, periodPossible
    global root, colorLeft, colorRight, left, right, score_labelL, score_labelR, scoreL, scoreR, side, timerValue, paused, timerText, possessionPossible
    timerValue = timerValuestr
    scoreL = 0
    scoreR = 0
    paused = True
    side = "left"
    possessionPossible = possession
    if possessionPossible == True:
        currentPos = '<'
    periodPossible = False
    if hasPeriod:
        periodPossible = True
        period = 1
    switchPossible = switch
    keybinds = """Press (Q, W) to change left score
Press (O, P) to change right score
Press space to switch sides
Press T to start/pause the timer
Press F11 To Toggle Fullscreen
Press arrow keys (< >) to change possession
Press Enter to Reset Timer
Press Ctrl + Enter to Reset Score, Possession, and Timer
Press F1 to show Keybinds again / Open Live Window"""
    messagebox.showinfo("Keybinds", keybinds)

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


    def update_scores(event, keysubl='w', keyaddl='q', keysubr='o', keyaddr='p', keyreset='Return'):
        global scoreL, scoreR, side, colorLeft, colorRight, side, timerValue, paused, possessionPossible, switchPossible, currentPos, keybinds

        if event.keysym == keyaddl:
            if side == "left":
                scoreL += 1
            else:
                scoreR += 1
        elif event.keysym == keysubl:
            if side == "left":
                scoreL -= 1
            else:
                scoreR -= 1
        elif event.keysym == keysubr:
            if side == "left":
                scoreR -= 1
            else:
                scoreL -= 1
        elif event.keysym == keyaddr:
            if side == "left":
                scoreR += 1
            else:
                scoreL += 1
        elif event.keysym == 'space':
            if switchPossible:
                if side == "left":
                    side = "right"
                else:
                    side = "left"
        elif event.keysym == "Return" and event.state == 0x4:  # 0x4 represents the Control key
            paused = True
            timerValue = timerValuestr
            scoreL = 0
            scoreR = 0
        elif event.keysym == "Return":
            paused = True
            timerValue = timerValuestr
        elif event.keysym == 't':
            if paused:
                paused = False
            else:
                paused = True
        elif event.keysym == "F1":
            show_keybinds(keysubl, keyaddl, keysubr, keyaddr, keyreset)




    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    keysubl = 'w'
    keyaddl = 'q'
    keysubr = 'o'
    keyaddr = 'p'
    keyreset = 'Return'

    root.bind("<F11>", toggle_fullscreen)
    root.bind("<Key>", lambda event: update_scores(event, keysubl, keyaddl, keysubr, keyaddr, keyreset))

    canvas = tk.Canvas(width=10000, height=10000, bg='black')
    canvas.pack()

    def graphics():
        global colorLeft, colorRight, left, right, score_labelR, score_labelL, side, colorRight, colorLeft, timerValue, timerText, timerBase
        if root.attributes('-fullscreen'):
            posxl = root.winfo_screenwidth() / 2 - 7.5
            posxr2 = root.winfo_screenwidth() - 15
            posxr1 = root.winfo_screenwidth() / 2 + 7.5
            posyb = root.winfo_screenheight() - 15
            posxT = root.winfo_screenwidth() / 2
            posyT = 110
            scoreFontSize = 175
            posyt = 230
            posxScoreL = (10 + posxl) / 2
            posyScoreL = (posyt + posyb) / 2
            posxScoreR = (posxr1 + posxr2) / 2
            posyScoreR = (posyt + posyb) / 2
            fontSize = 300
            tBase1 = posxT - 200
            tBase2 = -10
            tBase3 = posxT + 200
            tBase4 = posyT + 100
        else:
            posxT = 250
            scoreFontSize = 100
            posyT = 40
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
            tBase1 = posxT - 100
            tBase2 = -10
            tBase3 = posxT + 100
            tBase4 = posyT + 60

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

        if timerText:
            canvas.delete(timerText)
        timerText = canvas.create_text(posxT, posyT, text=f"{timerValue}", fill="red", font=font.Font(family='ds-digital', size=(scoreFontSize-50)), anchor="center")
        if timer:
            if timerBase:
                canvas.delete(timerBase)
            timerBase = canvas.create_rectangle(tBase1, tBase2, tBase3, tBase4, fill=None, outline='gray', width=2)

        root.after(100, graphics)

    timerText = None
    timerBase = None
    print("here1")
    def timerFunction():
        global root, timerValue, paused

        minutes, seconds = map(int, timerValue.split(":"))

        # Convert minutes and seconds to total seconds
        total_seconds = minutes * 60 + seconds
        
        if not paused:
            # Decrement total seconds
            if total_seconds > 10:
                total_seconds -= 1
            else:
                total_seconds -= .01

            # Calculate new minutes and seconds
            new_minutes = total_seconds // 60
            new_seconds = total_seconds % 60

            # Format the new values
            minutes_str = f"{new_minutes:02d}"
            seconds_str = f"{new_seconds:02d}"

            # Update timerValue
            timerValue = f"{minutes_str}:{seconds_str}"

            print(timerValue)

            if total_seconds > 0:
                # If there are remaining seconds, continue the countdown
                pass
            else:
                print("Timer reached 0:00")
                # Perform actions when timer reaches 0:00
        if total_seconds > 10:
            root.after(1000, timerFunction)
        else:
            root.after(10, timerFunction)

    left = None
    right = None
    score_labelL = None
    score_labelR = None
    print("here2")
    root.after(0, graphics)
    if timer:
        root.after(0, timerFunction)
    colorLeft = "#ff0000"
    colorRight = "#0000ff"



    print("here3")
    root.mainloop()

def show_keybinds(keysubl, keyaddl, keysubr, keyaddr, keyreset):
    global root, keybinds
    
    # Create a new window
    keybinds_window = tk.Toplevel(root)
    keybinds_window.title("Live Window")

    # Create a label to display the keybinds
    label = tk.Label(keybinds_window, text=keybinds, padx=10, pady=10)
    label.pack()

    # Create an OK button to close the window
    ok_button = tk.Button(keybinds_window, text="OK", command=keybinds_window.destroy)
    ok_button.pack(pady=10)
    keybinds_window.bind("<F11>", toggle_fullscreen)
    keybinds_window.bind("<Key>", lambda event: update_scores(event, keysubl, keyaddl, keysubr, keyaddr, keyreset))

if __name__ == "__main__":
    handelGraphics(True, '04:13', 'possession', 'switch', 'team1', 'team2', False, False, False, True)
