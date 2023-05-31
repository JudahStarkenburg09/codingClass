import tkinter as tk
from tkinter import messagebox
import random

def tic_tac_toe1P():
    # Create the main window
    window = tk.Tk()
    window.title("Tic Tac Toe")

    # Create variables for players
    human_player = "X"
    bot_player = "O"

    # Create the board
    board = [["" for _ in range(3)] for _ in range(3)]

    # Create the buttons
    buttons = []
    for row in range(3):
        button_row = []
        for col in range(3):
            button = tk.Button(
                window,
                text="",
                width=10,
                height=5,
                font=("Helvetica", 20, "bold"),
                command=lambda row=row, col=col: make_move(row, col),
            )
            button.grid(row=row, column=col, sticky="nsew")
            button_row.append(button)
        buttons.append(button_row)

    # Function to handle human player's move and update the game state
    def make_move(row, col):
        if board[row][col] == "":
            board[row][col] = human_player
            buttons[row][col].config(text=human_player)
            if check_win(human_player):
                draw_winning_line()
                messagebox.showinfo("Game Over", "You win!")
                reset_game()
            elif check_draw():
                messagebox.showinfo("Game Over", "It's a draw!")
                reset_game()
            else:
                make_bot_move()

    # Function to make the bot's move
    def make_bot_move():
        # Check if the bot can win
        for row in range(3):
            for col in range(3):
                if board[row][col] == "":
                    board[row][col] = bot_player
                    if check_win(bot_player):
                        buttons[row][col].config(text=bot_player)
                        draw_winning_line()
                        messagebox.showinfo("Game Over", "Bot wins!")
                        reset_game()
                        return
                    else:
                        board[row][col] = ""

        # Check if the bot needs to block the player's winning move
        for row in range(3):
            for col in range(3):
                if board[row][col] == "":
                    board[row][col] = human_player
                    if check_win(human_player):
                        buttons[row][col].config(text=bot_player)
                        board[row][col] = bot_player
                        return
                    else:
                        board[row][col] = ""

        # Randomly select an available spot for the bot's move
        available_spots = []
        for row in range(3):
            for col in range(3):
                if board[row][col] == "":
                    available_spots.append((row, col))
        if available_spots:
            row, col = random.choice(available_spots)
            board[row][col] = bot_player
            buttons[row][col].config(text=bot_player)
            if check_win(bot_player):
                draw_winning_line()
                messagebox.showinfo("Game Over", "Bot wins!")
                reset_game()
            elif check_draw():
                messagebox.showinfo("Game Over", "It's a draw!")

    # Function to check for a win
    def check_win(player):
        for i in range(3):
            if (
                board[i][0] == board[i][1] == board[i][2] == player
                or board[0][i] == board[1][i] == board[2][i] == player
            ):
                return True
        if (
            board[0][0] == board[1][1] == board[2][2] == player
            or board[0][2] == board[1][1] == board[2][0] == player
        ):
            return True
        return False

    # Function to check for a draw
    def check_draw():
        for row in board:
            if "" in row:
                return False
        return True

    # Function to reset the game
    def reset_game():
        nonlocal board
        board = [["" for _ in range(3)] for _ in range(3)]
        for row in buttons:
            for button in row:
                button.config(text="", bg="white")

    # Function to draw a green line on the winning spots
    def draw_winning_line():
        # Check rows
        for row in range(3):
            if (
                board[row][0] == board[row][1] == board[row][2] != ""
            ):
                buttons[row][0].config(bg="green")
                buttons[row][1].config(bg="green")
                buttons[row][2].config(bg="green")
                return

        # Check columns
        for col in range(3):
            if (
                board[0][col] == board[1][col] == board[2][col] != ""
            ):
                buttons[0][col].config(bg="green")
                buttons[1][col].config(bg="green")
                buttons[2][col].config(bg="green")
                return

        # Check diagonals
        if (
            board[0][0] == board[1][1] == board[2][2] != ""
        ):
            buttons[0][0].config(bg="green")
            buttons[1][1].config(bg="green")
            buttons[2][2].config(bg="green")
            return
        if (
            board[0][2] == board[1][1] == board[2][0] != ""
        ):
            buttons[0][2].config(bg="green")
            buttons[1][1].config(bg="green")
            buttons[2][0].config(bg="green")
            return

    # Start the game
    window.mainloop()

# Call the function to play the game
# tic_tac_toe1P()
