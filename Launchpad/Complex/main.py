import os
import json
import launchpad_py as launchpad
import time
import pygame
import os
import subprocess
import platform
import threading
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

file_to_delete = "config.json" # We will add it back later
if os.path.exists(file_to_delete):
    os.remove(file_to_delete)
else:
    print(f"The file '{file_to_delete}' does not exist.")

def change_volume(change_type, step=0.05):
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None
    ).QueryInterface(IAudioEndpointVolume)

    current_volume = interface.GetMasterVolumeLevelScalar()
    
    if change_type == "up":
        new_volume = min(1.0, current_volume + step)
    elif change_type == "down":
        new_volume = max(0.0, current_volume - step)
    else:
        print("Invalid change_type. Use 'up' or 'down'.")
        return

    interface.SetMasterVolumeLevelScalar(new_volume, None)

badNumbers= [8,24,40,56,72,88,104]


MAX_BUTTONS = 120
config_file_path = os.path.join(os.getcwd(), "config.json")
sounds_folder_path = os.path.join(os.getcwd(), "Sounds")

def stop_all_sounds():
    global lp

    config_data = loadConfig()
    
    lp.LedCtrlRaw(207, 255, 0)

    for button_data in config_data:
        button_number = button_data["Button#"]
        mp3_file = button_data["MP3File"]

        if mp3_file:
            # Stop the sound on the corresponding button channel
            pygame.mixer.Channel(button_number).stop()

            # Turn the button back to red
            lp.LedCtrlRaw(button_number, 255, 0)

    time.sleep(0.5)


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
        lp.LedCtrlRaw(207, 255, 255)
        lp.LedCtrlRaw(200, 255, 255)
        lp.LedCtrlRaw(201, 255, 255)

        while not done:
            countMP3s = len(mp3_files)
            done = True
            for button_number, mp3_file in enumerate(mp3_files):
                print(f"Sounds Left: {countMP3s}")
                countMP3s -= 1
                print(f"MP3 File: [{mp3_file}], Press a button to assign to the MP3 file")
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

def set_system_volume(volume):
    system_platform = platform.system()

    if system_platform == "Windows":
        subprocess.run(["nircmd.exe", "setsysvolume", str(int(volume * 65535))])
    elif system_platform == "Linux":
        subprocess.run(["amixer", "set", "Master", f"{int(volume * 100)}%"])
    elif system_platform == "Darwin":  # macOS
        subprocess.run(["osascript", "-e", f'set volume output volume {int(volume * 100)}'])

def playLoop():
    global lp
    print("Sound loop started")
    pygame.init()
    pygame.mixer.init()

    # Set the number of channels you want to use
    pygame.mixer.set_num_channels(MAX_BUTTONS)

    # Create a dictionary to map buttons to tracks
    button_tracks = {}
    volume = 0.5  # Initial volume

    while True:
        buttons = lp.ButtonStateRaw()
        if buttons:
            if buttons[1]:
                pressed_button = buttons[0]
                config_data = loadConfig()

                if pressed_button == 207:
                    stop_all_sounds()
                    lp.LedCtrlRaw(207, 255, 255)
                elif pressed_button == 200:
                    change_volume("up", step=0.1)
                    lp.LedCtrlRaw(200, 255, 255)

                elif pressed_button == 201:
                    change_volume("down", step=0.1)
                    lp.LedCtrlRaw(201, 255, 255)


                elif 0 <= pressed_button < MAX_BUTTONS and config_data[pressed_button]["MP3File"]:
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