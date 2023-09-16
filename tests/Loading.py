from termcolor import colored, cprint
import time
import os

length = 10

Lbracket = colored('[', 'yellow')
Rbracket = colored(']', 'yellow')
add = '█'
string = ''
def load(length, string, Lbracket, Rbracket):
    for i in range(1, length):
        os.system('cls')
        print(f"{Lbracket}{colored(string, 'red')}{Rbracket}")
        string += add
        time.sleep(1)
    os.system('cls')
    cprint("Done!", 'green')


load(length, string, Lbracket, Rbracket)
