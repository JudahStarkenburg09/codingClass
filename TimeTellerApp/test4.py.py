import random

listOf9Numbers = []

def printNumbers(listOf9Numbers):
    listOf9Numbers.sort(reverse=True)
    print('\n')
    print('\n')
    print('\n')
    print('\n')
    print(f"Success! {listOf9Numbers} Adds Up To {sum(listOf9Numbers)}")
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
        print(f"Combination Failed! f{listOf9Numbers} Adds Up To {sum(listOf9Numbers)}")
        listOf9Numbers = []


