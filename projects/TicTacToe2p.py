import tkinter as tk
from tkinter import messagebox

def tic_tac_toe2P():
    # Create the main window
    window = tk.Tk()
    window.title("Tic Tac Toe")

    # Create variables for players
    current_player = "X"

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

    # Function to handle button click and update the game state
    def make_move(row, col):
        nonlocal current_player
        if board[row][col] == "":
            board[row][col] = current_player
            buttons[row][col].config(text=current_player)
            if check_win(current_player):
                draw_winning_line()
                messagebox.showinfo("Game Over", f"Player {current_player} wins!")
                reset_game()
            elif check_draw():
                messagebox.showinfo("Game Over", "It's a draw!")
                reset_game()
            else:
                current_player = "O" if current_player == "X" else "X"

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
        nonlocal current_player, board
        current_player = "X"
        board = [["" for _ in range(3)] for _ in range(3)]
        for row in buttons:
            for button in row:
                button.config(text="",bg="white")

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
# tic_tac_toe2P()
