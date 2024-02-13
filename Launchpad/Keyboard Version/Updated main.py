import pygame
import sys
import pygame.midi
import json
from tkinter import messagebox, Tk

# Import the clipboard module
import pyperclip

pygame.init()
pygame.midi.init()
port = pygame.midi.get_default_output_id()
midi_output = pygame.midi.Output(port, 0)
midi_output.set_instrument(1)

# Define constants for the window dimensions
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 400

# Define colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Define keyboard layout as a list of rows
keyboard_layout = [
    ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'],
    ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],
    ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'],
    ['z', 'x', 'c', 'v', 'b', 'n', 'm']
]

keyboardToNote = [
    {'key': 'q', 'note#': 37, 'noteL': 'C'},  # Octave
    {'key': 'w', 'note#': 38, 'noteL': 'C#'},
    {'key': 'e', 'note#': 39, 'noteL': 'D'},
    {'key': 'r', 'note#': 40, 'noteL': 'D#'},
    {'key': 't', 'note#': 41, 'noteL': 'E'},
    {'key': 'y', 'note#': 42, 'noteL': 'F'},
    {'key': 'u', 'note#': 43, 'noteL': 'F#'},
    {'key': 'i', 'note#': 44, 'noteL': 'G'},
    {'key': 'o', 'note#': 45, 'noteL': 'G#'},
    {'key': 'p', 'note#': 46, 'noteL': 'A'},
    {'key': 'a', 'note#': 47, 'noteL': 'A#'},
    {'key': 's', 'note#': 48, 'noteL': 'B'},
    {'key': 'd', 'note#': 49, 'noteL': 'C'},  # New Octave
    {'key': 'f', 'note#': 50, 'noteL': 'C#'},
    {'key': 'g', 'note#': 51, 'noteL': 'D'},
    {'key': 'h', 'note#': 52, 'noteL': 'D#'},
    {'key': 'j', 'note#': 53, 'noteL': 'E'},
    {'key': 'k', 'note#': 54, 'noteL': 'F'},
    {'key': 'l', 'note#': 55, 'noteL': 'F#'},
    {'key': 'z', 'note#': 56, 'noteL': 'G'},
    {'key': 'x', 'note#': 57, 'noteL': 'G#'},
    {'key': 'c', 'note#': 58, 'noteL': 'A'},
    {'key': 'v', 'note#': 59, 'noteL': 'A#'},
    {'key': 'b', 'note#': 60, 'noteL': 'B'},
]

try:
    with open("instruments.json", 'r') as file:
        jsonFile = json.load(file)
    print(jsonFile)
    print("-------")
except FileNotFoundError:
    messagebox.showinfo("Missing File", "Make sure you have the instruments.json file in the same location as the exe! Also make sure its named 'instruments.json' EXACTLY!")
    exit()
except json.JSONDecodeError:
    messagebox.showinfo("Missing Instrument", "Please put a value for each number key. If you don't want a corresponding instrument, set the value to 0!")
    exit()
new_dict = {int(key): value for key, value in jsonFile.items()}

print(new_dict)

numberToInstrument = new_dict

def play_midi_note(note, velocity=127, needed_instrument=0):
    midi_output.set_instrument(needed_instrument)
    midi_output.note_on(note, velocity)
    active_notes.add(note)
    print(f"Playing MIDI note: {note}, Velocity: {velocity}, Instrument: {needed_instrument}")

def stop_midi_note(note, velocity=127, needed_instrument=0):
    midi_output.set_instrument(needed_instrument)
    midi_output.note_off(note, velocity)
    print(f"Stopping MIDI note: {note}, Velocity: {velocity}, Instrument: {needed_instrument}")

def stop_all_midi_notes():
    for i in range(0, 128):
        midi_output.note_off(i, velocity=127)

def copy_link_to_clipboard():
    # Define the link to be copied
    link = "https://docs.google.com/spreadsheets/d/1tCoK4zb98rY2qjzXvQwMqbRKKk75U-Ka_i3TH3o07lE/edit#gid=0"
    # Copy the link to the clipboard
    pyperclip.copy(link)
    # Show message box confirming that link is copied
    messagebox.showinfo("Link Copied", f"The link '{link}' has been copied to the clipboard!")

# Initialize Pygame
pygame.init()

# Set up the window
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("QWERTY Keyboard")

