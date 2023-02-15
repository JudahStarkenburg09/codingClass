from termcolor import colored

text1 = colored('You Must Guess 1-100!', 'yellow')
text2 = colored(' -1 Guess', 'red', attrs=["dark", "bold"])

print(text1 + text2)
