import random
fingerAmountLeft = int(input("p1: "))
fingerAmountRight = int(input("p2: "))

# Define the initial values
botFingerAmountLeft = int(input("b1:"))
botFingerAmountRight = int(input("b2: "))

#HERE -----------

desiredSum = botFingerAmountLeft + botFingerAmountRight
maxAttempts = 500
attempts = 0
while True:
    attempts += 1
    if attempts >= maxAttempts:
        rAttack = random.randint(1,5)
        if rAttack == 1:
            attack = ('left', 'left')
        elif rAttack == 2:
            attack = ('left', 'right')
        elif rAttack == 3:
            attack = ('right', 'left')
        elif rAttack == 4:
            attack = ('right', 'right')
        print(attack)
        break
    n1 = random.randint(1,5)
    n2 = random.randint(1,5)
    if (n1+n2) == desiredSum and (botFingerAmountLeft != n1) and (botFingerAmountRight != n1):
        break

if (n1 + fingerAmountLeft) >= 5 or (n1 + fingerAmountRight) >= 5 or (n2 + fingerAmountRight) >= 5 or (n2 + fingerAmountLeft) >= 5:
    rAttack = random.randint(1,5)
    if rAttack == 1:
        attack = ('left', 'left')
    elif rAttack == 2:
        attack = ('left', 'right')
    elif rAttack == 3:
        attack = ('right', 'left')
    elif rAttack == 4:
        attack = ('right', 'right')
    print(attack)

#HERE --------

print(f"{n1}, {n2}, Split")
