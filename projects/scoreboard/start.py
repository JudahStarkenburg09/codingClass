import tkinter as tk
from tkinter import messagebox
from tkinter import font
from PIL import Image, ImageTk, ImageFilter
import keyboard

class ScoreboardApp:
    def __init__(self, timer, timer_value_str, possession, switch, team1, team2, colored_sides, home_icon, away_icon, has_period):
        self.timer_value = timer_value_str
        self.leftName = None
        self.rightName = None
        self.isFullscreen = False
        self.home_icon_path = home_icon
        self.away_icon_path = away_icon
        self.origTimer = timer_value_str
        self.timerBase = None
        self.scoreL = 0
        self.scoreR = 0
        self.periodText = None
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
        self.period_possible = has_period
        self.period = 1
        self.switch_possible = switch
        self.keybinds = """Press (Q, W) to change left score
Press (O, P) to change right score
Press space to switch sides
Press T to start/pause the timer
Press F11 To Toggle Fullscreen
Press arrow keys (< >) to change possession
Press Enter to Reset Timer
Press Ctrl + Enter to Reset Score, Possession, and Timer
Press F1 to show Keybinds again / Open Live Window
Use the UP and DOWN arrow to change the period (v, ^)"""
        self.width = 500
        self.height = 400
        self.root = tk.Tk()
        self.root.geometry(f'{self.width}x{self.height}')
        self.root.title(" ")

        self.initialize_gui()

    def initialize_gui(self):
        self.root.bind("<F11>", self.toggle_fullscreen)
        keyboard.on_press(self.update_scores)

        self.canvas = tk.Canvas(width=10000, height=10000, bg='black')
        self.canvas.pack()

        self.left_name = None
        self.right_name = None
        self.timerText = None
        self.timer_base = None
        self.pos_text = None

        self.root.after(0, self.graphics)
        if self.timer:
            self.root.after(0, self.timer_function)

        self.color_left = "#ff0000"
        self.color_right = "#0000ff"

        self.root.mainloop()

    def toggle_fullscreen(self, event=None):
        state = not self.root.attributes('-fullscreen')
        self.root.attributes('-fullscreen', state)
        if self.root.attributes('-fullscreen'):
            self.isFullscreen = True
            toast = tk.Label(self.root, text='Press f11 to toggle fullscreen', background='gray', foreground='white')
            toast.place(x=self.root.winfo_screenwidth() / 2, y=15, anchor='center')
            self.root.after(2000, lambda: toast.destroy())
        else: 
            toast = tk.Label(self.root, text='Press f11 to toggle fullscreen', background='gray', foreground='white')
            toast.place(x=250, y=15, anchor='center')
            self.root.after(2000, lambda: toast.destroy())
            self.isFullscreen = False

    def update_scores(self, event):
        print(f"Keybind Detected: {event.name}")
        if event.name == 'space':
            if self.switch_possible:
                if self.side == "left":
                    self.side = "right"
                else:
                    self.side = "left"
        elif keyboard.is_pressed("ctrl+enter"):
            self.paused = True
            self.timer_value = self.origTimer
            self.scoreL = 0
            self.scoreR = 0
            self.side = "left"
            self.currentPos = "←"
            self.period = 1
            print("Control+Enter Pressed")
        elif event.name == "enter":
            self.paused = True
            self.timer_value = self.origTimer
            self.currentPos = "→"
            self.side = "right"
            print("Enter Pressed")
        elif event.name == 't':
            if self.paused:
                self.paused = False
            else:
                self.paused = True
        elif event.name == "f1":
            self.show_keybinds()
        elif event.name == 'right':
            self.currentPos = "→"
        elif event.name == 'left':
            self.currentPos = "←"
        elif event.name == 'q':
            if self.side == "left":
                self.scoreL += 1
            else:
                self.scoreR += 1
        elif event.name == 'w':
            if self.side == "left":
                self.scoreL -= 1
            else:
                self.scoreR -= 1
        elif event.name == 'o':
            if self.side == "left":
                self.scoreR -= 1
            else:
                self.scoreL -= 1
        elif event.name == 'p':
            if self.side == "left":
                self.scoreR += 1
            else:
                self.scoreL += 1
        elif event.name == 'up':
            self.period += 1
        elif event.name == "down":
            self.period -= 1

    def graphics(self):
        if self.isFullscreen:
            self.fullWidth = self.root.winfo_screenwidth()
            self.fullHeight = self.root.winfo_screenheight()
            self.LRHalf = self.root.winfo_screenwidth() / 2
            self.TBHalf = self.root.winfo_screenheight() / 2
            self.LRQuarter = self.root.winfo_screenwidth() / 4
            self.TBQuarter = self.root.winfo_screenheight() / 4
            self.WThirds = self.root.winfo_screenwidth() / 3
            self.WFifths = self.root.winfo_screenwidth() / 5
            self.fontMultiply = 3
            self.tBase1 = self.LRHalf - 200
            self.tBase2 = -10
            self.tBase3 = self.LRHalf + 200
            self.tBase4 = 200
        else:
            self.fullWidth = self.width
            self.fullHeight = self.height
            self.LRHalf = self.width / 2
            self.TBHalf = self.height / 2
            self.LRQuarter = self.width / 4
            self.TBQuarter = self.width / 4
            self.WThirds = self.width / 3
            self.WFifths = self.width / 5
            self.fontMultiply = 1
            self.tBase1 = self.LRHalf - 100
            self.tBase2 = -10
            self.tBase3 = self.LRHalf + 100
            self.tBase4 = 100

        # print(f"W: {self.fullWidth}, H: {self.fullHeight}")

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
            self.posText = self.canvas.create_text((self.LRHalf), (0+self.fullHeight/2.5), text=f"{self.currentPos}", fill="white" ,anchor="center", font=font.Font(family='ds-digital', size=40*self.fontMultiply))

        if self.period_possible: 
            if self.periodText:
                self.canvas.delete(self.periodText)
                self.canvas.delete(self.periodLabel)
            self.periodText = self.canvas.create_text((self.LRHalf), (self.TBHalf+self.TBQuarter+self.fullHeight/12), text="Period", font=font.Font(family='ds-digital', size=25*self.fontMultiply if not self.isFullscreen else 20*self.fontMultiply), fill="white", anchor='center')
            self.periodLabel = self.canvas.create_text((self.LRHalf), (self.TBHalf+self.TBQuarter-(40*self.fontMultiply)+self.fullHeight/12), text=f"{self.period}", font=font.Font(family='ds-digital', size=50*self.fontMultiply if not self.isFullscreen else 40*self.fontMultiply), fill="yellow", anchor='center')

        if self.side == "left":
            self.leftName = self.canvas.create_text((self.WFifths), (self.TBHalf+self.fullHeight/10), anchor='center', text=f"{self.team1Name}", fill="white", font=font.Font(family='ds-digital', size=30*self.fontMultiply))
            self.rightName = self.canvas.create_text((self.fullWidth-self.WFifths), (self.TBHalf+self.fullHeight/10), anchor='center', text=f"{self.team2Name}", fill="white", font=font.Font(family='ds-digital', size=30*self.fontMultiply))
            self.score_labelL = self.canvas.create_text((self.WFifths), (self.fullHeight-self.TBQuarter+self.fullHeight/10), text=str(self.scoreL), fill="white", font=font.Font(family='ds-digital', size=(70*self.fontMultiply)), anchor="center")
            self.score_labelR = self.canvas.create_text((self.fullWidth-self.WFifths), (self.fullHeight-self.TBQuarter+self.fullHeight/10), text=str(self.scoreR), fill="white", font=font.Font(family='ds-digital', size=(70*self.fontMultiply)), anchor="center")
            if self.home_icon_path:
                image1 = Image.open(self.home_icon_path)
                image1 = image1.resize((int(self.fullWidth/5), int(self.fullWidth/5)), Image.LANCZOS)
                # Convert the image to a Tkinter PhotoImage object
                tk_image1 = ImageTk.PhotoImage(image1)
                # Display the image on the canvas
                self.canvas.create_image((self.WFifths), (self.TBQuarter+self.fullHeight/12), anchor="center", image=tk_image1)
                # Ensure that the image is not garbage collected by keeping a reference
                self.canvas.imageOne = tk_image1
            if self.away_icon_path:
                image2 = Image.open(self.away_icon_path)
                image2 = image2.resize((int(self.fullWidth/5), int(self.fullWidth/5)), Image.LANCZOS)
                # Convert the image to a Tkinter PhotoImage object
                tk_image2 = ImageTk.PhotoImage(image2)
                # Display the image on the canvas
                self.canvas.create_image((self.fullWidth-self.WFifths), (self.TBQuarter+self.fullHeight/12), anchor="center", image=tk_image2)
                # Ensure that the image is not garbage collected by keeping a reference
                self.canvas.imageTwo = tk_image2
        else:
            self.leftName = self.canvas.create_text((self.WFifths), (self.TBHalf+self.fullHeight/10), anchor='center', text=f"{self.team2Name}", fill="white", font=font.Font(family='ds-digital', size=30*self.fontMultiply))
            self.rightName = self.canvas.create_text((self.fullWidth-self.WFifths), (self.TBHalf+self.fullHeight/10), anchor='center', text=f"{self.team1Name}", fill="white", font=font.Font(family='ds-digital', size=30*self.fontMultiply))
            self.score_labelL = self.canvas.create_text((self.WFifths), (self.fullHeight-self.TBQuarter+self.fullHeight/10), text=str(self.scoreR), fill="white", font=font.Font(family='ds-digital', size=(70*self.fontMultiply)), anchor="center")
            self.score_labelR = self.canvas.create_text((self.fullWidth-self.WFifths), (self.fullHeight-self.TBQuarter+self.fullHeight/10), text=str(self.scoreL), fill="white", font=font.Font(family='ds-digital', size=(70*self.fontMultiply)), anchor="center")    
            if self.away_icon_path:
                image1 = Image.open(self.away_icon_path)
                image1 = image1.resize((int(self.fullWidth/5), int(self.fullWidth/5)), Image.LANCZOS)
                # Convert the image to a Tkinter PhotoImage object
                tk_image1 = ImageTk.PhotoImage(image1)
                # Display the image on the canvas
                self.canvas.create_image((self.WFifths), (self.TBQuarter+self.fullHeight/12), anchor="center", image=tk_image1)
                # Ensure that the image is not garbage collected by keeping a reference
                self.canvas.imageOne = tk_image1
            if self.home_icon_path:
                image2 = Image.open(self.home_icon_path)
                image2 = image2.resize((int(self.fullWidth/5), int(self.fullWidth/5)), Image.LANCZOS)
                # Convert the image to a Tkinter PhotoImage object
                tk_image2 = ImageTk.PhotoImage(image2)
                # Display the image on the canvas
                self.canvas.create_image((self.fullWidth-self.WFifths), (self.TBQuarter+self.fullHeight/12), anchor="center", image=tk_image2)
                # Ensure that the image is not garbage collected by keeping a reference
                self.canvas.imageTwo = tk_image2


        self.timerText = self.canvas.create_text(self.LRHalf, self.tBase4/2, text=f"{self.timer_value}", fill="red", font=font.Font(family='ds-digital', size=(self.fontMultiply*40)), anchor="center")
        if self.timer:
            if self.timerBase:
                self.canvas.delete(self.timerBase)
            self.timerBase = self.canvas.create_rectangle(self.tBase1, self.tBase2, self.tBase3, self.tBase4, fill=None, outline='gray', width=2)

        self.root.after(10, self.graphics)


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

        # Create labels and buttons
        label = tk.Label(keybinds_window, text=self.keybinds, padx=10, pady=10)
        label.pack()
        def buttonScoreboard(team=False, amount=False, pressed=False):
            if team:
                if team == "L":
                    self.scoreL += amount
                if team == "R":
                    self.scoreR += amount
            elif pressed:
                if pressed == "timer":
                    if self.paused:
                        self.paused = False
                    else:
                        self.paused = True
                elif pressed == "reset timer":
                    self.timer_value = self.origTimer
                    self.paused = True
                elif pressed == "pos change":
                    if self.currentPos == "←":
                        self.currentPos = "→"
                    elif self.currentPos == "→":
                        self.currentPos = "←"
                elif pressed == "switch":
                    if self.side == "left":
                        self.side = "right"
                        print("Side is Right")
                    else:
                        self.side = "left"
                        print("Side is Left")
                elif pressed == "period":
                    self.period += amount


        # Up arrow button for "q"
        up_q_button = tk.Button(keybinds_window, text="↑", command=lambda: buttonScoreboard("L", 1))
        up_q_button.pack(side=tk.LEFT, padx=10)

        # Down arrow button for "w"
        down_w_button = tk.Button(keybinds_window, text="↓", command=lambda: buttonScoreboard("L", -1))
        down_w_button.pack(side=tk.LEFT, padx=10)

        # Up arrow button for "p"
        up_p_button = tk.Button(keybinds_window, text="↑", command=lambda: buttonScoreboard("R", 1))
        up_p_button.pack(side=tk.RIGHT, padx=10)

        # Down arrow button for "o"
        down_o_button = tk.Button(keybinds_window, text="↓", command=lambda: buttonScoreboard("R", -1))
        down_o_button.pack(side=tk.RIGHT, padx=10)

        ok_button = tk.Button(keybinds_window, text="Exit", command=keybinds_window.destroy)
        ok_button.pack(pady=10)

        timerUnpause = tk.Button(keybinds_window, text="Pause/Unpause Timer", command=lambda: buttonScoreboard(False, False, "timer"))
        timerUnpause.pack(pady=5)

        timerReset = tk.Button(keybinds_window, text="Reset Timer", command=lambda: buttonScoreboard(False,False,"reset timer"))
        timerReset.pack(pady=5)

        posChange = tk.Button(keybinds_window, text="Change Possession", command=lambda: buttonScoreboard(False,False,"pos change"))
        posChange.pack(pady=5)

        addPeriod = tk.Button(keybinds_window, text="Period +", command=lambda: buttonScoreboard(False,1,"period"))
        addPeriod.pack(padx=10, side=tk.LEFT)

        subPeriod = tk.Button(keybinds_window, text="Period -", command=lambda: buttonScoreboard(False,-1,"period"))
        subPeriod.pack(padx=10, side=tk.RIGHT)

        switchSides = tk.Button(keybinds_window, text="Switch Sides", command=lambda: buttonScoreboard(False,False,"switch"))
        switchSides.pack(pady=5)
    
        keybinds_window.bind("<F11>", self.toggle_fullscreen)

if __name__ == "__main__":
    app = ScoreboardApp(True, '04:13', True, 'switch', 'Home', 'Away', False, r"C:\Users\judah\OneDrive\Desktop\OtherFolders\Coding\codingClass\projects\scoreboard\NCASymbol.png", r"C:\Users\judah\OneDrive\Desktop\OtherFolders\Coding\codingClass\projects\scoreboard\ANS png.png", True)