# Define dimensions for each key square
KEY_WIDTH = (WINDOW_WIDTH - 20) // len(keyboard_layout[0])  # Adjusted to allow space for octave buttons
KEY_HEIGHT = WINDOW_HEIGHT // len(keyboard_layout)

# Calculate starting positions for each row
start_x_list = [(WINDOW_WIDTH - len(row) * KEY_WIDTH) // 2 for row in keyboard_layout]
start_y = (WINDOW_HEIGHT - len(keyboard_layout) * KEY_HEIGHT) // 2

# Main loop
selected_number = '1'  # Default selected number
pressed_keys = set()    # Currently pressed keys
active_notes = set()    # Currently active notes
octave_shift = 0        # Current octave shift

running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:  # Exit if ESC is pressed
                running = False
            elif event.key == pygame.K_UP:  # Increase note numbers by 12
                octave_shift += 12
                for item in keyboardToNote:
                    item['note#'] = min(127, item['note#'] + 12)
            elif event.key == pygame.K_DOWN:  # Decrease note numbers by 12
                octave_shift -= 12
                for item in keyboardToNote:
                    item['note#'] = max(0, item['note#'] - 12)
            elif event.unicode.isdigit() and event.unicode in '1234567890':
                num = int(event.unicode)
                if num == 1:
                    selected_number = str(num)
                elif num in numberToInstrument:
                    selected_number = str(num)
                    needed_instrument = numberToInstrument[num]
                    try:
                        for note in active_notes:
                            stop_midi_note(note, needed_instrument=needed_instrument)
                    except:
                        print("Error: Please stop playing the note before changing instruments!")
                        exit()
                    active_notes.clear()
                else:
                    selected_number = None
            else:
                for item in keyboardToNote:
                    if event.unicode == item['key']:
                        note = item['note#'] + octave_shift
                        needed_instrument = numberToInstrument.get(int(selected_number), 0)
                        if 0 <= note <= 127:
                            play_midi_note(note, needed_instrument=needed_instrument)
                            active_notes.add(note)
                        break
                pressed_keys.add(event.unicode)
        elif event.type == pygame.KEYUP:
            for item in keyboardToNote:
                if event.unicode == item['key']:
                    note = item['note#'] + octave_shift
                    needed_instrument = numberToInstrument.get(int(selected_number), 0)
                    if 0 <= note <= 127:
                        stop_midi_note(note, velocity=127, needed_instrument=needed_instrument)
                        active_notes.discard(note)
                    break
            pressed_keys.discard(event.unicode)

    # Draw the keyboard
    window.fill(WHITE)
    for row_index, row in enumerate(keyboard_layout):
        start_x = start_x_list[row_index]
        for col_index, char in enumerate(row):
            key_rect = pygame.Rect(start_x + col_index * KEY_WIDTH, start_y + row_index * KEY_HEIGHT, KEY_WIDTH,
                                    KEY_HEIGHT)
            if char.isdigit():
                color = GREEN if char == selected_number else WHITE
            elif char in pressed_keys:
                color = GREEN
            else:
                color = RED if (keyboardToNote[col_index]['note#'] + octave_shift) not in range(0, 128) else WHITE
            pygame.draw.rect(window, color, key_rect)
            pygame.draw.rect(window, (0, 0, 0), key_rect, 1)  # Draw a border around the square
            font = pygame.font.SysFont(None, 36)
            if char.isdigit():
                text = font.render(char, True, (0, 0, 0))
            else:
                note_letter = None
                for item in keyboardToNote:
                    if char == item['key']:
                        note_letter = item['noteL']
                        break
                if note_letter:
                    text = font.render(note_letter, True, (0, 0, 0))
                else:
                    text = font.render("", True, (0, 0, 0))
            text_rect = text.get_rect(center=key_rect.center)
            window.blit(text, text_rect)
    
    # Draw a button
    button_rect = pygame.Rect(685, 335, 100, 40)
    pygame.draw.rect(window, (0, 0, 255), button_rect)
    font = pygame.font.SysFont(None, 24)
    text = font.render("Copy Link", True, (255, 255, 255))
    text_rect = text.get_rect(center=button_rect.center)
    window.blit(text, text_rect)

    # Update the display
    pygame.display.flip()

    # Check for button click event
    mouse_pos = pygame.mouse.get_pos()
    if button_rect.collidepoint(mouse_pos):
        if pygame.mouse.get_pressed()[0]:  # Left mouse button clicked
            copy_link_to_clipboard()

# Quit Pygame
pygame.quit()
sys.exit()
