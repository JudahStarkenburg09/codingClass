import random
from PIL import Image
import sys
import os
from termcolor import colored
current_directory = os.getcwd()
folder1 = 'data'
os.chdir(os.path.join(current_directory, folder1))
def hangManGame():

    livesUsed = 0

    techWordsForHangGame = ["monitor", "laptop", "keyboard", "router", 
    "mouse", "printer", "camera", "memory", "software", "hardware", 
    "scanner", "microphone", "speaker", "headphone", "firewall", "encryption", 
    "data", "backup", "storage", "database", "programming", "internet", "server", 
    "cloud", "digital", "cyber", "algorithm", "virtual", "artificial", "security"]

    houseWordsForHangGame = ["door", "window", "roof", "chimney", "garage", "attic",
    "basement", "fireplace", "staircase", "hallway", "ceiling", "flooring", "furniture",
    "painting", "cabinet", "curtain", "shutter", "blinds", "carpet", "lamp", "bedroom",
    "kitchen", "bathroom", "livingroom", "diningroom", "laundryroom", "backyard",
    "frontporch", "fence", "mailbox"]

    print("""
1. Technology
2. Home
3. Random

""")
    randomCategoryChosen = "False"
    chooseRandOrOption = input('Choose An Option [Number In List]: ')
    wordsForHangGameAll = [techWordsForHangGame, houseWordsForHangGame]
    if chooseRandOrOption == '1':
        categoryName = 'Technology'
        category = wordsForHangGameAll[0]
    elif chooseRandOrOption == '2':
        categoryName = 'Home'
        category = wordsForHangGameAll[1]
    elif chooseRandOrOption == '3':
        category = random.choice(wordsForHangGameAll)
        if category == wordsForHangGameAll[0]:
            randomCategoryChosen = "True"
            categoryName = 'Technology'
        else:
            categoryName = 'Home'



    print('\n')
    os.system('cls')
    if randomCategoryChosen == "True":
        print("Category Is " + colored('Random', 'yellow', attrs=['dark', 'bold']) + '\n' + "Begin Guessing Letters!")
    elif randomCategoryChosen == "False":
        print("Category Is " + colored(categoryName, 'yellow', attrs=['dark', 'bold']) + '\n' + "Begin Guessing Letters!")

    hangWord = random.choice(category)

    head = colored('   O', 'red', attrs=['dark', 'bold'])
    rightArm = colored('  /', 'red', attrs=['dark', 'bold'])
    chest = colored('|', 'red', attrs=['dark', 'bold'])
    leftArm = colored('\\', 'red', attrs=['dark', 'bold'])
    rightLeg = colored('  /', 'red', attrs=['dark', 'bold'])
    leftLeg = colored(' \\', 'red', attrs=['dark', 'bold'])

    displayWord = "_" * len(hangWord)
    guessedLetters = []

    while True:
        print('\n' + '\n')
        print(displayWord)
        guess = input('Enter Letter: ')
        guessedLetters.append(guess)
        os.system('cls')
        guessedLetters_str = ", ".join(guessedLetters)
        print("Letters guessed: " + guessedLetters_str)
        print('\n')
        if guess not in hangWord:
            livesUsed += 1

        if guess in hangWord:
            # Update displayWord with the new guess
            for i in range(len(hangWord)):
                if hangWord[i] == guess:
                    displayWord = displayWord[:i] + guess + displayWord[i+1:]

            # Check if the entire word has been guessed
            if displayWord == hangWord:
                hangWord = colored(hangWord, 'yellow', attrs=['dark', 'bold'])
                print(colored('You Win!', 'green', attrs=['dark', 'bold']) + '\n' + f'The Word Was {hangWord}')
                print("\n")
                break

        if livesUsed == 0:
            print('\n' + '\n' + '\n' + '\n')

        elif livesUsed == 1:
            print(head + '\n' + '\n' + '\n')

        elif livesUsed == 2:
            print(head + '\n' + rightArm + '\n' + '\n')

        elif livesUsed == 3:
            print(head + '\n' + rightArm + chest + '\n' + '\n')

        elif livesUsed == 4:
            print(head + '\n' + rightArm + chest + leftArm + '\n' + '\n')

        elif livesUsed == 5:
            print(head + '\n' + rightArm + chest + leftArm + '\n' + rightLeg + '\n')

        elif livesUsed == 6:
            print(head + '\n' + rightArm + chest + leftArm + '\n' + rightLeg + leftLeg + '\n')
            print(colored("You Lost!", 'red', attrs=['dark', 'bold']) + '\n')
            break

            

    
    







    
    

hangManGame()

