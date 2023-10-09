import webview
import threading
import time
import keyboard
import tkinter as tk
import pyautogui

def simulate_typing():
    global root
    root.destroy()
    # Simulate typing a username
    keyboard.write("NCAServerStarter")
    # Press Enter to move to the next field (you may need to adjust this)
    keyboard.press_and_release("tab")

    # Simulate typing a password
    keyboard.write("123NCA")

    # Press Enter again to submit the form (you may need to adjust this)
    keyboard.press_and_release("enter")
    
alreadyLoaded = False
def getLogin():
    
    global root, alreadyLoaded
    if alreadyLoaded == False:
        alreadyLoaded = True
        root = tk.Tk()
        root.title("Login")

        # Create a label
        label = tk.Label(root, text="Log In?")
        label.pack(pady=10)

        # Create "Yes" button
        yes_button = tk.Button(root, text="Yes", command=simulate_typing)
        yes_button.pack(padx=10, pady=5)

        # Create "Already Logged In" button
        already_logged_in_button = tk.Button(root, text="Already Logged In!", command=root.destroy)
        already_logged_in_button.pack(padx=10, pady=5)

    root.mainloop()

def on_loaded():
    time.sleep(5)
    print("Webview window has fully loaded")
    getLogin()

def main():
    # Create a webview window
    window_width, window_height = pyautogui.size()
    webview.create_window("Aternos Server", "https://aternos.org/server/")
    # Run the webview main loop
    threadTime = threading.Thread(target=on_loaded)
    threadTime.start()
    webview.start()

if __name__ == "__main__":
    main()