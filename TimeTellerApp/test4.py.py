import random

listOf9Numbers = []
Tries = 0
def printNumbers(listOf9Numbers):
    listOf9Numbers.sort(reverse=True)
    print('\n')
    print('\n')
    print('\n')
    print('\n')
    print(f"Success! {listOf9Numbers} Adds Up To {sum(listOf9Numbers)} With {Tries} Tries!")
    print('\n')
    print('\n')
    print('\n')
    print('\n')
    exit()

while True:
    for i in range(9):
        n = round(random.uniform(1,30), 2)
        listOf9Numbers.append(n)
    if sum(listOf9Numbers) == 100:
        printNumbers(listOf9Numbers)
    else:
        Tries += 1
        print(f"Combination Failed! f{listOf9Numbers} Adds Up To {sum(listOf9Numbers)}") #CHANCE OF FIRST TRY IS 1 IN 1.3 BILLION
        listOf9Numbers = []


