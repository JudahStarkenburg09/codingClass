import random
import time

listOf9Numbers = []
Tries = 0
def tryAgain():
    global listOf9Numbers, Tries, startTime
    tryAgain = input("Try Again? [y/n]: ")
    if 'y' in tryAgain:
        startTime = time.time()
        Tries = 0
        return
    else:
        exit()


print("Success Rate For First Try Is 0.0007%.")
input("Press Enter To Start")
def printNumbers():
    global listOf9Numbers, Tries, startTime
    endTime = time.time()

    # Make a copy of the original list so that we can modify it without changing the original
    modifiedList = listOf9Numbers[:]

    # Keep subtracting 0.5 from each of the other 8 numbers and adding 4 to the first number
    # until the smallest number is no longer negative

    modifiedList.sort(reverse=True)
    
    going = True
    while going == True:
        if modifiedList[8] > .5:
            modifiedList[0] += 4
            modifiedList[1] -= .5
            modifiedList[2] -= .5
            modifiedList[3] -= .5
            modifiedList[4] -= .5
            modifiedList[5] -= .5
            modifiedList[6] -= .5
            modifiedList[7] -= .5
            modifiedList[8] -= .5

        else: 
            going = False

    # Sort the list in reverse order
    modifiedList.sort(reverse=True)

    # Round each number to one decimal place
    for i in range(9):
        modifiedList[i] = round(modifiedList[i], 1)

    # Print the modified list, the sum of the numbers, the number of tries, and the time it took
    print('\n\n\n\n')
    print(f"Success! {modifiedList} Adds Up To {sum(modifiedList)} With {Tries} Tries! Calculation Took {round(endTime-startTime, 1)} Seconds!")
    print('\n\n\n\n')
    tryAgain()
    



startTime = time.time()
Tries = 0
while True:
    listOf9Numbers = []
    for i in range(9):
        n = round(random.uniform(1,30), 1)
        listOf9Numbers.append(n)
    if round(sum(listOf9Numbers), 2) == 100: # round the sum to 2 decimal places
        printNumbers()
    else:
        currentTime = time.time()
        if currentTime - startTime > 30:
            print(f"ERROR: Elapsed Time[{currentTime-startTime}] > 30! [Please Try Again!]")
            tryAgain
        Tries += 1
        print(f"Combination Failed! {listOf9Numbers} Adds Up To {round(sum(listOf9Numbers), 2)}")




