import sys
import os
import re
from itertools import product
from termcolor import cprint, colored
import time

def run_mastermind():
    os.system('python Mastermindbot.py')
    

def color_to_emoji(color):
    emoji_map = {
        'R': "🔴",
        'Y': "🟡",
        'G': "🟢",
        'C': "🔵",
        'W': "⚪",
        'B': "⚫"
    }
    return emoji_map.get(color, color)

os.system('cls')

regexColors = re.compile("(R|Y|G|C|W|B)(?: )*(R|Y|G|C|W|B)(?: )*(R|Y|G|C|W|B)(?: )*(R|Y|G|C|W|B)", re.IGNORECASE)
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
    # print("Here1")
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

ctext = f"{colored('Guesses should be four letters representing the colors ', 'white', attrs=['bold'])} ({colored('R', 'red')} {colored('Y', 'yellow')} {colored('G', 'green')} {colored('C', 'blue')} {colored('W', 'white')} {colored('B', 'dark_grey')})"
import random

next_best = random.choice([
    ['Y', 'G', 'C', 'R'],  # Covering four different colors
    ['W', 'B', 'Y', 'G'],  # Covering another set of four different colors
    ['C', 'R', 'B', 'W'],  # Another combination covering different colors
    ['Y', 'Y', 'G', 'G'],  # Two of each for a balanced approach
    ['C', 'C', 'R', 'R'],  # Another balanced approach with different colors
    ['B', 'B', 'W', 'W'],  # Covering the last two colors in pairs
    ['G', 'R', 'Y', 'B']   # Another diverse combination
])

print(ctext)
while master:
    while True:
        g = input(f"{colored('Enter A Guess, or press enter to autofill next best guess: ', 'white', attrs=['bold'])}")
        if g == "":
            g = ' '.join(map(str,next_best))
        pattern = re.search(regexColors, g)
        try:
            if pattern.group(1) and pattern.group(2) and pattern.group(3) and pattern.group(4):
                temp = [pattern.group(1).upper(), pattern.group(2).upper(), pattern.group(3).upper(), pattern.group(4).upper()]
                print("-----------------------------------")
                print(f"You Guessed: {' '.join(color_to_emoji(i) for i in temp)}")
                break
        except:
            os.system('cls')
            print(f"{colored('Must match Valid 4-Pin Format. R Y G C', 'red', attrs=['dark', 'bold'])}")
            print(ctext)
            


    while True:
        print("-----------------------------------")
        b = input(f"Enter the {colored('black', 'grey', attrs=['bold'])} pins returned: ")
        w = input(f"Enter the {colored('white', 'white', attrs=['bold'])} pins returned: ")
        try:
            w = int(w)
            b = int(b)
        except:
            os.system('cls')
            cprint("Must enter numbers!", "red", attrs=['dark', 'bold'])
        else:
            if 0 <= w <= 4 and 0 <= b <= 4 and b + w <= 4:
                break
            else:
                os.system('cls')
                cprint("Pins must add up between 0 and 4!", "red", attrs=['dark', 'bold'])

    guess = (pattern.group(1).upper(), pattern.group(2).upper(), pattern.group(3).upper(), pattern.group(4).upper())
    guesses.append({
        "guess": guess,
        "result": {
            "black": b,
            "white": w
        }
    })


    cprint("___________________________________", 'white')
    print(' ' * 35)
    cprint("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾", 'white')
    sys.stdout.write('\033[F\033[F')
    sys.stdout.flush()
    for i in range(36):
        tstring = '█' * i + ' ' * (35 - i)
        sys.stdout.write('\r' + colored(tstring, 'red'))
        sys.stdout.flush()
        time.sleep(random.uniform(0.25, 0.01))
    sys.stdout.write('\n')
    sys.stdout.flush()
    cprint("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾", 'white')

    # Filter possible combinations based on all guesses so far
    possible_combinations = all_combinations
    for past_guess in guesses:
        possible_combinations = filter_combinations(possible_combinations, past_guess["guess"], (past_guess["result"]["black"], past_guess["result"]["white"]))
    # print("Here2")
    printCombinations(possible_combinations)

    # Rate the next possible guesses
    next_guess_ratings = rate_next_guesses(possible_combinations)
    cprint("\nNext guesses ranked (worst to best):", 'magenta', attrs=['dark', 'bold'])
    for rank, (next_guess, remaining_possibilities) in enumerate(next_guess_ratings, start=1):
        guess_string = ""
        for color in next_guess:
            match color:
                case 'R':
                    guess_string += "🔴 "
                case 'Y':
                    guess_string += "🟡 "
                case "G":
                    guess_string += "🟢 "
                case "C":
                    guess_string += "🔵 "
                case "W":
                    guess_string += "⚪ "
                case "B":
                    guess_string += "⚫ "

        rankNumber = colored(f"{len(possible_combinations) - rank + 1}:{'' if (len(possible_combinations) - rank + 1) >= 100 else (' ' if (len(possible_combinations) - rank + 1) >= 10 else '  ')}", 'white', attrs=['bold'])

        correctOR = (
    colored("Eliminates possibilities left to", 'magenta', attrs=['bold'])
    if len(possible_combinations) != 1
    else f"{colored('Correct Answer!', 'green', attrs=['bold'])}"
)
        
        
        
        formatted_string =   f"{rankNumber} {guess_string} ({correctOR}{f' {remaining_possibilities}' if len(possible_combinations) != 1 else ''})"
        
        
        
        
        # formatted_string = f"{colored(f'{len(possible_combinations) - rank + 1}', 'white', attrs=['bold'])}: {guess_string} ({colored(f'{'Eliminates possibilities left to' if possible_combinations != 1 else f'{colored('Correct Answer!', 'green', 'on_blue', attrs=['bold'])}'}', 'magenta', attrs=['bold'])} {remaining_possibilities if possible_combinations != 1 else ''})"
        print(formatted_string)
        

    total_possible_combinations = len(possible_combinations)
    # print("Here3")
    t1 = colored("Total possible combinations left: ", 'red', attrs=['bold'])
    t2 = colored(f'{total_possible_combinations}', 'yellow', attrs=['bold'])
    print(t1 + t2)
    # print("Here4")
    previous_guess_emojis = ' '.join(color_to_emoji(color) for color in guess)
    # print("Here5")
    next_best = []
    try:
        for i in next_guess_ratings[-1][0]:
            next_best.append(i)
    except:
        cprint("Impossible Combinations! Ending Program!", 'yellow', 'on_red', attrs=['bold'])
        end = input(f"{colored('Press enter to start again, type exit to end program', 'green', attrs=['bold'])}\n{colored('Note: Running multiple times in a row may result in high memory usage!', 'red')}\n")
        if 'exit' in end.lower():
            os.system('cls')
            exit()
        else:
            run_mastermind()
            os.system('cls')
    
    # print(next_best)
    # print("Here6")
    next_best_guess_emojis = ' '.join(color_to_emoji(color) for color in next_guess_ratings[-1][0])
    # print("Here7")
    print( "----------------------------")
    print(f"Previous Guess  {previous_guess_emojis}")
    print( "----------------------------")
    print(f"Next best Guess {next_best_guess_emojis}")
    print( "----------------------------")

    print('\n')



