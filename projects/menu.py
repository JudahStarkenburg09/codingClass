import time
import os
import re
from termcolor import cprint, colored

menuList = ["Hamburger", "Pizza", "Salad", "French Fries", 'Hot Dog']
menuPrice = [11.99     ,  4.99  ,  3.99  ,  .99         ,    6.99  ,]
tax = 2.75
os.system('cls')

while True:
    orderMade = False
    found = False
    n = 0
    pn = 0
    for i in menuList:
        n += 1
        cprint(f"{n}. {i}", 'green')
    
    order = (input(colored("What would you like to order? \n", 'green')))
    print('\n')
    for item in menuList:
        if item.lower() == order.lower():
            re.sub(r'\s*', '', item)
            if found == False:
                found = True
    

    if order.isdigit() and int(order) <= len(menuList):
        equation = (((menuPrice[int(order)-1]/100)*tax)+ menuPrice[(int(order)-1)])
        cprint(menuList[(int(order)-1)] + f" has been order, price is ${menuPrice[(int(order)-1)]} + tax: ${round(equation, 2)}", 'green')
    elif found:
        for i in menuList:
            pn += 1
            re.sub(r'\s*', '', i)
            if str(i).lower() == order.lower():
                order = int(pn)
                equation = (((menuPrice[int(order)-1]/100)*tax)+ menuPrice[(int(order)-1)])
                cprint(menuList[(int(order)-1)] + f" has been order, price is ${menuPrice[(int(order)-1)]} + tax: ${round(equation, 2)}", 'green')
                break
    else:
        cprint(f"Invalid Order '{order}'", 'red')


    time.sleep(5)
    os.system('cls')
        
