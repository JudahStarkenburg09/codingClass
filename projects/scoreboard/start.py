import tkinter as tk
from tkinter import messagebox
from tkinter import font
from PIL import Image, ImageTk, ImageFilter

class ScoreboardApp:
    def __init__(self, timer, timer_value_str, possession, switch, team1, team2, colored_sides, home_icon, away_icon, has_period):
        self.timer_value = timer_value_str
        self.leftName = None
        self.rightName = None
        self.home_icon_path = home_icon
        self.away_icon_path = away_icon
        self.origTimer = timer_value_str
        self.timerBase = None
        self.away_icon_image = None
        self.home_icon_image = None
        self.timer_value = timer_value_str
        self.scoreL = 0
        self.scoreR = 0
        self.left = None
        self.right = None
        self.posText = None
        self.possessionPossible = possession
        self.coloredSides = colored_sides
        self.team1Name = team1
        self.team2Name = team2
        self.score_labelL = None
        self.score_labelR = None
        self.timer = timer
        self.paused = True
        self.side = "left"
        self.currentPos = '←'
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
        self.timerText = None
        self.timer_base = None
        self.pos_text = None

        self.root.after(0, self.graphics)
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
        # print(f"Keybind Detected: {event.keysym}")
        if event.keysym == 'space':
            if self.switch_possible:
                if self.side == "left":
                    self.side = "right"
                else:
                    self.side = "left"
        elif event.keysym == "Return" and event.state == 0x4:
            self.paused = True
            self.timer_value = self.origTimer
            self.scoreL = 0
            self.scoreR = 0
            self.side = "left"
            self.currentPos = "←"
        elif event.keysym == "Return":
            self.paused = True
            self.timer_value = self.origTimer
        elif event.keysym == 't':
            if self.paused:
                self.paused = False
                print("Timer Unpaused")
            else:
                self.paused = True
                print("Timer Paused")
        elif event.keysym == "F1":
            self.show_keybinds()
        elif event.keysym == 'Right':
            self.currentPos = "→"
        elif event.keysym == 'Left':
            self.currentPos = "←"
        if event.keysym == 'q':
            if self.side == "left":
                self.scoreL += 1
            else:
                self.scoreR += 1
        elif event.keysym == 'w':
            if self.side == "left":
                self.scoreL -= 1
            else:
                self.scoreR -= 1
        elif event.keysym == 'o':
            if self.side == "left":
                self.scoreR -= 1
            else:
                self.scoreL -= 1
        elif event.keysym == 'p':
            if self.side == "left":
                self.scoreR += 1
            else:
                self.scoreL += 1

    def graphics(self):
        # print(f"Graphics Running, Left Score: {self.scoreL}. Right Score: {self.scoreR}. Timer: {self.timer_value}")
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

            if (self.score_labelL):
                self.canvas.delete(self.score_labelL)
                self.canvas.delete(self.score_labelR)
            if self.timerText:
                self.canvas.delete(self.timerText)

            if self.leftName:
                self.canvas.delete(self.leftName)
                self.canvas.delete(self.rightName)

            if self.posText:
                self.canvas.delete(self.posText)

            if self.possessionPossible:
                self.posText = self.canvas.create_text(self.possPos[0], self.possPos[1], text=f"{self.currentPos}", fill="white" ,anchor="center", font=font.Font(family='ds-digital', size=self.possPos[2]))

            if self.side == "left":
                self.color_left = "#ff0000"
                self.color_right = "#0000ff"
                self.leftName = self.canvas.create_text(self.team1XYSize[0], self.team1XYSize[1], anchor='center', text=f"{self.team1Name}", fill="white", font=font.Font(family='ds-digital', size=self.team1XYSize[2]))
                self.rightName = self.canvas.create_text(self.team2XYSize[0], self.team1XYSize[1], anchor='center', text=f"{self.team2Name}", fill="white", font=font.Font(family='ds-digital', size=self.team1XYSize[2]))
                if self.coloredSides:
                    self.left = self.canvas.create_rectangle(10, self.posyt+50, self.posxl, self.posyb, fill=self.color_left)
                    self.right = self.canvas.create_rectangle(self.posxr1, self.posyt+50, self.posxr2, self.posyb, fill=self.color_right)
                self.score_labelL = self.canvas.create_text(self.posxScoreL-50, self.posyScoreL+50, text=str(self.scoreL), fill="white", font=font.Font(family='ds-digital', size=self.fontSize), anchor="center")
                self.score_labelR = self.canvas.create_text(self.posxScoreR+50, self.posyScoreR+50, text=str(self.scoreR), fill="white", font=font.Font(family='ds-digital', size=self.fontSize), anchor="center")
            else:
                self.color_left = "#0000ff"
                self.color_right = "#ff0000"
                self.leftName = self.canvas.create_text(self.team1XYSize[0], self.team1XYSize[1], anchor='center',text=f"{self.team2Name}", fill="white", font=font.Font(family='ds-digital', size=self.team1XYSize[2]))
                self.rightName = self.canvas.create_text(self.team2XYSize[0], self.team1XYSize[1], anchor='center', text=f"{self.team1Name}", fill="white", font=font.Font(family='ds-digital', size=self.team1XYSize[2]))
                if self.coloredSides:
                    self.left = self. canvas.create_rectangle(10, self.posyt+50, self.posxl, self.posyb, fill=self.color_left)
                    self.right = self.canvas.create_rectangle(self.posxr1, self.posyt+50, self.posxr2, self.posyb, fill=self.color_right)
                self.score_labelL = self.canvas.create_text(self.posxScoreL-50, self.posyScoreL+50, text=str(self.scoreR), fill="white", font=font.Font(family='ds-digital', size=self.fontSize), anchor="center")
                self.score_labelR = self.canvas.create_text(self.posxScoreR+50, self.posyScoreR+50, text=str(self.scoreL), fill="white", font=font.Font(family='ds-digital', size=self.fontSize), anchor="center")

            self.timerText = self.canvas.create_text(self.posxT, self.posyT, text=f"{self.timer_value}", fill="red", font=font.Font(family='ds-digital', size=(self.scoreFontSize-50)), anchor="center")
            if self.timer:
                if self.timerBase:
                    self.canvas.delete(self.timerBase)
                self.timerBase = self.canvas.create_rectangle(self.tBase1, self.tBase2, self.tBase3, self.tBase4, fill=None, outline='gray', width=2)

            self.root.after(100, self.graphics)


    def timer_function(self):
        minutes, seconds = map(int, self.timer_value.split(":"))
        total_seconds = minutes * 60 + seconds
        # print("Timer Function Running")
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
            # print(self.timer_value)
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
