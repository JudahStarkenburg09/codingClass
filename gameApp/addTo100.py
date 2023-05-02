import tkinter as tk

# Initialize player variable and board list
player = 1

total = 0

def switch_player():
    global player
    if player == 1:
        player = 2
    else:
        player = 1

def on_key_press(event):
    global player, gray_rect_id, total
    number = event.char
    if number.isdigit() and int(number) in range(1, 10):
        print(f"Player {player}: {number}")
        total = total + int(number)
        print(f"Total: {total}")
        if total >= 100:
            if player == 1:
                print("Winner is Player 2!")
            else:
                print("Winner is Player 1!")


        if gray_rect_id is not None:
            canvas.delete(gray_rect_id)
            gray_rect_id = None
        switch_player()
        # Add gray overlay to non-active player's side
        if player == 1:
            gray_rect_id = canvas.create_polygon(200, 0, 400, 0, 400, 200, 200, 200, fill="#808080", outline="", stipple="gray50")

        else:
            gray_rect_id = canvas.create_polygon(0, 0, 200, 0, 200, 200, 0, 200, fill="#808080", outline="", stipple="gray50")




# Initialize Tkinter window and canvas
window = tk.Tk()
window.title("Add To 100")
window.geometry("400x300")
canvas = tk.Canvas(window, width=400, height=200)
canvas.pack()

# Add rectangles to represent each player's half of the canvas
canvas.create_rectangle(0, 0, 200, 200, fill="red")
canvas.create_rectangle(200, 0, 400, 200, fill="blue")

# Add labels to identify each player
canvas.create_text(100, 50, text="Player 1", font=("Arial", 20))
canvas.create_text(300, 50, text="Player 2", font=("Arial", 20))

gray_rect_id = canvas.create_polygon(200, 0, 400, 0, 400, 200, 200, 200, fill="#808080", outline="", stipple="gray50")

# Bind key press event to the window
window.bind("<KeyPress>", on_key_press)

# Start the main loop
window.mainloop()
