import os
import re
from itertools import product

os.system('cls')

regexColors = re.compile("(R|Y|G|C|W|B) (R|Y|G|C|W|B) (R|Y|G|C|W|B) (R|Y|G|C|W|B)", re.IGNORECASE)
colors = ['R', 'Y', 'G', 'C', 'W', 'B']
guesses = []
master = True

def printCombinations(combinations):
    for comb in combinations:
        string = ""
        for i in comb:
            match i:
                case 'R':
                    string += "🔴"
                case 'Y':
                    string += "🟡"
                case "G":
                    string += "🟢"
                case "C":
                    string += "🔵"
                case "W":
                    string += "⚪"
                case "B":
                    string += "⚫"
        # print(string)

def generate_combinations(colors, length=4):
    return list(product(colors, repeat=length))

def get_feedback(guess, code):
    black_pegs = sum(g == c for g, c in zip(guess, code))
    white_pegs = sum(min(guess.count(color), code.count(color)) for color in set(colors)) - black_pegs
    return black_pegs, white_pegs

def filter_combinations(possible_combinations, guess, feedback):
    return [comb for comb in possible_combinations if get_feedback(guess, comb) == feedback]

def rate_next_guesses(current_combinations):
    next_guess_ratings = []
    
    for next_guess in current_combinations:
        feedback_counts = {}
        
        for possible_code in current_combinations:
            feedback = get_feedback(next_guess, possible_code)
            if feedback not in feedback_counts:
                feedback_counts[feedback] = 0
            feedback_counts[feedback] += 1
        
        max_remaining_possibilities = max(feedback_counts.values())
        next_guess_ratings.append((next_guess, max_remaining_possibilities))
    
    next_guess_ratings.sort(key=lambda x: x[1], reverse=True)
    return next_guess_ratings

all_combinations = generate_combinations(colors)

print("Guesses should be formatted with spaces (Red Yellow Green Cyan White Black)")
while master:
    while True:
        g = input("Enter a guess: ")
        pattern = re.search(regexColors, g)
        try:
            if pattern.group(1) and pattern.group(2) and pattern.group(3) and pattern.group(4):
                break
        except:
            os.system('cls')
            print("Must match Valid 4-Pin Format. R Y G C")
            print("Guesses should be formatted with spaces (Red Yellow Green Cyan White Black)")

    while True:
        w = input("Enter the white pins returned: ")
        b = input("Enter the black pins returned: ")
        try:
            w = int(w)
            b = int(b)
        except:
            os.system('cls')
            print("Must enter numbers!")
        else:
            if 0 <= w <= 4 and 0 <= b <= 4 and b + w <= 4:
                break
            else:
                os.system('cls')
                print("Pins must add up between 0 and 4!")

    guess = (pattern.group(1).upper(), pattern.group(2).upper(), pattern.group(3).upper(), pattern.group(4).upper())
    guesses.append({
        "guess": guess,
        "result": {
            "black": b,
            "white": w
        }
    })

    # Filter possible combinations based on all guesses so far
    possible_combinations = all_combinations
    for past_guess in guesses:
        possible_combinations = filter_combinations(possible_combinations, past_guess["guess"], (past_guess["result"]["black"], past_guess["result"]["white"]))

    printCombinations(possible_combinations)

    # Rate the next possible guesses
    next_guess_ratings = rate_next_guesses(possible_combinations)
    print("\nNext guesses ranked (worst to best):")
    for rank, (next_guess, remaining_possibilities) in enumerate(next_guess_ratings, start=1):
        guess_string = ""
        for color in next_guess:
            match color:
                case 'R':
                    guess_string += "🔴"
                case 'Y':
                    guess_string += "🟡"
                case "G":
                    guess_string += "🟢"
                case "C":
                    guess_string += "🔵"
                case "W":
                    guess_string += "⚪"
                case "B":
                    guess_string += "⚫"
        
        print(f"{len(possible_combinations) - rank + 1}: {guess_string} (Eliminates possibilities to: {remaining_possibilities})")
    total_possible_combinations = len(possible_combinations)
    print(f"Total possible combinations left: {total_possible_combinations}")
