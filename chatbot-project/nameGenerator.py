import random
import time
import os
from termcolor import colored
def randName():
    text_linus = colored('<Linus> ', 'green', attrs=['dark','bold'])
    print(text_linus + "Put your names in, and write 'no more' when done!")
    nameList = []
    nameNumber = 0
    def pickName(fromNames):
        pickingProgress = 0
        picking = True
        pickedName = random.choice(fromNames)
        waitTime = 0
        while picking:
            os.system('cls')
            print(random.choice(fromNames))
            pickingProgress += 1
            if pickingProgress >= 40:
                os.system('cls')
                picking = False
                print(pickedName)
                time.sleep(1)
                fromNames.remove(pickedName)
                print("The Winner Is: " + pickedName + "!")
                
            waitTime += 0.005
            time.sleep(waitTime)
        while True:
            remove = input("Remove name and spin again? [y/n] ")
            if remove.lower() == 'y':
                if fromNames:
                    return pickName(fromNames)
                else:
                    return "Final Winner Was: " + pickedName + "! "
            elif remove.lower() == 'n':
                listAmountFinal = len(fromNames)
                finalStanders = [
                    f"{i+1}. {name}" for i, name in enumerate(fromNames)
                ]
                return ("Spinning Finished! Last Standers Are:\n" + "\n".join(finalStanders) + '\n' + 'Most Recent Winner: ' + pickedName)
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
    return pickName(nameList)

