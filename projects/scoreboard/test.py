import tkinter as tk

def show_keybinds():
    keybinds = """Press (Q, W) to change left score
Press (O, P) to change right score
Press space to switch sides
Press T to start/pause the timer
Press F11 To Toggle Fullscreen
Press arrow keys (< >) to change possession
Press Enter to Reset Timer
Press Ctrl + Enter to Reset Score, Possession, and Timer
Press f1 to show Keybinds again"""
    
    # Create a new window
    keybinds_window = tk.Toplevel(root)
    keybinds_window.title("Keybinds")

    # Create a label to display the keybinds
    label = tk.Label(keybinds_window, text=keybinds, padx=10, pady=10)
    label.pack()

    # Create an OK button to close the window
    ok_button = tk.Button(keybinds_window, text="OK", command=keybinds_window.destroy)
    ok_button.pack(pady=10)

# Example usage
root = tk.Tk()
root.title("ROOT")

# Assuming you have a function to call this, for example, a button command
# This function will open a new window with the keybinds information
show_keybinds()

# Start the Tkinter event loop
root.mainloop()
