import os
import json
import launchpad_py as launchpad
import time
import pygame
import threading

badNumbers= [8,24,40,56,72,88,104]


MAX_BUTTONS = 120
config_file_path = os.path.join(os.getcwd(), "config.json")
sounds_folder_path = os.path.join(os.getcwd(), "Sounds")

def createConfig():
    config_data = [{"Button#": i, "MP3File": ""} for i in range(MAX_BUTTONS)]

    try:
        with open(config_file_path, 'w') as config_file:
            json.dump(config_data, config_file, indent=2)
        print(f"{config_file_path} created successfully.")
    except Exception as e:
        print(f"Error creating config file: {e}")

def loadConfig():
    try:
        with open(config_file_path, 'r') as config_file:
            config_data = json.load(config_file)
        return config_data
    except FileNotFoundError:
        createConfig()
        return loadConfig()
    except Exception as e:
        print(f"Error reading config file: {e}")
        return None

def saveConfig(config_data):
    try:
        with open(config_file_path, 'w') as config_file:
            json.dump(config_data, config_file, indent=2)
    except Exception as e:
        print(f"Error saving config file: {e}")

def getButtonPress(lp):
    while True:
        buttons = lp.ButtonStateRaw()
        if buttons:
            if buttons[1] == True:
                return buttons[0]
        time.sleep(0.1)

def assignSounds():
    global lp, badNumbers
    print("Launchpad Mk1")

    lp = launchpad.Launchpad()

    if lp.Open():
        lp.ButtonFlush()
        lp.Reset()
        mp3_files = [file for file in os.listdir(sounds_folder_path) if file.endswith(".mp3")]
        config_data = loadConfig()
        done = False
        while not done:
            done = True
            for button_number, mp3_file in enumerate(mp3_files):
                print(f"MP3 File: {mp3_file}")
                print("Press a button to assign to the MP3 file")
                button_pressed = getButtonPress(lp)

                if (0 <= button_pressed < MAX_BUTTONS) and not any(int(button_pressed) == i for i in badNumbers):
                    config_data[button_pressed]["MP3File"] = mp3_file
                    print(f"Assigned {mp3_file} to Button# {button_pressed}.")
                    lp.LedCtrlRaw(button_pressed, 255, 0)
                    print("\n\n")
                else:
                    print("\n\n-------------------------------------------")
                    print("Invalid input. Please enter a valid button")
                    print("------------------------------------------- \n\n")
                    done = False
                    lp.Reset()
                    break

        saveConfig(config_data)
        print("DONE!!! Starting sound loop in 3 seconds, Do not press any buttons until the loop has started!")
        time.sleep(3)
    else:
        print("Did not find any Launchpad Mk1.")

def play_sound(button, mp3_path):
    global lp

    channel = pygame.mixer.Channel(button)
    sound = pygame.mixer.Sound(mp3_path)
    channel.play(sound)

    # Wait for the sound to finish playing
    while channel.get_busy():
        time.sleep(0.1)

    # Sound has finished, turn the button back to red
    lp.LedCtrlRaw(button, 255, 0)

def playLoop():
    global lp
    print("Sound loop started")
    pygame.init()
    pygame.mixer.init()

    # Set the number of channels you want to use
    pygame.mixer.set_num_channels(MAX_BUTTONS)

    # Create a dictionary to map buttons to tracks
    button_tracks = {}

    while True:
        buttons = lp.ButtonStateRaw()
        if buttons:
            if buttons[1]:
                pressed_button = buttons[0]
                config_data = loadConfig()

                if 0 <= pressed_button < MAX_BUTTONS and config_data[pressed_button]["MP3File"]:
                    mp3_file = config_data[pressed_button]["MP3File"]
                    mp3_path = os.path.join(sounds_folder_path, mp3_file)

                    if os.path.exists(mp3_path):
                        # Turn the button green while the sound is playing
                        lp.LedCtrlRaw(pressed_button, 0, 255)

                        # Create and start a new thread for each sound
                        track_thread = threading.Thread(target=play_sound, args=(pressed_button, mp3_path))
                        track_thread.start()

                        # Store the thread in the dictionary
                        button_tracks[pressed_button] = track_thread



assignSounds()
print("Playing loop")
playLoop()