import tkinter as tk
whitish = '#B6B6B6'  # Order from lightest to darkest
light_gray = '#8A8A8A'
lighterish_gray = '#4D4D4D'
lightish_gray = '#3F3F3F'
darkGray = '#343434'
hotPinkRed = '#FF69B4'
font = ("Arial", 15)

def switch_screen(screen):
    current_screen = screen
    if current_screen == 1:
        # canvas.delete("all")
        create_screen1()
        # userIcoUnderscoreFalse.config(fill="blue")
        # homeIcoUnderscoreTrue.config(fill="white")
        # menuIcoUnderscoreFalse.config(fill="white")
    elif current_screen == 2:
        # canvas.delete("all")
        create_screen2()
        # userIcoUnderscoreFalse.config(fill="white")
        # homeIcoUnderscoreTrue.config(fill="blue")
        # menuIcoUnderscoreFalse.config(fill="white")
    elif current_screen == 3:
        # canvas.delete("all")
        create_screen3()
        # userIcoUnderscoreFalse.config(fill="white")
        # homeIcoUnderscoreTrue.config(fill="white")
        # menuIcoUnderscoreFalse.config(fill="blue")

def create_screen1():
    # Graphics for screen 1
    print("screen1")
    

def create_screen2():
    # Graphics for screen 2
    print("screen2")

def create_screen3():
    # Graphics for screen 3
    print("screen3")

root = tk.Tk()
root.title("Screen Switching App")

canvas = tk.Canvas(root, width=500, height=500)
canvas.pack()

rect1bar = canvas.create_rectangle(0, 0, 50, 500, fill=lightish_gray, outline="")
rect2bar = canvas.create_rectangle(0, 0, 500, 50, fill=lightish_gray, outline="")

left_rectangle = canvas.create_rectangle(50, 100, 75, 150, fill=light_gray, outline="",tags="home")
right_rectangle = canvas.create_rectangle(95, 100, 120, 150, fill=light_gray, outline="", tags="home")
roof_triangle = canvas.create_polygon(30, 100, 85, 30, 140, 100, fill=light_gray, outline="", tags="home")
homeIcoUnderscoreTrue = canvas.create_line(50, 163, 120, 163, fill="blue", tags="home")
homeRectBind = canvas.create_rectangle(30, 30, 140, 155, fill=None, width=0, tags="home")
canvas.scale("home", 1, 1, 0.33, 0.28)
canvas.move("home", -3, 90)

circle = canvas.create_oval(66.7, 66.7, 133.3, 133.3, fill=light_gray, outline=light_gray, width=1.5, tags=('userSymbol'))
half_circle = canvas.create_arc(50, 134, 150, 234, start=0, extent=180, fill=light_gray, outline=light_gray, width=1.5, tags=('userSymbol'))
line1 = canvas.create_line(48, 184, 152, 184, width=1.5, fill=light_gray, tags=('userSymbol'))
userSymbolRectBind = canvas.create_rectangle(45, 62.7, 155, 187, fill=None, width=0 ,tags="userSymbol")
userIcoUnderscoreFalse = canvas.create_line(48, 197, 152, 197, fill=light_gray,tags="userSymbol")
canvas.scale("userSymbol", 1, 1, 0.25, 0.25)
canvas.move("userSymbol", 0, 140)

rectIco = canvas.create_rectangle(50, 50, 150, 150, fill=light_gray, outline="", tags="menuIco")
line1Ico = canvas.create_line(60, 80, 140, 80, width=4, fill=darkGray, tags="menuIco")
line2Ico = canvas.create_line(60, 100, 140, 100, width=4, fill=darkGray, tags="menuIco")
line3Ico = canvas.create_line(60, 120, 140, 120, width=4, fill=darkGray, tags="menuIco")
menuIcoSymbolRectBind = canvas.create_rectangle(50, 50, 150, 150, fill=None, outline="", width=0 ,tags="menuIco")
menuIcoUnderscoreFalse = canvas.create_line(50, 163, 150, 163, fill=light_gray, tags="menuIco")
canvas.scale("menuIco", 1, 1, 0.3, 0.3)
canvas.move("menuIco", -5, 200)

canvas.tag_bind(userSymbolRectBind, "<Button-1>", lambda event: switch_screen(1))
canvas.tag_bind(homeRectBind, "<Button-1>", lambda event: switch_screen(2))
canvas.tag_bind(menuIcoSymbolRectBind, "<Button-1>", lambda event: switch_screen(3))

root.mainloop()
