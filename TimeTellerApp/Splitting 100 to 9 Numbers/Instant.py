import random
import time


listOf9Numbers = []
Tries = 0

print("Success Rate For First Try Is 99.978%")
input("Press Enter To Start")


def tryAgain():
    global listOf9Numbers, Tries, startTime
    tryAgain = input("Try Again? [y/n]: ")
    if 'y' in tryAgain:
        startTime = time.time()
        Tries = 0
        return
    else:
        exit()

def printNumbers():
    global listOf9Numbers, Tries, startTime
    Tries += 1
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
while True:
    # Generate 9 random numbers using a normal distribution with mean 17.5 and std dev 5
    randomList = [round(random.gauss(17.5, 5), 1) for _ in range(9)]
    # Clip the random numbers to be between 1 and 30
    randomList = [max(min(num, 30), 1) for num in randomList]
    # Adjust the random numbers to sum to 100
    factor = 100 / sum(randomList)
    randomList = [round(num * factor, 1) for num in randomList]
    # Check if the adjustment resulted in any negative numbers
    if all(num >= 0 for num in randomList):
        listOf9Numbers = randomList
        printNumbers()
    else:
        currentTime = time.time()
        if currentTime - startTime > 3:
            print(f"ERROR: Elapsed Time[{currentTime-startTime}] > 3! [Please Try Again!]")
            tryAgain()
        Tries += 1
        print(f"Combination Failed! {randomList} Adds Up To {sum(randomList)}")





