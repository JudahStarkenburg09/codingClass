import os
import time
import random
print("Shopping List: ")
#Create The List
Shop = [(input('1: ')), (input('2: ')), (input('3: ')), (input('4: ')), (input('5: ')), (input('6: ')), (input('7: ')), (input('8: ')), (input('9: ')), (input('10: ')), ]
n = 0
print('Creating Shopping list...')
time.sleep(1)
os.system('cls')
print('Things To Buy:')
print('--------------')
totalcost = 0
#Print The List
for i in Shop:
    p = random.randint(1, 15)
    n = n + 1
    totalcost = totalcost + p
    print(str(n) + ': ' + i + ' -> $' + str(p) + '.00')
#Print Total Cost
print('Total Cost Is: $' + str(totalcost) + '.00')
