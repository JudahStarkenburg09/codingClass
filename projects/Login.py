import tkinter as tk
import cv2
import os
from PIL import Image, ImageDraw, ImageTk
from guessWord import wordGuessing
from addTo100 import addTo100Game
from TicTacToe1p import tic_tac_toe1P
from TicTacToe2p import tic_tac_toe2P

def take_picture():
    # Open the camera
    cap = cv2.VideoCapture(0)

    # Check if the camera is opened successfully
    if not cap.isOpened():
        print("Failed to open the camera")
        return

    # Capture a frame from the camera
    ret, frame = cap.read()

    # Release the camera
    cap.release()

    # Check if the frame was captured successfully
    if not ret:
        print("Failed to capture frame")
        return

    # Save the captured frame as an image file
    cv2.imwrite("profile.jpg", frame)
    return


whitish = '#B6B6B6'  # Order from lightest to darkest
light_gray = '#8A8A8A'
lighterish_gray = '#4D4D4D'
lightish_gray = '#3F3F3F'
darkGray = '#343434'
hotPinkRed = '#FF69B4'
font = ("Arial", 15)
firstName = False
middleName = False
lastName = False
ageBirth = False
dateOfBirth = False
occupation = False

 
    


def runApp():
    global username, usernameText, masked_password, expression, PasswordText
    canvas.delete("all")
    
    usernameText = tk.Entry(canvas, width=10, fg=light_gray, font=('Arial', 12), bd=0, insertbackground=lighterish_gray) #border=.5,)
    usernameText.insert(0, f'{username}')
    usernameText.configure({"background": darkGray})
    PasswordText = tk.Entry(canvas, width=10, fg=light_gray, font=('Arial', 12), bd=0, insertbackground=lighterish_gray) #border=.5,)
    PasswordText.insert(0, f'{masked_password}')
    PasswordText.configure({"background": darkGray})

    masked_password = re.sub(expression, r'\1*******', PasswordText.get())


    rect1bar = canvas.create_rectangle(0, 0, 50, 500, fill=lightish_gray, outline="", tags='bar')
    rect2bar = canvas.create_rectangle(0, 0, 500, 50, fill=lightish_gray, outline="", tags='bar')
    welcomeText = canvas.create_text(250, 25, text=f"Welcome, {username}", font=font, fill=light_gray)
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
        global usernameText, username, expression, PasswordText, masked_password
        username = usernameText.get()
        masked_password = re.sub(expression, r'\1*****', PasswordText.get())
        print("home")
        canvas.itemconfigure("homeIcoUnderscoreFalse", fill=light_gray)
        canvas.itemconfigure("homeIcoUnderscoreTrue", fill="blue")
        canvas.delete("all")
        rect1bar = canvas.create_rectangle(0, 0, 50, 500, fill=lightish_gray, outline="", tags='bar')
        rect2bar = canvas.create_rectangle(0, 0, 500, 50, fill=lightish_gray, outline="", tags='bar')
        welcomeText = canvas.create_text(250, 25, text=f"Welcome, {username}", font=font, fill=light_gray)
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
        global usernameText, masked_password, expression, masked_password, username, PasswordText, firstName, middleName, lastName, age, occupation, dateOfBirth
        username = usernameText.get()
        masked_password = re.sub(expression, r'\1*******', str(PasswordText.get()))
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



        circle2 = canvas.create_oval(66.7, 66.7, 133.3, 133.3, fill=light_gray, outline=light_gray, width=1.5, tags=('userSymbol2'))
        half_circle2 = canvas.create_arc(50, 134, 150, 234, start=0, extent=180, fill=light_gray, outline=light_gray, width=1.5, tags=('userSymbol2'))
        line1_2 = canvas.create_line(48, 184, 152, 184, width=1.5, fill=light_gray, tags=('userSymbol2'))
        userSymbolRectBind2 = canvas.create_rectangle(45, 62.7, 155, 187, fill=None, width=0 ,tags=("userSymbol2"))
        canvas.scale("userSymbol2", 1, 1, 1, 1)
        canvas.move("userSymbol2", 20, 0)
        # clickToTakePicure = canvas.create_text(200, 200, text="Click To Set Avatar", tags='underline1', fill="light blue", font=('Arial', 8))
        # clickToTakePicureUnderlineCoords = canvas.bbox("underline1")
        # uX1, uY1, uX2, uY2 = clickToTakePicureUnderlineCoords
        # underlineClickToTakePicture = canvas.create_line(uX1, uY2 + 1, uX2, uY2 + 1, fill="light blue", tags="underline1")
        # canvas.tag_bind("underline1", "<Button-1>", lambda event: take_picture())
        # canvas.tag_bind(userSymbolRectBind2, "<Button-1>", lambda event: take_picture())
        if os.path.isfile("profile.jpg"):
            canvas.delete("userSymbol2")
            print("found profile.jpg")
            try:
                profile = Image.open("profile.jpg")
                profile = profile.resize((200, 200))  # Resize the image if necessary

                profileImg = ImageTk.PhotoImage(profile)
                lableProfile = tk.Label(root, image=profileImg)
                lableProfile.pack()
                print("Image loaded and displayed successfully!")
            except Exception as e:
                print("Error loading the image:", str(e))

        usernameText = tk.Entry(canvas, width=11, fg=light_gray, justify="center", font=('Arial', 12), bd=0, insertbackground=lighterish_gray) #border=.5,)
        usernameText.insert(0, f'{username}')
        usernameText.configure({"background": darkGray})

        canvas.create_window(120, 200, window=usernameText)

        PasswordText = tk.Entry(canvas, width=10, fg=light_gray, font=('Arial', 12), bd=0, insertbackground=lighterish_gray) #border=.5,)
        PasswordText.insert(0, f'{masked_password}')
        PasswordText.configure({"background": darkGray})

        canvas.create_window(120, 220, window=PasswordText)
        if lastName == False:
            def lastNameAsk():
                global lastName
                def on_close_lastAsk():
                    global lastName
                    lastName = lastNameAskVar.get()
                    print(lastName)
                    ask.destroy()
                    switch_to_user_symbol_screen()
                ask = tk.Tk()
                ask.geometry('200x100')
                ask.title("Last Name")
                text = tk.Text(ask)
                text.place(x=10, y=30)
                text.insert(tk.END, "Enter Your First Name!")
                lastNameAskVar = tk.Entry(ask)
                lastNameAskVar.place(x=10, y=10)
                lastNameAskVar.bind('<Return>', lambda event: on_close_lastAsk())  # Bind Enter key
                ask.protocol("WM_DELETE_WINDOW", on_close_lastAsk)
                ask.mainloop()
            lastNameText = canvas.create_text(300, 130, text="Click to Add Last Name", fill="light blue")
            canvas.tag_bind(lastNameText, "<Button-1>", lambda event: lastNameAsk())
        else:
            lastNameText = canvas.create_text(280, 130, text=f"{lastName}", fill=light_gray, font=font)
            canvas.tag_bind(lastNameText, "<Button-1>", lambda event: lastNameAsk())
        if firstName == False:
            def firstNameAsk():
                global firstName
                def on_close_NameAsk():
                    global firstName
                    firstName = nameAsk.get()
                    print(firstName)
                    ask.destroy()
                    switch_to_user_symbol_screen()

                global firstName
                ask = tk.Tk()
                ask.geometry('200x100')
                ask.title("Name")
                text = tk.Text(ask)
                text.place(x=10, y=30)
                text.insert(tk.END, "Enter Your First Name!")
                nameAsk = tk.Entry(ask)
                nameAsk.place(x=10, y=10)
                ask.protocol("WM_DELETE_WINDOW", on_close_NameAsk)
                nameAsk.bind('<Return>', lambda event: on_close_NameAsk())  # Bind Enter key
                ask.mainloop()
            firstNameText = canvas.create_text(300, 100, text="Click to Add First Name", fill="light blue")
            canvas.tag_bind(firstNameText, "<Button-1>", lambda event: firstNameAsk())
        else:
            firstNameText = canvas.create_text(280, 100, text=f"{firstName}", fill=light_gray, font=font)
            canvas.tag_bind(firstNameText, "<Button-1>", lambda event: firstNameAsk())
        if ageBirth == False:
            def ageBirthAsk():
                global ageBirth
                def on_close_NameAsk():
                    global ageBirth
                    ageBirth = nameAsk.get()
                    print(ageBirth)
                    ask.destroy()
                    switch_to_user_symbol_screen()

                global ageBirth
                ask = tk.Tk()
                ask.geometry('200x100')
                ask.title("Age")
                text = tk.Text(ask)
                text.place(x=10, y=30)
                text.insert(tk.END, "Enter Your Date Of Birth!")
                nameAsk = tk.Entry(ask)
                nameAsk.place(x=10, y=10)
                ask.protocol("WM_DELETE_WINDOW", on_close_NameAsk)
                nameAsk.bind('<Return>', lambda event: on_close_NameAsk())  # Bind Enter key
                ask.mainloop()
            ageBirthText = canvas.create_text(300, 160, text="Click to Add Birth-Date", fill="light blue")
            canvas.tag_bind(ageBirthText, "<Button-1>", lambda event: ageBirthAsk())
        else:
            ageBirthText = canvas.create_text(280, 160, text=f"{ageBirth}", fill=light_gray, font=font)
            canvas.tag_bind(ageBirthText, "<Button-1>", lambda event: ageBirthAsk())
            
        

        


    def switch_to_menu_ico_screen():
        global usernameText, PasswordText, expression, masked_password, username
        username = usernameText.get()
        masked_password = re.sub(expression, r'\1*******', PasswordText.get())
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

        wordGuessGame = canvas.create_text(250, 130, text=f"Click To Play Word Guess Game!", fill="light blue", font=font)
        canvas.tag_bind(wordGuessGame, "<Button-1>", lambda event: wordGuessing())

        def tictactoe():
            rootTTTAsk = tk.Tk()
            rootTTTAsk.geometry('300x100')
            rootTTTAsk.title("Tic Tac Toe")
            def playTTT1():
                rootTTTAsk.destroy()
                tic_tac_toe1P()
                return
            def playTTT2():
                rootTTTAsk.destroy()
                tic_tac_toe2P()
                return



            # Create a button for 1 player game
            btn_1p = tk.Button(rootTTTAsk, text="1 Player", command=playTTT1)
            btn_1p.pack()

            # Create a button for 2 player game
            btn_2p = tk.Button(rootTTTAsk, text="2 Player", command=playTTT2)
            btn_2p.pack()

            rootTTTAsk.mainloop()


        tttText = canvas.create_text(250, 160, text=f"Click To Play Tic Tac Toe!", fill="light blue", font=font)
        canvas.tag_bind(tttText, "<Button-1>", lambda event: tictactoe())

        


        addto100Text = canvas.create_text(250, 190, text=f"Click To Play Add To 100 Game!", fill="light blue", font=font)
        canvas.tag_bind(addto100Text, "<Button-1>", lambda event: addTo100Game())

    # Bind click events to rectangles using lambda functions
    canvas.tag_bind(homeRectBind, "<Button-1>", lambda event: switch_to_home_screen())
    canvas.tag_bind(userSymbolRectBind, "<Button-1>", lambda event: switch_to_user_symbol_screen())
    canvas.tag_bind(menuIcoSymbolRectBind, "<Button-1>", lambda event: switch_to_menu_ico_screen())

        

    








