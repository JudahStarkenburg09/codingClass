import time
import random
import os
while True:
    numberList = []
    os.system('cls')
    tries = 0
    for i in range(1,100):
        numberList.append(i)
    print("I'm going to guess the number you are thinking of...")
    time.sleep(1)
    print("Pick a number 1-100...")
    time.sleep(1)
    while True:
        os.system('cls')
        print(numberList)
        tries +=1
        numGuessed = random.choice(numberList)
        print(f"I'm going to guess '{numGuessed}'")
        right = input("Is that right!? (y/n)\n")
        if 'y' in right:
            if tries == 1:
                playagain = input(f"YAY! I win with {tries} try. Do you want to play again? (y/n) \n")
            else:
                playagain = input(f"YAY! I win with {tries} tries.  Do you want to play again? (y/n) \n")
            if 'n' in playagain:
                exit()
            else:
                print("Playing again!")
                time.sleep(1)
                break
        higherOrLower = input("Higher or lower? \n")
        if 'high' in higherOrLower.lower():
            numberList.remove(numGuessed)
            for b in numberList:
                if b <= numGuessed:
                    numberList.remove(b)
        elif 'low' in higherOrLower.lower():
            numberList.remove(numGuessed)
            for b in numberList:
                if b >= numGuessed:
                    numberList.remove(b)
        else:
            print("Please tell me higher or lower!")
        