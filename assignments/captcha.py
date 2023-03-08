from tkinter import *
import random
import time
wronged = False
failCount = 0
notRobot = False
import os
def returnOriginalPage():
    global tk
    os.system('cls')
    print('PUT RETURN PAGE HERE')

def runNextFunction():
    #COMPLETE CAPTCHA HERE:
    
    tk = Tk()
    tk.title('Success')
    tk.geometry('300x50')
    success = Label(tk, text="You Are Not A Robot")
    success.pack()
    tk.mainloop()

def failCaptchaReturn():
    #RETURN TO OTHER ORIGINAL PAGE:
    global tk
    tk = Tk()
    tk.title('Fail')
    tk.geometry('300x50')
    fail = Label(tk, text="Fail! Too Many Attempts! Please Try Again Later!")
    fail.pack()
    button = Button(tk, text='Back', command=returnOriginalPage)
    button.pack()
    os.system('cls')
    tk.mainloop()
    os.system('cls')

def on_window_close():
    global notRobot
    global wronged
    window.destroy()
    notRobot = True



def captcha():
    global failCount
    window.destroy()
    root = Tk()
    root.title('Captcha')
    root.geometry('400x400')
    root.protocol("WM_DELETE_WINDOW", on_window_close)

    canvas = Canvas(root, width=300, height=300)
    canvas.pack()

    shapes = ["square", "triangle", "circle"]
    colors = ["red", "green", "blue", "yellow", "orange", "cyan", "pink", "purple", "gray"]
    listOfCombos = []




    positions = []
    for i in range(3):
        for j in range(3):
            x1 = i * 100 + 10
            y1 = j * 100 + 10
            x2 = x1 + 80
            y2 = y1 + 80
            positions.append([x1, y1, x2, y2])

    for i in range(9):
        shape_choice = random.choice(shapes)
        square_choice = random.choice(positions)
        positions.remove(square_choice)
        color_choice = random.choice(colors)
        colors.remove(color_choice)
        if shape_choice == "square":
            shape = canvas.create_rectangle(square_choice[0], square_choice[1], square_choice[2], square_choice[3], fill=color_choice)
        elif shape_choice == "triangle":
            x1, y1 = square_choice[0] + 40, square_choice[1] + 10
            x2, y2 = square_choice[2] - 10, square_choice[3] - 10
            x3, y3 = square_choice[0] + 10, square_choice[3] - 10
            shape = canvas.create_polygon(x1, y1, x2, y2, x3, y3, fill=color_choice)
        elif shape_choice == "circle":
            shape = canvas.create_oval(square_choice[0], square_choice[1], square_choice[2], square_choice[3], fill=color_choice, outline="")
        canvas.tag_bind(shape, "<Button-1>", lambda event, shape=shape_choice, color=color_choice: on_click(event, shape, color))
        listOfCombos.append(f"{color_choice} {shape_choice}")


    clickOn = random.choice(listOfCombos)
    text_label = Label(root, text=f"To Verify You Are Human, Click a {clickOn}")
    text_label.pack(side=BOTTOM)

    def on_click(event, shape, color):
        global wronged
        global failCount
        global notRobot
        # print(f"You clicked on a {color} {shape}.")
        clicked = f"{color} {shape}"
        if clickOn == clicked:
            notRobot = True
            root.destroy()
            runNextFunction()
        else:
            failCount = failCount + 1
            wronged = True
            root.destroy()
            
    
    root.mainloop()


while notRobot == False:
    window = Tk()
    window.title('Verify You Are Not A Robot')
    window.geometry('300x300')
    window.protocol("WM_DELETE_WINDOW", on_window_close)
    canvas = Canvas(window, width=250, height=250, bg="light gray")
    canvas.pack()
    square = canvas.create_rectangle(60, 60, 220, 100, fill="white", width=0)
    # create the square shape
    square = canvas.create_rectangle(60, 60, 100, 100, fill="white")
    if wronged == True:
        textLabel4 = Label(window, text="Wrong!")
        textLabel4.config(bg='light gray', fg='red')
        textLabel4.place(x=125, y=10)
    if failCount == 3:
        notRobot = True
        window.destroy()
        failCaptchaReturn()

        
    textLabel = Label(window, text="I Am Not A Robot")
    textLabel.config(bg='white')
    textLabel.place(x=130, y=70)

    # define the checkmark line coordinates
    checkmark_coords = [(70, 80), (80, 90), (95, 70)]

    # create a boolean variable to keep track of whether the checkbox is checked
    checked = False

    # create a function to handle checkbox clicks
    def on_checkbox_click(event):
        global checked
        if not checked:
            # draw the checkmark line on top of the square
            canvas.create_line(*checkmark_coords, width=3, fill="black")
            checked = True
            textLabel = Label(window, text="Please Wait...           ")
            textLabel.config(bg='white')
            textLabel.place(x=130, y=70)
            canvas.after(2000, captcha)


    # bind the click event to the square
    canvas.tag_bind(square, "<Button-1>", on_checkbox_click)

    window.mainloop()

