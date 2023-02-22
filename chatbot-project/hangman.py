import random
from PIL import Image
import sys
import os
from termcolor import colored
from wordsDatabase import someWords
# current_directory = os.getcwd()
# folder1 = 'data'
# os.chdir(os.path.join(current_directory, folder1))

from termcolor import colored


stage0 = colored("""
                +=======+
               ||      ||
               ||      ||
               ||      ||
                       ||
                       ||
                       ||
                       ||
                       ||
                       ||
                       ||
                       ||
                       ||
                       ||
                       ||
                       ||
                       ||
                       ||
                       ||
                       ||
                       ||
        ====================================
""", 'red', attrs=['dark', 'bold'])


stage1 = colored("""
                +=======+
               ||      ||
              //       ||
   =======   //        ||
 // @   @ \\\\//         ||
 ||  ____ ||/          ||
  \\\\_____///           ||
                       ||
                       ||
                       ||
                       ||
                       ||
                       ||
                       ||
                       ||
                       ||
                       ||
                       ||
                       ||
        ====================================
""", 'red', attrs=['dark', 'bold'])

stage2 = colored("""
                +=======+
               ||      ||
              //       ||
   =======   //        ||
 // @   @ \\\\//         ||
 ||  ____ ||/          ||
  \\\\  ¯  ///           ||
     |||//             ||
     |||               ||
     |||               ||
     |||               ||
     |||               ||
     |||               ||
     |||               ||
                       ||
                       || 
                       ||
                       ||
                       ||
        ====================================
""", 'red', attrs=['dark', 'bold'])


stage3 = colored("""
                +=======+
               ||      ||
              //       ||
   =======   //        ||
 // @   @ \\\\//         ||
 ||  ____ ||/          ||
  \\\\      //           ||
     |||//             ||
    /|||               ||
   //|||               ||
 //  |||               ||
||   |||               ||
     |||               ||
     |||               ||
                       ||
                       ||
                       ||
                       ||
                       ||
        ====================================
""", 'red', attrs=['dark', 'bold'])



stage4 = colored("""
                +=======+
               ||      ||
              //       ||
   =======   //        ||
 // @   @ \\\\//         ||
 ||  ___  ||/          ||
  \\\\      //           ||
     |||//             ||
    /|||\\              ||
   //|||\\\\             ||
 //  |||  \\\\           ||
||   |||   ||          ||
     |||               ||
     |||               ||
                       ||
                       ||
                       ||
                       ||
                       ||
        ====================================
""", 'red', attrs=['dark', 'bold'])


stage5 = colored("""
                +=======+
               ||      ||
              //       ||
   =======   //        ||
 // @   @ \\\\//         ||
 ||   ___ ||/          ||
  \\\\      //           ||
     |||//             ||
    /|||\\              ||
   //|||\\\\             ||
 //  |||  \\\\           ||
||   |||   ||          ||
     |||               ||
     |||               ||
    //                 ||
  //                   ||
//                     ||
                       ||
                       ||
        ====================================
""", 'red', attrs=['dark', 'bold'])


