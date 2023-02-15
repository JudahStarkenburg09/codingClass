from termcolor import colored
import random
import os

text1 = colored('You Must Guess 1-100!', 'yellow')
text2 = colored(' -1 Guess', 'red', attrs=["dark", "bold"])
text3 = colored('Guesses Left: ', 'blue', attrs=["dark", "bold"])
text5 = colored('You Lose! The Number Was ', 'red', attrs=['dark', 'bold'])


number = random.randrange(1,500)
guesses = 0
left = 8
os.system('cls')
print('Welcome To The Guessing Game, Guess The Number, In 8 Tries!')
while guesses <= 8:
    guesses += 1
    left -= 1
    text4 = colored(left, 'red')
    guess = float(input('Guess A Number 1-500: '))
    os.system('cls')
    print((colored('Your Last Guess Was: ', 'red')) + str(guess))
    if guess == number:
        print(colored('########', 'green'))
        print(colored('You Win!', 'yellow'))
        print(colored('########', 'green'))
        break
    if left == 0:
        answer = str(colored(number, 'green'))
        print(text5 + answer)
        break
    elif guess < number:
        print(colored('The Number Is Higher!', 'cyan'))
    elif guess > number:
        print(colored('The Number Is Lower!', 'cyan'))
    if guess > 500:
        print(text1 + text2)
    if guess < 0:
        print(text1 + text2)
    print(text3 + str(text4))