#-----------------------------------------------


# Create a Tkinter window
root = tk.Tk()
root.geometry("500x400")
root.config(bg=darkGray)
root.title("Login")

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
password_entry = tk.Entry(canvas, width=34, fg=light_gray, font=font, bd=0, insertbackground=lighterish_gray) #border=.5,)
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


loginTopText = canvas.create_text(170, 50, text="Login to your account", fill='#818181', font=("Helvetica", 18))

# Bind focus and unfocus events to entry box
password_entry.bind('<FocusIn>', on_entry_click2)
password_entry.bind('<FocusOut>', on_entry_unfocus2)

# Place entry box on canvas
canvas.create_window(265, 175, window=password_entry)

# Define function to remove focus from canvas
def remove_focus(event):
    root.focus()

# Bind the function to the '<Button-1>' event of the canvas
canvas.bind('<Button-1>', remove_focus)

# button = tk.Button(text='Login', command=lambda: print("clicked"), bg=lightish_gray, fg=whitish, activebackground=lighterish_gray, activeforeground=whitish, padx=10, pady=5, highlightthickness=0, font=('Arial', 10, 'bold'), relief='solid', bd=1, borderwidth=1, highlightbackground='black')

# canvas.create_window(250, 200, window=button)

# region button
# Create the button symbol using create methods
canvas_bg_color = canvas.cget('background')

