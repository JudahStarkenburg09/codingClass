import tkinter as tk
from tkinter import messagebox
import random

# List of words for the game
word_list = [
    "apple", "banana", "carrot", "dog", "elephant", "frog", "giraffe", "horse",
    "island", "jungle", "kangaroo", "lion", "monkey", "noodle", "ocean", "penguin",
    "queen", "rabbit", "sun", "tiger", "umbrella", "violet", "whale", "xylophone",
    "yogurt", "zebra", "acorn", "bird", "cat", "dolphin", "elephant", "flamingo",
    "giraffe", "hippo", "iguana", "jaguar", "koala", "lemur", "monkey", "narwhal",
    "octopus", "penguin", "quokka", "rhino", "sloth", "toucan", "unicorn", "vulture",
    "whale", "xray", "yak", "zebra", "almond", "butterfly", "cherry", "daisy",
    "elephant", "feather", "grape", "honey", "ice cream", "jellyfish", "kiwi", "lemon",
    "mango", "nightingale", "oak", "peacock", "quartz", "rose", "sunflower", "tulip",
    "umbrella", "violet", "watermelon", "xylophone", "yacht", "zeppelin", "alligator",
    "butterfly", "cactus", "dragonfly", "elephant", "flamingo", "giraffe", "hippo",
    "iguana", "jaguar", "kangaroo", "lemur", "mongoose", "narwhal", "octopus", "peacock",
    "quokka", "rhino", "sloth", "toucan", "unicorn", "vulture", "whale", "xray", "yak",
    "zebra", "antelope", "buffalo", "camel", "deer", "elephant", "fox", "gazelle",
    "hippo", "ibis", "jaguar", "koala", "lion", "mongoose", "narwhal", "otter",
    "penguin", "quokka", "rhino", "squirrel", "toucan", "unicorn", "vampire", "whale",
    "xenon", "yak", "zebra", "alpaca", "buffalo", "cheetah", "dolphin", "elephant",
    "flamingo", "giraffe", "hippo", "iguana", "jaguar", "koala", "lemur", "mongoose",
    "narwhal", "octopus", "peacock", "quokka", "rhino", "sloth", "toucan", "unicorn",
    "vulture", "whale", "xray", "yak", "zebra", "almond", "beetle", "caterpillar",
    "dolphin", "elephant", "firefly", "giraffe", "honeybee", "iguana", "jaguar", "kiwi",
    "lemur", "mantis", "narwhal", "ostrich", "peacock", "quokka", "rhino", "sloth",
    "toucan", "unicorn", "vulture", "whale", "xray", "yak", "zebra"
]

# Function to start a new game
def new_game():
    global word_to_guess, revealed_letters, remaining_lives

    # Choose a random word from the list
    word_to_guess = random.choice(word_list)

    # Initialize the revealed letters and remaining lives
    revealed_letters = ["_" for _ in word_to_guess]
    remaining_lives = 7

    # Update the GUI
    word_label.config(text=" ".join(revealed_letters))
    lives_label.config(text=f"Lives: {remaining_lives}")
    letters_frame.pack()  # Use pack() instead of grid()

# Function to handle letter button clicks
def guess_letter(letter):
    global remaining_lives

    # Check if the guessed letter is in the word
    if letter in word_to_guess:
        for i in range(len(word_to_guess)):
            if word_to_guess[i] == letter:
                revealed_letters[i] = letter
        word_label.config(text=" ".join(revealed_letters))

        # Check if the word has been completely guessed
        if "_" not in revealed_letters:
            messagebox.showinfo("Congratulations", "You guessed the word correctly!")
            letters_frame.pack_forget()
    else:
        remaining_lives -= 1
        lives_label.config(text=f"Lives: {remaining_lives}")

        # Check if the player has run out of lives
        if remaining_lives == 0:
            messagebox.showinfo("Game Over", f"The word was '{word_to_guess}'. Better luck next time!")
            letters_frame.pack_forget()

# Function to handle key presses
def key_press(event):
    key = event.char.lower()
    if key in letters:
        guess_letter(key)

# Create the main window
root = tk.Tk()
root.title("Word Guessing Game")

# Create a frame for the letters
letters_frame = tk.Frame(root)

# Create buttons for each letter
letters = "abcdefghijklmnopqrstuvwxyz"
for letter in letters:
    btn = tk.Button(letters_frame, text=letter, command=lambda l=letter: guess_letter(l))
    btn.pack(side=tk.LEFT)
    root.bind(letter, key_press)  # Bind letter keys to key_press function

# Create labels for the word and remaining lives
word_label = tk.Label(root, text="", font=("Arial", 18))
word_label.pack(pady=10)
lives_label = tk.Label(root, text="", font=("Arial", 14))
lives_label.pack(pady=5)

# Start a new game
new_game()

# Run the main window
root.mainloop()
