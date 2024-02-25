from pynput.mouse import Listener, Button
import pyautogui
import time

def on_click(x, y, button, pressed):
    if button == desired_button and pressed:
        pyautogui.press('8')

def record(x, y, button, pressed):
    global desired_button
    if pressed:
        desired_button = button
        print(f"Selected hotkey: {button}")
        return False  # Stop the listener after recording the button
    
desired_button = None
print("Press the mouse button you want to use for the action...")

# Wait for the user to press a mouse button and record it
with Listener(on_click=record) as listener:
    listener.join()

print(f"Hotkey is {desired_button}, starting in 2 seconds")
time.sleep(2)
print("Started")

# Create a listener that listens for mouse button press and triggers the action
with Listener(on_click=on_click) as listener:
    listener.join()
