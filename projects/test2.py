import random
import os
import time
from termcolor import colored, cprint


gameTrue = True
userInput = None

while True:
    os.system('cls')
    answer = random.randint(1,100)
    gameTrue = True
    previousClue = None
    previousGuess = None
    maxTries = input("Difficulty? 0-10 (10=Hard): \n")
    if not maxTries.isdigit():
        print("Enter A Number!")
        gameTrue = False
    else:
        maxTries = 15-int(maxTries)
    tries = 0
    while gameTrue:
        if tries >= maxTries:
            playAgain = input(f"You {colored('lost', 'red', attrs=['dark', 'bold'])}! The Number Was {answer}! Would you like to play again? (y/n) \n")
            if 'y' in playAgain:
                gameTrue = False
                break
            elif 'n' in playAgain:
                print("Bye!")
                exit()
        tries += 1
        os.system('cls')
        if previousGuess is not None:
            userInput = input(f"(Previous Guess: {previousGuess}, {previousClue} ) \n Try #{tries}/{maxTries}, Enter a number 1-100: \n")
        else:
            userInput = input(f"Try #{tries}/{maxTries}, Enter a number 1-100: \n")
        if userInput.isdigit():
            userInput = int(userInput)
        else:
            cprint("Must enter an interger! Picking new number! ", 'red', attrs=['dark', 'bold'])
            time.sleep(3)
            gameTrue = False
            break
        if userInput > 0 and userInput < 101:
            if userInput > answer:
                print(f"The Number is {colored('Lower', 'blue')}!")
                previousClue = colored('Lower', 'blue')
            elif userInput < answer:
                print(f"The Number is {colored('Higher', 'yellow')}!")
                previousClue = colored('Higher', 'yellow')
            elif userInput == answer:
                playAgain = input(f"{colored('You Win!', 'green', attrs=['dark', 'bold'])} Would you like to play again? (y/n) \n")
                if 'y' in playAgain:
                    gameTrue = False
                elif 'n' in playAgain:
                    print("Bye!")
                    exit()
        else:
            cprint("Must enter a number between 1 and 100! Picking new number!", 'red', attrs=['dark', 'bold'])
            time.sleep(3)
            gameTrue = False
        previousGuess = str(userInput)
        time.sleep(2)

            
