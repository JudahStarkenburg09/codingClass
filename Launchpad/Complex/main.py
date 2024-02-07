import sys
import pygame.midi
from pydub import AudioSegment
from pydub.generators import Sine
from pydub import AudioSegment
import os
import json
import launchpad_py as launchpad
import time
import pygame
import subprocess
import platform
import threading
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

file_to_delete = "config.json"

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

badNumbers = [8, 24, 40, 56, 72, 88, 104]

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
            pygame.mixer.Channel(button_number).stop()
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
            if buttons[1]:
                return buttons[0]
        time.sleep(0.1)

buttonsToColorSFX = []


def assignSounds():
    global lp, badNumbers, buttonsToColorSFX

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
        lp.LedCtrlRaw(205, 255, 255)


        while not done:
            countMP3s = len(mp3_files)
            done = True
            for button_number, mp3_file in enumerate(mp3_files):
                print(f"Sounds Left: {countMP3s}")
                countMP3s -= 1
                print(f"MP3 File: [{mp3_file}], Press a button to assign to the MP3 file")
                button_pressed = getButtonPress(lp)

                if 0 <= button_pressed < MAX_BUTTONS and button_pressed not in badNumbers:
                    config_data[button_pressed]["MP3File"] = mp3_file
                    print(f"Assigned {mp3_file} to Button# {button_pressed}.")
                    lp.LedCtrlRaw(button_pressed, 255, 0)
                    buttonsToColorSFX.append(int(button_pressed))
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

def play_sound(button, mp3_path, volume=0.25):  # Adjust volume as needed (between 0.0 and 1.0)
    global lp, page

    channel = pygame.mixer.Channel(button)
    sound = pygame.mixer.Sound(mp3_path)
    
    # Set the volume before playing the sound
    sound.set_volume(volume)

    channel.play(sound)

    while channel.get_busy():
        time.sleep(0.1)

    if page == "SFX":
        lp.LedCtrlRaw(button, 255, 0)

def set_system_volume(volume):
    system_platform = platform.system()

    if system_platform == "Windows":
        subprocess.run(["nircmd.exe", "setsysvolume", str(int(volume * 65535))])
    elif system_platform == "Linux":
        subprocess.run(["amixer", "set", "Master", f"{int(volume * 100)}%"])
    elif system_platform == "Darwin":
        subprocess.run(["osascript", "-e", f'set volume output volume {int(volume * 100)}'])

def SFXLoop():
    global page, lp, midi_output, buttonsToColorSFX

    print("Sound loop started")

    pygame.mixer.init()
    pygame.mixer.set_num_channels(MAX_BUTTONS)
    button_tracks = {}
    volume = 0.5
    lp.Reset()
    lp.LedCtrlRaw(207, 255, 255)
    lp.LedCtrlRaw(200, 255, 255)
    lp.LedCtrlRaw(201, 255, 255)

    lp.LedCtrlRaw(205, 255, 0)


    for i in buttonsToColorSFX:
        lp.LedCtrlRaw(i, 255, 0)


    while True:
        if not pygame.midi.get_init():
            pygame.midi.init()

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
                elif pressed_button == 206:
                    page = "SYNTH"
                    pygame.midi.quit()
                    return
                    
                elif 0 <= pressed_button < MAX_BUTTONS and config_data[pressed_button]["MP3File"]:
                    mp3_file = config_data[pressed_button]["MP3File"]
                    mp3_path = os.path.join(sounds_folder_path, mp3_file)

                    if os.path.exists(mp3_path):
                        lp.LedCtrlRaw(pressed_button, 0, 255)
                        track_thread = threading.Thread(target=play_sound, args=(pressed_button, mp3_path))
                        track_thread.start()
                        button_tracks[pressed_button] = track_thread

    pygame.midi.quit()





    
