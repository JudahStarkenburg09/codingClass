import tkinter as tk
from tkinter import messagebox
from tkinter import font
from PIL import Image, ImageTk, ImageFilter

class ScoreboardApp:
    def __init__(self, timer, timer_value_str, possession, switch, team1, team2, colored_sides, home_icon, away_icon, has_period):
        self.timer_value = timer_value_str
        self.home_icon_path = home_icon
        self.away_icon_path = away_icon
        self.away_icon_image = None
        self.home_icon_image = None
        self.score_l = 0
        self.score_r = 0
        self.team1_name = team1
        self.team2_name = team2
        self.paused = True
        self.side = "left"
        self.current_pos = '←'
        self.period_possible = False
        self.period = 1 if has_period else None
        self.switch_possible = switch
        self.keybinds = """Press (Q, W) to change left score
Press (O, P) to change right score
Press space to switch sides
Press T to start/pause the timer
Press F11 To Toggle Fullscreen
Press arrow keys (< >) to change possession
Press Enter to Reset Timer
Press Ctrl + Enter to Reset Score, Possession, and Timer
Press F1 to show Keybinds again / Open Live Window"""
        
        self.root = tk.Tk()
        self.root.geometry('500x400')
        self.root.title(" ")

        self.initialize_gui()

    def initialize_gui(self):
        self.root.bind("<F11>", self.toggle_fullscreen)
        self.root.bind("<Key>", self.update_scores)

        self.canvas = tk.Canvas(width=10000, height=10000, bg='black')
        self.canvas.pack()

        self.left_name = None
        self.right_name = None
        self.timer_text = None
        self.timer_base = None
        self.pos_text = None

        self.root.after(0, self.graphics)
        if self.period:
            self.root.after(0, self.timer_function)

        self.color_left = "#ff0000"
        self.color_right = "#0000ff"

        self.root.mainloop()

    def toggle_fullscreen(self, event=None):
        state = not self.root.attributes('-fullscreen')
        self.root.attributes('-fullscreen', state)
        if self.root.attributes('-fullscreen'):
            toast = tk.Label(self.root, text='Press f11 to toggle fullscreen', background='gray', foreground='white')
            toast.place(x=self.root.winfo_screenwidth() / 2, y=15, anchor='center')
            self.root.after(2000, lambda: toast.destroy())
        else: 
            toast = tk.Label(self.root, text='Press f11 to toggle fullscreen', background='gray', foreground='white')
            toast.place(x=250, y=15, anchor='center')
            self.root.after(2000, lambda: toast.destroy())

    def update_scores(self, event):
        if event.keysym == 'space':
            if self.switch_possible:
                if self.side == "left":
                    self.side = "right"
                else:
                    self.side = "left"
        elif event.keysym == "Return" and event.state == 0x4:
            self.paused = True
            self.timer_value = self.timer_value
            self.score_l = 0
            self.score_r = 0
            self.side = "left"
            self.current_pos = "←"
        elif event.keysym == "Return":
            self.paused = True
            self.timer_value = self.timer_value
            self.current_pos = "→"
        elif event.keysym == 't':
            if self.paused:
                self.paused = False
            else:
                self.paused = True
        elif event.keysym == "F1":
            self.show_keybinds()

    def graphics(self):
        if self.root.attributes('-fullscreen'):
            self.posxl = self.root.winfo_screenwidth() / 2 - 7.5
            self.posxr2 = self.root.winfo_screenwidth() - 15
            self.posxr1 = self.root.winfo_screenwidth() / 2 + 7.5
            self.posyb = self.root.winfo_screenheight() - 15
            self.posxT = self.root.winfo_screenwidth() / 2
            self.posyT = 110
            self.scoreFontSize = 175
            self.posyt = 230
            self.posxScoreL = ((10 + self.posxl) / 2) - 75
            self.posyScoreL = ((self.posyt + self.posyb) / 2) + 25
            self.posxScoreR = ((self.posxr1 + self.posxr2) / 2) - 75
            self.posyScoreR = ((self.posyt + self.posyb) / 2) + 25
            self.fontSize = 300
            self.tBase1 = self.posxT - 200
            self.tBase2 = -10
            self.tBase3 = self.posxT + 200
            self.tBase4 = self.posyT + 100
            self.team1XYSize = [300, 400, 100]
            self.team2XYSize = [1200, 400, 100]
            self.possPos = [800, 350, 75]
            self.imagePosLeft = [300, 200, 250]
            self.imagePosRight = [800, 200, 250]
        else:
            self.posxT = 250
            self.scoreFontSize = 100
            self.posyT = 40
            self.posxl = 245
            self.posxr2 = 490
            self.posxr1 = 255
            self.posyb = 390
            self.posyt = 100
            self.posxScoreL = (10 + self.posxl) / 2
            self.posyScoreL = (self.posyt + self.posyb) / 2
            self.posxScoreR = (self.posxr1 + self.posxr2) / 2
            self.posyScoreR = (self.posyt + self.posyb) / 2
            self.fontSize = 125
            self.tBase1 = self.posxT - 100
            self.tBase2 = -10
            self.tBase3 = self.posxT + 100
            self.tBase4 = self.posyT + 60
            self.team1XYSize = [75, 200, 30]
            self.team2XYSize = [425, 200, 30]
            self.possPos = [250, 175, 50]
            self.imagePosLeft = [75, 100, 100]
            self.imagePosRight = [425, 100, 100]

            if (left and right) or (self.coloredSides == False):
                self.canvas.delete(score_labelL)
                self.canvas.delete(score_labelR)
            if timerText:
                self.canvas.delete(timerText)

            if leftName:
                self.canvas.delete(leftName)
                self.canvas.delete(rightName)

            if posText:
                self.canvas.delete(posText)

            if self.possessionPossible:
                posText = self.canvas.create_text(self.possPos[0], self.possPos[1], text=f"{self.currentPos}", fill="white" ,anchor="center", font=font.Font(family='ds-digital', size=self.possPos[2]))

            if self.side == "left":
                colorLeft = "#ff0000"
                colorRight = "#0000ff"
                leftName = self.canvas.create_text(self.team1XYSize[0], self.team1XYSize[1], anchor='center', text=f"{self.team1Name}", fill="white", font=font.Font(family='ds-digital', size=self.team1XYSize[2]))
                rightName = self.canvas.create_text(self.team2XYSize[0], self.team1XYSize[1], anchor='center', text=f"{self.team2Name}", fill="white", font=font.Font(family='ds-digital', size=self.team1XYSize[2]))
                if self.coloredSides:
                    left = self.canvas.create_rectangle(10, self.posyt+50, self.posxl, self.posyb, fill=colorLeft)
                    right = self.canvas.create_rectangle(self.posxr1, self.posyt+50, self.posxr2, self.posyb, fill=colorRight)
                score_labelL = self.canvas.create_text(self.posxScoreL-50, self.posyScoreL+50, text=str(self.scoreL), fill="white", font=font.Font(family='ds-digital', size=self.fontSize), anchor="center")
                score_labelR = self.canvas.create_text(self.posxScoreR+50, self.posyScoreR+50, text=str(self.scoreR), fill="white", font=font.Font(family='ds-digital', size=self.fontSize), anchor="center")
            else:
                colorLeft = "#0000ff"
                colorRight = "#ff0000"
                leftName = self.canvas.create_text(self.team1XYSize[0], team1XYSize[1], anchor='center',text=f"{team2Name}", fill="white", font=font.Font(family='ds-digital', size=self.team1XYSize[2]))
                rightName = self.canvas.create_text(self.team2XYSize[0], team1XYSize[1], anchor='center', text=f"{team1Name}", fill="white", font=font.Font(family='ds-digital', size=self.team1XYSize[2]))
                if coloredSides:
                    left = self. canvas.create_rectangle(10, self.posyt+50, posxl, posyb, fill=colorLeft)
                    right = self.canvas.create_rectangle(self.posxr1, posyt+50, posxr2, posyb, fill=colorRight)
                score_labelL = self.canvas.create_text(self.posxScoreL-50, posyScoreL+50, text=str(scoreR), fill="white", font=font.Font(family='ds-digital', size=fontSize), anchor="center")
                score_labelR = self.canvas.create_text(self.posxScoreR+50, posyScoreR+50, text=str(scoreL), fill="white", font=font.Font(family='ds-digital', size=fontSize), anchor="center")

            timerText = self.canvas.create_text(self.posxT, self.posyT, text=f"{timerValue}", fill="red", font=font.Font(family='ds-digital', size=(scoreFontSize-50)), anchor="center")
            if timer:
                if timerBase:
                    canvas.delete(timerBase)
                timerBase = canvas.create_rectangle(tBase1, tBase2, tBase3, tBase4, fill=None, outline='gray', width=2)


    def timer_function(self):
        minutes, seconds = map(int, self.timer_value.split(":"))
        total_seconds = minutes * 60 + seconds
        
        if not self.paused:
            if total_seconds > 10:
                total_seconds -= 1
            else:
                total_seconds -= .01

            new_minutes = total_seconds // 60
            new_seconds = total_seconds % 60

            minutes_str = f"{new_minutes:02d}"
            seconds_str = f"{new_seconds:02d}"

            self.timer_value = f"{minutes_str}:{seconds_str}"

        if total_seconds > 10:
            self.root.after(1000, self.timer_function)
        else:
            self.root.after(10, self.timer_function)

    def show_keybinds(self):
        keybinds_window = tk.Toplevel(self.root)
        keybinds_window.title("Live Window")

        label = tk.Label(keybinds_window, text=self.keybinds, padx=10, pady=10)
        label.pack()

        ok_button = tk.Button(keybinds_window, text="OK", command=keybinds_window.destroy)
        ok_button.pack(pady=10)
        keybinds_window.bind("<F11>", self.toggle_fullscreen)
        keybinds_window.bind("<Key>", self.update_scores)

if __name__ == "__main__":
    app = ScoreboardApp(True, '04:13', True, 'switch', 'Home', 'Away', False, False, False, True)
