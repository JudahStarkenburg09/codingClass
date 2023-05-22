import tkinter as tk
whitish = '#B6B6B6'  # Order from lightest to darkest
light_gray = '#8A8A8A'
lighterish_gray = '#4D4D4D'
lightish_gray = '#3F3F3F'
darkGray = '#343434'
hotPinkRed = '#FF69B4'
font = ("Arial", 15)


root = tk.Tk()
root.title("Screen Switching App")

canvas = tk.Canvas(root, width=500, height=500)
canvas.config(bg=darkGray)
canvas.pack()

def runApp():
    rect1bar = canvas.create_rectangle(0, 0, 50, 500, fill=lightish_gray, outline="", tags='bar')
    rect2bar = canvas.create_rectangle(0, 0, 500, 50, fill=lightish_gray, outline="", tags='bar')

    left_rectangle = canvas.create_rectangle(50, 100, 75, 150, fill=light_gray, outline="",tags=("home", "bar"))
    right_rectangle = canvas.create_rectangle(95, 100, 120, 150, fill=light_gray, outline="", tags=("home", "bar"))
    roof_triangle = canvas.create_polygon(30, 100, 85, 30, 140, 100, fill=light_gray, outline="", tags=("home", "bar"))
    homeIcoUnderscoreTrue = canvas.create_line(50, 163, 120, 163, fill="blue", tags=("home", "bar"))
    homeRectBind = canvas.create_rectangle(30, 30, 140, 155, fill=None, width=0, tags=("home", "bar"))
    canvas.scale("home", 1, 1, 0.33, 0.28)
    canvas.move("home", -3, 90)

    circle = canvas.create_oval(66.7, 66.7, 133.3, 133.3, fill=light_gray, outline=light_gray, width=1.5, tags=('userSymbol', "bar"))
    half_circle = canvas.create_arc(50, 134, 150, 234, start=0, extent=180, fill=light_gray, outline=light_gray, width=1.5, tags=('userSymbol', "bar"))
    line1 = canvas.create_line(48, 184, 152, 184, width=1.5, fill=light_gray, tags=('userSymbol', "bar"))
    userSymbolRectBind = canvas.create_rectangle(45, 62.7, 155, 187, fill=None, width=0 ,tags=("userSymbol", "bar"))
    userIcoUnderscoreFalse = canvas.create_line(48, 197, 152, 197, fill=light_gray,tags=("userSymbol", "bar"))
    canvas.scale("userSymbol", 1, 1, 0.25, 0.25)
    canvas.move("userSymbol", 0, 140)

    rectIco = canvas.create_rectangle(50, 50, 150, 150, fill=light_gray, outline="", tags=("menuIco", "bar"))
    line1Ico = canvas.create_line(60, 80, 140, 80, width=4, fill=darkGray, tags=("menuIco", "bar"))
    line2Ico = canvas.create_line(60, 100, 140, 100, width=4, fill=darkGray, tags=("menuIco", "bar"))
    line3Ico = canvas.create_line(60, 120, 140, 120, width=4, fill=darkGray, tags=("menuIco", "bar"))
    menuIcoSymbolRectBind = canvas.create_rectangle(50, 50, 150, 150, fill=None, outline="", width=0 ,tags=("menuIco", "bar"))
    menuIcoUnderscoreFalse = canvas.create_line(50, 163, 150, 163, fill=light_gray, tags=("menuIco", "bar"))
    canvas.scale("menuIco", 1, 1, 0.3, 0.3)
    canvas.move("menuIco", -5, 200)

    def switch_to_home_screen():
        print("home")
        canvas.itemconfigure("homeIcoUnderscoreFalse", fill=light_gray)
        canvas.itemconfigure("homeIcoUnderscoreTrue", fill="blue")
        canvas.delete("all")
        rect1bar = canvas.create_rectangle(0, 0, 50, 500, fill=lightish_gray, outline="", tags='bar')
        rect2bar = canvas.create_rectangle(0, 0, 500, 50, fill=lightish_gray, outline="", tags='bar')

        left_rectangle = canvas.create_rectangle(50, 100, 75, 150, fill=light_gray, outline="",tags=("home", "bar"))
        right_rectangle = canvas.create_rectangle(95, 100, 120, 150, fill=light_gray, outline="", tags=("home", "bar"))
        roof_triangle = canvas.create_polygon(30, 100, 85, 30, 140, 100, fill=light_gray, outline="", tags=("home", "bar"))
        homeIcoUnderscoreTrue = canvas.create_line(50, 163, 120, 163, fill="blue", tags=("home", "bar"))
        homeRectBind = canvas.create_rectangle(30, 30, 140, 155, fill=None, width=0, tags=("home", "bar"))
        canvas.scale("home", 1, 1, 0.33, 0.28)
        canvas.move("home", -3, 90)

        circle = canvas.create_oval(66.7, 66.7, 133.3, 133.3, fill=light_gray, outline=light_gray, width=1.5, tags=('userSymbol', "bar"))
        half_circle = canvas.create_arc(50, 134, 150, 234, start=0, extent=180, fill=light_gray, outline=light_gray, width=1.5, tags=('userSymbol', "bar"))
        line1 = canvas.create_line(48, 184, 152, 184, width=1.5, fill=light_gray, tags=('userSymbol', "bar"))
        userSymbolRectBind = canvas.create_rectangle(45, 62.7, 155, 187, fill=None, width=0 ,tags=("userSymbol", "bar"))
        userIcoUnderscoreFalse = canvas.create_line(48, 197, 152, 197, fill=light_gray,tags=("userSymbol", "bar"))
        canvas.scale("userSymbol", 1, 1, 0.25, 0.25)
        canvas.move("userSymbol", 0, 140)

        rectIco = canvas.create_rectangle(50, 50, 150, 150, fill=light_gray, outline="", tags=("menuIco", "bar"))
        line1Ico = canvas.create_line(60, 80, 140, 80, width=4, fill=darkGray, tags=("menuIco", "bar"))
        line2Ico = canvas.create_line(60, 100, 140, 100, width=4, fill=darkGray, tags=("menuIco", "bar"))
        line3Ico = canvas.create_line(60, 120, 140, 120, width=4, fill=darkGray, tags=("menuIco", "bar"))
        menuIcoSymbolRectBind = canvas.create_rectangle(50, 50, 150, 150, fill=None, outline="", width=0 ,tags=("menuIco", "bar"))
        menuIcoUnderscoreFalse = canvas.create_line(50, 163, 150, 163, fill=light_gray, tags=("menuIco", "bar"))
        canvas.scale("menuIco", 1, 1, 0.3, 0.3)
        canvas.move("menuIco", -5, 200)
        canvas.tag_bind(homeRectBind, "<Button-1>", lambda event: switch_to_home_screen())
        canvas.tag_bind(userSymbolRectBind, "<Button-1>", lambda event: switch_to_user_symbol_screen())
        canvas.tag_bind(menuIcoSymbolRectBind, "<Button-1>", lambda event: switch_to_menu_ico_screen())
        # Additional logic to update the graphics for the home screen

    def switch_to_user_symbol_screen():
        print("user")
        canvas.itemconfigure("userIcoUnderscoreFalse", fill=light_gray)
        canvas.itemconfigure("userIcoUnderscoreTrue", fill="blue")
        canvas.delete("all")
        rect1bar = canvas.create_rectangle(0, 0, 50, 500, fill=lightish_gray, outline="", tags='bar')
        rect2bar = canvas.create_rectangle(0, 0, 500, 50, fill=lightish_gray, outline="", tags='bar')

        left_rectangle = canvas.create_rectangle(50, 100, 75, 150, fill=light_gray, outline="",tags=("home", "bar"))
        right_rectangle = canvas.create_rectangle(95, 100, 120, 150, fill=light_gray, outline="", tags=("home", "bar"))
        roof_triangle = canvas.create_polygon(30, 100, 85, 30, 140, 100, fill=light_gray, outline="", tags=("home", "bar"))
        homeIcoUnderscoreTrue = canvas.create_line(50, 163, 120, 163, fill=light_gray, tags=("home", "bar"))
        homeRectBind = canvas.create_rectangle(30, 30, 140, 155, fill=None, width=0, tags=("home", "bar"))
        canvas.scale("home", 1, 1, 0.33, 0.28)
        canvas.move("home", -3, 90)

        circle = canvas.create_oval(66.7, 66.7, 133.3, 133.3, fill=light_gray, outline=light_gray, width=1.5, tags=('userSymbol', "bar"))
        half_circle = canvas.create_arc(50, 134, 150, 234, start=0, extent=180, fill=light_gray, outline=light_gray, width=1.5, tags=('userSymbol', "bar"))
        line1 = canvas.create_line(48, 184, 152, 184, width=1.5, fill=light_gray, tags=('userSymbol', "bar"))
        userSymbolRectBind = canvas.create_rectangle(45, 62.7, 155, 187, fill=None, width=0 ,tags=("userSymbol", "bar"))
        userIcoUnderscoreFalse = canvas.create_line(48, 197, 152, 197, fill="blue",tags=("userSymbol", "bar"))
        canvas.scale("userSymbol", 1, 1, 0.25, 0.25)
        canvas.move("userSymbol", 0, 140)

        rectIco = canvas.create_rectangle(50, 50, 150, 150, fill=light_gray, outline="", tags=("menuIco", "bar"))
        line1Ico = canvas.create_line(60, 80, 140, 80, width=4, fill=darkGray, tags=("menuIco", "bar"))
        line2Ico = canvas.create_line(60, 100, 140, 100, width=4, fill=darkGray, tags=("menuIco", "bar"))
        line3Ico = canvas.create_line(60, 120, 140, 120, width=4, fill=darkGray, tags=("menuIco", "bar"))
        menuIcoSymbolRectBind = canvas.create_rectangle(50, 50, 150, 150, fill=None, outline="", width=0 ,tags=("menuIco", "bar"))
        menuIcoUnderscoreFalse = canvas.create_line(50, 163, 150, 163, fill=light_gray, tags=("menuIco", "bar"))
        canvas.scale("menuIco", 1, 1, 0.3, 0.3)
        canvas.move("menuIco", -5, 200)
        canvas.tag_bind(homeRectBind, "<Button-1>", lambda event: switch_to_home_screen())
        canvas.tag_bind(userSymbolRectBind, "<Button-1>", lambda event: switch_to_user_symbol_screen())
        canvas.tag_bind(menuIcoSymbolRectBind, "<Button-1>", lambda event: switch_to_menu_ico_screen())
        # Additional logic to update the graphics for the user symbol screen

    def switch_to_menu_ico_screen():
        print("menu")
        canvas.delete("all")
        rect1bar = canvas.create_rectangle(0, 0, 50, 500, fill=lightish_gray, outline="", tags='bar')
        rect2bar = canvas.create_rectangle(0, 0, 500, 50, fill=lightish_gray, outline="", tags='bar')

        left_rectangle = canvas.create_rectangle(50, 100, 75, 150, fill=light_gray, outline="",tags=("home", "bar"))
        right_rectangle = canvas.create_rectangle(95, 100, 120, 150, fill=light_gray, outline="", tags=("home", "bar"))
        roof_triangle = canvas.create_polygon(30, 100, 85, 30, 140, 100, fill=light_gray, outline="", tags=("home", "bar"))
        homeIcoUnderscoreFalse = canvas.create_line(50, 163, 120, 163, fill=light_gray, tags=("home", "bar"))
        homeRectBind = canvas.create_rectangle(30, 30, 140, 155, fill=None, width=0, tags=("home", "bar"))
        canvas.scale("home", 1, 1, 0.33, 0.28)
        canvas.move("home", -3, 90)

        circle = canvas.create_oval(66.7, 66.7, 133.3, 133.3, fill=light_gray, outline=light_gray, width=1.5, tags=('userSymbol', "bar"))
        half_circle = canvas.create_arc(50, 134, 150, 234, start=0, extent=180, fill=light_gray, outline=light_gray, width=1.5, tags=('userSymbol', "bar"))
        line1 = canvas.create_line(48, 184, 152, 184, width=1.5, fill=light_gray, tags=('userSymbol', "bar"))
        userSymbolRectBind = canvas.create_rectangle(45, 62.7, 155, 187, fill=None, width=0 ,tags=("userSymbol", "bar"))
        userIcoUnderscoreFalse = canvas.create_line(48, 197, 152, 197, fill=light_gray,tags=("userSymbol", "bar"))
        canvas.scale("userSymbol", 1, 1, 0.25, 0.25)
        canvas.move("userSymbol", 0, 140)

        rectIco = canvas.create_rectangle(50, 50, 150, 150, fill=light_gray, outline="", tags=("menuIco", "bar"))
        line1Ico = canvas.create_line(60, 80, 140, 80, width=4, fill=darkGray, tags=("menuIco", "bar"))
        line2Ico = canvas.create_line(60, 100, 140, 100, width=4, fill=darkGray, tags=("menuIco", "bar"))
        line3Ico = canvas.create_line(60, 120, 140, 120, width=4, fill=darkGray, tags=("menuIco", "bar"))
        menuIcoSymbolRectBind = canvas.create_rectangle(50, 50, 150, 150, fill=None, outline="", width=0 ,tags=("menuIco", "bar"))
        menuIcoUnderscoreTrue = canvas.create_line(50, 163, 150, 163, fill="blue", tags=("menuIco", "bar"))
        canvas.scale("menuIco", 1, 1, 0.3, 0.3)
        canvas.move("menuIco", -5, 200)
        canvas.tag_bind(homeRectBind, "<Button-1>", lambda event: switch_to_home_screen())
        canvas.tag_bind(userSymbolRectBind, "<Button-1>", lambda event: switch_to_user_symbol_screen())
        canvas.tag_bind(menuIcoSymbolRectBind, "<Button-1>", lambda event: switch_to_menu_ico_screen())
        # Additional logic to update the graphics for the menu icon screen

    # Bind click events to rectangles using lambda functions
    canvas.tag_bind(homeRectBind, "<Button-1>", lambda event: switch_to_home_screen())
    canvas.tag_bind(userSymbolRectBind, "<Button-1>", lambda event: switch_to_user_symbol_screen())
    canvas.tag_bind(menuIcoSymbolRectBind, "<Button-1>", lambda event: switch_to_menu_ico_screen())


input('')
runApp()

root.mainloop()