def SYNTHLoop():
    global page, lp, midi_output, selected
    selected = "synth.json"


    try:
        import launchpad_py as launchpad
    except ImportError:
        sys.exit("Error loading launchpad.py")

    pygame.init()

    BAD_NUMBERS = [8, 24, 40, 56, 72, 88, 104, 120]
    instrumentButtons = {8: "synth.json", 24: "piano.json", 40: "trumpet.json", 56: "bagpipe.json", 72:"Bass.json", 88:"SawtoothSynth.json", 104: "aahs.json", 120:"e-guitar.json", 204:"custom.json"}
    instrumentButtonsN = [8,24,40,56,72, 88, 104, 120, 204] #REMEMBER TO HAVE THIS THE SAME AS THE INSTRUMENTBUTTONS JUST NUMBERS
    

    GRAND_PIANO = 0
    CHURCH_ORGAN = 19
    instrument = CHURCH_ORGAN

    pygame.init()
    pygame.midi.init()
    port = pygame.midi.get_default_output_id()
    midi_output = pygame.midi.Output(port, 0)
    midi_output.set_instrument(instrument)

    active_notes = set()

    def play_orchestra_note(pressedButton, jsonFilePath):
        with open(jsonFilePath, 'r') as file:
            json_file = json.load(file)
            for i, entry in enumerate(json_file):
                if entry['Button'] == pressedButton:
                    index = i
        print(json_file[index]["Instrument"])
        instrument_dict = json_file[index]["Instrument"]
        instrument_NOTE = json_file[index]["Note"]
        for instrument, velocity in instrument_dict.items():
            midi_output.set_instrument(int(instrument))
            midi_output.note_on(instrument_NOTE, velocity)
            # active_notes.add(instrument_NOTE)
                
        
        



    def stop_orchestra_note(pressedButton, jsonFilePath):
        with open(jsonFilePath, 'r') as file:
            json_file = json.load(file)
            for i, entry in enumerate(json_file):
                if entry['Button'] == pressedButton:
                    index = i
        instrument_dict = json_file[index]["Instrument"]
        instrument_NOTE = json_file[index]["Note"]
        for instrument, velocity in instrument_dict.items():
            midi_output.set_instrument(int(instrument))
            midi_output.note_off(instrument_NOTE, velocity)  # Send note off message for each instrument
            # active_notes.remove(instrument_NOTE)






    def apply_distortion(velocity):
        # Apply distortion effect to the note
        # You can experiment with different techniques to achieve the desired distortion effect
        # For simplicity, let's just increase the velocity, which can create a harsher sound
        distorted_velocity = min(velocity + 150, 127)  # Increase velocity by 50, capped at 127
        return distorted_velocity

    def play_midi_note(note, velocity=127, needed_instrument=0):
        global selected
        if selected == "SawtoothSynth.json":
            # Apply distortion effect
            distorted_velocity = apply_distortion(velocity)
            
            midi_output.set_instrument(needed_instrument)
            midi_output.note_on(note, distorted_velocity)   
            active_notes.add(note)
        else:
            midi_output.set_instrument(needed_instrument)
            midi_output.note_on(note, velocity)
            active_notes.add(note)

    def stop_midi_note(note, velocity=127, needed_instrument=0):
        global selected
        midi_output.set_instrument(needed_instrument)
        midi_output.note_off(note, velocity)
        active_notes.remove(note)


    pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=2 ** 12)

    lp = launchpad.Launchpad()

    if lp.Open():
        print("Launchpad Mk1")
        lp.ButtonFlush()
        lp.Reset()

        print("Waiting for button inputs. Press Ctrl+C to exit.")

        lp.LedCtrlRaw(200, 255, 255)
        lp.LedCtrlRaw(201, 255, 255)
        lp.LedCtrlRaw(206, 255, 0)


        # Load the default instrument configuration
        with open("synth.json", "r") as json_file1:
            button_config1 = json.load(json_file1)
            selected = json_file1

        button_to_note = {config["Button"]: config["Note"] for config in button_config1}
        button_to_instrument = {config["Button"]: config["Instrument"] for config in button_config1}
        button_to_color = {config["Button"]: (config["Red"], config["Green"]) for config in button_config1}

        # Set colors on the Launchpad
        for button1, (red, green) in button_to_color.items():
            lp.LedCtrlRaw(button1, red, green)


        for i in instrumentButtonsN:
            lp.LedCtrlRaw(i, 255, 255)
        lp.LedCtrlRaw(8, 255, 0)

        while True:
            # Check for button events
            buttons1 = lp.ButtonStateRaw()
            if not pygame.midi.get_init():
                pygame.midi.init()

            if buttons1:
                pressed_button1 = buttons1[0]

                if pressed_button1 == 205 and buttons1[1]:
                    # Close midi_output before quitting pygame.midi
                    # pygame.midi.quit()
                    midi_output.close()
                    page = "SFX"
                    return


                # Switch instrument if instrument button is pressed
                if pressed_button1 in instrumentButtons and buttons1[1]:
                    with open(instrumentButtons[pressed_button1], "r") as json_file:
                        button_config1 = json.load(json_file)
                        selected = instrumentButtons[pressed_button1]
                        print(selected)
                    
                    button_to_color = {config["Button"]: (config["Red"], config["Green"]) for config in button_config1}
                    if not selected == "custom.json":
                        button_to_note = {config["Button"]: config["Note"] for config in button_config1}
                        button_to_instrument = {config["Button"]: config["Instrument"] for config in button_config1}

                        # Set colors on the Launchpad
                        for button1, (red, green) in button_to_color.items():
                            lp.LedCtrlRaw(button1, red, green)
                        
                        for i in instrumentButtonsN:
                            lp.LedCtrlRaw(i, 255, 255)
                        lp.LedCtrlRaw(pressed_button1, 255, 0)
                    else:
                        lp.LedCtrlRaw(204, 255, 0)
                        for i in instrumentButtonsN:
                            lp.LedCtrlRaw(i, 255, 255)
                    
                    

                if pressed_button1 == 200:
                    change_volume("up", step=0.1)
                    lp.LedCtrlRaw(200, 255, 255)
                elif pressed_button1 == 201:
                    change_volume("down", step=0.1)
                    lp.LedCtrlRaw(201, 255, 255)

                if pressed_button1 in range(120) and pressed_button1 not in BAD_NUMBERS:
                    if not selected == "custom.json":
                        print(f"Button pressed orchestra not selected, selected is '{selected}'")
                        if buttons1[1]:
                            note = button_to_note.get(pressed_button1, None)
                            instrument = button_to_instrument.get(pressed_button1, 0)
                            # Set button color to 0, 0 (black) when pressed
                            lp.LedCtrlRaw(pressed_button1, 0, 0)
                            play_midi_note(note, needed_instrument=instrument)
                        else:
                            released_note = button_to_note.get(pressed_button1, None)
                            instrument = button_to_instrument.get(pressed_button1, 0)
                            if released_note in active_notes:
                                # Set button color back to original color when released
                                lp.LedCtrlRaw(pressed_button1, *button_to_color[pressed_button1])
                                stop_midi_note(released_note, needed_instrument=instrument)
                    else:
                        if buttons1[1]:
                            play_orchestra_note(pressed_button1, selected)
                            # Set button color to 0, 0 (black) when pressed
                            lp.LedCtrlRaw(pressed_button1, 0, 0)


                        else:
                            stop_orchestra_note(pressed_button1, selected)
                            # Set button color back to original color when released
                            lp.LedCtrlRaw(pressed_button1, *button_to_color[pressed_button1])


            time.sleep(0.000001)

    else:
        print("Did not find any Launchpad Mk1.")

    lp.Close()


assignSounds()
print("\n\n")
print("Playing loop")
page = "SFX"
while True:
    if page == "SFX":
        SFXLoop()
    elif page == "SYNTH":
        SYNTHLoop()
