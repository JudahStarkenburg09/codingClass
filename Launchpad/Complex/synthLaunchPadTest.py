import pygame
import json
import sys
from pygame import time
import pygame.midi

try:
    import launchpad_py as launchpad
except ImportError:
    sys.exit("Error loading launchpad.py")

pygame.init()

GRAND_PIANO = 0
CHURCH_ORGAN = 19
instrument = CHURCH_ORGAN
pygame.init()
pygame.midi.init()
port = pygame.midi.get_default_output_id()
midi_output = pygame.midi.Output(port, 0)
midi_output.set_instrument(instrument)

# Play a MIDI note
def play_midi_note(note, velocity=127):
    midi_output.note_on(note, velocity)

# Stop playing a MIDI note
def stop_midi_note(note, velocity=127):
    midi_output.note_off(note, velocity)

# Set up the Pygame mixer
pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=2**12)

# Create an instance for Launchpad Mk1
lp = launchpad.Launchpad()

# Open the Launchpad
if lp.Open():
    print("Launchpad Mk1")

    # Clear the buffer
    lp.ButtonFlush()

    print("Waiting for button inputs. Press Ctrl+C to exit.")

    # Load button configuration from the JSON file
    with open("synth.json", "r") as json_file:
        button_config = json.load(json_file)

    # Map button configurations to notes and colors
    button_to_note = {config["Button"]: config["Note"] for config in button_config}
    button_to_color = {config["Button"]: (config["Red"], config["Green"]) for config in button_config}

    # Set colors on the Launchpad
    for button, (red, green) in button_to_color.items():
        lp.LedCtrlRaw(button, red, green)

    while True:
        # Check for button events
        buttons = lp.ButtonStateRaw()

        if buttons: # Add function to see if pressed bad button
            if buttons[1]:
                note = button_to_note.get(buttons[0], None)
                print(f"Played note {note}")
                play_midi_note(note)
            else:
                for note in button_to_note.values():
                    print(f"Stoped note {note}")
                    stop_midi_note(note)

        # Wait for a short duration to avoid high CPU usage
        time.wait(5)

else:
    print("Did not find any Launchpad Mk1.")

# Cleanup
lp.Close()
