import random
totalSubtractFrom = 100
for i in range(1, 4):
    for b in range(1, 4):
        percentage = totalSubtractFrom - random.uniform(0,99)
        largestOfPercentages = 100
        totalSubtractFrom = percentage
        print(f'Cell({i}, {b}): {percentage}%') #Needs to create 9 numbers, but all numbers add up to 100, and set largestOfPercentages to the largest of those 9 numbers
print(f"Largest Number Is {largestOfPercentages}")