import random
from PIL import Image
import sys
import os
current_directory = os.getcwd()
folder1 = 'data'
os.chdir(os.path.join(current_directory, folder1))
def hangManGame():
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

    chooseRandOrOption = input('Choose An Option [Number In List]: ')
    wordsForHangGameAll = [techWordsForHangGame, houseWordsForHangGame]
    if chooseRandOrOption == '1':
        categoryName = 'Technology'
        category = wordsForHangGameAll[0]
    elif chooseRandOrOption == '2':
        categoryName = 'Home'
        category = wordsForHangGameAll[1]
    else:
        category = random.choice(wordsForHangGameAll)
        if category == wordsForHangGameAll[0]:
            categoryName = 'Technology'
        else:
            categoryName = 'Home'



    print('\n')
    print("Category Is " + categoryName + '\n' + "Begin Guessing Letters!")

    hangWord = random.choice(category)
    print("THIS IS TEMPORARY BUT THE WORD IS: " + hangWord)

    head = '   O'
    rightArm = '  /'
    chest = '|'
    leftArm = '\\'
    rightLeg = '  /'
    leftLeg = ' \\'

def print_stickman():
    print('   O')
    print('  /|\\')
    print('  / \\')
    print(' /   \\')




    
    

hangManGame()
print_stickman()
