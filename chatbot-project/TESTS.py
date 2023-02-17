import random
import time
import os
from termcolor import colored
# def randName():
text_linus = colored('<Linus> ', 'green', attrs=['dark','bold'])
nameList = []
nameNumber = 0
def pickName(fromNames):
    pickingProgress = 0
    picking = True
    pickedName = random.choice(fromNames)
    while picking:
        os.system('cls')
        print(random.choice(fromNames))
        pickingProgress += 1
        if pickingProgress >= 30:
            os.system('cls')
            picking = False
            print(pickedName)
            time.sleep(1)
            return ("The Winner Is: " + pickedName + "!")
        time.sleep(0.1)
    () #choose names
    
#Stage 1, input names
while True:
    nameNumber += 1
    names = input("Enter name " + str(nameNumber) + ": ")
    if "no more" in names:
        break
    nameList.append(names)

#Stage 2, pick name
pickName(nameList)
