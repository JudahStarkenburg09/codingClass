import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

# Function to check if the guess is correct
def check_guess(guess):
    if guess == secret_number:
        return "Correct! You guessed the number."
    elif guess < secret_number:
        return "Try higher."
    else:
        return "Try lower."