stage6 = colored("""
                +=======+
               ||      ||
              //       ||
   =======   //        ||
 // X   X \\\\//         ||
 ||  ____ ||/          ||
  \\\\/    \\//           ||
     |||//             ||
    /|||\\              ||
   //|||\\\\             ||
 //  |||  \\\\           ||
||   |||   ||          ||
     |||               ||
     |||               ||
    //\\\\               ||
  //    \\\\             ||
//        \\\\           ||
                       ||
                       ||
        ====================================
""", 'red', attrs=['dark', 'bold'])




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

    sportsWordsForHangGame = ['basketball', 'soccer', 'football', 'tennis', 'baseball',
    'hockey', 'golf', 'volleyball', 'cricket', 'boxing', 'swimming',
    'cycling', 'skiing', 'snowboarding', 'surfing', 'skateboarding',
    'gymnastics', 'wrestling', 'karate', 'taekwondo']

    foodWordsForHangGame = ['pizza', 'burger', 'spaghetti', 'sushi',
    'taco', 'fries', 'steak', 'lasagna', 'ramen', 'pancake', 'waffle',
    'sandwich', 'dumpling', 'noodle', 'croissant', 'bagel', 'muffin', 
    'cheese', 'bacon', 'sausage']

    carBrandWordsForHangGame = ['audi', 'bmw', 'mercedes', 'toyota', 
    'honda', 'nissan', 'kia', 'hyundai', 'tesla', 'volvo', 'jaguar',
    'porsche', 'mazda', 'subaru', 'lexus', 'ford', 'chevrolet', 'dodge',
    'jeep', 'cadillac']

    nameWordsForHangGame = ['alex', 'jessica', 'michael', 'samantha', 
    'daniel', 'emily', 'joshua', 'natalie', 'ryan', 'ashley', 'justin',
    'madison', 'william', 'olivia', 'christopher', 'lauren', 'kevin', 
    'abigail', 'matthew', 'amanda']

    movieCharacterWordsForHangGame = ['harrypotter', 'spiderman', 'ironman',
    'batman', 'superman', 'thor', 'captainamerica', 'wonderwoman', 'jamesbond', 
    'indianajones', 'lukeskywalker', 'hanniballecter', 'forrestgump', 'joker', 
    'gollum', 'gandalf', 'frodo', 'legolas', 'hagrid', 'dumbledore']

    harryPotterCharacterWordsForHangGame = ['harry', 'ron', 'hermione', 'ginny', 
    'dumbledore', 'snape', 'voldemort', 'malfoy', 'hagrid', 'mcgonagall', 'fred', 
    'george', 'neville', 'luna', 'sirius', 'bellatrix', 'dobby', 'remus', 'fenrir', 
    'cedric']

    lotrCharacterWordsForHangGame = ['frodo', 'sam', 'gandalf', 'aragorn', 'legolas', 
    'gimli', 'boromir', 'pippin', 'merry', 'bilbo', 'thorin', 'gollum', 'smaug', 'elrond', 
    'galadriel', 'faramir', 'denethor', 'eomer', 'eowyn', 'saruman']


    print("""
1. Technology
2. Home
3. Food
4. Sports
5. Movie Characters
6. Random

""")
    randomCategoryChosen = "False"
    chooseRandOrOption = input('Choose An Option [Number In List]: ').lower()

    wordsForHangGameAll = [techWordsForHangGame, houseWordsForHangGame, foodWordsForHangGame, sportsWordsForHangGame, movieCharacterWordsForHangGame]

    if chooseRandOrOption == '1' or 'tech' in chooseRandOrOption:
        categoryName = 'Technology'
        category = wordsForHangGameAll[0]
    elif chooseRandOrOption == '2' or 'home' in chooseRandOrOption:
        categoryName = 'Home'
        category = wordsForHangGameAll[1]
    elif chooseRandOrOption == '3' or 'food' in chooseRandOrOption:
        categoryName = 'Food'
        category = wordsForHangGameAll[2]
    elif chooseRandOrOption == '4' or 'sport' in chooseRandOrOption:
        categoryName = 'Sports'
        category = wordsForHangGameAll[3]
    elif chooseRandOrOption == '5' or 'characters' in chooseRandOrOption:
        categoryName = 'Movie Characters'
        category = wordsForHangGameAll[4]
    elif chooseRandOrOption == '6' or 'random' in chooseRandOrOption:
        category = random.choice(wordsForHangGameAll)
        randomCategoryChosen = "True"
        if category == wordsForHangGameAll[0]:
            categoryName = 'Technology'
        elif category == wordsForHangGameAll[1]:
            categoryName = 'Home'
        elif category == wordsForHangGameAll[2]:
            categoryName = 'Food'
        elif category == wordsForHangGameAll[3]:
            categoryName = 'Sports'
    else:
        category = random.choice(wordsForHangGameAll)
        randomCategoryChosen = "True"
        if category == wordsForHangGameAll[0]:
            categoryName = 'Technology'
        elif category == wordsForHangGameAll[1]:
            categoryName = 'Home'
        elif category == wordsForHangGameAll[2]:
            categoryName = 'Food'
        elif category == wordsForHangGameAll[3]:
            categoryName = 'Sports'
        elif category == wordsForHangGameAll[4]:
            categoryName = 'Movie Characters'


    print('\n')
    os.system('cls')
    if randomCategoryChosen == "True":
        print("Category Is " + colored('Random', 'yellow', attrs=['dark', 'bold']) + '\n' + "Begin Guessing Letters!")
    elif randomCategoryChosen == "False":
        print("Category Is " + colored(categoryName, 'yellow', attrs=['dark', 'bold']) + '\n' + "Begin Guessing Letters!")

    hangWord = random.choice(category)


    displayWord = "_" * len(hangWord)
    guessedLetters = []

    print(stage0)

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

                print(colored(("Guessed letters: " + guessedLetters_str), 'red', attrs=['dark', 'bold']) + '\n')
                return "Nice Job!"

        if livesUsed == 0:
            print(stage0)

        elif livesUsed == 1:
            print(stage1)

        elif livesUsed == 2:
            print(stage2)

        elif livesUsed == 3:
            print(stage3)

        elif livesUsed == 4:
            print(stage4)

        elif livesUsed == 5:
            print(stage5)

        elif guess == hangWord:
                print(colored('You Win!', 'green', attrs=['dark', 'bold']) + '\n' + f'The Word Was {hangWord}')
                print("\n")

                print(colored(("Guessed letters: " + guessedLetters_str), 'red', attrs=['dark', 'bold']) + '\n')
                return "Nice Job!"

        elif livesUsed == 6:
            print(stage6), print('\n')
            print(colored("You Lost!", 'red', attrs=['dark', 'bold']) + '\n')
            print(colored(("Guessed letters: " + guessedLetters_str), 'red', attrs=['dark', 'bold']) + '\n')
            return str("The Word Was " + colored(hangWord, 'yellow', attrs=['dark', 'bold']))


