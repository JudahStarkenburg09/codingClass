import pygame
import json
import sys
import pygame.midi
import time
from pydub import AudioSegment
from pydub.generators import Sine
from pydub import AudioSegment

# Set the path to the FFmpeg executable
AudioSegment.converter = "ffmpeg.exe"


try:
    import launchpad_py as launchpad
except ImportError:
    sys.exit("Error loading launchpad.py")

pygame.init()

BAD_NUMBERS = [8, 24, 40, 56, 72, 88, 104]

# Constants
GRAND_PIANO = 0
CHURCH_ORGAN = 19
instrument = CHURCH_ORGAN

# Initialize Pygame MIDI
pygame.init()
pygame.midi.init()
port = pygame.midi.get_default_output_id()
midi_output = pygame.midi.Output(port, 0)
midi_output.set_instrument(instrument)

# Keep track of notes being played
active_notes = set()

# Play a MIDI note
def play_midi_note(note, velocity=127, needed_instrument=0):
    midi_output.set_instrument(needed_instrument)
    midi_output.note_on(note, velocity)
    active_notes.add(note)

# Stop playing a MIDI note
def stop_midi_note(note, velocity=127, needed_instrument=0):
    midi_output.set_instrument(needed_instrument)
    midi_output.note_off(note, velocity)
    active_notes.remove(note)

# Apply reverb to an AudioSegment
def apply_reverb(audio_segment):
    # Adjust the frequency, duration, and fade-out parameters
    reverb = Sine(100).to_audio_segment(duration=1000).fade_out(1000)
    
    # Apply reverb to the entire audio segment
    return audio_segment.overlay(reverb, loop=True) 

# Set up the Pygame mixer
pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=2**12)

# Create an instance for Launchpad Mk1
lp = launchpad.Launchpad()

# Open the Launchpad
if lp.Open():
    print("Launchpad Mk1")

    # Clear the buffer
    lp.ButtonFlush()
    lp.Reset()

    print("Waiting for button inputs. Press Ctrl+C to exit.")

    # Load button configuration from the JSON file
    with open("synth.json", "r") as json_file1:
        button_config1 = json.load(json_file1)

    # Map button configurations to notes, instruments, and colors
    button_to_note = {config["Button"]: config["Note"] for config in button_config1}
    button_to_instrument = {config["Button"]: config["Instrument"] for config in button_config1}
    button_to_color = {config["Button"]: (config["Red"], config["Green"]) for config in button_config1}

    # Set colors on the Launchpad
    for button1, (red, green) in button_to_color.items():
        lp.LedCtrlRaw(button1, red, green)

    reverb_active = False

    while True:
        # Check for button events
        buttons1 = lp.ButtonStateRaw()

        if buttons1:
            pressed_button1 = buttons1[0]

            if pressed_button1 in range(121) and pressed_button1 not in BAD_NUMBERS:
                if pressed_button1 == 120:  # Reverb toggle button
                    if buttons1[1]:  # Button pressed
                        reverb_active = not reverb_active
                        lp.LedCtrlRaw(pressed_button1, 255 * reverb_active, 255 * reverb_active)  # Toggle color
                else:
                    if buttons1[1]:  # Button pressed
                        note = button_to_note.get(pressed_button1, None)
                        instrument = button_to_instrument.get(pressed_button1, 0)
                        print(f"Played note {note} with instrument {instrument}")
                        lp.LedCtrlRaw(pressed_button1, 0, 0)  # Set color to 0, 0
                        play_midi_note(note, needed_instrument=instrument)
                    else:  # Button released
                        released_note = button_to_note.get(pressed_button1, None)
                        instrument = button_to_instrument.get(pressed_button1, 0)
                        if released_note in active_notes:
                            print(f"Stopped note {released_note} with instrument {instrument}")
                            stop_midi_note(released_note, needed_instrument=instrument)
                            lp.LedCtrlRaw(pressed_button1, *button_to_color[pressed_button1])  # Set color back to original

        # Wait 1 microsecond to avoid high CPU usage
        time.sleep(0.000001)

else:
    print("Did not find any Launchpad Mk1.")

# Cleanup
lp.Close()