leftCircleSubmitBind = canvas.create_arc(150, 100, 230, 150, start=90, extent=180, width=0, outline=canvas_bg_color, tags=('submit'), fill=canvas_bg_color) #set fill to bg color
rightCircleSubmitBind = canvas.create_arc(460, 100, 540, 150, start=90, extent=-180, width=0, outline=canvas_bg_color, tags=('submit'), fill=canvas_bg_color) #set fill to bg color

rectBaseSubmit = canvas.create_rectangle(190, 100, 500, 150, fill=None, outline=None, width=0, tags=('submit'))
rectBaseTop = canvas.create_line(190, 100, 500, 100, width=2, fill='#818181', tags=('submit'))
rectBaseBottom = canvas.create_line(190, 150, 500, 150, width=2, fill='#818181', tags=('submit'))
leftCircleSubmit = canvas.create_arc(150, 100, 230, 150, start=90, extent=180, style="arc", width=2, outline='#818181', tags=('submit'))
rightCircleSubmit = canvas.create_arc(460, 100, 540, 150, start=90, extent=-180, style="arc", width=2, outline='#818181', tags=('submit'))
loginText = canvas.create_text(340, 125, text="Log In", fill='#818181', font=("Helvetica", 18), tags='submit')
# endregion button


def on_mouse_move(event):
    x = event.x
    y = event.y
    
    # print(f"Mouse position: ({x}, {y})")

