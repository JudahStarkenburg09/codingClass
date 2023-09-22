import pyautogui
import time

def main():
    # Sleep for a few seconds to allow the computer to detect the USB drive
    time.sleep(5)

    # Simulate typing "hi"
    pyautogui.typewrite("hi")

if __name__ == "__main__":
    main()
