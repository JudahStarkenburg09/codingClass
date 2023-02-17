import random
import time
import os
from termcolor import colored
# def randName():
text_linus = colored('<Linus> ', 'green', attrs=['dark','bold'])
print(text_linus + "Put your names in, and write 'no more' when done!")
nameList = []
nameNumber = 0
def pickName(fromNames):
    while True:
        os.system('cls')
        pickedName = random.choice(fromNames)
        print(random.choice(fromNames))
        time.sleep(0.1)
        if random.random() < 0.2:
            break
    os.system('cls')
    print(pickedName)
    fromNames.remove(pickedName)
    print("The Winner Is: " + pickedName + "!")
    while True:
        remove = input("Remove name and spin again? [y/n] ")
        if remove.lower() == 'y':
            if fromNames:
                return pickName(fromNames)
            else:
                print("No more names!")
                return
        elif remove.lower() == 'n':
            return
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

    
#Stage 1, input names
while True:
    nameNumber += 1
    names = input("Enter name " + str(nameNumber) + ": ")
    if "no more" in names.lower():
        break
    nameList.append(names)

#Stage 2, pick name
pickName(nameList)

