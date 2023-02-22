from termcolor import colored
import os

while True:
    livesUsed = int(input("?: "))
    os.system('cls')

    if livesUsed == 0:
        print(colored("""
     ___
    |   |
    |   |
        |
        |
        |
      __|__        
        """, 'red', attrs=['dark', 'bold']))
    elif livesUsed == 1:
        print(colored("""
     ___
    /   | 
  O/    |
        |
        |
        |
      __|__
        """, 'red', attrs=['bold', 'dark']))
    elif livesUsed == 2:
        print(colored("""
     ___
    /   | 
  O/    |
  |     |
        |
        |
      __|__
        """, 'red', attrs=['bold', 'dark']))
    elif livesUsed == 3:
        print(colored("""
     ___
    /   | 
  O/    |
 /|     |
        |
        |
      __|__
        """, 'red', attrs=['bold', 'dark']))
    elif livesUsed == 4:
        print(colored("""
     ___
    /   | 
  O/    |
 /|\\    |
        |
        |
      __|__
        """, 'red', attrs=['bold', 'dark']))
    elif livesUsed == 5:
        print(colored("""
     ___
    /   | 
  O/    |
 /|\\    |
 /      |
        |
      __|__
        """, 'red', attrs=['bold', 'dark']))
    elif livesUsed == 6:
        print(colored("""
     ___
    /   | 
  O/    |
 /|\\    |
 / \\    |
        |
      __|__
        """, 'red', attrs=['bold', 'dark']))