canvas.bind("<Motion>", on_mouse_move)

import re
from tkinter import messagebox
def click(event):
    global username, password, masked_password, expression
    username = username_entry.get()
    password = password_entry.get()
    expression = r'(.*).....$'  # Match any characters before the last 5 characters
    masked_password = re.sub(expression, r'\1*****', password)  # Substitute last 5 characters with '*'
    if password.lower() != str('password') and username.lower() != str('username') and username.lower() != '':
        if any(char.isdigit() for char in password):
            if len(password) >= 8:
                if len(username) >= 3:
                    runApp()
                else:
                    messagebox.showwarning("Error", "Your username must be at least 3 characters long!")
            else:
                messagebox.showwarning("Error", "Your password must be at least 8 characters long!")
        else:
            messagebox.showwarning("Error", "Your password must have at least one number!")
    else:
        messagebox.showwarning("Error", "Please fill out all the required fields!")
    

# Bind the clicked function to the left mouse button click event on the button symbol
canvas.tag_bind('submit', '<Button-1>', click)
root.bind('<Return>', click)

canvas.scale('submit', 0, 0, .6, .85)
canvas.move('submit', -25, 200)


hide_password = False

# region eye Symbol

# Create a circle
circle = canvas.create_oval(27.2, 17.2, 42.8, 32.8, fill=light_gray, outline=light_gray, tags=('eyeShowPassword'))
# Create a half circle, Create a line to close off the bottom
half_circle = canvas.create_arc(0, 0, 70, 60, start=0, extent=180, fill=light_gray, outline=light_gray, style="arc", width=2, tags=('eyeShowPassword'))
rectToBindEye = canvas.create_rectangle(-5, -5, 75, 40, fill=None, outline=None, width=0,tags=('eyeShowPassword'))
# endregion

canvas.scale('eyeShowPassword', 0, 0, 0.3, 0.3)  # shrink the size of the symbol
canvas.move('eyeShowPassword', 460, 170)  # move the symbol with x, y directional pixel





canvas.tag_bind(rectToBindEye, "<Button-1>", lambda event: toggle_password_visibility())



root.mainloop()
