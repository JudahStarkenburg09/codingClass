import tkinter as tk
def addTo100Game():
    global disableGame, total, player, gray_rect_id, totalText, turnText, goalORwinText, switch_player
    # Initialize player variable and board list
    player = 1
    disableGame = False
    total = 0

    def saveNames():
        global player1Name, player2Name
        nonlocal player1entry, player2entry
        if player1entry.get() == "":
            player1Name = "Player 1"
        else:
            player1Name = player1entry.get()

        if player2entry.get() == "":
            player2Name = "Player 2"
        else:
            player2Name = player2entry.get()
        root100Game.destroy()

    def on_closing():
        exit()

    root100Game = tk.Tk()
    root100Game.geometry('350x100')
    root100Game.title("ENTER PLAYER NAMES")
    root100Game.protocol("WM_DELETE_WINDOW", on_closing)

    login_frame = tk.Frame(root100Game)
    login_frame.pack(padx=20, pady=20)

    player1entry = tk.Entry(login_frame)
    player1entry.pack(side=tk.LEFT, padx=5)

    player2entry = tk.Entry(login_frame)
    player2entry.pack(side=tk.LEFT, padx=5)

    login_button = tk.Button(login_frame, text="Play", command=saveNames)
    login_button.pack(side=tk.LEFT, padx=5)

    root100Game.protocol("WM_DELETE_WINDOW", on_closing)

    root100Game.mainloop()





    def switch_player():
        global player, gray_rect_id, total, totalText, goalORwinText, disableGame, turnText,player1entry,player2entry,player1Name,player2Name,switch_player
        global player
        if player == 1:
            player = 2
        else:
            player = 1

    def on_key_press(event):
        global player, gray_rect_id, total, totalText, goalORwinText, disableGame, turnText,player1entry,player2entry,player1Name,player2Name,switch_player
        
        number = event.char
        if disableGame == False:
            if number.isdigit() and int(number) in range(1, 10):
                total = total + int(number)
                if total >= 50:
                    canvas100Game.delete(goalORwinText)
                    if player == 1:
                        goalORwinText = canvas100Game.create_text(200, 230, text=f"Winner Is {player2Name}!", font=("Arial", 25))
                        disableGame = True
                    else:
                        goalORwinText = canvas100Game.create_text(200, 230, text=f"Winner Is {player1Name}!", font=("Arial", 25))  
                        disableGame = True
                    gray_rect_id_OVER = canvas100Game.create_polygon(200, 0, 400, 0, 400, 200, 200, 200, fill="#000000", outline="", stipple="gray75")
                    gray_rect_id_OVER = canvas100Game.create_polygon(0, 0, 200, 0, 200, 200, 0, 200, fill="#000000", outline="", stipple="gray75")
                    canvas100Game.delete(turnText)
                    canvas100Game.delete(totalText)
                    totalText = canvas100Game.create_text(200, 320, text=f"{total}", font=("Arial", 40))
                    return
                    



                if gray_rect_id is not None:
                    canvas100Game.delete(gray_rect_id)
                    gray_rect_id = None
                switch_player()
                # Add gray overlay to non-active player's side
                if player == 1:
                    gray_rect_id = canvas100Game.create_polygon(200, 0, 400, 0, 400, 200, 200, 200, fill="#000000", outline="", stipple="gray75")

                else:
                    gray_rect_id = canvas100Game.create_polygon(0, 0, 200, 0, 200, 200, 0, 200, fill="#000000", outline="", stipple="gray75")
                canvas100Game.delete(totalText)
                totalText = canvas100Game.create_text(200, 320, text=f"{total}", font=("Arial", 40))
                canvas100Game.delete(turnText)
                if player == 1:
                    whoseTurn = player1Name
                else:
                    whoseTurn = player2Name
                turnText = canvas100Game.create_text(200, 370, text=f"{whoseTurn} Turn", font=("Arial", 25))




    # Initialize Tkinter window and canvas
    window100Game = tk.Tk()
    window100Game.title("Add To 50")
    window100Game.geometry("400x400")
    canvas100Game = tk.Canvas(window100Game, width=1000, height=1000)
    canvas100Game.pack()




    if player == 1:
        whoseTurn = player1Name
    else:
        whoseTurn = player2Name



    # Add rectangles to represent each player's half of the canvas
    canvas100Game.create_rectangle(0, 0, 200, 200, fill="#FCC300")
    canvas100Game.create_rectangle(200, 0, 400, 200, fill="#1BFF00")

    # Add labels to identify each player
    canvas100Game.create_text(100, 50, text=f"{player1Name}", font=("Arial", 20))
    canvas100Game.create_text(300, 50, text=f"{player2Name}", font=("Arial", 20))

    totalText = canvas100Game.create_text(200, 320, text=f"{total}", font=("Arial", 40))
    turnText = canvas100Game.create_text(200, 370, text=f"{whoseTurn} Turn", font=("Arial", 25))
    goalORwinText = canvas100Game.create_text(200, 250, text="""         The Goal Of The Game Is:
    Force The Other Player To Add to 50!
                Type a Number 1-9...""", font=("Arial", 15))

    gray_rect_id = canvas100Game.create_polygon(200, 0, 400, 0, 400, 200, 200, 200, fill="#000000", outline="", stipple="gray75")

    # Bind key press event to the window
    window100Game.bind("<KeyPress>", on_key_press)

    # Start the main loop
    window100Game.mainloop()