import tkinter as tk

# Create the main window
root = tk.Tk()

# Set the window title
root.title("Game Menu")
root.geometry('295x300')
# Create the login frame
login_frame = tk.Frame(root)
login_frame.pack(padx=20, pady=20)

# Create the username label and entry field
username_label = tk.Label(login_frame, text="Username:")
username_label.pack(side=tk.LEFT, padx=5)
username_entry = tk.Entry(login_frame)
username_entry.pack(side=tk.LEFT, padx=5)

# Create the login button
def login():
    global userName
    userName = username_entry.get()
    menu_frame.pack()
    login_frame.pack_forget()

login_button = tk.Button(login_frame, text="Login", command=login)
login_button.pack(side=tk.LEFT, padx=5)

# Create the menu frame
menu_frame = tk.Frame(root)

# Create the hangman button
def play_hangman():
    print("Playing Hangman...")

hangman_button = tk.Button(menu_frame, text="Hangman", command=play_hangman)
hangman_button.pack(pady=5)

# Create the pong button
def play_pong():
    print("Playing Pong...")

pong_button = tk.Button(menu_frame, text="Pong", command=play_pong)
pong_button.pack(pady=5)

# Create the car highway button
def play_car_highway():
    print("Playing Car Highway...")

car_highway_button = tk.Button(menu_frame, text="Car Highway", command=play_car_highway)
car_highway_button.pack(pady=5)

# Create the tic tac toe 1 player button
def play_tic_tac_toe_1p():
    print("Playing Tic Tac Toe 1 Player...")

tic_tac_toe_1p_button = tk.Button(menu_frame, text="Tic Tac Toe 1 Player", command=play_tic_tac_toe_1p)
tic_tac_toe_1p_button.pack(pady=5)

# Create the tic tac toe 2 player button
def play_tic_tac_toe_2p():
    print("Playing Tic Tac Toe 2 Player...")

tic_tac_toe_2p_button = tk.Button(menu_frame, text="Tic Tac Toe 2 Player", command=play_tic_tac_toe_2p)
tic_tac_toe_2p_button.pack(pady=5)

# Create the baseball game button
def play_baseball():
    print("Playing Baseball Game...")

baseball_button = tk.Button(menu_frame, text="Baseball Game", command=play_baseball)
baseball_button.pack(pady=5)

# Hide the menu frame initially
menu_frame.pack_forget()

# Start the application
root.mainloop()
